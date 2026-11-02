# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class PipelinesChecksClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(PipelinesChecksClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '4a933897-0488-45af-bd82-6fd3ad33f46a'

    def add_check_configuration(self, configuration, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(configuration, 'CheckConfiguration')
        response = self._send(http_method='POST',
                              location_id='86c8381e-5aee-4cde-8ae4-25c0c7f5eaea',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CheckConfiguration', response)

    def delete_check_configuration(self, project, id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        self._send(http_method='DELETE',
                   location_id='86c8381e-5aee-4cde-8ae4-25c0c7f5eaea',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_check_configuration(self, project, id, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='86c8381e-5aee-4cde-8ae4-25c0c7f5eaea',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CheckConfiguration', response)

    def get_check_configurations_on_resource(self, project, resource_type=None, resource_id=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if resource_type is not None:
            query_parameters['resourceType'] = self._serialize.query('resource_type', resource_type, 'str')
        if resource_id is not None:
            query_parameters['resourceId'] = self._serialize.query('resource_id', resource_id, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='86c8381e-5aee-4cde-8ae4-25c0c7f5eaea',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[CheckConfiguration]', self._unwrap_collection(response))

    def update_check_configuration(self, configuration, project, id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        content = self._serialize.body(configuration, 'CheckConfiguration')
        response = self._send(http_method='PATCH',
                              location_id='86c8381e-5aee-4cde-8ae4-25c0c7f5eaea',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CheckConfiguration', response)

    def query_check_configurations_on_resources(self, resources, project, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        content = self._serialize.body(resources, '[Resource]')
        response = self._send(http_method='POST',
                              location_id='5f3d0e64-f943-4584-8811-77eb495e831e',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[CheckConfiguration]', self._unwrap_collection(response))

    def evaluate_check_suite(self, request, project, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        content = self._serialize.body(request, 'CheckSuiteRequest')
        response = self._send(http_method='POST',
                              location_id='91282c1d-c183-444f-9554-1485bfb3879d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('CheckSuite', response)

    def get_check_suite(self, project, check_suite_id, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if check_suite_id is not None:
            route_values['checkSuiteId'] = self._serialize.url('check_suite_id', check_suite_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='91282c1d-c183-444f-9554-1485bfb3879d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CheckSuite', response)

