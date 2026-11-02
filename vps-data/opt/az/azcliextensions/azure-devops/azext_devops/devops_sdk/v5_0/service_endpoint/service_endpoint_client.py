# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class ServiceEndpointClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(ServiceEndpointClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '1814ab31-2f4f-4a9f-8761-f4d77dc5a5d7'

    def execute_service_endpoint_request(self, service_endpoint_request, project, endpoint_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if endpoint_id is not None:
            query_parameters['endpointId'] = self._serialize.query('endpoint_id', endpoint_id, 'str')
        content = self._serialize.body(service_endpoint_request, 'ServiceEndpointRequest')
        response = self._send(http_method='POST',
                              location_id='cc63bb57-2a5f-4a7a-b79c-c142d308657e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ServiceEndpointRequestResult', response)

    def create_service_endpoint(self, endpoint, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(endpoint, 'ServiceEndpoint')
        response = self._send(http_method='POST',
                              location_id='e85f1c62-adfc-4b74-b618-11a150fb195e',
                              version='5.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ServiceEndpoint', response)

    def delete_service_endpoint(self, project, endpoint_id, deep=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if endpoint_id is not None:
            route_values['endpointId'] = self._serialize.url('endpoint_id', endpoint_id, 'str')
        query_parameters = {}
        if deep is not None:
            query_parameters['deep'] = self._serialize.query('deep', deep, 'bool')
        self._send(http_method='DELETE',
                   location_id='e85f1c62-adfc-4b74-b618-11a150fb195e',
                   version='5.0-preview.2',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_service_endpoint_details(self, project, endpoint_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if endpoint_id is not None:
            route_values['endpointId'] = self._serialize.url('endpoint_id', endpoint_id, 'str')
        response = self._send(http_method='GET',
                              location_id='e85f1c62-adfc-4b74-b618-11a150fb195e',
                              version='5.0-preview.2',
                              route_values=route_values)
        return self._deserialize('ServiceEndpoint', response)

    def get_service_endpoints(self, project, type=None, auth_schemes=None, endpoint_ids=None, include_failed=None, include_details=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if auth_schemes is not None:
            auth_schemes = ",".join(auth_schemes)
            query_parameters['authSchemes'] = self._serialize.query('auth_schemes', auth_schemes, 'str')
        if endpoint_ids is not None:
            endpoint_ids = ",".join(endpoint_ids)
            query_parameters['endpointIds'] = self._serialize.query('endpoint_ids', endpoint_ids, 'str')
        if include_failed is not None:
            query_parameters['includeFailed'] = self._serialize.query('include_failed', include_failed, 'bool')
        if include_details is not None:
            query_parameters['includeDetails'] = self._serialize.query('include_details', include_details, 'bool')
        response = self._send(http_method='GET',
                              location_id='e85f1c62-adfc-4b74-b618-11a150fb195e',
                              version='5.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ServiceEndpoint]', self._unwrap_collection(response))

    def get_service_endpoints_by_names(self, project, endpoint_names, type=None, auth_schemes=None, include_failed=None, include_details=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if endpoint_names is not None:
            endpoint_names = ",".join(endpoint_names)
            query_parameters['endpointNames'] = self._serialize.query('endpoint_names', endpoint_names, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if auth_schemes is not None:
            auth_schemes = ",".join(auth_schemes)
            query_parameters['authSchemes'] = self._serialize.query('auth_schemes', auth_schemes, 'str')
        if include_failed is not None:
            query_parameters['includeFailed'] = self._serialize.query('include_failed', include_failed, 'bool')
        if include_details is not None:
            query_parameters['includeDetails'] = self._serialize.query('include_details', include_details, 'bool')
        response = self._send(http_method='GET',
                              location_id='e85f1c62-adfc-4b74-b618-11a150fb195e',
                              version='5.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ServiceEndpoint]', self._unwrap_collection(response))

    def update_service_endpoint(self, endpoint, project, endpoint_id, operation=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if endpoint_id is not None:
            route_values['endpointId'] = self._serialize.url('endpoint_id', endpoint_id, 'str')
        query_parameters = {}
        if operation is not None:
            query_parameters['operation'] = self._serialize.query('operation', operation, 'str')
        content = self._serialize.body(endpoint, 'ServiceEndpoint')
        response = self._send(http_method='PUT',
                              location_id='e85f1c62-adfc-4b74-b618-11a150fb195e',
                              version='5.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ServiceEndpoint', response)

    def update_service_endpoints(self, endpoints, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(endpoints, '[ServiceEndpoint]')
        response = self._send(http_method='PUT',
                              location_id='e85f1c62-adfc-4b74-b618-11a150fb195e',
                              version='5.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[ServiceEndpoint]', self._unwrap_collection(response))

    def get_service_endpoint_execution_records(self, project, endpoint_id, top=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if endpoint_id is not None:
            route_values['endpointId'] = self._serialize.url('endpoint_id', endpoint_id, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='10a16738-9299-4cd1-9a81-fd23ad6200d0',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ServiceEndpointExecutionRecord]', self._unwrap_collection(response))

    def get_service_endpoint_types(self, type=None, scheme=None):
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if scheme is not None:
            query_parameters['scheme'] = self._serialize.query('scheme', scheme, 'str')
        response = self._send(http_method='GET',
                              location_id='5a7938a4-655e-486c-b562-b78c54a7e87b',
                              version='5.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[ServiceEndpointType]', self._unwrap_collection(response))

