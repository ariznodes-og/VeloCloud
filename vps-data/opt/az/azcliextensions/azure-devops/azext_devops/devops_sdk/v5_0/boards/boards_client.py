# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class BoardsClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(BoardsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '11635d5f-a4f9-43ea-a48b-d56be43fee0f'

