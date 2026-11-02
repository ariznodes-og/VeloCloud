# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class CoreClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(CoreClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '79134c72-4a58-4b42-976c-04e7115f32bf'

    def create_connected_service(self, connected_service_creation_data, project_id):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        content = self._serialize.body(connected_service_creation_data, 'WebApiConnectedServiceDetails')
        response = self._send(http_method='POST',
                              location_id='b4f70219-e18b-42c5-abe3-98b07d35525e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WebApiConnectedService', response)

    def get_connected_service_details(self, project_id, name):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='b4f70219-e18b-42c5-abe3-98b07d35525e',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('WebApiConnectedServiceDetails', response)

    def get_connected_services(self, project_id, kind=None):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        query_parameters = {}
        if kind is not None:
            query_parameters['kind'] = self._serialize.query('kind', kind, 'str')
        response = self._send(http_method='GET',
                              location_id='b4f70219-e18b-42c5-abe3-98b07d35525e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WebApiConnectedService]', self._unwrap_collection(response))

    def get_team_members_with_extended_properties(self, project_id, team_id, top=None, skip=None):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if team_id is not None:
            route_values['teamId'] = self._serialize.url('team_id', team_id, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='294c494c-2600-4d7e-b76c-3dd50c3c95be',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TeamMember]', self._unwrap_collection(response))

    def get_process_by_id(self, process_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        response = self._send(http_method='GET',
                              location_id='93878975-88c5-4e6a-8abb-7ddd77a8a7d8',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('Process', response)

    def get_processes(self):
        response = self._send(http_method='GET',
                              location_id='93878975-88c5-4e6a-8abb-7ddd77a8a7d8',
                              version='5.0')
        return self._deserialize('[Process]', self._unwrap_collection(response))

    def get_project_collection(self, collection_id):
        route_values = {}
        if collection_id is not None:
            route_values['collectionId'] = self._serialize.url('collection_id', collection_id, 'str')
        response = self._send(http_method='GET',
                              location_id='8031090f-ef1d-4af6-85fc-698cd75d42bf',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('TeamProjectCollection', response)

    def get_project_collections(self, top=None, skip=None):
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='8031090f-ef1d-4af6-85fc-698cd75d42bf',
                              version='5.0',
                              query_parameters=query_parameters)
        return self._deserialize('[TeamProjectCollectionReference]', self._unwrap_collection(response))

    def get_project(self, project_id, include_capabilities=None, include_history=None):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        query_parameters = {}
        if include_capabilities is not None:
            query_parameters['includeCapabilities'] = self._serialize.query('include_capabilities', include_capabilities, 'bool')
        if include_history is not None:
            query_parameters['includeHistory'] = self._serialize.query('include_history', include_history, 'bool')
        response = self._send(http_method='GET',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TeamProject', response)

    def get_projects(self, state_filter=None, top=None, skip=None, continuation_token=None, get_default_team_image_url=None):
        query_parameters = {}
        if state_filter is not None:
            query_parameters['stateFilter'] = self._serialize.query('state_filter', state_filter, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if get_default_team_image_url is not None:
            query_parameters['getDefaultTeamImageUrl'] = self._serialize.query('get_default_team_image_url', get_default_team_image_url, 'bool')
        response = self._send(http_method='GET',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.0',
                              query_parameters=query_parameters)
        return self._deserialize('[TeamProjectReference]', self._unwrap_collection(response))

    def queue_create_project(self, project_to_create):
        content = self._serialize.body(project_to_create, 'TeamProject')
        response = self._send(http_method='POST',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.0',
                              content=content)
        return self._deserialize('OperationReference', response)

    def queue_delete_project(self, project_id):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        response = self._send(http_method='DELETE',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('OperationReference', response)

    def update_project(self, project_update, project_id):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        content = self._serialize.body(project_update, 'TeamProject')
        response = self._send(http_method='PATCH',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('OperationReference', response)

    def get_project_properties(self, project_id, keys=None):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        query_parameters = {}
        if keys is not None:
            keys = ",".join(keys)
            query_parameters['keys'] = self._serialize.query('keys', keys, 'str')
        response = self._send(http_method='GET',
                              location_id='4976a71a-4487-49aa-8aab-a1eda469037a',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ProjectProperty]', self._unwrap_collection(response))

    def set_project_properties(self, project_id, patch_document):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        content = self._serialize.body(patch_document, '[JsonPatchOperation]')
        self._send(http_method='PATCH',
                   location_id='4976a71a-4487-49aa-8aab-a1eda469037a',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content,
                   media_type='application/json-patch+json')

    def create_or_update_proxy(self, proxy):
        content = self._serialize.body(proxy, 'Proxy')
        response = self._send(http_method='PUT',
                              location_id='ec1f4311-f2b4-4c15-b2b8-8990b80d2908',
                              version='5.0-preview.2',
                              content=content)
        return self._deserialize('Proxy', response)

    def delete_proxy(self, proxy_url, site=None):
        query_parameters = {}
        if proxy_url is not None:
            query_parameters['proxyUrl'] = self._serialize.query('proxy_url', proxy_url, 'str')
        if site is not None:
            query_parameters['site'] = self._serialize.query('site', site, 'str')
        self._send(http_method='DELETE',
                   location_id='ec1f4311-f2b4-4c15-b2b8-8990b80d2908',
                   version='5.0-preview.2',
                   query_parameters=query_parameters)

    def get_proxies(self, proxy_url=None):
        query_parameters = {}
        if proxy_url is not None:
            query_parameters['proxyUrl'] = self._serialize.query('proxy_url', proxy_url, 'str')
        response = self._send(http_method='GET',
                              location_id='ec1f4311-f2b4-4c15-b2b8-8990b80d2908',
                              version='5.0-preview.2',
                              query_parameters=query_parameters)
        return self._deserialize('[Proxy]', self._unwrap_collection(response))

    def create_team(self, team, project_id):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        content = self._serialize.body(team, 'WebApiTeam')
        response = self._send(http_method='POST',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WebApiTeam', response)

    def delete_team(self, project_id, team_id):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if team_id is not None:
            route_values['teamId'] = self._serialize.url('team_id', team_id, 'str')
        self._send(http_method='DELETE',
                   location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                   version='5.0',
                   route_values=route_values)

    def get_team(self, project_id, team_id):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if team_id is not None:
            route_values['teamId'] = self._serialize.url('team_id', team_id, 'str')
        response = self._send(http_method='GET',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('WebApiTeam', response)

    def get_teams(self, project_id, mine=None, top=None, skip=None):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        query_parameters = {}
        if mine is not None:
            query_parameters['$mine'] = self._serialize.query('mine', mine, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WebApiTeam]', self._unwrap_collection(response))

    def update_team(self, team_data, project_id, team_id):
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if team_id is not None:
            route_values['teamId'] = self._serialize.url('team_id', team_id, 'str')
        content = self._serialize.body(team_data, 'WebApiTeam')
        response = self._send(http_method='PATCH',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WebApiTeam', response)

    def get_all_teams(self, mine=None, top=None, skip=None):
        query_parameters = {}
        if mine is not None:
            query_parameters['$mine'] = self._serialize.query('mine', mine, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='7a4d9ee9-3433-4347-b47a-7a80f1cf307e',
                              version='5.0-preview.2',
                              query_parameters=query_parameters)
        return self._deserialize('[WebApiTeam]', self._unwrap_collection(response))

