# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

import msrest.serialization

from ._service_bus_management_client_enums import *


class CreateEntityBody(msrest.serialization.Model):
    """The response from a CreateQueue operation.

    :param content: TODO: Add description.
    :type content: ~azure.service._control_client2.models.CreateEntityBodyContent
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'CreateEntityBodyContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        content: Optional["CreateEntityBodyContent"] = None,
        **kwargs
    ):
        super(CreateEntityBody, self).__init__(**kwargs)
        self.content = content


class CreateEntityBodyContent(msrest.serialization.Model):
    """TODO: Add description.

    :param type: TODO: Add description.
    :type type: str
    :param entity: Any object.
    :type entity: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'entity': {'key': 'entity', 'type': 'object'},
    }
    _xml_map = {
        'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        type: Optional[str] = "application/xml",
        entity: Optional[object] = None,
        **kwargs
    ):
        super(CreateEntityBodyContent, self).__init__(**kwargs)
        self.type = type
        self.entity = entity


class MessageCountDetails(msrest.serialization.Model):
    """Details about the message counts in queue.

    :param active_message_count: Number of active messages in the queue, topic, or subscription.
    :type active_message_count: int
    :param dead_letter_message_count: Number of messages that are dead lettered.
    :type dead_letter_message_count: int
    :param scheduled_message_count: Number of scheduled messages.
    :type scheduled_message_count: int
    :param transfer_dead_letter_message_count: Number of messages transferred into dead letters.
    :type transfer_dead_letter_message_count: int
    :param transfer_message_count: Number of messages transferred to another queue, topic, or
     subscription.
    :type transfer_message_count: int
    """

    _attribute_map = {
        'active_message_count': {'key': 'ActiveMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
        'dead_letter_message_count': {'key': 'DeadLetterMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
        'scheduled_message_count': {'key': 'ScheduledMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
        'transfer_dead_letter_message_count': {'key': 'TransferDeadLetterMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
        'transfer_message_count': {'key': 'TransferMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
    }
    _xml_map = {
        'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'
    }

    def __init__(
        self,
        *,
        active_message_count: Optional[int] = None,
        dead_letter_message_count: Optional[int] = None,
        scheduled_message_count: Optional[int] = None,
        transfer_dead_letter_message_count: Optional[int] = None,
        transfer_message_count: Optional[int] = None,
        **kwargs
    ):
        super(MessageCountDetails, self).__init__(**kwargs)
        self.active_message_count = active_message_count
        self.dead_letter_message_count = dead_letter_message_count
        self.scheduled_message_count = scheduled_message_count
        self.transfer_dead_letter_message_count = transfer_dead_letter_message_count
        self.transfer_message_count = transfer_message_count


class QueueMetrics(msrest.serialization.Model):
    """Service Bus queue metrics.

    :param queue_name: Name of the queue.
    :type queue_name: str
    :param accessed_at: Last time a message was sent, or the last time there was a receive request
     to this queue.
    :type accessed_at: ~datetime.datetime
    :param created_at: The exact time the queue was created.
    :type created_at: ~datetime.datetime
    :param updated_at: The exact time a message was updated in the queue.
    :type updated_at: ~datetime.datetime
    :param size_in_bytes: The size of the queue, in bytes.
    :type size_in_bytes: int
    :param message_count: The number of messages in the queue.
    :type message_count: int
    :param message_count_details: Details about the message counts in queue.
    :type message_count_details: ~azure.service._control_client2.models.MessageCountDetails
    """

    _attribute_map = {
        'queue_name': {'key': 'QueueName', 'type': 'str'},
        'accessed_at': {'key': 'AccessedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'created_at': {'key': 'CreatedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'updated_at': {'key': 'UpdatedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'size_in_bytes': {'key': 'SizeInBytes', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'message_count': {'key': 'MessageCount', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'message_count_details': {'key': 'MessageCountDetails', 'type': 'MessageCountDetails'},
    }
    _xml_map = {
        'name': 'QueueMetrics', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        *,
        queue_name: Optional[str] = None,
        accessed_at: Optional[datetime.datetime] = None,
        created_at: Optional[datetime.datetime] = None,
        updated_at: Optional[datetime.datetime] = None,
        size_in_bytes: Optional[int] = None,
        message_count: Optional[int] = None,
        message_count_details: Optional["MessageCountDetails"] = None,
        **kwargs
    ):
        super(QueueMetrics, self).__init__(**kwargs)
        self.queue_name = queue_name
        self.accessed_at = accessed_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.size_in_bytes = size_in_bytes
        self.message_count = message_count
        self.message_count_details = message_count_details


class QueueProperties(msrest.serialization.Model):
    """Description of a Service Bus queue resource.

    :param queue_name: Name of the queue.
    :type queue_name: str
    :param authorization_rules: Authorization rules for resource.
    :type authorization_rules: list[str]
    :param auto_delete_on_idle: ISO 8061 timeSpan idle interval after which the queue is
     automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: ~datetime.timedelta
    :param dead_lettering_on_message_expiration: A value that indicates whether this queue has dead
     letter support when a message expires.
    :type dead_lettering_on_message_expiration: bool
    :param default_message_time_to_live: ISO 8601 default message timespan to live value. This is
     the duration after which the message expires, starting from when the message is sent to Service
     Bus. This is the default value used when TimeToLive is not set on a message itself.
    :type default_message_time_to_live: ~datetime.timedelta
    :param duplicate_detection_history_time_window: ISO 8601 timeSpan structure that defines the
     duration of the duplicate detection history. The default value is 10 minutes.
    :type duplicate_detection_history_time_window: ~datetime.timedelta
    :param entity_availability_status: Availibility status of the entity. Possible values include:
     "Available", "Limited", "Renaming", "Restoring", "Unknown".
    :type entity_availability_status: str or
     ~azure.service._control_client2.models.EntityAvailabilityStatus
    :param enable_batched_operations: Value that indicates whether server-side batched operations
     are enabled.
    :type enable_batched_operations: bool
    :param enable_express: A value that indicates whether Express Entities are enabled. An express
     queue holds a message in memory temporarily before writing it to persistent storage.
    :type enable_express: bool
    :param enable_partitioning: A value that indicates whether the queue is to be partitioned
     across multiple message brokers.
    :type enable_partitioning: bool
    :param is_anonymous_accessible: A value indicating if the resource can be accessed without
     authorization.
    :type is_anonymous_accessible: bool
    :param lock_duration: ISO 8601 timespan duration of a peek-lock; that is, the amount of time
     that the message is locked for other receivers. The maximum value for LockDuration is 5
     minutes; the default value is 1 minute.
    :type lock_duration: ~datetime.timedelta
    :param max_delivery_count: The maximum delivery count. A message is automatically deadlettered
     after this number of deliveries. Default value is 10.
    :type max_delivery_count: int
    :param max_size_in_megabytes: The maximum size of the queue in megabytes, which is the size of
     memory allocated for the queue.
    :type max_size_in_megabytes: float
    :param requires_duplicate_detection: A value indicating if this queue requires duplicate
     detection.
    :type requires_duplicate_detection: bool
    :param requires_session: A value that indicates whether the queue supports the concept of
     sessions.
    :type requires_session: bool
    :param status: Status of a Service Bus resource. Possible values include: "Active", "Creating",
     "Deleting", "Disabled", "ReceiveDisabled", "Renaming", "Restoring", "SendDisabled", "Unknown".
    :type status: str or ~azure.service._control_client2.models.EntityStatus
    :param support_ordering: A value that indicates whether the queue supports ordering.
    :type support_ordering: bool
    """

    _attribute_map = {
        'queue_name': {'key': 'QueueName', 'type': 'str'},
        'authorization_rules': {'key': 'AuthorizationRules', 'type': '[str]', 'xml': {'itemsNs': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'auto_delete_on_idle': {'key': 'AutoDeleteOnIdle', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'dead_lettering_on_message_expiration': {'key': 'DeadLetteringOnMessageExpiration', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'default_message_time_to_live': {'key': 'DefaultMessageTimeToLive', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'duplicate_detection_history_time_window': {'key': 'DuplicateDetectionHistoryTimeWindow', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'entity_availability_status': {'key': 'EntityAvailabilityStatus', 'type': 'str'},
        'enable_batched_operations': {'key': 'EnableBatchedOperations', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_express': {'key': 'EnableExpress', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_partitioning': {'key': 'EnablePartitioning', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'is_anonymous_accessible': {'key': 'IsAnonymousAccessible', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'lock_duration': {'key': 'LockDuration', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'max_delivery_count': {'key': 'MaxDeliveryCount', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'max_size_in_megabytes': {'key': 'MaxSizeInMegabytes', 'type': 'float', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'requires_duplicate_detection': {'key': 'RequiresDuplicateDetection', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'requires_session': {'key': 'RequiresSession', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'status': {'key': 'Status', 'type': 'str'},
        'support_ordering': {'key': 'SupportOrdering', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
    }
    _xml_map = {
        'name': 'QueueDescription', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        *,
        queue_name: Optional[str] = None,
        authorization_rules: Optional[List[str]] = None,
        auto_delete_on_idle: Optional[datetime.timedelta] = None,
        dead_lettering_on_message_expiration: Optional[bool] = None,
        default_message_time_to_live: Optional[datetime.timedelta] = None,
        duplicate_detection_history_time_window: Optional[datetime.timedelta] = None,
        entity_availability_status: Optional[Union[str, "EntityAvailabilityStatus"]] = None,
        enable_batched_operations: Optional[bool] = None,
        enable_express: Optional[bool] = None,
        enable_partitioning: Optional[bool] = None,
        is_anonymous_accessible: Optional[bool] = None,
        lock_duration: Optional[datetime.timedelta] = None,
        max_delivery_count: Optional[int] = None,
        max_size_in_megabytes: Optional[float] = None,
        requires_duplicate_detection: Optional[bool] = None,
        requires_session: Optional[bool] = None,
        status: Optional[Union[str, "EntityStatus"]] = None,
        support_ordering: Optional[bool] = None,
        **kwargs
    ):
        super(QueueProperties, self).__init__(**kwargs)
        self.queue_name = queue_name
        self.authorization_rules = authorization_rules
        self.auto_delete_on_idle = auto_delete_on_idle
        self.dead_lettering_on_message_expiration = dead_lettering_on_message_expiration
        self.default_message_time_to_live = default_message_time_to_live
        self.duplicate_detection_history_time_window = duplicate_detection_history_time_window
        self.entity_availability_status = entity_availability_status
        self.enable_batched_operations = enable_batched_operations
        self.enable_express = enable_express
        self.enable_partitioning = enable_partitioning
        self.is_anonymous_accessible = is_anonymous_accessible
        self.lock_duration = lock_duration
        self.max_delivery_count = max_delivery_count
        self.max_size_in_megabytes = max_size_in_megabytes
        self.requires_duplicate_detection = requires_duplicate_detection
        self.requires_session = requires_session
        self.status = status
        self.support_ordering = support_ordering
