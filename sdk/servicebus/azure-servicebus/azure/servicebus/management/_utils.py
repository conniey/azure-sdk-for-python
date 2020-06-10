from typing import cast, Union
from xml.etree.ElementTree import ElementTree

from azure.core.exceptions import ResourceNotFoundError

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse  # python 2.7

from azure.servicebus.management import _constants as constants
from ._handle_response_error import _handle_response_error


def convert_to_external(entity_class, entry):
    qd = entity_class._from_internal_entity(entry.content.queue_description)
    qd.queue_name = entry.title
    return qd


def extract_data_template(feed_class, entity_class, feed_element):
    deserialized = feed_class.deserialize(feed_element)
    list_of_qd = [convert_to_external(entity_class, x) for x in deserialized.entry]
    next_link = None
    if deserialized.link and len(deserialized.link) == 2:
        next_link = deserialized.link[1].href
    return next_link, iter(list_of_qd)


def get_next_template(list_func, *args, **kwargs):
    if len(args) > 0:
        next_link = args[0]
    else:
        next_link = kwargs.pop("next_link")
    if not next_link:
        start_index = kwargs.pop("start_index", 0)
        max_count = kwargs.pop("max_count", 100)
        api_version = constants.API_VERSION
    else:
        queries = urlparse.parse_qs(urlparse.urlparse(next_link).query)
        start_index = int(queries['$skip'][0])
        max_count = int(queries['$top'][0])
        api_version = queries['api-version'][0]
    with _handle_response_error():
        feed_element = cast(
            ElementTree,
            list_func(
                entity_type=constants.ENTITY_TYPE_QUEUES, skip=start_index, top=max_count,
                api_version=api_version
            )
        )
    return feed_element
