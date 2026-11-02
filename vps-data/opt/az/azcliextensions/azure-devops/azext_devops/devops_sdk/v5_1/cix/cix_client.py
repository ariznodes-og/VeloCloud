# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class CixClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(CixClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_configurations(self, project, repository_type=None, repository_id=None, branch=None, service_connection_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if branch is not None:
            query_parameters['branch'] = self._serialize.query('branch', branch, 'str')
        if service_connection_id is not None:
            query_parameters['serviceConnectionId'] = self._serialize.query('service_connection_id', service_connection_id, 'str')
        response = self._send(http_method='GET',
                              location_id='8fc87684-9ebc-4c37-ab92-f4ac4a58cb3a',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ConfigurationFile]', self._unwrap_collection(response))

    def create_project_connection(self, create_connection_inputs, project):
        query_parameters = {}
        if project is not None:
            query_parameters['project'] = self._serialize.query('project', project, 'str')
        content = self._serialize.body(create_connection_inputs, 'CreatePipelineConnectionInputs')
        response = self._send(http_method='POST',
                              location_id='00df4879-9216-45d5-b38d-4a487b626b2c',
                              version='5.1-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('PipelineConnection', response)

    def get_detected_build_frameworks(self, project, repository_type=None, repository_id=None, branch=None, detection_type=None, service_connection_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if branch is not None:
            query_parameters['branch'] = self._serialize.query('branch', branch, 'str')
        if detection_type is not None:
            query_parameters['detectionType'] = self._serialize.query('detection_type', detection_type, 'str')
        if service_connection_id is not None:
            query_parameters['serviceConnectionId'] = self._serialize.query('service_connection_id', service_connection_id, 'str')
        response = self._send(http_method='GET',
                              location_id='29a30bab-9efb-4652-bf1b-9269baca0980',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[DetectedBuildFramework]', self._unwrap_collection(response))

    def get_template_recommendations(self, project, repository_type=None, repository_id=None, branch=None, service_connection_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if branch is not None:
            query_parameters['branch'] = self._serialize.query('branch', branch, 'str')
        if service_connection_id is not None:
            query_parameters['serviceConnectionId'] = self._serialize.query('service_connection_id', service_connection_id, 'str')
        response = self._send(http_method='GET',
                              location_id='63ea8f13-b563-4be7-bc31-3a96eda27220',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Template]', self._unwrap_collection(response))

    def create_resources(self, creation_parameters, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(creation_parameters, '{ResourceCreationParameter}')
        response = self._send(http_method='POST',
                              location_id='43201899-7690-4870-9c79-ab69605f21ed',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CreatedResources', response)

    def render_template(self, template_parameters, template_id):
        route_values = {}
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        content = self._serialize.body(template_parameters, 'TemplateParameters')
        response = self._send(http_method='POST',
                              location_id='eb5d6d1d-98a2-4bbd-9028-f9a6b2d66515',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Template', response)

