# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class FeatureAvailabilityClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(FeatureAvailabilityClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_all_feature_flags(self, user_email=None):
        query_parameters = {}
        if user_email is not None:
            query_parameters['userEmail'] = self._serialize.query('user_email', user_email, 'str')
        response = self._send(http_method='GET',
                              location_id='3e2b80f8-9e6f-441e-8393-005610692d9c',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[FeatureFlag]', self._unwrap_collection(response))

    def get_feature_flag_by_name(self, name, check_feature_exists=None):
        route_values = {}
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        query_parameters = {}
        if check_feature_exists is not None:
            query_parameters['checkFeatureExists'] = self._serialize.query('check_feature_exists', check_feature_exists, 'bool')
        response = self._send(http_method='GET',
                              location_id='3e2b80f8-9e6f-441e-8393-005610692d9c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('FeatureFlag', response)

    def get_feature_flag_by_name_and_user_email(self, name, user_email, check_feature_exists=None):
        route_values = {}
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        query_parameters = {}
        if user_email is not None:
            query_parameters['userEmail'] = self._serialize.query('user_email', user_email, 'str')
        if check_feature_exists is not None:
            query_parameters['checkFeatureExists'] = self._serialize.query('check_feature_exists', check_feature_exists, 'bool')
        response = self._send(http_method='GET',
                              location_id='3e2b80f8-9e6f-441e-8393-005610692d9c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('FeatureFlag', response)

    def get_feature_flag_by_name_and_user_id(self, name, user_id, check_feature_exists=None):
        route_values = {}
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        query_parameters = {}
        if user_id is not None:
            query_parameters['userId'] = self._serialize.query('user_id', user_id, 'str')
        if check_feature_exists is not None:
            query_parameters['checkFeatureExists'] = self._serialize.query('check_feature_exists', check_feature_exists, 'bool')
        response = self._send(http_method='GET',
                              location_id='3e2b80f8-9e6f-441e-8393-005610692d9c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('FeatureFlag', response)

    def update_feature_flag(self, state, name, user_email=None, check_feature_exists=None, set_at_application_level_also=None):
        route_values = {}
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        query_parameters = {}
        if user_email is not None:
            query_parameters['userEmail'] = self._serialize.query('user_email', user_email, 'str')
        if check_feature_exists is not None:
            query_parameters['checkFeatureExists'] = self._serialize.query('check_feature_exists', check_feature_exists, 'bool')
        if set_at_application_level_also is not None:
            query_parameters['setAtApplicationLevelAlso'] = self._serialize.query('set_at_application_level_also', set_at_application_level_also, 'bool')
        content = self._serialize.body(state, 'FeatureFlagPatch')
        response = self._send(http_method='PATCH',
                              location_id='3e2b80f8-9e6f-441e-8393-005610692d9c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('FeatureFlag', response)

