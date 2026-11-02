# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class FeatureManagementClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(FeatureManagementClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_feature(self, feature_id):
        route_values = {}
        if feature_id is not None:
            route_values['featureId'] = self._serialize.url('feature_id', feature_id, 'str')
        response = self._send(http_method='GET',
                              location_id='c4209f25-7a27-41dd-9f04-06080c7b6afd',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ContributedFeature', response)

    def get_features(self, target_contribution_id=None):
        query_parameters = {}
        if target_contribution_id is not None:
            query_parameters['targetContributionId'] = self._serialize.query('target_contribution_id', target_contribution_id, 'str')
        response = self._send(http_method='GET',
                              location_id='c4209f25-7a27-41dd-9f04-06080c7b6afd',
                              version='5.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[ContributedFeature]', self._unwrap_collection(response))

    def get_feature_state(self, feature_id, user_scope):
        route_values = {}
        if feature_id is not None:
            route_values['featureId'] = self._serialize.url('feature_id', feature_id, 'str')
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        response = self._send(http_method='GET',
                              location_id='98911314-3f9b-4eaf-80e8-83900d8e85d9',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ContributedFeatureState', response)

    def set_feature_state(self, feature, feature_id, user_scope, reason=None, reason_code=None):
        route_values = {}
        if feature_id is not None:
            route_values['featureId'] = self._serialize.url('feature_id', feature_id, 'str')
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        query_parameters = {}
        if reason is not None:
            query_parameters['reason'] = self._serialize.query('reason', reason, 'str')
        if reason_code is not None:
            query_parameters['reasonCode'] = self._serialize.query('reason_code', reason_code, 'str')
        content = self._serialize.body(feature, 'ContributedFeatureState')
        response = self._send(http_method='PATCH',
                              location_id='98911314-3f9b-4eaf-80e8-83900d8e85d9',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ContributedFeatureState', response)

    def get_feature_state_for_scope(self, feature_id, user_scope, scope_name, scope_value):
        route_values = {}
        if feature_id is not None:
            route_values['featureId'] = self._serialize.url('feature_id', feature_id, 'str')
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if scope_name is not None:
            route_values['scopeName'] = self._serialize.url('scope_name', scope_name, 'str')
        if scope_value is not None:
            route_values['scopeValue'] = self._serialize.url('scope_value', scope_value, 'str')
        response = self._send(http_method='GET',
                              location_id='dd291e43-aa9f-4cee-8465-a93c78e414a4',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ContributedFeatureState', response)

    def set_feature_state_for_scope(self, feature, feature_id, user_scope, scope_name, scope_value, reason=None, reason_code=None):
        route_values = {}
        if feature_id is not None:
            route_values['featureId'] = self._serialize.url('feature_id', feature_id, 'str')
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if scope_name is not None:
            route_values['scopeName'] = self._serialize.url('scope_name', scope_name, 'str')
        if scope_value is not None:
            route_values['scopeValue'] = self._serialize.url('scope_value', scope_value, 'str')
        query_parameters = {}
        if reason is not None:
            query_parameters['reason'] = self._serialize.query('reason', reason, 'str')
        if reason_code is not None:
            query_parameters['reasonCode'] = self._serialize.query('reason_code', reason_code, 'str')
        content = self._serialize.body(feature, 'ContributedFeatureState')
        response = self._send(http_method='PATCH',
                              location_id='dd291e43-aa9f-4cee-8465-a93c78e414a4',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ContributedFeatureState', response)

    def query_feature_states(self, query):
        content = self._serialize.body(query, 'ContributedFeatureStateQuery')
        response = self._send(http_method='POST',
                              location_id='2b4486ad-122b-400c-ae65-17b6672c1f9d',
                              version='5.0-preview.1',
                              content=content)
        return self._deserialize('ContributedFeatureStateQuery', response)

    def query_feature_states_for_default_scope(self, query, user_scope):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        content = self._serialize.body(query, 'ContributedFeatureStateQuery')
        response = self._send(http_method='POST',
                              location_id='3f810f28-03e2-4239-b0bc-788add3005e5',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ContributedFeatureStateQuery', response)

    def query_feature_states_for_named_scope(self, query, user_scope, scope_name, scope_value):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if scope_name is not None:
            route_values['scopeName'] = self._serialize.url('scope_name', scope_name, 'str')
        if scope_value is not None:
            route_values['scopeValue'] = self._serialize.url('scope_value', scope_value, 'str')
        content = self._serialize.body(query, 'ContributedFeatureStateQuery')
        response = self._send(http_method='POST',
                              location_id='f29e997b-c2da-4d15-8380-765788a1a74c',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ContributedFeatureStateQuery', response)

