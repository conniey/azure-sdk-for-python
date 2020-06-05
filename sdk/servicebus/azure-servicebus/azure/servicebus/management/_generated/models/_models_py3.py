# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._service_bus_management_client_enums import *


class AuthorizationRule(msrest.serialization.Model):
    """Authorization rule of an entity.

    :param type:
    :type type: str
    :param claim_type:
    :type claim_type: str
    :param claim_value:
    :type claim_value: str
    :param rights: Access rights of the entity. Values are 'Send', 'Listen', or 'Manage'.
    :type rights: list[str]
    :param created_time: The date and time when the authorization rule was created.
    :type created_time: ~datetime.datetime
    :param modified_time: The date and time when the authorization rule was modified.
    :type modified_time: ~datetime.datetime
    :param key_name: The authorization rule key name.
    :type key_name: str
    :param primary_key: The primary key of the authorization rule.
    :type primary_key: str
    :param secondary_key: The primary key of the authorization rule.
    :type secondary_key: str
    """

    _attribute_map = {
        'type': {'key': 'Type', 'type': 'str', 'xml': {'attr': True, 'prefix': 'i', 'ns': 'http://www.w3.org/2001/XMLSchema-instance'}},
        'claim_type': {'key': 'ClaimType', 'type': 'str', 'xml': {'attr': True, 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'claim_value': {'key': 'ClaimValue', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'rights': {'key': 'Rights', 'type': '[str]', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect', 'wrapped': True, 'itemsName': 'AccessRights', 'itemsNs': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'created_time': {'key': 'CreatedTime', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'modified_time': {'key': 'ModifiedTime', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'key_name': {'key': 'KeyName', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'primary_key': {'key': 'PrimaryKey', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'secondary_key': {'key': 'SecondaryKey', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
    }
    _xml_map = {
        'name': 'AuthorizationRule', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        claim_type: Optional[str] = None,
        claim_value: Optional[str] = None,
        rights: Optional[List[str]] = None,
        created_time: Optional[datetime.datetime] = None,
        modified_time: Optional[datetime.datetime] = None,
        key_name: Optional[str] = None,
        primary_key: Optional[str] = None,
        secondary_key: Optional[str] = None,
        **kwargs
    ):
        super(AuthorizationRule, self).__init__(**kwargs)
        self.type = type
        self.claim_type = claim_type
        self.claim_value = claim_value
        self.rights = rights
        self.created_time = created_time
        self.modified_time = modified_time
        self.key_name = key_name
        self.primary_key = primary_key
        self.secondary_key = secondary_key


class CreateQueueBody(msrest.serialization.Model):
    """The request body for creating a queue.

    :param content: QueueDescription for the new queue.
    :type content: ~azure.servicebus.management._generated.models.CreateQueueBodyContent
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'CreateQueueBodyContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        content: Optional["CreateQueueBodyContent"] = None,
        **kwargs
    ):
        super(CreateQueueBody, self).__init__(**kwargs)
        self.content = content


class CreateQueueBodyContent(msrest.serialization.Model):
    """QueueDescription for the new queue.

    :param type: MIME type of content.
    :type type: str
    :param queue_description: Properties of the new queue.
    :type queue_description: ~azure.servicebus.management._generated.models.QueueDescription
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'queue_description': {'key': 'QueueDescription', 'type': 'QueueDescription'},
    }
    _xml_map = {
        'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        type: Optional[str] = "application/xml",
        queue_description: Optional["QueueDescription"] = None,
        **kwargs
    ):
        super(CreateQueueBodyContent, self).__init__(**kwargs)
        self.type = type
        self.queue_description = queue_description


class CreateTopicBody(msrest.serialization.Model):
    """The request body for creating a topic.

    :param content: TopicDescription for the new topic.
    :type content: ~azure.servicebus.management._generated.models.CreateTopicBodyContent
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'CreateTopicBodyContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        content: Optional["CreateTopicBodyContent"] = None,
        **kwargs
    ):
        super(CreateTopicBody, self).__init__(**kwargs)
        self.content = content


class CreateTopicBodyContent(msrest.serialization.Model):
    """TopicDescription for the new topic.

    :param type: MIME type of content.
    :type type: str
    :param topic_description: Topic information to create.
    :type topic_description: ~azure.servicebus.management._generated.models.TopicDescription
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'topic_description': {'key': 'TopicDescription', 'type': 'TopicDescription'},
    }
    _xml_map = {
        'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        type: Optional[str] = "application/xml",
        topic_description: Optional["TopicDescription"] = None,
        **kwargs
    ):
        super(CreateTopicBodyContent, self).__init__(**kwargs)
        self.type = type
        self.topic_description = topic_description


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
        'name': 'CountDetails', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
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


class QueueDescription(msrest.serialization.Model):
    """Description of a Service Bus queue resource.

    :param authorization_rules: Authorization rules for resource.
    :type authorization_rules:
     list[~azure.servicebus.management._generated.models.AuthorizationRule]
    :param auto_delete_on_idle: ISO 8601 timeSpan idle interval after which the queue is
     automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: ~datetime.timedelta
    :param created_at: The exact time the queue was created.
    :type created_at: ~datetime.datetime
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
     ~azure.servicebus.management._generated.models.EntityAvailabilityStatus
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
    :type max_size_in_megabytes: int
    :param requires_duplicate_detection: A value indicating if this queue requires duplicate
     detection.
    :type requires_duplicate_detection: bool
    :param requires_session: A value that indicates whether the queue supports the concept of
     sessions.
    :type requires_session: bool
    :param status: Status of a Service Bus resource. Possible values include: "Active", "Creating",
     "Deleting", "Disabled", "ReceiveDisabled", "Renaming", "Restoring", "SendDisabled", "Unknown".
    :type status: str or ~azure.servicebus.management._generated.models.EntityStatus
    :param support_ordering: A value that indicates whether the queue supports ordering.
    :type support_ordering: bool
    :param accessed_at: Last time a message was sent, or the last time there was a receive request
     to this queue.
    :type accessed_at: ~datetime.datetime
    :param updated_at: The exact time a message was updated in the queue.
    :type updated_at: ~datetime.datetime
    :param size_in_bytes: The size of the queue, in bytes.
    :type size_in_bytes: int
    :param message_count: The number of messages in the queue.
    :type message_count: int
    :param message_count_details: Details about the message counts in queue.
    :type message_count_details: ~azure.servicebus.management._generated.models.MessageCountDetails
    """

    _attribute_map = {
        'authorization_rules': {'key': 'AuthorizationRules', 'type': '[AuthorizationRule]', 'xml': {'name': 'AuthorizationRules', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect', 'wrapped': True, 'itemsName': 'AuthorizationRule', 'itemsNs': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'auto_delete_on_idle': {'key': 'AutoDeleteOnIdle', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'created_at': {'key': 'CreatedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'dead_lettering_on_message_expiration': {'key': 'DeadLetteringOnMessageExpiration', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'default_message_time_to_live': {'key': 'DefaultMessageTimeToLive', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'duplicate_detection_history_time_window': {'key': 'DuplicateDetectionHistoryTimeWindow', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'entity_availability_status': {'key': 'EntityAvailabilityStatus', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_batched_operations': {'key': 'EnableBatchedOperations', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_express': {'key': 'EnableExpress', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_partitioning': {'key': 'EnablePartitioning', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'is_anonymous_accessible': {'key': 'IsAnonymousAccessible', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'lock_duration': {'key': 'LockDuration', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'max_delivery_count': {'key': 'MaxDeliveryCount', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'max_size_in_megabytes': {'key': 'MaxSizeInMegabytes', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'requires_duplicate_detection': {'key': 'RequiresDuplicateDetection', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'requires_session': {'key': 'RequiresSession', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'status': {'key': 'Status', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'support_ordering': {'key': 'SupportOrdering', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'accessed_at': {'key': 'AccessedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'updated_at': {'key': 'UpdatedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'size_in_bytes': {'key': 'SizeInBytes', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'message_count': {'key': 'MessageCount', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'message_count_details': {'key': 'MessageCountDetails', 'type': 'MessageCountDetails'},
    }
    _xml_map = {
        'name': 'QueueDescription', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        *,
        authorization_rules: Optional[List["AuthorizationRule"]] = None,
        auto_delete_on_idle: Optional[datetime.timedelta] = None,
        created_at: Optional[datetime.datetime] = None,
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
        max_size_in_megabytes: Optional[int] = None,
        requires_duplicate_detection: Optional[bool] = None,
        requires_session: Optional[bool] = None,
        status: Optional[Union[str, "EntityStatus"]] = None,
        support_ordering: Optional[bool] = None,
        accessed_at: Optional[datetime.datetime] = None,
        updated_at: Optional[datetime.datetime] = None,
        size_in_bytes: Optional[int] = None,
        message_count: Optional[int] = None,
        message_count_details: Optional["MessageCountDetails"] = None,
        **kwargs
    ):
        super(QueueDescription, self).__init__(**kwargs)
        self.authorization_rules = authorization_rules
        self.auto_delete_on_idle = auto_delete_on_idle
        self.created_at = created_at
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
        self.accessed_at = accessed_at
        self.updated_at = updated_at
        self.size_in_bytes = size_in_bytes
        self.message_count = message_count
        self.message_count_details = message_count_details


class QueueDescriptionEntry(msrest.serialization.Model):
    """Represents an entry in the feed when querying queues.

    :param base: Base URL for the query.
    :type base: str
    :param id: The URL of the GET request.
    :type id: str
    :param title: The name of the queue.
    :type title: ~azure.servicebus.management._generated.models.ResponseTitle
    :param published: The timestamp for when this queue was published.
    :type published: ~datetime.datetime
    :param updated: The timestamp for when this queue was last updated.
    :type updated: ~datetime.datetime
    :param author: The author that created this resource.
    :type author: ~azure.servicebus.management._generated.models.ResponseAuthor
    :param link: The URL for the HTTP request.
    :type link: ~azure.servicebus.management._generated.models.ResponseLink
    :param content: The QueueDescription.
    :type content: ~azure.servicebus.management._generated.models.QueueDescriptionEntryContent
    """

    _attribute_map = {
        'base': {'key': 'base', 'type': 'str', 'xml': {'name': 'base', 'attr': True, 'prefix': 'xml'}},
        'id': {'key': 'id', 'type': 'str'},
        'title': {'key': 'title', 'type': 'ResponseTitle'},
        'published': {'key': 'published', 'type': 'iso-8601'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
        'author': {'key': 'author', 'type': 'ResponseAuthor'},
        'link': {'key': 'link', 'type': 'ResponseLink'},
        'content': {'key': 'content', 'type': 'QueueDescriptionEntryContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        base: Optional[str] = None,
        id: Optional[str] = None,
        title: Optional["ResponseTitle"] = None,
        published: Optional[datetime.datetime] = None,
        updated: Optional[datetime.datetime] = None,
        author: Optional["ResponseAuthor"] = None,
        link: Optional["ResponseLink"] = None,
        content: Optional["QueueDescriptionEntryContent"] = None,
        **kwargs
    ):
        super(QueueDescriptionEntry, self).__init__(**kwargs)
        self.base = base
        self.id = id
        self.title = title
        self.published = published
        self.updated = updated
        self.author = author
        self.link = link
        self.content = content


class QueueDescriptionEntryContent(msrest.serialization.Model):
    """The QueueDescription.

    :param type: Type of content in queue response.
    :type type: str
    :param queue_description: Description of a Service Bus queue resource.
    :type queue_description: ~azure.servicebus.management._generated.models.QueueDescription
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'queue_description': {'key': 'QueueDescription', 'type': 'QueueDescription'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        queue_description: Optional["QueueDescription"] = None,
        **kwargs
    ):
        super(QueueDescriptionEntryContent, self).__init__(**kwargs)
        self.type = type
        self.queue_description = queue_description


class QueueDescriptionFeed(msrest.serialization.Model):
    """Response from listing Service Bus queues.

    :param id: URL of the list queues query.
    :type id: str
    :param title: The entity type for the feed.
    :type title: str
    :param updated: Datetime of the query.
    :type updated: ~datetime.datetime
    :param link: Links to paginated response.
    :type link: list[~azure.servicebus.management._generated.models.ResponseLink]
    :param entry: Queue entries.
    :type entry: list[~azure.servicebus.management._generated.models.QueueDescriptionEntry]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
        'link': {'key': 'link', 'type': '[ResponseLink]'},
        'entry': {'key': 'entry', 'type': '[QueueDescriptionEntry]'},
    }
    _xml_map = {
        'name': 'feed', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        title: Optional[str] = None,
        updated: Optional[datetime.datetime] = None,
        link: Optional[List["ResponseLink"]] = None,
        entry: Optional[List["QueueDescriptionEntry"]] = None,
        **kwargs
    ):
        super(QueueDescriptionFeed, self).__init__(**kwargs)
        self.id = id
        self.title = title
        self.updated = updated
        self.link = link
        self.entry = entry


class QueueDescriptionResponse(msrest.serialization.Model):
    """The response from a Queue_Get operation.

    :param id: The URL of the GET request.
    :type id: str
    :param title: The name of the queue.
    :type title: str
    :param published: The timestamp for when this queue was published.
    :type published: str
    :param updated: The timestamp for when this queue was last updated.
    :type updated: str
    :param author: The author that created this resource.
    :type author: ~azure.servicebus.management._generated.models.ResponseAuthor
    :param link: The URL for the HTTP request.
    :type link: ~azure.servicebus.management._generated.models.ResponseLink
    :param content: Contents of a Queue_Get response.
    :type content: ~azure.servicebus.management._generated.models.QueueDescriptionResponseContent
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'published': {'key': 'published', 'type': 'str'},
        'updated': {'key': 'updated', 'type': 'str'},
        'author': {'key': 'author', 'type': 'ResponseAuthor'},
        'link': {'key': 'link', 'type': 'ResponseLink'},
        'content': {'key': 'content', 'type': 'QueueDescriptionResponseContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        title: Optional[str] = None,
        published: Optional[str] = None,
        updated: Optional[str] = None,
        author: Optional["ResponseAuthor"] = None,
        link: Optional["ResponseLink"] = None,
        content: Optional["QueueDescriptionResponseContent"] = None,
        **kwargs
    ):
        super(QueueDescriptionResponse, self).__init__(**kwargs)
        self.id = id
        self.title = title
        self.published = published
        self.updated = updated
        self.author = author
        self.link = link
        self.content = content


class QueueDescriptionResponseContent(msrest.serialization.Model):
    """Contents of a Queue_Get response.

    :param type: Type of content in queue response.
    :type type: str
    :param queue_description: Description of a Service Bus queue resource.
    :type queue_description: ~azure.servicebus.management._generated.models.QueueDescription
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'queue_description': {'key': 'QueueDescription', 'type': 'QueueDescription'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        queue_description: Optional["QueueDescription"] = None,
        **kwargs
    ):
        super(QueueDescriptionResponseContent, self).__init__(**kwargs)
        self.type = type
        self.queue_description = queue_description


class ResponseAuthor(msrest.serialization.Model):
    """The author that created this resource.

    :param name: The Service Bus namespace.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        **kwargs
    ):
        super(ResponseAuthor, self).__init__(**kwargs)
        self.name = name


class ResponseLink(msrest.serialization.Model):
    """The URL for the HTTP request.

    :param href: The URL of the GET request.
    :type href: str
    :param rel: What the link href is relative to.
    :type rel: str
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str', 'xml': {'attr': True}},
        'rel': {'key': 'rel', 'type': 'str', 'xml': {'attr': True}},
    }
    _xml_map = {
        'name': 'link', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        *,
        href: Optional[str] = None,
        rel: Optional[str] = None,
        **kwargs
    ):
        super(ResponseLink, self).__init__(**kwargs)
        self.href = href
        self.rel = rel


class ResponseTitle(msrest.serialization.Model):
    """The title of the response.

    :param type: Type of value.
    :type type: str
    :param title: Contents of the title.
    :type title: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'title': {'key': 'title', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        title: Optional[str] = None,
        **kwargs
    ):
        super(ResponseTitle, self).__init__(**kwargs)
        self.type = type
        self.title = title


class ServiceBusManagementError(msrest.serialization.Model):
    """The error response from Service Bus.

    :param code: The service error code.
    :type code: int
    :param detail: The service error message.
    :type detail: str
    """

    _attribute_map = {
        'code': {'key': 'Code', 'type': 'int'},
        'detail': {'key': 'Detail', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[int] = None,
        detail: Optional[str] = None,
        **kwargs
    ):
        super(ServiceBusManagementError, self).__init__(**kwargs)
        self.code = code
        self.detail = detail


class TopicDescription(msrest.serialization.Model):
    """Description of a Service Bus topic resource.

    :param topic_name: Name of the topic.
    :type topic_name: str
    :param authorization_rules: Authorization rules for resource.
    :type authorization_rules:
     list[~azure.servicebus.management._generated.models.AuthorizationRule]
    :param auto_delete_on_idle: ISO 8601 timeSpan idle interval after which the topic is
     automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: ~datetime.timedelta
    :param default_message_time_to_live: ISO 8601 default message timespan to live value. This is
     the duration after which the message expires, starting from when the message is sent to Service
     Bus. This is the default value used when TimeToLive is not set on a message itself.
    :type default_message_time_to_live: ~datetime.timedelta
    :param duplicate_detection_history_time_window: ISO 8601 timeSpan structure that defines the
     duration of the duplicate detection history. The default value is 10 minutes.
    :type duplicate_detection_history_time_window: ~datetime.timedelta
    :param enable_batched_operations: Value that indicates whether server-side batched operations
     are enabled.
    :type enable_batched_operations: bool
    :param enable_partitioning: A value that indicates whether the topic is to be partitioned
     across multiple message brokers.
    :type enable_partitioning: bool
    :param max_size_in_megabytes: The maximum size of the topic in megabytes, which is the size of
     memory allocated for the topic.
    :type max_size_in_megabytes: long
    :param requires_duplicate_detection: A value indicating if this topic requires duplicate
     detection.
    :type requires_duplicate_detection: bool
    :param status: Status of a Service Bus resource. Possible values include: "Active", "Creating",
     "Deleting", "Disabled", "ReceiveDisabled", "Renaming", "Restoring", "SendDisabled", "Unknown".
    :type status: str or ~azure.servicebus.management._generated.models.EntityStatus
    :param support_ordering: A value that indicates whether the topic supports ordering.
    :type support_ordering: bool
    :param user_metadata: Metadata associated with the topic.
    :type user_metadata: str
    """

    _attribute_map = {
        'topic_name': {'key': 'TopicName', 'type': 'str'},
        'authorization_rules': {'key': 'AuthorizationRules', 'type': '[AuthorizationRule]', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect', 'wrapped': True, 'itemsName': 'AuthorizationRule', 'itemsNs': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'auto_delete_on_idle': {'key': 'AutoDeleteOnIdle', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'default_message_time_to_live': {'key': 'DefaultMessageTimeToLive', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'duplicate_detection_history_time_window': {'key': 'DuplicateDetectionHistoryTimeWindow', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_batched_operations': {'key': 'EnableBatchedOperations', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_partitioning': {'key': 'EnablePartitioning', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'max_size_in_megabytes': {'key': 'MaxSizeInMegabytes', 'type': 'long'},
        'requires_duplicate_detection': {'key': 'RequiresDuplicateDetection', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'status': {'key': 'Status', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'support_ordering': {'key': 'SupportOrdering', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'user_metadata': {'key': 'UserMetadata', 'type': 'str'},
    }
    _xml_map = {
        'name': 'TopicDescription', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        *,
        topic_name: Optional[str] = None,
        authorization_rules: Optional[List["AuthorizationRule"]] = None,
        auto_delete_on_idle: Optional[datetime.timedelta] = None,
        default_message_time_to_live: Optional[datetime.timedelta] = None,
        duplicate_detection_history_time_window: Optional[datetime.timedelta] = None,
        enable_batched_operations: Optional[bool] = None,
        enable_partitioning: Optional[bool] = None,
        max_size_in_megabytes: Optional[int] = None,
        requires_duplicate_detection: Optional[bool] = None,
        status: Optional[Union[str, "EntityStatus"]] = None,
        support_ordering: Optional[bool] = None,
        user_metadata: Optional[str] = None,
        **kwargs
    ):
        super(TopicDescription, self).__init__(**kwargs)
        self.topic_name = topic_name
        self.authorization_rules = authorization_rules
        self.auto_delete_on_idle = auto_delete_on_idle
        self.default_message_time_to_live = default_message_time_to_live
        self.duplicate_detection_history_time_window = duplicate_detection_history_time_window
        self.enable_batched_operations = enable_batched_operations
        self.enable_partitioning = enable_partitioning
        self.max_size_in_megabytes = max_size_in_megabytes
        self.requires_duplicate_detection = requires_duplicate_detection
        self.status = status
        self.support_ordering = support_ordering
        self.user_metadata = user_metadata
