# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class PolicyClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(PolicyClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'fb13a388-40dd-4a04-b530-013a739c72ef'

    def create_policy_configuration(self, configuration, project, configuration_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        content = self._serialize.body(configuration, 'PolicyConfiguration')
        response = self._send(http_method='POST',
                              location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('PolicyConfiguration', response)

    def delete_policy_configuration(self, project, configuration_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        self._send(http_method='DELETE',
                   location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                   version='5.1',
                   route_values=route_values)

    def get_policy_configuration(self, project, configuration_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        response = self._send(http_method='GET',
                              location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('PolicyConfiguration', response)

    def get_policy_configurations(self, project, scope=None, top=None, continuation_token=None, policy_type=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if scope is not None:
            query_parameters['scope'] = self._serialize.query('scope', scope, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if policy_type is not None:
            query_parameters['policyType'] = self._serialize.query('policy_type', policy_type, 'str')
        response = self._send(http_method='GET',
                              location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[PolicyConfiguration]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetPolicyConfigurationsResponseValue(response_value, continuation_token)

    class GetPolicyConfigurationsResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def update_policy_configuration(self, configuration, project, configuration_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        content = self._serialize.body(configuration, 'PolicyConfiguration')
        response = self._send(http_method='PUT',
                              location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('PolicyConfiguration', response)

    def get_policy_evaluation(self, project, evaluation_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if evaluation_id is not None:
            route_values['evaluationId'] = self._serialize.url('evaluation_id', evaluation_id, 'str')
        response = self._send(http_method='GET',
                              location_id='46aecb7a-5d2c-4647-897b-0209505a9fe4',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('PolicyEvaluationRecord', response)

    def requeue_policy_evaluation(self, project, evaluation_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if evaluation_id is not None:
            route_values['evaluationId'] = self._serialize.url('evaluation_id', evaluation_id, 'str')
        response = self._send(http_method='PATCH',
                              location_id='46aecb7a-5d2c-4647-897b-0209505a9fe4',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('PolicyEvaluationRecord', response)

    def get_policy_evaluations(self, project, artifact_id, include_not_applicable=None, top=None, skip=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if artifact_id is not None:
            query_parameters['artifactId'] = self._serialize.query('artifact_id', artifact_id, 'str')
        if include_not_applicable is not None:
            query_parameters['includeNotApplicable'] = self._serialize.query('include_not_applicable', include_not_applicable, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='c23ddff5-229c-4d04-a80b-0fdce9f360c8',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[PolicyEvaluationRecord]', self._unwrap_collection(response))

    def get_policy_configuration_revision(self, project, configuration_id, revision_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        if revision_id is not None:
            route_values['revisionId'] = self._serialize.url('revision_id', revision_id, 'int')
        response = self._send(http_method='GET',
                              location_id='fe1e68a2-60d3-43cb-855b-85e41ae97c95',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('PolicyConfiguration', response)

    def get_policy_configuration_revisions(self, project, configuration_id, top=None, skip=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='fe1e68a2-60d3-43cb-855b-85e41ae97c95',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[PolicyConfiguration]', self._unwrap_collection(response))

    def get_policy_type(self, project, type_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type_id is not None:
            route_values['typeId'] = self._serialize.url('type_id', type_id, 'str')
        response = self._send(http_method='GET',
                              location_id='44096322-2d3d-466a-bb30-d1b7de69f61f',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('PolicyType', response)

    def get_policy_types(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='44096322-2d3d-466a-bb30-d1b7de69f61f',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[PolicyType]', self._unwrap_collection(response))

