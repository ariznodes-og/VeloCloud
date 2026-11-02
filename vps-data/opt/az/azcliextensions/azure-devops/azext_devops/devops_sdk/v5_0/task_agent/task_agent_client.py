# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class TaskAgentClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(TaskAgentClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'a85b8835-c1a1-4aac-ae97-1c3d0ba72dbd'

    def add_agent_cloud(self, agent_cloud):
        content = self._serialize.body(agent_cloud, 'TaskAgentCloud')
        response = self._send(http_method='POST',
                              location_id='bfa72b3d-0fc6-43fb-932b-a7f6559f93b9',
                              version='5.0-preview.1',
                              content=content)
        return self._deserialize('TaskAgentCloud', response)

    def delete_agent_cloud(self, agent_cloud_id):
        route_values = {}
        if agent_cloud_id is not None:
            route_values['agentCloudId'] = self._serialize.url('agent_cloud_id', agent_cloud_id, 'int')
        response = self._send(http_method='DELETE',
                              location_id='bfa72b3d-0fc6-43fb-932b-a7f6559f93b9',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('TaskAgentCloud', response)

    def get_agent_cloud(self, agent_cloud_id):
        route_values = {}
        if agent_cloud_id is not None:
            route_values['agentCloudId'] = self._serialize.url('agent_cloud_id', agent_cloud_id, 'int')
        response = self._send(http_method='GET',
                              location_id='bfa72b3d-0fc6-43fb-932b-a7f6559f93b9',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('TaskAgentCloud', response)

    def get_agent_clouds(self):
        response = self._send(http_method='GET',
                              location_id='bfa72b3d-0fc6-43fb-932b-a7f6559f93b9',
                              version='5.0-preview.1')
        return self._deserialize('[TaskAgentCloud]', self._unwrap_collection(response))

    def get_agent_cloud_types(self):
        response = self._send(http_method='GET',
                              location_id='5932e193-f376-469d-9c3e-e5588ce12cb5',
                              version='5.0-preview.1')
        return self._deserialize('[TaskAgentCloudType]', self._unwrap_collection(response))

    def add_deployment_group(self, deployment_group, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(deployment_group, 'DeploymentGroupCreateParameter')
        response = self._send(http_method='POST',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentGroup', response)

    def delete_deployment_group(self, project, deployment_group_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        self._send(http_method='DELETE',
                   location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                   version='5.0-preview.1',
                   route_values=route_values)

    def get_deployment_group(self, project, deployment_group_id, action_filter=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeploymentGroup', response)

    def get_deployment_groups(self, project, name=None, action_filter=None, expand=None, continuation_token=None, top=None, ids=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        response = self._send(http_method='GET',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[DeploymentGroup]', self._unwrap_collection(response))

    def update_deployment_group(self, deployment_group, project, deployment_group_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(deployment_group, 'DeploymentGroupUpdateParameter')
        response = self._send(http_method='PATCH',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentGroup', response)

    def get_agent_cloud_requests(self, agent_cloud_id):
        route_values = {}
        if agent_cloud_id is not None:
            route_values['agentCloudId'] = self._serialize.url('agent_cloud_id', agent_cloud_id, 'int')
        response = self._send(http_method='GET',
                              location_id='20189bd7-5134-49c2-b8e9-f9e856eea2b2',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[TaskAgentCloudRequest]', self._unwrap_collection(response))

    def delete_deployment_target(self, project, deployment_group_id, target_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if target_id is not None:
            route_values['targetId'] = self._serialize.url('target_id', target_id, 'int')
        self._send(http_method='DELETE',
                   location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                   version='5.0-preview.1',
                   route_values=route_values)

    def get_deployment_target(self, project, deployment_group_id, target_id, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if target_id is not None:
            route_values['targetId'] = self._serialize.url('target_id', target_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeploymentMachine', response)

    def get_deployment_targets(self, project, deployment_group_id, tags=None, name=None, partial_name_match=None, expand=None, agent_status=None, agent_job_result=None, continuation_token=None, top=None, enabled=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if tags is not None:
            tags = ",".join(tags)
            query_parameters['tags'] = self._serialize.query('tags', tags, 'str')
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if partial_name_match is not None:
            query_parameters['partialNameMatch'] = self._serialize.query('partial_name_match', partial_name_match, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if agent_status is not None:
            query_parameters['agentStatus'] = self._serialize.query('agent_status', agent_status, 'str')
        if agent_job_result is not None:
            query_parameters['agentJobResult'] = self._serialize.query('agent_job_result', agent_job_result, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if enabled is not None:
            query_parameters['enabled'] = self._serialize.query('enabled', enabled, 'bool')
        response = self._send(http_method='GET',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[DeploymentMachine]', self._unwrap_collection(response))

    def update_deployment_targets(self, machines, project, deployment_group_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(machines, '[DeploymentTargetUpdateParameter]')
        response = self._send(http_method='PATCH',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[DeploymentMachine]', self._unwrap_collection(response))

    def add_task_group(self, task_group, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(task_group, 'TaskGroupCreateParameter')
        response = self._send(http_method='POST',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskGroup', response)

    def delete_task_group(self, project, task_group_id, comment=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        self._send(http_method='DELETE',
                   location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                   version='5.0-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_task_groups(self, project, task_group_id=None, expanded=None, task_id_filter=None, deleted=None, top=None, continuation_token=None, query_order=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        query_parameters = {}
        if expanded is not None:
            query_parameters['expanded'] = self._serialize.query('expanded', expanded, 'bool')
        if task_id_filter is not None:
            query_parameters['taskIdFilter'] = self._serialize.query('task_id_filter', task_id_filter, 'str')
        if deleted is not None:
            query_parameters['deleted'] = self._serialize.query('deleted', deleted, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'iso-8601')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        response = self._send(http_method='GET',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TaskGroup]', self._unwrap_collection(response))

    def update_task_group(self, task_group, project, task_group_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        content = self._serialize.body(task_group, 'TaskGroupUpdateParameter')
        response = self._send(http_method='PUT',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskGroup', response)

    def add_variable_group(self, group, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(group, 'VariableGroupParameters')
        response = self._send(http_method='POST',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('VariableGroup', response)

    def delete_variable_group(self, project, group_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        self._send(http_method='DELETE',
                   location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                   version='5.0-preview.1',
                   route_values=route_values)

    def get_variable_group(self, project, group_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('VariableGroup', response)

    def get_variable_groups(self, project, group_name=None, action_filter=None, top=None, continuation_token=None, query_order=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if group_name is not None:
            query_parameters['groupName'] = self._serialize.query('group_name', group_name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'int')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[VariableGroup]', self._unwrap_collection(response))

    def get_variable_groups_by_id(self, project, group_ids):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if group_ids is not None:
            group_ids = ",".join(map(str, group_ids))
            query_parameters['groupIds'] = self._serialize.query('group_ids', group_ids, 'str')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[VariableGroup]', self._unwrap_collection(response))

    def update_variable_group(self, group, project, group_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        content = self._serialize.body(group, 'VariableGroupParameters')
        response = self._send(http_method='PUT',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('VariableGroup', response)

