# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.release import models


class ReleaseClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(ReleaseClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'efc2f575-36ef-48e9-b672-0c6fb4a48ac5'

    def get_approvals(self, project, assigned_to_filter=None, status_filter=None, release_ids_filter=None, type_filter=None, top=None, continuation_token=None, query_order=None, include_my_group_approvals=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if assigned_to_filter is not None:
            query_parameters['assignedToFilter'] = self._serialize.query('assigned_to_filter', assigned_to_filter, 'str')
        if status_filter is not None:
            query_parameters['statusFilter'] = self._serialize.query('status_filter', status_filter, 'str')
        if release_ids_filter is not None:
            release_ids_filter = ",".join(map(str, release_ids_filter))
            query_parameters['releaseIdsFilter'] = self._serialize.query('release_ids_filter', release_ids_filter, 'str')
        if type_filter is not None:
            query_parameters['typeFilter'] = self._serialize.query('type_filter', type_filter, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'int')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if include_my_group_approvals is not None:
            query_parameters['includeMyGroupApprovals'] = self._serialize.query('include_my_group_approvals', include_my_group_approvals, 'bool')
        response = self._send(http_method='GET',
                              location_id='b47c6458-e73b-47cb-a770-4df1e8813a91',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[ReleaseApproval]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetApprovalsResponseValue(response_value, continuation_token)

    class GetApprovalsResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def update_release_approval(self, approval, project, approval_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if approval_id is not None:
            route_values['approvalId'] = self._serialize.url('approval_id', approval_id, 'int')
        content = self._serialize.body(approval, 'ReleaseApproval')
        response = self._send(http_method='PATCH',
                              location_id='9328e074-59fb-465a-89d9-b09c82ee5109',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseApproval', response)

    def create_release_definition(self, release_definition, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(release_definition, 'ReleaseDefinition')
        response = self._send(http_method='POST',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseDefinition', response)

    def delete_release_definition(self, project, definition_id, comment=None, force_delete=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        if force_delete is not None:
            query_parameters['forceDelete'] = self._serialize.query('force_delete', force_delete, 'bool')
        self._send(http_method='DELETE',
                   location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                   version='5.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_release_definition(self, project, definition_id, property_filters=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReleaseDefinition', response)

    def get_release_definitions(self, project, search_text=None, expand=None, artifact_type=None, artifact_source_id=None, top=None, continuation_token=None, query_order=None, path=None, is_exact_name_match=None, tag_filter=None, property_filters=None, definition_id_filter=None, is_deleted=None, search_text_contains_folder_name=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if search_text is not None:
            query_parameters['searchText'] = self._serialize.query('search_text', search_text, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if artifact_type is not None:
            query_parameters['artifactType'] = self._serialize.query('artifact_type', artifact_type, 'str')
        if artifact_source_id is not None:
            query_parameters['artifactSourceId'] = self._serialize.query('artifact_source_id', artifact_source_id, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if is_exact_name_match is not None:
            query_parameters['isExactNameMatch'] = self._serialize.query('is_exact_name_match', is_exact_name_match, 'bool')
        if tag_filter is not None:
            tag_filter = ",".join(tag_filter)
            query_parameters['tagFilter'] = self._serialize.query('tag_filter', tag_filter, 'str')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if definition_id_filter is not None:
            definition_id_filter = ",".join(definition_id_filter)
            query_parameters['definitionIdFilter'] = self._serialize.query('definition_id_filter', definition_id_filter, 'str')
        if is_deleted is not None:
            query_parameters['isDeleted'] = self._serialize.query('is_deleted', is_deleted, 'bool')
        if search_text_contains_folder_name is not None:
            query_parameters['searchTextContainsFolderName'] = self._serialize.query('search_text_contains_folder_name', search_text_contains_folder_name, 'bool')
        response = self._send(http_method='GET',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[ReleaseDefinition]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetReleaseDefinitionsResponseValue(response_value, continuation_token)

    class GetReleaseDefinitionsResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def update_release_definition(self, release_definition, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(release_definition, 'ReleaseDefinition')
        response = self._send(http_method='PUT',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseDefinition', response)

    def get_deployments(self, project, definition_id=None, definition_environment_id=None, created_by=None, min_modified_time=None, max_modified_time=None, deployment_status=None, operation_status=None, latest_attempts_only=None, query_order=None, top=None, continuation_token=None, created_for=None, min_started_time=None, max_started_time=None, source_branch=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definition_id is not None:
            query_parameters['definitionId'] = self._serialize.query('definition_id', definition_id, 'int')
        if definition_environment_id is not None:
            query_parameters['definitionEnvironmentId'] = self._serialize.query('definition_environment_id', definition_environment_id, 'int')
        if created_by is not None:
            query_parameters['createdBy'] = self._serialize.query('created_by', created_by, 'str')
        if min_modified_time is not None:
            query_parameters['minModifiedTime'] = self._serialize.query('min_modified_time', min_modified_time, 'iso-8601')
        if max_modified_time is not None:
            query_parameters['maxModifiedTime'] = self._serialize.query('max_modified_time', max_modified_time, 'iso-8601')
        if deployment_status is not None:
            query_parameters['deploymentStatus'] = self._serialize.query('deployment_status', deployment_status, 'str')
        if operation_status is not None:
            query_parameters['operationStatus'] = self._serialize.query('operation_status', operation_status, 'str')
        if latest_attempts_only is not None:
            query_parameters['latestAttemptsOnly'] = self._serialize.query('latest_attempts_only', latest_attempts_only, 'bool')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'int')
        if created_for is not None:
            query_parameters['createdFor'] = self._serialize.query('created_for', created_for, 'str')
        if min_started_time is not None:
            query_parameters['minStartedTime'] = self._serialize.query('min_started_time', min_started_time, 'iso-8601')
        if max_started_time is not None:
            query_parameters['maxStartedTime'] = self._serialize.query('max_started_time', max_started_time, 'iso-8601')
        if source_branch is not None:
            query_parameters['sourceBranch'] = self._serialize.query('source_branch', source_branch, 'str')
        response = self._send(http_method='GET',
                              location_id='b005ef73-cddc-448e-9ba2-5193bf36b19f',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[Deployment]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetDeploymentsResponseValue(response_value, continuation_token)

    class GetDeploymentsResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def get_manual_intervention(self, project, release_id, manual_intervention_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if manual_intervention_id is not None:
            route_values['manualInterventionId'] = self._serialize.url('manual_intervention_id', manual_intervention_id, 'int')
        response = self._send(http_method='GET',
                              location_id='616c46e4-f370-4456-adaa-fbaf79c7b79e',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('ManualIntervention', response)

    def get_manual_interventions(self, project, release_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        response = self._send(http_method='GET',
                              location_id='616c46e4-f370-4456-adaa-fbaf79c7b79e',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[ManualIntervention]', self._unwrap_collection(response))

    def update_manual_intervention(self, manual_intervention_update_metadata, project, release_id, manual_intervention_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if manual_intervention_id is not None:
            route_values['manualInterventionId'] = self._serialize.url('manual_intervention_id', manual_intervention_id, 'int')
        content = self._serialize.body(manual_intervention_update_metadata, 'ManualInterventionUpdateMetadata')
        response = self._send(http_method='PATCH',
                              location_id='616c46e4-f370-4456-adaa-fbaf79c7b79e',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ManualIntervention', response)

    def get_releases(self, project=None, definition_id=None, definition_environment_id=None, search_text=None, created_by=None, status_filter=None, environment_status_filter=None, min_created_time=None, max_created_time=None, query_order=None, top=None, continuation_token=None, expand=None, artifact_type_id=None, source_id=None, artifact_version_id=None, source_branch_filter=None, is_deleted=None, tag_filter=None, property_filters=None, release_id_filter=None, path=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definition_id is not None:
            query_parameters['definitionId'] = self._serialize.query('definition_id', definition_id, 'int')
        if definition_environment_id is not None:
            query_parameters['definitionEnvironmentId'] = self._serialize.query('definition_environment_id', definition_environment_id, 'int')
        if search_text is not None:
            query_parameters['searchText'] = self._serialize.query('search_text', search_text, 'str')
        if created_by is not None:
            query_parameters['createdBy'] = self._serialize.query('created_by', created_by, 'str')
        if status_filter is not None:
            query_parameters['statusFilter'] = self._serialize.query('status_filter', status_filter, 'str')
        if environment_status_filter is not None:
            query_parameters['environmentStatusFilter'] = self._serialize.query('environment_status_filter', environment_status_filter, 'int')
        if min_created_time is not None:
            query_parameters['minCreatedTime'] = self._serialize.query('min_created_time', min_created_time, 'iso-8601')
        if max_created_time is not None:
            query_parameters['maxCreatedTime'] = self._serialize.query('max_created_time', max_created_time, 'iso-8601')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'int')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if artifact_type_id is not None:
            query_parameters['artifactTypeId'] = self._serialize.query('artifact_type_id', artifact_type_id, 'str')
        if source_id is not None:
            query_parameters['sourceId'] = self._serialize.query('source_id', source_id, 'str')
        if artifact_version_id is not None:
            query_parameters['artifactVersionId'] = self._serialize.query('artifact_version_id', artifact_version_id, 'str')
        if source_branch_filter is not None:
            query_parameters['sourceBranchFilter'] = self._serialize.query('source_branch_filter', source_branch_filter, 'str')
        if is_deleted is not None:
            query_parameters['isDeleted'] = self._serialize.query('is_deleted', is_deleted, 'bool')
        if tag_filter is not None:
            tag_filter = ",".join(tag_filter)
            query_parameters['tagFilter'] = self._serialize.query('tag_filter', tag_filter, 'str')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if release_id_filter is not None:
            release_id_filter = ",".join(map(str, release_id_filter))
            query_parameters['releaseIdFilter'] = self._serialize.query('release_id_filter', release_id_filter, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        response = self._send(http_method='GET',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[Release]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetReleasesResponseValue(response_value, continuation_token)

    class GetReleasesResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def create_release(self, release_start_metadata, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(release_start_metadata, 'ReleaseStartMetadata')
        response = self._send(http_method='POST',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Release', response)

    def get_release(self, project, release_id, approval_filters=None, property_filters=None, expand=None, top_gate_records=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        query_parameters = {}
        if approval_filters is not None:
            query_parameters['approvalFilters'] = self._serialize.query('approval_filters', approval_filters, 'str')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if top_gate_records is not None:
            query_parameters['$topGateRecords'] = self._serialize.query('top_gate_records', top_gate_records, 'int')
        response = self._send(http_method='GET',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Release', response)

    def get_release_revision(self, project, release_id, definition_snapshot_revision, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        query_parameters = {}
        if definition_snapshot_revision is not None:
            query_parameters['definitionSnapshotRevision'] = self._serialize.query('definition_snapshot_revision', definition_snapshot_revision, 'int')
        response = self._send(http_method='GET',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_release(self, release, project, release_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        content = self._serialize.body(release, 'Release')
        response = self._send(http_method='PUT',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Release', response)

    def update_release_resource(self, release_update_metadata, project, release_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        content = self._serialize.body(release_update_metadata, 'ReleaseUpdateMetadata')
        response = self._send(http_method='PATCH',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Release', response)

