# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class BuildClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(BuildClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '965220d5-5bb9-42cf-8d67-9b146df2a5a4'

    def create_artifact(self, artifact, project, build_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(artifact, 'BuildArtifact')
        response = self._send(http_method='POST',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildArtifact', response)

    def get_artifact(self, project, build_id, artifact_name):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildArtifact', response)

    def get_artifact_content_zip(self, project, build_id, artifact_name, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_artifacts(self, project, build_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BuildArtifact]', self._unwrap_collection(response))

    def get_file(self, project, build_id, artifact_name, file_id, file_name, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        if file_id is not None:
            query_parameters['fileId'] = self._serialize.query('file_id', file_id, 'str')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_attachments(self, project, build_id, type):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='f2192269-89fa-4f94-baf6-8fb128c55159',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[Attachment]', self._unwrap_collection(response))

    def get_attachment(self, project, build_id, timeline_id, record_id, type, name, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        if record_id is not None:
            route_values['recordId'] = self._serialize.url('record_id', record_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='af5122d3-3438-485e-a25a-2dbbfde84ee6',
                              version='5.1-preview.2',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def authorize_project_resources(self, resources, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(resources, '[DefinitionResourceReference]')
        response = self._send(http_method='PATCH',
                              location_id='398c85bc-81aa-4822-947c-a194a05f0fef',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[DefinitionResourceReference]', self._unwrap_collection(response))

    def get_project_resources(self, project, type=None, id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if id is not None:
            query_parameters['id'] = self._serialize.query('id', id, 'str')
        response = self._send(http_method='GET',
                              location_id='398c85bc-81aa-4822-947c-a194a05f0fef',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[DefinitionResourceReference]', self._unwrap_collection(response))

    def list_branches(self, project, provider_name, service_endpoint_id=None, repository=None, branch_name=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='e05d4403-9b81-4244-8763-20fde28d1976',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_build_badge(self, project, repo_type, repo_id=None, branch_name=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repo_type is not None:
            route_values['repoType'] = self._serialize.url('repo_type', repo_type, 'str')
        query_parameters = {}
        if repo_id is not None:
            query_parameters['repoId'] = self._serialize.query('repo_id', repo_id, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='21b3b9ce-fad5-4567-9ad0-80679794e003',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildBadge', response)

    def get_build_badge_data(self, project, repo_type, repo_id=None, branch_name=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repo_type is not None:
            route_values['repoType'] = self._serialize.url('repo_type', repo_type, 'str')
        query_parameters = {}
        if repo_id is not None:
            query_parameters['repoId'] = self._serialize.query('repo_id', repo_id, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='21b3b9ce-fad5-4567-9ad0-80679794e003',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('str', response)

    def delete_build(self, project, build_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        self._send(http_method='DELETE',
                   location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                   version='5.1',
                   route_values=route_values)

    def get_build(self, project, build_id, property_filters=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if property_filters is not None:
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Build', response)

    def get_builds(self, project, definitions=None, queues=None, build_number=None, min_time=None, max_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definitions is not None:
            definitions = ",".join(map(str, definitions))
            query_parameters['definitions'] = self._serialize.query('definitions', definitions, 'str')
        if queues is not None:
            queues = ",".join(map(str, queues))
            query_parameters['queues'] = self._serialize.query('queues', queues, 'str')
        if build_number is not None:
            query_parameters['buildNumber'] = self._serialize.query('build_number', build_number, 'str')
        if min_time is not None:
            query_parameters['minTime'] = self._serialize.query('min_time', min_time, 'iso-8601')
        if max_time is not None:
            query_parameters['maxTime'] = self._serialize.query('max_time', max_time, 'iso-8601')
        if requested_for is not None:
            query_parameters['requestedFor'] = self._serialize.query('requested_for', requested_for, 'str')
        if reason_filter is not None:
            query_parameters['reasonFilter'] = self._serialize.query('reason_filter', reason_filter, 'str')
        if status_filter is not None:
            query_parameters['statusFilter'] = self._serialize.query('status_filter', status_filter, 'str')
        if result_filter is not None:
            query_parameters['resultFilter'] = self._serialize.query('result_filter', result_filter, 'str')
        if tag_filters is not None:
            tag_filters = ",".join(tag_filters)
            query_parameters['tagFilters'] = self._serialize.query('tag_filters', tag_filters, 'str')
        if properties is not None:
            properties = ",".join(properties)
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if max_builds_per_definition is not None:
            query_parameters['maxBuildsPerDefinition'] = self._serialize.query('max_builds_per_definition', max_builds_per_definition, 'int')
        if deleted_filter is not None:
            query_parameters['deletedFilter'] = self._serialize.query('deleted_filter', deleted_filter, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        if build_ids is not None:
            build_ids = ",".join(map(str, build_ids))
            query_parameters['buildIds'] = self._serialize.query('build_ids', build_ids, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        response = self._send(http_method='GET',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[Build]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetBuildsResponseValue(response_value, continuation_token)

    class GetBuildsResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def queue_build(self, build, project, ignore_warnings=None, check_in_ticket=None, source_build_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ignore_warnings is not None:
            query_parameters['ignoreWarnings'] = self._serialize.query('ignore_warnings', ignore_warnings, 'bool')
        if check_in_ticket is not None:
            query_parameters['checkInTicket'] = self._serialize.query('check_in_ticket', check_in_ticket, 'str')
        if source_build_id is not None:
            query_parameters['sourceBuildId'] = self._serialize.query('source_build_id', source_build_id, 'int')
        content = self._serialize.body(build, 'Build')
        response = self._send(http_method='POST',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Build', response)

    def update_build(self, build, project, build_id, retry=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if retry is not None:
            query_parameters['retry'] = self._serialize.query('retry', retry, 'bool')
        content = self._serialize.body(build, 'Build')
        response = self._send(http_method='PATCH',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Build', response)

    def update_builds(self, builds, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(builds, '[Build]')
        response = self._send(http_method='PATCH',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[Build]', self._unwrap_collection(response))

    def get_build_changes(self, project, build_id, continuation_token=None, top=None, include_source_change=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if include_source_change is not None:
            query_parameters['includeSourceChange'] = self._serialize.query('include_source_change', include_source_change, 'bool')
        response = self._send(http_method='GET',
                              location_id='54572c7b-bbd3-45d4-80dc-28be08941620',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[Change]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetBuildChangesResponseValue(response_value, continuation_token)

    class GetBuildChangesResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def get_changes_between_builds(self, project, from_build_id=None, to_build_id=None, top=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if from_build_id is not None:
            query_parameters['fromBuildId'] = self._serialize.query('from_build_id', from_build_id, 'int')
        if to_build_id is not None:
            query_parameters['toBuildId'] = self._serialize.query('to_build_id', to_build_id, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='f10f0ea5-18a1-43ec-a8fb-2042c7be9b43',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Change]', self._unwrap_collection(response))

    def get_build_controller(self, controller_id):
        route_values = {}
        if controller_id is not None:
            route_values['controllerId'] = self._serialize.url('controller_id', controller_id, 'int')
        response = self._send(http_method='GET',
                              location_id='fcac1932-2ee1-437f-9b6f-7f696be858f6',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('BuildController', response)

    def get_build_controllers(self, name=None):
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='fcac1932-2ee1-437f-9b6f-7f696be858f6',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[BuildController]', self._unwrap_collection(response))

    def create_definition(self, definition, project, definition_to_clone_id=None, definition_to_clone_revision=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definition_to_clone_id is not None:
            query_parameters['definitionToCloneId'] = self._serialize.query('definition_to_clone_id', definition_to_clone_id, 'int')
        if definition_to_clone_revision is not None:
            query_parameters['definitionToCloneRevision'] = self._serialize.query('definition_to_clone_revision', definition_to_clone_revision, 'int')
        content = self._serialize.body(definition, 'BuildDefinition')
        response = self._send(http_method='POST',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('BuildDefinition', response)

    def delete_definition(self, project, definition_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        self._send(http_method='DELETE',
                   location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                   version='5.1',
                   route_values=route_values)

    def get_definition(self, project, definition_id, revision=None, min_metrics_time=None, property_filters=None, include_latest_builds=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        response = self._send(http_method='GET',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildDefinition', response)

    def get_definitions(self, project, name=None, repository_id=None, repository_type=None, query_order=None, top=None, continuation_token=None, min_metrics_time=None, definition_ids=None, path=None, built_after=None, not_built_after=None, include_all_properties=None, include_latest_builds=None, task_id_filter=None, process_type=None, yaml_filename=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        if definition_ids is not None:
            definition_ids = ",".join(map(str, definition_ids))
            query_parameters['definitionIds'] = self._serialize.query('definition_ids', definition_ids, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if built_after is not None:
            query_parameters['builtAfter'] = self._serialize.query('built_after', built_after, 'iso-8601')
        if not_built_after is not None:
            query_parameters['notBuiltAfter'] = self._serialize.query('not_built_after', not_built_after, 'iso-8601')
        if include_all_properties is not None:
            query_parameters['includeAllProperties'] = self._serialize.query('include_all_properties', include_all_properties, 'bool')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        if task_id_filter is not None:
            query_parameters['taskIdFilter'] = self._serialize.query('task_id_filter', task_id_filter, 'str')
        if process_type is not None:
            query_parameters['processType'] = self._serialize.query('process_type', process_type, 'int')
        if yaml_filename is not None:
            query_parameters['yamlFilename'] = self._serialize.query('yaml_filename', yaml_filename, 'str')
        response = self._send(http_method='GET',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[BuildDefinitionReference]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetDefinitionsResponseValue(response_value, continuation_token)

    class GetDefinitionsResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def restore_definition(self, project, definition_id, deleted):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if deleted is not None:
            query_parameters['deleted'] = self._serialize.query('deleted', deleted, 'bool')
        response = self._send(http_method='PATCH',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildDefinition', response)

    def update_definition(self, definition, project, definition_id, secrets_source_definition_id=None, secrets_source_definition_revision=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if secrets_source_definition_id is not None:
            query_parameters['secretsSourceDefinitionId'] = self._serialize.query('secrets_source_definition_id', secrets_source_definition_id, 'int')
        if secrets_source_definition_revision is not None:
            query_parameters['secretsSourceDefinitionRevision'] = self._serialize.query('secrets_source_definition_revision', secrets_source_definition_revision, 'int')
        content = self._serialize.body(definition, 'BuildDefinition')
        response = self._send(http_method='PUT',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('BuildDefinition', response)

    def get_file_contents(self, project, provider_name, service_endpoint_id=None, repository=None, commit_or_branch=None, path=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        if commit_or_branch is not None:
            query_parameters['commitOrBranch'] = self._serialize.query('commit_or_branch', commit_or_branch, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        response = self._send(http_method='GET',
                              location_id='29d12225-b1d9-425f-b668-6c594a981313',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def create_folder(self, folder, project, path):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        content = self._serialize.body(folder, 'Folder')
        response = self._send(http_method='PUT',
                              location_id='a906531b-d2da-4f55-bda7-f3e676cc50d9',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Folder', response)

    def delete_folder(self, project, path):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        self._send(http_method='DELETE',
                   location_id='a906531b-d2da-4f55-bda7-f3e676cc50d9',
                   version='5.1-preview.2',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_folders(self, project, path=None, query_order=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        query_parameters = {}
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        response = self._send(http_method='GET',
                              location_id='a906531b-d2da-4f55-bda7-f3e676cc50d9',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Folder]', self._unwrap_collection(response))

    def update_folder(self, folder, project, path):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        content = self._serialize.body(folder, 'Folder')
        response = self._send(http_method='POST',
                              location_id='a906531b-d2da-4f55-bda7-f3e676cc50d9',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Folder', response)

    def get_latest_build(self, project, definition, branch_name=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition is not None:
            route_values['definition'] = self._serialize.url('definition', definition, 'str')
        query_parameters = {}
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='54481611-01f4-47f3-998f-160da0f0c229',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Build', response)

    def get_build_log(self, project, build_id, log_id, start_line=None, end_line=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_log_lines(self, project, build_id, log_id, start_line=None, end_line=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_build_logs(self, project, build_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BuildLog]', self._unwrap_collection(response))

    def get_build_logs_zip(self, project, build_id, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='5.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_log_zip(self, project, build_id, log_id, start_line=None, end_line=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_project_metrics(self, project, metric_aggregation_type=None, min_metrics_time=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if metric_aggregation_type is not None:
            route_values['metricAggregationType'] = self._serialize.url('metric_aggregation_type', metric_aggregation_type, 'str')
        query_parameters = {}
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='7433fae7-a6bc-41dc-a6e2-eef9005ce41a',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[BuildMetric]', self._unwrap_collection(response))

    def get_definition_metrics(self, project, definition_id, min_metrics_time=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='d973b939-0ce0-4fec-91d8-da3940fa1827',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[BuildMetric]', self._unwrap_collection(response))

    def get_build_option_definitions(self, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='591cb5a4-2d46-4f3a-a697-5cd42b6bd332',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BuildOptionDefinition]', self._unwrap_collection(response))

    def get_path_contents(self, project, provider_name, service_endpoint_id=None, repository=None, commit_or_branch=None, path=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        if commit_or_branch is not None:
            query_parameters['commitOrBranch'] = self._serialize.query('commit_or_branch', commit_or_branch, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        response = self._send(http_method='GET',
                              location_id='7944d6fb-df01-4709-920a-7a189aa34037',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[SourceRepositoryItem]', self._unwrap_collection(response))

    def get_build_properties(self, project, build_id, filter=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if filter is not None:
            filter = ",".join(filter)
            query_parameters['filter'] = self._serialize.query('filter', filter, 'str')
        response = self._send(http_method='GET',
                              location_id='0a6312e9-0627-49b7-8083-7d74a64849c9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def update_build_properties(self, document, project, build_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='0a6312e9-0627-49b7-8083-7d74a64849c9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('object', response)

    def get_definition_properties(self, project, definition_id, filter=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if filter is not None:
            filter = ",".join(filter)
            query_parameters['filter'] = self._serialize.query('filter', filter, 'str')
        response = self._send(http_method='GET',
                              location_id='d9826ad7-2a68-46a9-a6e9-677698777895',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def update_definition_properties(self, document, project, definition_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='d9826ad7-2a68-46a9-a6e9-677698777895',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('object', response)

    def get_pull_request(self, project, provider_name, pull_request_id, repository_id=None, service_endpoint_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'str')
        query_parameters = {}
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        response = self._send(http_method='GET',
                              location_id='d8763ec7-9ff0-4fb4-b2b2-9d757906ff14',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PullRequest', response)

    def get_build_report(self, project, build_id, type=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='45bcaa88-67e1-4042-a035-56d3b4a7d44c',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildReportMetadata', response)

    def get_build_report_html_content(self, project, build_id, type=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='45bcaa88-67e1-4042-a035-56d3b4a7d44c',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/html')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def list_repositories(self, project, provider_name, service_endpoint_id=None, repository=None, result_set=None, page_results=None, continuation_token=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        if result_set is not None:
            query_parameters['resultSet'] = self._serialize.query('result_set', result_set, 'str')
        if page_results is not None:
            query_parameters['pageResults'] = self._serialize.query('page_results', page_results, 'bool')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='d44d1680-f978-4834-9b93-8c6e132329c9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('SourceRepositories', response)

    def authorize_definition_resources(self, resources, project, definition_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        content = self._serialize.body(resources, '[DefinitionResourceReference]')
        response = self._send(http_method='PATCH',
                              location_id='ea623316-1967-45eb-89ab-e9e6110cf2d6',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[DefinitionResourceReference]', self._unwrap_collection(response))

    def get_definition_resources(self, project, definition_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        response = self._send(http_method='GET',
                              location_id='ea623316-1967-45eb-89ab-e9e6110cf2d6',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[DefinitionResourceReference]', self._unwrap_collection(response))

    def get_resource_usage(self):
        response = self._send(http_method='GET',
                              location_id='3813d06c-9e36-4ea1-aac3-61a485d60e3d',
                              version='5.1-preview.2')
        return self._deserialize('BuildResourceUsage', response)

    def get_definition_revisions(self, project, definition_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        response = self._send(http_method='GET',
                              location_id='7c116775-52e5-453e-8c5d-914d9762d8c4',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BuildDefinitionRevision]', self._unwrap_collection(response))

    def get_build_settings(self, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('BuildSettings', response)

    def update_build_settings(self, settings, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(settings, 'BuildSettings')
        response = self._send(http_method='PATCH',
                              location_id='aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildSettings', response)

    def list_source_providers(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='3ce81729-954f-423d-a581-9fea01d25186',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[SourceProviderAttributes]', self._unwrap_collection(response))

    def get_status_badge(self, project, definition, branch_name=None, stage_name=None, job_name=None, configuration=None, label=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition is not None:
            route_values['definition'] = self._serialize.url('definition', definition, 'str')
        query_parameters = {}
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        if stage_name is not None:
            query_parameters['stageName'] = self._serialize.query('stage_name', stage_name, 'str')
        if job_name is not None:
            query_parameters['jobName'] = self._serialize.query('job_name', job_name, 'str')
        if configuration is not None:
            query_parameters['configuration'] = self._serialize.query('configuration', configuration, 'str')
        if label is not None:
            query_parameters['label'] = self._serialize.query('label', label, 'str')
        response = self._send(http_method='GET',
                              location_id='07acfdce-4757-4439-b422-ddd13a2fcc10',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('str', response)

    def add_build_tag(self, project, build_id, tag):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='PUT',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def add_build_tags(self, tags, project, build_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(tags, '[str]')
        response = self._send(http_method='POST',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_build_tag(self, project, build_id, tag):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='DELETE',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_build_tags(self, project, build_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_tags(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='d84ac5c6-edc7-43d5-adc9-1b34be5dea09',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def add_definition_tag(self, project, definition_id, tag):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='PUT',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def add_definition_tags(self, tags, project, definition_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        content = self._serialize.body(tags, '[str]')
        response = self._send(http_method='POST',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_definition_tag(self, project, definition_id, tag):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='DELETE',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_definition_tags(self, project, definition_id, revision=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        response = self._send(http_method='GET',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_template(self, project, template_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        self._send(http_method='DELETE',
                   location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                   version='5.1',
                   route_values=route_values)

    def get_template(self, project, template_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        response = self._send(http_method='GET',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('BuildDefinitionTemplate', response)

    def get_templates(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BuildDefinitionTemplate]', self._unwrap_collection(response))

    def save_template(self, template, project, template_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        content = self._serialize.body(template, 'BuildDefinitionTemplate')
        response = self._send(http_method='PUT',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildDefinitionTemplate', response)

    def get_build_timeline(self, project, build_id, timeline_id=None, change_id=None, plan_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        query_parameters = {}
        if change_id is not None:
            query_parameters['changeId'] = self._serialize.query('change_id', change_id, 'int')
        if plan_id is not None:
            query_parameters['planId'] = self._serialize.query('plan_id', plan_id, 'str')
        response = self._send(http_method='GET',
                              location_id='8baac422-4c6e-4de5-8532-db96d92acffa',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Timeline', response)

    def restore_webhooks(self, trigger_types, project, provider_name, service_endpoint_id=None, repository=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        content = self._serialize.body(trigger_types, '[DefinitionTriggerType]')
        self._send(http_method='POST',
                   location_id='793bceb8-9736-4030-bd2f-fb3ce6d6b478',
                   version='5.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters,
                   content=content)

    def list_webhooks(self, project, provider_name, service_endpoint_id=None, repository=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        response = self._send(http_method='GET',
                              location_id='8f20ff82-9498-4812-9f6e-9c01bdc50e99',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[RepositoryWebhook]', self._unwrap_collection(response))

    def get_build_work_items_refs(self, project, build_id, top=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='5a21f5d2-5642-47e4-a0bd-1356e6731bee',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

    def get_build_work_items_refs_from_commits(self, commit_ids, project, build_id, top=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(commit_ids, '[str]')
        response = self._send(http_method='POST',
                              location_id='5a21f5d2-5642-47e4-a0bd-1356e6731bee',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

    def get_work_items_between_builds(self, project, from_build_id, to_build_id, top=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if from_build_id is not None:
            query_parameters['fromBuildId'] = self._serialize.query('from_build_id', from_build_id, 'int')
        if to_build_id is not None:
            query_parameters['toBuildId'] = self._serialize.query('to_build_id', to_build_id, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='52ba8915-5518-42e3-a4bb-b0182d159e2d',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

