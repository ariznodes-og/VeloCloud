# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class TokenAdminClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(TokenAdminClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'af68438b-ed04-4407-9eb6-f1dbae3f922e'

    def list_personal_access_tokens(self, subject_descriptor, page_size=None, continuation_token=None, is_public=None):
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
        response = self._send(http_method='GET',
                              location_id='af68438b-ed04-4407-9eb6-f1dbae3f922e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TokenAdminPagedSessionTokens', response)

    def create_revocation_rule(self, revocation_rule):
        content = self._serialize.body(revocation_rule, 'TokenAdminRevocationRule')
        self._send(http_method='POST',
                   location_id='ee4afb16-e7ab-4ed8-9d4b-4ef3e78f97e4',
                   version='5.0-preview.1',
                   content=content)

    def revoke_authorizations(self, revocations, is_public=None):
        query_parameters = {}
        if is_public is not None:
            query_parameters['isPublic'] = self._serialize.query('is_public', is_public, 'bool')
        content = self._serialize.body(revocations, '[TokenAdminRevocation]')
        self._send(http_method='POST',
                   location_id='a9c08b2c-5466-4e22-8626-1ff304ffdf0f',
                   version='5.0-preview.1',
                   query_parameters=query_parameters,
                   content=content)

