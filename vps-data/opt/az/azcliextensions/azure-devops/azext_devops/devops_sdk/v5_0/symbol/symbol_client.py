# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class SymbolClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(SymbolClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'af607f94-69ba-4821-8159-f04e37b66350'

    def check_availability(self):
        self._send(http_method='GET',
                   location_id='97c893cc-e861-4ef4-8c43-9bad4a963dee',
                   version='5.0-preview.1')

    def get_client(self, client_type):
        route_values = {}
        if client_type is not None:
            route_values['clientType'] = self._serialize.url('client_type', client_type, 'str')
        response = self._send(http_method='GET',
                              location_id='79c83865-4de3-460c-8a16-01be238e0818',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('object', response)

    def head_client(self):
        self._send(http_method='HEAD',
                   location_id='79c83865-4de3-460c-8a16-01be238e0818',
                   version='5.0-preview.1')

    def create_requests(self, request_to_create):
        content = self._serialize.body(request_to_create, 'Request')
        response = self._send(http_method='POST',
                              location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                              version='5.0-preview.1',
                              content=content)
        return self._deserialize('Request', response)

    def create_requests_request_id_debug_entries(self, batch, request_id, collection):
        route_values = {}
        if request_id is not None:
            route_values['requestId'] = self._serialize.url('request_id', request_id, 'str')
        query_parameters = {}
        if collection is not None:
            query_parameters['collection'] = self._serialize.query('collection', collection, 'str')
        content = self._serialize.body(batch, 'DebugEntryCreateBatch')
        response = self._send(http_method='POST',
                              location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[DebugEntry]', self._unwrap_collection(response))

    def create_requests_request_name_debug_entries(self, batch, request_name, collection):
        query_parameters = {}
        if request_name is not None:
            query_parameters['requestName'] = self._serialize.query('request_name', request_name, 'str')
        if collection is not None:
            query_parameters['collection'] = self._serialize.query('collection', collection, 'str')
        content = self._serialize.body(batch, 'DebugEntryCreateBatch')
        response = self._send(http_method='POST',
                              location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                              version='5.0-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[DebugEntry]', self._unwrap_collection(response))

    def delete_requests_request_id(self, request_id, synchronous=None):
        route_values = {}
        if request_id is not None:
            route_values['requestId'] = self._serialize.url('request_id', request_id, 'str')
        query_parameters = {}
        if synchronous is not None:
            query_parameters['synchronous'] = self._serialize.query('synchronous', synchronous, 'bool')
        self._send(http_method='DELETE',
                   location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                   version='5.0-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def delete_requests_request_name(self, request_name, synchronous=None):
        query_parameters = {}
        if request_name is not None:
            query_parameters['requestName'] = self._serialize.query('request_name', request_name, 'str')
        if synchronous is not None:
            query_parameters['synchronous'] = self._serialize.query('synchronous', synchronous, 'bool')
        self._send(http_method='DELETE',
                   location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                   version='5.0-preview.1',
                   query_parameters=query_parameters)

    def get_requests_request_id(self, request_id):
        route_values = {}
        if request_id is not None:
            route_values['requestId'] = self._serialize.url('request_id', request_id, 'str')
        response = self._send(http_method='GET',
                              location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('Request', response)

    def get_requests_request_name(self, request_name):
        query_parameters = {}
        if request_name is not None:
            query_parameters['requestName'] = self._serialize.query('request_name', request_name, 'str')
        response = self._send(http_method='GET',
                              location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                              version='5.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('Request', response)

    def update_requests_request_id(self, update_request, request_id):
        route_values = {}
        if request_id is not None:
            route_values['requestId'] = self._serialize.url('request_id', request_id, 'str')
        content = self._serialize.body(update_request, 'Request')
        response = self._send(http_method='PATCH',
                              location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Request', response)

    def update_requests_request_name(self, update_request, request_name):
        query_parameters = {}
        if request_name is not None:
            query_parameters['requestName'] = self._serialize.query('request_name', request_name, 'str')
        content = self._serialize.body(update_request, 'Request')
        response = self._send(http_method='PATCH',
                              location_id='ebc09fe3-1b20-4667-abc5-f2b60fe8de52',
                              version='5.0-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Request', response)

    def get_sym_srv_debug_entry_client_key(self, debug_entry_client_key):
        route_values = {}
        if debug_entry_client_key is not None:
            route_values['debugEntryClientKey'] = self._serialize.url('debug_entry_client_key', debug_entry_client_key, 'str')
        self._send(http_method='GET',
                   location_id='9648e256-c9f9-4f16-8a27-630b06396942',
                   version='5.0-preview.1',
                   route_values=route_values)

