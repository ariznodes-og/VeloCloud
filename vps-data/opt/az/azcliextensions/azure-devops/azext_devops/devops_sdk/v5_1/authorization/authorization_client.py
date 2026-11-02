# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class AuthorizationClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(AuthorizationClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '2e426be0-da4d-48c4-9178-978da8562255'

