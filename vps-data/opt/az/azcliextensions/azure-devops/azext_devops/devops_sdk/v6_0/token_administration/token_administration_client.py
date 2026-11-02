# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class TokenAdministrationClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(TokenAdministrationClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '95935461-9e54-44bd-b9fb-04f4dd05d640'

    def list_identities_with_global_access_tokens(self, revocations, is_public=None):
        query_parameters = {}
        if is_public is not None:
            query_parameters['isPublic'] = self._serialize.query('is_public', is_public, 'bool')
        content = self._serialize.body(revocations, '[TokenAdminRevocation]')
        response = self._send(http_method='POST',
                              location_id='30d3a12b-66c3-4669-b016-ecb0706c8d0f',
                              version='6.0-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def list_personal_access_tokens(self, audience, subject_descriptor, page_size=None, continuation_token=None, is_public=None):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        query_parameters = {}
        if page_size is not None:
            query_parameters['pageSize'] = self._serialize.query('page_size', page_size, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if is_public is not None:
            query_parameters['isPublic'] = self._serialize.query('is_public', is_public, 'bool')
        content = self._serialize.body(audience, '[str]')
        response = self._send(http_method='POST',
                              location_id='1bb7db14-87c5-4762-bf77-a70ad34a9ab3',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TokenAdminPagedSessionTokens', response)

    def revoke_authorizations(self, revocations, host_id, is_public=None):
        query_parameters = {}
        if host_id is not None:
            query_parameters['hostId'] = self._serialize.query('host_id', host_id, 'str')
        if is_public is not None:
            query_parameters['isPublic'] = self._serialize.query('is_public', is_public, 'bool')
        content = self._serialize.body(revocations, 'TokenAdministrationRevocation')
        response = self._send(http_method='POST',
                              location_id='a2e4520b-1cc8-4526-871e-f3a8f865f221',
                              version='6.0-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[SessionToken]', self._unwrap_collection(response))

