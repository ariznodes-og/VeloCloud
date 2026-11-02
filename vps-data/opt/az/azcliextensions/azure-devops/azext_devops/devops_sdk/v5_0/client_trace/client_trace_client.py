# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class ClientTraceClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(ClientTraceClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def publish_events(self, events):
        content = self._serialize.body(events, '[ClientTraceEvent]')
        self._send(http_method='POST',
                   location_id='06bcc74a-1491-4eb8-a0eb-704778f9d041',
                   version='5.0-preview.1',
                   content=content)

