# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import logging
from typing import Any, Union, Dict, Tuple, TYPE_CHECKING, Callable, List

from .common import EventHubSharedKeyCredential, EventHubSASTokenCredential, EventData
from .client import EventHubClient
from ._eventprocessor.event_processor import EventProcessor
from ._eventprocessor.partition_context import PartitionContext

if TYPE_CHECKING:
    from azure.core.credentials import TokenCredential  # type: ignore

log = logging.getLogger(__name__)


class EventHubConsumerClient(EventHubClient):
    """ The EventHubProducerClient class defines a high level interface for
    receiving events from the Azure Event Hubs service.

    The main goal of `EventHubConsumerClient` is to receive events from all partitions of an EventHub with
    load balancing and checkpointing.

    When multiple `EventHubConsumerClient` works with one process, multiple processes, or multiple computer machines
    and if they use the same repository as the load balancing and checkpointing store, they will balance automatically.
    To enable the load balancing and / or checkpointing, partition_manager must be set when creating the
    `EventHubConsumerClient`.

    An `EventHubConsumerClient` can also receive from a specific partition when you call its method `receive()`
    and specify the partition_id.
    Load balancing won't work in single-partition mode. But users can still save checkpoint if the partition_manager
    is set.

    :param str host: The hostname of the Event Hub.
    :param str event_hub_path: The path of the specific Event Hub to connect the client to.
    :param credential: The credential object used for authentication which implements particular interface
     of getting tokens.
    :type credential: ~azure.eventhub.EventHubSharedKeyCredential,~azure.eventhub.EventHubSASTokenCredential,
     Credential objects in azure-identity and objects that implement `get_token(self, *scopes)` method
    :keyword bool network_tracing: Whether to output network trace logs to the logger. Default is `False`.
    :keyword dict http_proxy: HTTP proxy settings. This must be a dictionary with the following
     keys: 'proxy_hostname' (str value) and 'proxy_port' (int value).
     Additionally the following keys may also be present: 'username', 'password'.
    :keyword float auth_timeout: The time in seconds to wait for a token to be authorized by the service.
     The default value is 60 seconds. If set to 0, no timeout will be enforced from the client.
    :keyword str user_agent: The user agent that needs to be appended to the built in user agent string.
    :keyword int retry_total: The total number of attempts to redo the failed operation when an error happened. Default
     value is 3.
    :keyword transport_type: The type of transport protocol that will be used for communicating with
     the Event Hubs service. Default is ~azure.eventhub.TransportType.Amqp.
    :paramtype transport_type: ~azure.eventhub.TransportType
    :keyword partition_manager: stores the load balancing data and checkpoint data when receiving events
     if partition_manager is specified. If it's None, this EventHubConsumerClient instance will receive
     events without load balancing and checkpoint.
    :paramtype partition_manager: Implementation classes of ~azure.eventhub.PartitionManager
    :keyword float load_balancing_interval: When load balancing kicks in, this is the interval in seconds
     between two load balancing. Default is 10.

    .. admonition:: Example:

        .. literalinclude:: ../samples/sync_samples/sample_code_eventhub.py
            :start-after: [START create_eventhub_consumer_client_sync]
            :end-before: [END create_eventhub_consumer_client_sync]
            :language: python
            :dedent: 4
            :caption: Create a new instance of the EventHubConsumerClient.
    """

    def __init__(self, host, event_hub_path, credential, **kwargs):
        # type:(str, str, Union[EventHubSharedKeyCredential, EventHubSASTokenCredential, TokenCredential], Any) -> None
        receive_timeout = kwargs.get("receive_timeout", 3)
        if receive_timeout <= 0:
            raise ValueError("receive_timeout must be greater than 0.")

        kwargs['receive_timeout'] = receive_timeout

        super(EventHubConsumerClient, self).__init__(
            host=host, event_hub_path=event_hub_path, credential=credential, **kwargs)
        self._partition_manager = kwargs.get("partition_manager")
        self._load_balancing_interval = kwargs.get("load_balancing_interval", 10)
        self._event_processors = dict()  # type: Dict[Tuple[str, str], EventProcessor]
        self._closed = False

    @classmethod
    def _stop_eventprocessor(cls, event_processor):
        # pylint: disable=protected-access
        eventhub_client = event_processor._eventhub_client
        consumer_group = event_processor._consumer_group_name
        partition_id = event_processor._partition_id
        with eventhub_client._lock:
            event_processor.stop()
            if partition_id and (consumer_group, partition_id) in eventhub_client._event_processors:
                del eventhub_client._event_processors[(consumer_group, partition_id)]
            elif (consumer_group, '-1') in eventhub_client._event_processors:
                del eventhub_client._event_processors[(consumer_group, "-1")]

    def receive(self, on_event, consumer_group, **kwargs):
        #  type: (Callable[[PartitionContext, List[EventData]], None], str, Any) -> None
        """Receive events from partition(s) optionally with load balancing and checkpointing.

        :param on_event: The callback function for handling received events. The callback takes two
         parameters: partition_context` which contains partition information and `events` which are the received events.
         Please define the callback like `on_event(partition_context, events)`.
         For detailed partition context information, please refer to ~azure.eventhub.PartitionContext.
        :type on_event: Callable[PartitionContext, List[EventData]]
        :param str consumer_group: The name of the consumer group this consumer is associated with.
         Events are read in the context of this group. The default consumer_group for an event hub is "$Default".
        :keyword str partition_id: The identifier of the Event Hub partition from which events will be received.
        :keyword int owner_level: The priority of the exclusive consumer. An exclusive consumer will be created
         if owner_level is set.
        :keyword int prefetch: The message prefetch count of the consumer. Default is 300.
        :keyword bool track_last_enqueued_event_properties: Indicates whether or not the consumer should
         request information on the last enqueued event on its associated partition, and track that information
         as events are received. When information about the partition's last enqueued event is being tracked,
         each event received from the Event Hubs service will carry metadata about the partition. This results in
         a small amount of additional network bandwidth consumption that is generally a favorable trade-off when
         considered against periodically making requests for partition properties using the Event Hub client.
         It is set to `False` by default.
        :keyword initial_event_position: Start receiving from this initial_event_position
         if there isn't checkpoint data for a partition. Use the checkpoint data if there it's available. This can be a
         a dict with partition id as the key and position as the value for individual partitions, or a single
         EventPosition instance for all partitions. This parameter could be type of ~azure.eventhub.EventPosition or
         dict[str,~azure.eventhub.EventPosition] where the key is partition id.
        :paramtype initial_event_position: ~azure.eventhub.EventPosition, dict[str,~azure.eventhub.EventPosition]
        :keyword on_error: The callback function which would be called when there is an error met during the receiving
         time. The callback takes two parameters: `partition_context` which contains partition information
         and `error` being the exception. Please define the callback like `on_error(partition_context, error)`.
        :paramtype on_error: Callable[[PartitionContext, Exception]]
        :keyword on_partition_initialize: The callback function which will be called after a consumer for certain
         partition finishes initialization. The callback takes two parameter: `partition_context` which contains
         the partition information. Please define the callback like`on_partition_initialize(partition_context)`.
        :paramtype on_partition_initialize: Callable[[PartitionContext]]
        :keyword on_partition_close: The callback function which will be called after a consumer for certain
         partition is closed. The callback takes two parameters: `partition_context` which contains partition
         information and `reason` for the close. Please define the callback like `on_error(partition_context, reason)`.
         Please refer to `azure.eventhub.CloseReason` for different closing reason.
        :paramtype on_partition_close: Callable[[PartitionContext, CloseReason]]
        :rtype: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/sync_samples/sample_code_eventhub.py
                :start-after: [START eventhub_consumer_client_receive_sync]
                :end-before: [END eventhub_consumer_client_receive_sync]
                :language: python
                :dedent: 4
                :caption: Receive events from the EventHub.
        """
        partition_id = kwargs.get("partition_id")

        with self._lock:
            error = None
            if (consumer_group, '-1') in self._event_processors:
                error = ValueError("This consumer client is already receiving events from all partitions for"
                                   " consumer group {}. "
                                   "Cannot receive from any other partitions again.".format(consumer_group))
            elif partition_id is None and any(x[0] == consumer_group for x in self._event_processors):
                error = ValueError("This consumer client is already receiving events for consumer group {}. "
                                   "Cannot receive from all partitions again.".format(consumer_group))
            elif (consumer_group, partition_id) in self._event_processors:
                error = ValueError("This consumer is already receiving events from partition {} for consumer group {}. "
                                   "Cannot receive from it again.".format(partition_id, consumer_group))
            if error:
                log.warning(error)
                raise error

            event_processor = EventProcessor(
                self, consumer_group, on_event,
                partition_manager=self._partition_manager,
                polling_interval=self._load_balancing_interval,
                **kwargs
            )
            self._event_processors[(consumer_group, partition_id or "-1")] = event_processor

        event_processor.start()

    def close(self):
        # type: () -> None
        """Stop retrieving events from event hubs and close the underlying AMQP connection and links.

        :rtype: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/sync_samples/sample_code_eventhub.py
                :start-after: [START eventhub_consumer_client_close_sync]
                :end-before: [END eventhub_consumer_client_close_sync]
                :language: python
                :dedent: 4
                :caption: Close down the client.

        """
        with self._lock:
            for _ in range(len(self._event_processors)):
                _, ep = self._event_processors.popitem()
                ep.stop()
            super(EventHubConsumerClient, self).close()
