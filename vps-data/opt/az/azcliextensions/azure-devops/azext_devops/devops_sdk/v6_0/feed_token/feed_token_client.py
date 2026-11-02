# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class FeedTokenClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(FeedTokenClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'cdeb6c7d-6b25-4d6f-b664-c2e3ede202e8'

    def get_personal_access_token(self, feed_name=None):
        route_values = {}
        if feed_name is not None:
            route_values['feedName'] = self._serialize.url('feed_name', feed_name, 'str')
        response = self._send(http_method='GET',
                              location_id='dfdb7ad7-3d8e-4907-911e-19b4a8330550',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('FeedSessionToken', response)

