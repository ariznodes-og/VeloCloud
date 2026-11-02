# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AccountMyWorkResult(Model):

    _attribute_map = {
        'query_size_limit_exceeded': {'key': 'querySizeLimitExceeded', 'type': 'bool'},
        'work_item_details': {'key': 'workItemDetails', 'type': '[AccountWorkWorkItemModel]'}
    }

    def __init__(self, query_size_limit_exceeded=None, work_item_details=None):
        super(AccountMyWorkResult, self).__init__()
        self.query_size_limit_exceeded = query_size_limit_exceeded
        self.work_item_details = work_item_details


class AccountRecentActivityWorkItemModelBase(Model):

    _attribute_map = {
        'activity_date': {'key': 'activityDate', 'type': 'iso-8601'},
        'activity_type': {'key': 'activityType', 'type': 'object'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'team_project': {'key': 'teamProject', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, activity_date=None, activity_type=None, changed_date=None, id=None, identity_id=None, state=None, team_project=None, title=None, work_item_type=None):
        super(AccountRecentActivityWorkItemModelBase, self).__init__()
        self.activity_date = activity_date
        self.activity_type = activity_type
        self.changed_date = changed_date
        self.id = id
        self.identity_id = identity_id
        self.state = state
        self.team_project = team_project
        self.title = title
        self.work_item_type = work_item_type


class AccountRecentMentionWorkItemModel(Model):

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'mentioned_date_field': {'key': 'mentionedDateField', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'team_project': {'key': 'teamProject', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, id=None, mentioned_date_field=None, state=None, team_project=None, title=None, work_item_type=None):
        super(AccountRecentMentionWorkItemModel, self).__init__()
        self.assigned_to = assigned_to
        self.id = id
        self.mentioned_date_field = mentioned_date_field
        self.state = state
        self.team_project = team_project
        self.title = title
        self.work_item_type = work_item_type


class AccountWorkWorkItemModel(Model):

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'team_project': {'key': 'teamProject', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, changed_date=None, id=None, state=None, team_project=None, title=None, work_item_type=None):
        super(AccountWorkWorkItemModel, self).__init__()
        self.assigned_to = assigned_to
        self.changed_date = changed_date
        self.id = id
        self.state = state
        self.team_project = team_project
        self.title = title
        self.work_item_type = work_item_type


class ArtifactUriQuery(Model):

    _attribute_map = {
        'artifact_uris': {'key': 'artifactUris', 'type': '[str]'}
    }

    def __init__(self, artifact_uris=None):
        super(ArtifactUriQuery, self).__init__()
        self.artifact_uris = artifact_uris


class ArtifactUriQueryResult(Model):

    _attribute_map = {
        'artifact_uris_query_result': {'key': 'artifactUrisQueryResult', 'type': '{[WorkItemReference]}'}
    }

    def __init__(self, artifact_uris_query_result=None):
        super(ArtifactUriQueryResult, self).__init__()
        self.artifact_uris_query_result = artifact_uris_query_result


class AttachmentReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(AttachmentReference, self).__init__()
        self.id = id
        self.url = url


class CommentCreate(Model):

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, text=None):
        super(CommentCreate, self).__init__()
        self.text = text


class CommentUpdate(Model):

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, text=None):
        super(CommentUpdate, self).__init__()
        self.text = text


class ExternalDeployment(Model):

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'environment': {'key': 'environment', 'type': 'ExternalEnvironment'},
        'group': {'key': 'group', 'type': 'str'},
        'pipeline': {'key': 'pipeline', 'type': 'ExternalPipeline'},
        'related_work_item_ids': {'key': 'relatedWorkItemIds', 'type': '[int]'},
        'run_id': {'key': 'runId', 'type': 'int'},
        'sequence_number': {'key': 'sequenceNumber', 'type': 'int'},
        'status': {'key': 'status', 'type': 'str'},
        'status_date': {'key': 'statusDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, artifact_id=None, created_by=None, description=None, display_name=None, environment=None, group=None, pipeline=None, related_work_item_ids=None, run_id=None, sequence_number=None, status=None, status_date=None, url=None):
        super(ExternalDeployment, self).__init__()
        self.artifact_id = artifact_id
        self.created_by = created_by
        self.description = description
        self.display_name = display_name
        self.environment = environment
        self.group = group
        self.pipeline = pipeline
        self.related_work_item_ids = related_work_item_ids
        self.run_id = run_id
        self.sequence_number = sequence_number
        self.status = status
        self.status_date = status_date
        self.url = url


class ExternalEnvironment(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, type=None):
        super(ExternalEnvironment, self).__init__()
        self.display_name = display_name
        self.id = id
        self.type = type


class ExternalPipeline(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, url=None):
        super(ExternalPipeline, self).__init__()
        self.display_name = display_name
        self.id = id
        self.url = url


class GraphSubjectBase(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class IdentityRef(GraphSubjectBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


class IdentityReference(IdentityRef):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None, id=None, name=None):
        super(IdentityReference, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, directory_alias=directory_alias, image_url=image_url, inactive=inactive, is_aad_identity=is_aad_identity, is_container=is_container, is_deleted_in_origin=is_deleted_in_origin, profile_url=profile_url, unique_name=unique_name)
        self.id = id
        self.name = name


class JsonPatchOperation(Model):

    _attribute_map = {
        'from_': {'key': 'from', 'type': 'str'},
        'op': {'key': 'op', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, from_=None, op=None, path=None, value=None):
        super(JsonPatchOperation, self).__init__()
        self.from_ = from_
        self.op = op
        self.path = path
        self.value = value


class Link(Model):

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'rel': {'key': 'rel', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, attributes=None, rel=None, url=None):
        super(Link, self).__init__()
        self.attributes = attributes
        self.rel = rel
        self.url = url


class ProcessIdModel(Model):

    _attribute_map = {
        'type_id': {'key': 'typeId', 'type': 'str'}
    }

    def __init__(self, type_id=None):
        super(ProcessIdModel, self).__init__()
        self.type_id = type_id


class ProcessMigrationResultModel(Model):

    _attribute_map = {
        'process_id': {'key': 'processId', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'}
    }

    def __init__(self, process_id=None, project_id=None):
        super(ProcessMigrationResultModel, self).__init__()
        self.process_id = process_id
        self.project_id = project_id


class ProjectWorkItemStateColors(Model):

    _attribute_map = {
        'project_name': {'key': 'projectName', 'type': 'str'},
        'work_item_type_state_colors': {'key': 'workItemTypeStateColors', 'type': '[WorkItemTypeStateColors]'}
    }

    def __init__(self, project_name=None, work_item_type_state_colors=None):
        super(ProjectWorkItemStateColors, self).__init__()
        self.project_name = project_name
        self.work_item_type_state_colors = work_item_type_state_colors


class ProvisioningResult(Model):

    _attribute_map = {
        'provisioning_import_events': {'key': 'provisioningImportEvents', 'type': '[str]'}
    }

    def __init__(self, provisioning_import_events=None):
        super(ProvisioningResult, self).__init__()
        self.provisioning_import_events = provisioning_import_events


class QueryBatchGetRequest(Model):

    _attribute_map = {
        'expand': {'key': '$expand', 'type': 'object'},
        'error_policy': {'key': 'errorPolicy', 'type': 'object'},
        'ids': {'key': 'ids', 'type': '[str]'}
    }

    def __init__(self, expand=None, error_policy=None, ids=None):
        super(QueryBatchGetRequest, self).__init__()
        self.expand = expand
        self.error_policy = error_policy
        self.ids = ids


class QueryHierarchyItemsResult(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'has_more': {'key': 'hasMore', 'type': 'bool'},
        'value': {'key': 'value', 'type': '[QueryHierarchyItem]'}
    }

    def __init__(self, count=None, has_more=None, value=None):
        super(QueryHierarchyItemsResult, self).__init__()
        self.count = count
        self.has_more = has_more
        self.value = value


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ReportingWorkItemRevisionsFilter(Model):

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '[str]'},
        'include_deleted': {'key': 'includeDeleted', 'type': 'bool'},
        'include_identity_ref': {'key': 'includeIdentityRef', 'type': 'bool'},
        'include_latest_only': {'key': 'includeLatestOnly', 'type': 'bool'},
        'include_tag_ref': {'key': 'includeTagRef', 'type': 'bool'},
        'types': {'key': 'types', 'type': '[str]'}
    }

    def __init__(self, fields=None, include_deleted=None, include_identity_ref=None, include_latest_only=None, include_tag_ref=None, types=None):
        super(ReportingWorkItemRevisionsFilter, self).__init__()
        self.fields = fields
        self.include_deleted = include_deleted
        self.include_identity_ref = include_identity_ref
        self.include_latest_only = include_latest_only
        self.include_tag_ref = include_tag_ref
        self.types = types


class StreamedBatch(Model):

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'is_last_batch': {'key': 'isLastBatch', 'type': 'bool'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'values': {'key': 'values', 'type': '[object]'}
    }

    def __init__(self, continuation_token=None, is_last_batch=None, next_link=None, values=None):
        super(StreamedBatch, self).__init__()
        self.continuation_token = continuation_token
        self.is_last_batch = is_last_batch
        self.next_link = next_link
        self.values = values


class TeamContext(Model):

    _attribute_map = {
        'project': {'key': 'project', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'team': {'key': 'team', 'type': 'str'},
        'team_id': {'key': 'teamId', 'type': 'str'}
    }

    def __init__(self, project=None, project_id=None, team=None, team_id=None):
        super(TeamContext, self).__init__()
        self.project = project
        self.project_id = project_id
        self.team = team
        self.team_id = team_id


class UpdateWorkItemField(Model):

    _attribute_map = {
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'}
    }

    def __init__(self, is_deleted=None):
        super(UpdateWorkItemField, self).__init__()
        self.is_deleted = is_deleted


class Wiql(Model):

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'}
    }

    def __init__(self, query=None):
        super(Wiql, self).__init__()
        self.query = query


class WorkArtifactLink(Model):

    _attribute_map = {
        'artifact_type': {'key': 'artifactType', 'type': 'str'},
        'link_type': {'key': 'linkType', 'type': 'str'},
        'tool_type': {'key': 'toolType', 'type': 'str'}
    }

    def __init__(self, artifact_type=None, link_type=None, tool_type=None):
        super(WorkArtifactLink, self).__init__()
        self.artifact_type = artifact_type
        self.link_type = link_type
        self.tool_type = tool_type


class WorkItemBatchGetRequest(Model):

    _attribute_map = {
        'expand': {'key': '$expand', 'type': 'object'},
        'as_of': {'key': 'asOf', 'type': 'iso-8601'},
        'error_policy': {'key': 'errorPolicy', 'type': 'object'},
        'fields': {'key': 'fields', 'type': '[str]'},
        'ids': {'key': 'ids', 'type': '[int]'}
    }

    def __init__(self, expand=None, as_of=None, error_policy=None, fields=None, ids=None):
        super(WorkItemBatchGetRequest, self).__init__()
        self.expand = expand
        self.as_of = as_of
        self.error_policy = error_policy
        self.fields = fields
        self.ids = ids


class WorkItemDeleteReference(Model):

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'deleted_by': {'key': 'deletedBy', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, code=None, deleted_by=None, deleted_date=None, id=None, message=None, name=None, project=None, type=None, url=None):
        super(WorkItemDeleteReference, self).__init__()
        self.code = code
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.id = id
        self.message = message
        self.name = name
        self.project = project
        self.type = type
        self.url = url


class WorkItemDeleteShallowReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WorkItemDeleteShallowReference, self).__init__()
        self.id = id
        self.url = url


class WorkItemDeleteUpdate(Model):

    _attribute_map = {
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'}
    }

    def __init__(self, is_deleted=None):
        super(WorkItemDeleteUpdate, self).__init__()
        self.is_deleted = is_deleted


class WorkItemFieldOperation(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None):
        super(WorkItemFieldOperation, self).__init__()
        self.name = name
        self.reference_name = reference_name


class WorkItemFieldReference(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None, url=None):
        super(WorkItemFieldReference, self).__init__()
        self.name = name
        self.reference_name = reference_name
        self.url = url


class WorkItemFieldUpdate(Model):

    _attribute_map = {
        'new_value': {'key': 'newValue', 'type': 'object'},
        'old_value': {'key': 'oldValue', 'type': 'object'}
    }

    def __init__(self, new_value=None, old_value=None):
        super(WorkItemFieldUpdate, self).__init__()
        self.new_value = new_value
        self.old_value = old_value


class WorkItemIcon(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WorkItemIcon, self).__init__()
        self.id = id
        self.url = url


class WorkItemLink(Model):

    _attribute_map = {
        'rel': {'key': 'rel', 'type': 'str'},
        'source': {'key': 'source', 'type': 'WorkItemReference'},
        'target': {'key': 'target', 'type': 'WorkItemReference'}
    }

    def __init__(self, rel=None, source=None, target=None):
        super(WorkItemLink, self).__init__()
        self.rel = rel
        self.source = source
        self.target = target


class WorkItemNextStateOnTransition(Model):

    _attribute_map = {
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'state_on_transition': {'key': 'stateOnTransition', 'type': 'str'}
    }

    def __init__(self, error_code=None, id=None, message=None, state_on_transition=None):
        super(WorkItemNextStateOnTransition, self).__init__()
        self.error_code = error_code
        self.id = id
        self.message = message
        self.state_on_transition = state_on_transition


class WorkItemQueryClause(Model):

    _attribute_map = {
        'clauses': {'key': 'clauses', 'type': '[WorkItemQueryClause]'},
        'field': {'key': 'field', 'type': 'WorkItemFieldReference'},
        'field_value': {'key': 'fieldValue', 'type': 'WorkItemFieldReference'},
        'is_field_value': {'key': 'isFieldValue', 'type': 'bool'},
        'logical_operator': {'key': 'logicalOperator', 'type': 'object'},
        'operator': {'key': 'operator', 'type': 'WorkItemFieldOperation'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, clauses=None, field=None, field_value=None, is_field_value=None, logical_operator=None, operator=None, value=None):
        super(WorkItemQueryClause, self).__init__()
        self.clauses = clauses
        self.field = field
        self.field_value = field_value
        self.is_field_value = is_field_value
        self.logical_operator = logical_operator
        self.operator = operator
        self.value = value


class WorkItemQueryResult(Model):

    _attribute_map = {
        'as_of': {'key': 'asOf', 'type': 'iso-8601'},
        'columns': {'key': 'columns', 'type': '[WorkItemFieldReference]'},
        'query_result_type': {'key': 'queryResultType', 'type': 'object'},
        'query_type': {'key': 'queryType', 'type': 'object'},
        'sort_columns': {'key': 'sortColumns', 'type': '[WorkItemQuerySortColumn]'},
        'work_item_relations': {'key': 'workItemRelations', 'type': '[WorkItemLink]'},
        'work_items': {'key': 'workItems', 'type': '[WorkItemReference]'}
    }

    def __init__(self, as_of=None, columns=None, query_result_type=None, query_type=None, sort_columns=None, work_item_relations=None, work_items=None):
        super(WorkItemQueryResult, self).__init__()
        self.as_of = as_of
        self.columns = columns
        self.query_result_type = query_result_type
        self.query_type = query_type
        self.sort_columns = sort_columns
        self.work_item_relations = work_item_relations
        self.work_items = work_items


class WorkItemQuerySortColumn(Model):

    _attribute_map = {
        'descending': {'key': 'descending', 'type': 'bool'},
        'field': {'key': 'field', 'type': 'WorkItemFieldReference'}
    }

    def __init__(self, descending=None, field=None):
        super(WorkItemQuerySortColumn, self).__init__()
        self.descending = descending
        self.field = field


class WorkItemReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WorkItemReference, self).__init__()
        self.id = id
        self.url = url


class WorkItemRelation(Link):

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'rel': {'key': 'rel', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, attributes=None, rel=None, url=None):
        super(WorkItemRelation, self).__init__(attributes=attributes, rel=rel, url=url)


class WorkItemRelationUpdates(Model):

    _attribute_map = {
        'added': {'key': 'added', 'type': '[WorkItemRelation]'},
        'removed': {'key': 'removed', 'type': '[WorkItemRelation]'},
        'updated': {'key': 'updated', 'type': '[WorkItemRelation]'}
    }

    def __init__(self, added=None, removed=None, updated=None):
        super(WorkItemRelationUpdates, self).__init__()
        self.added = added
        self.removed = removed
        self.updated = updated


class WorkItemStateColor(Model):

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'color': {'key': 'color', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, category=None, color=None, name=None):
        super(WorkItemStateColor, self).__init__()
        self.category = category
        self.color = color
        self.name = name


class WorkItemStateTransition(Model):

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[str]'},
        'to': {'key': 'to', 'type': 'str'}
    }

    def __init__(self, actions=None, to=None):
        super(WorkItemStateTransition, self).__init__()
        self.actions = actions
        self.to = to


class WorkItemTagDefinition(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(WorkItemTagDefinition, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class WorkItemTrackingResourceReference(Model):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, url=None):
        super(WorkItemTrackingResourceReference, self).__init__()
        self.url = url


class WorkItemTypeColor(Model):

    _attribute_map = {
        'primary_color': {'key': 'primaryColor', 'type': 'str'},
        'secondary_color': {'key': 'secondaryColor', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, primary_color=None, secondary_color=None, work_item_type_name=None):
        super(WorkItemTypeColor, self).__init__()
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.work_item_type_name = work_item_type_name


class WorkItemTypeColorAndIcon(Model):

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, color=None, icon=None, work_item_type_name=None):
        super(WorkItemTypeColorAndIcon, self).__init__()
        self.color = color
        self.icon = icon
        self.work_item_type_name = work_item_type_name


class WorkItemTypeFieldInstanceBase(WorkItemFieldReference):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'always_required': {'key': 'alwaysRequired', 'type': 'bool'},
        'dependent_fields': {'key': 'dependentFields', 'type': '[WorkItemFieldReference]'},
        'help_text': {'key': 'helpText', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None, url=None, always_required=None, dependent_fields=None, help_text=None):
        super(WorkItemTypeFieldInstanceBase, self).__init__(name=name, reference_name=reference_name, url=url)
        self.always_required = always_required
        self.dependent_fields = dependent_fields
        self.help_text = help_text


class WorkItemTypeFieldWithReferences(WorkItemTypeFieldInstanceBase):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'always_required': {'key': 'alwaysRequired', 'type': 'bool'},
        'dependent_fields': {'key': 'dependentFields', 'type': '[WorkItemFieldReference]'},
        'help_text': {'key': 'helpText', 'type': 'str'},
        'allowed_values': {'key': 'allowedValues', 'type': '[object]'},
        'default_value': {'key': 'defaultValue', 'type': 'object'}
    }

    def __init__(self, name=None, reference_name=None, url=None, always_required=None, dependent_fields=None, help_text=None, allowed_values=None, default_value=None):
        super(WorkItemTypeFieldWithReferences, self).__init__(name=name, reference_name=reference_name, url=url, always_required=always_required, dependent_fields=dependent_fields, help_text=help_text)
        self.allowed_values = allowed_values
        self.default_value = default_value


class WorkItemTypeReference(WorkItemTrackingResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, url=None, name=None):
        super(WorkItemTypeReference, self).__init__(url=url)
        self.name = name


class WorkItemTypeStateColors(Model):

    _attribute_map = {
        'state_colors': {'key': 'stateColors', 'type': '[WorkItemStateColor]'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, state_colors=None, work_item_type_name=None):
        super(WorkItemTypeStateColors, self).__init__()
        self.state_colors = state_colors
        self.work_item_type_name = work_item_type_name


class WorkItemTypeTemplate(Model):

    _attribute_map = {
        'template': {'key': 'template', 'type': 'str'}
    }

    def __init__(self, template=None):
        super(WorkItemTypeTemplate, self).__init__()
        self.template = template


class WorkItemTypeTemplateUpdateModel(Model):

    _attribute_map = {
        'action_type': {'key': 'actionType', 'type': 'object'},
        'methodology': {'key': 'methodology', 'type': 'str'},
        'template': {'key': 'template', 'type': 'str'},
        'template_type': {'key': 'templateType', 'type': 'object'}
    }

    def __init__(self, action_type=None, methodology=None, template=None, template_type=None):
        super(WorkItemTypeTemplateUpdateModel, self).__init__()
        self.action_type = action_type
        self.methodology = methodology
        self.template = template
        self.template_type = template_type


class AccountRecentActivityWorkItemModel(AccountRecentActivityWorkItemModelBase):

    _attribute_map = {
        'activity_date': {'key': 'activityDate', 'type': 'iso-8601'},
        'activity_type': {'key': 'activityType', 'type': 'object'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'team_project': {'key': 'teamProject', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'},
        'assigned_to': {'key': 'assignedTo', 'type': 'str'}
    }

    def __init__(self, activity_date=None, activity_type=None, changed_date=None, id=None, identity_id=None, state=None, team_project=None, title=None, work_item_type=None, assigned_to=None):
        super(AccountRecentActivityWorkItemModel, self).__init__(activity_date=activity_date, activity_type=activity_type, changed_date=changed_date, id=id, identity_id=identity_id, state=state, team_project=team_project, title=title, work_item_type=work_item_type)
        self.assigned_to = assigned_to


class AccountRecentActivityWorkItemModel2(AccountRecentActivityWorkItemModelBase):

    _attribute_map = {
        'activity_date': {'key': 'activityDate', 'type': 'iso-8601'},
        'activity_type': {'key': 'activityType', 'type': 'object'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'team_project': {'key': 'teamProject', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'},
        'assigned_to': {'key': 'assignedTo', 'type': 'IdentityRef'}
    }

    def __init__(self, activity_date=None, activity_type=None, changed_date=None, id=None, identity_id=None, state=None, team_project=None, title=None, work_item_type=None, assigned_to=None):
        super(AccountRecentActivityWorkItemModel2, self).__init__(activity_date=activity_date, activity_type=activity_type, changed_date=changed_date, id=id, identity_id=identity_id, state=state, team_project=team_project, title=title, work_item_type=work_item_type)
        self.assigned_to = assigned_to


class ReportingWorkItemLinksBatch(StreamedBatch):

    _attribute_map = {
    }

    def __init__(self):
        super(ReportingWorkItemLinksBatch, self).__init__()


class ReportingWorkItemRevisionsBatch(StreamedBatch):

    _attribute_map = {
    }

    def __init__(self):
        super(ReportingWorkItemRevisionsBatch, self).__init__()


class WorkItemCommentVersionRef(WorkItemTrackingResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'created_in_revision': {'key': 'createdInRevision', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, url=None, comment_id=None, created_in_revision=None, is_deleted=None, text=None, version=None):
        super(WorkItemCommentVersionRef, self).__init__(url=url)
        self.comment_id = comment_id
        self.created_in_revision = created_in_revision
        self.is_deleted = is_deleted
        self.text = text
        self.version = version


class WorkItemDelete(WorkItemDeleteReference):

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'deleted_by': {'key': 'deletedBy', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'WorkItem'}
    }

    def __init__(self, code=None, deleted_by=None, deleted_date=None, id=None, message=None, name=None, project=None, type=None, url=None, resource=None):
        super(WorkItemDelete, self).__init__(code=code, deleted_by=deleted_by, deleted_date=deleted_date, id=id, message=message, name=name, project=project, type=type, url=url)
        self.resource = resource


class WorkItemTrackingResource(WorkItemTrackingResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'}
    }

    def __init__(self, url=None, _links=None):
        super(WorkItemTrackingResource, self).__init__(url=url)
        self._links = _links


class WorkItemType(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'field_instances': {'key': 'fieldInstances', 'type': '[WorkItemTypeFieldInstance]'},
        'fields': {'key': 'fields', 'type': '[WorkItemTypeFieldInstance]'},
        'icon': {'key': 'icon', 'type': 'WorkItemIcon'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'states': {'key': 'states', 'type': '[WorkItemStateColor]'},
        'transitions': {'key': 'transitions', 'type': '{[WorkItemStateTransition]}'},
        'xml_form': {'key': 'xmlForm', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, color=None, description=None, field_instances=None, fields=None, icon=None, is_disabled=None, name=None, reference_name=None, states=None, transitions=None, xml_form=None):
        super(WorkItemType, self).__init__(url=url, _links=_links)
        self.color = color
        self.description = description
        self.field_instances = field_instances
        self.fields = fields
        self.icon = icon
        self.is_disabled = is_disabled
        self.name = name
        self.reference_name = reference_name
        self.states = states
        self.transitions = transitions
        self.xml_form = xml_form


class WorkItemTypeCategory(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'default_work_item_type': {'key': 'defaultWorkItemType', 'type': 'WorkItemTypeReference'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'work_item_types': {'key': 'workItemTypes', 'type': '[WorkItemTypeReference]'}
    }

    def __init__(self, url=None, _links=None, default_work_item_type=None, name=None, reference_name=None, work_item_types=None):
        super(WorkItemTypeCategory, self).__init__(url=url, _links=_links)
        self.default_work_item_type = default_work_item_type
        self.name = name
        self.reference_name = reference_name
        self.work_item_types = work_item_types


class WorkItemTypeFieldInstance(WorkItemTypeFieldInstanceBase):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'always_required': {'key': 'alwaysRequired', 'type': 'bool'},
        'dependent_fields': {'key': 'dependentFields', 'type': '[WorkItemFieldReference]'},
        'help_text': {'key': 'helpText', 'type': 'str'},
        'allowed_values': {'key': 'allowedValues', 'type': '[str]'},
        'default_value': {'key': 'defaultValue', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None, url=None, always_required=None, dependent_fields=None, help_text=None, allowed_values=None, default_value=None):
        super(WorkItemTypeFieldInstance, self).__init__(name=name, reference_name=reference_name, url=url, always_required=always_required, dependent_fields=dependent_fields, help_text=help_text)
        self.allowed_values = allowed_values
        self.default_value = default_value


class WorkItemUpdate(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'fields': {'key': 'fields', 'type': '{WorkItemFieldUpdate}'},
        'id': {'key': 'id', 'type': 'int'},
        'relations': {'key': 'relations', 'type': 'WorkItemRelationUpdates'},
        'rev': {'key': 'rev', 'type': 'int'},
        'revised_by': {'key': 'revisedBy', 'type': 'IdentityReference'},
        'revised_date': {'key': 'revisedDate', 'type': 'iso-8601'},
        'work_item_id': {'key': 'workItemId', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, fields=None, id=None, relations=None, rev=None, revised_by=None, revised_date=None, work_item_id=None):
        super(WorkItemUpdate, self).__init__(url=url, _links=_links)
        self.fields = fields
        self.id = id
        self.relations = relations
        self.rev = rev
        self.revised_by = revised_by
        self.revised_date = revised_date
        self.work_item_id = work_item_id


class Comment(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_on_behalf_date': {'key': 'createdOnBehalfDate', 'type': 'iso-8601'},
        'created_on_behalf_of': {'key': 'createdOnBehalfOf', 'type': 'IdentityRef'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'mentions': {'key': 'mentions', 'type': '[CommentMention]'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'reactions': {'key': 'reactions', 'type': '[CommentReaction]'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'},
        'work_item_id': {'key': 'workItemId', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, created_by=None, created_date=None, created_on_behalf_date=None, created_on_behalf_of=None, id=None, is_deleted=None, mentions=None, modified_by=None, modified_date=None, reactions=None, text=None, version=None, work_item_id=None):
        super(Comment, self).__init__(url=url, _links=_links)
        self.created_by = created_by
        self.created_date = created_date
        self.created_on_behalf_date = created_on_behalf_date
        self.created_on_behalf_of = created_on_behalf_of
        self.id = id
        self.is_deleted = is_deleted
        self.mentions = mentions
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.reactions = reactions
        self.text = text
        self.version = version
        self.work_item_id = work_item_id


class CommentList(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'next_page': {'key': 'nextPage', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comments=None, continuation_token=None, count=None, next_page=None, total_count=None):
        super(CommentList, self).__init__(url=url, _links=_links)
        self.comments = comments
        self.continuation_token = continuation_token
        self.count = count
        self.next_page = next_page
        self.total_count = total_count


class CommentMention(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'artifact_type': {'key': 'artifactType', 'type': 'str'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'target_id': {'key': 'targetId', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, artifact_id=None, artifact_type=None, comment_id=None, target_id=None):
        super(CommentMention, self).__init__(url=url, _links=_links)
        self.artifact_id = artifact_id
        self.artifact_type = artifact_type
        self.comment_id = comment_id
        self.target_id = target_id


class CommentReaction(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'is_current_user_engaged': {'key': 'isCurrentUserEngaged', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, url=None, _links=None, comment_id=None, count=None, is_current_user_engaged=None, type=None):
        super(CommentReaction, self).__init__(url=url, _links=_links)
        self.comment_id = comment_id
        self.count = count
        self.is_current_user_engaged = is_current_user_engaged
        self.type = type


class CommentVersion(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_on_behalf_date': {'key': 'createdOnBehalfDate', 'type': 'iso-8601'},
        'created_on_behalf_of': {'key': 'createdOnBehalfOf', 'type': 'IdentityRef'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'rendered_text': {'key': 'renderedText', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, created_by=None, created_date=None, created_on_behalf_date=None, created_on_behalf_of=None, id=None, is_deleted=None, modified_by=None, modified_date=None, rendered_text=None, text=None, version=None):
        super(CommentVersion, self).__init__(url=url, _links=_links)
        self.created_by = created_by
        self.created_date = created_date
        self.created_on_behalf_date = created_on_behalf_date
        self.created_on_behalf_of = created_on_behalf_of
        self.id = id
        self.is_deleted = is_deleted
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.rendered_text = rendered_text
        self.text = text
        self.version = version


class FieldDependentRule(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dependent_fields': {'key': 'dependentFields', 'type': '[WorkItemFieldReference]'}
    }

    def __init__(self, url=None, _links=None, dependent_fields=None):
        super(FieldDependentRule, self).__init__(url=url, _links=_links)
        self.dependent_fields = dependent_fields


class QueryHierarchyItem(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'children': {'key': 'children', 'type': '[QueryHierarchyItem]'},
        'clauses': {'key': 'clauses', 'type': 'WorkItemQueryClause'},
        'columns': {'key': 'columns', 'type': '[WorkItemFieldReference]'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityReference'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'filter_options': {'key': 'filterOptions', 'type': 'object'},
        'has_children': {'key': 'hasChildren', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_invalid_syntax': {'key': 'isInvalidSyntax', 'type': 'bool'},
        'is_public': {'key': 'isPublic', 'type': 'bool'},
        'last_executed_by': {'key': 'lastExecutedBy', 'type': 'IdentityReference'},
        'last_executed_date': {'key': 'lastExecutedDate', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityReference'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
        'link_clauses': {'key': 'linkClauses', 'type': 'WorkItemQueryClause'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'query_recursion_option': {'key': 'queryRecursionOption', 'type': 'object'},
        'query_type': {'key': 'queryType', 'type': 'object'},
        'sort_columns': {'key': 'sortColumns', 'type': '[WorkItemQuerySortColumn]'},
        'source_clauses': {'key': 'sourceClauses', 'type': 'WorkItemQueryClause'},
        'target_clauses': {'key': 'targetClauses', 'type': 'WorkItemQueryClause'},
        'wiql': {'key': 'wiql', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, children=None, clauses=None, columns=None, created_by=None, created_date=None, filter_options=None, has_children=None, id=None, is_deleted=None, is_folder=None, is_invalid_syntax=None, is_public=None, last_executed_by=None, last_executed_date=None, last_modified_by=None, last_modified_date=None, link_clauses=None, name=None, path=None, query_recursion_option=None, query_type=None, sort_columns=None, source_clauses=None, target_clauses=None, wiql=None):
        super(QueryHierarchyItem, self).__init__(url=url, _links=_links)
        self.children = children
        self.clauses = clauses
        self.columns = columns
        self.created_by = created_by
        self.created_date = created_date
        self.filter_options = filter_options
        self.has_children = has_children
        self.id = id
        self.is_deleted = is_deleted
        self.is_folder = is_folder
        self.is_invalid_syntax = is_invalid_syntax
        self.is_public = is_public
        self.last_executed_by = last_executed_by
        self.last_executed_date = last_executed_date
        self.last_modified_by = last_modified_by
        self.last_modified_date = last_modified_date
        self.link_clauses = link_clauses
        self.name = name
        self.path = path
        self.query_recursion_option = query_recursion_option
        self.query_type = query_type
        self.sort_columns = sort_columns
        self.source_clauses = source_clauses
        self.target_clauses = target_clauses
        self.wiql = wiql


class WorkItem(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_version_ref': {'key': 'commentVersionRef', 'type': 'WorkItemCommentVersionRef'},
        'fields': {'key': 'fields', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'relations': {'key': 'relations', 'type': '[WorkItemRelation]'},
        'rev': {'key': 'rev', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comment_version_ref=None, fields=None, id=None, relations=None, rev=None):
        super(WorkItem, self).__init__(url=url, _links=_links)
        self.comment_version_ref = comment_version_ref
        self.fields = fields
        self.id = id
        self.relations = relations
        self.rev = rev


class WorkItemClassificationNode(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'children': {'key': 'children', 'type': '[WorkItemClassificationNode]'},
        'has_children': {'key': 'hasChildren', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'structure_type': {'key': 'structureType', 'type': 'object'}
    }

    def __init__(self, url=None, _links=None, attributes=None, children=None, has_children=None, id=None, identifier=None, name=None, path=None, structure_type=None):
        super(WorkItemClassificationNode, self).__init__(url=url, _links=_links)
        self.attributes = attributes
        self.children = children
        self.has_children = has_children
        self.id = id
        self.identifier = identifier
        self.name = name
        self.path = path
        self.structure_type = structure_type


class WorkItemComment(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'revised_by': {'key': 'revisedBy', 'type': 'IdentityReference'},
        'revised_date': {'key': 'revisedDate', 'type': 'iso-8601'},
        'revision': {'key': 'revision', 'type': 'int'},
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, revised_by=None, revised_date=None, revision=None, text=None):
        super(WorkItemComment, self).__init__(url=url, _links=_links)
        self.revised_by = revised_by
        self.revised_date = revised_date
        self.revision = revision
        self.text = text


class WorkItemComments(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[WorkItemComment]'},
        'count': {'key': 'count', 'type': 'int'},
        'from_revision_count': {'key': 'fromRevisionCount', 'type': 'int'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comments=None, count=None, from_revision_count=None, total_count=None):
        super(WorkItemComments, self).__init__(url=url, _links=_links)
        self.comments = comments
        self.count = count
        self.from_revision_count = from_revision_count
        self.total_count = total_count


class WorkItemField(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'can_sort_by': {'key': 'canSortBy', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_identity': {'key': 'isIdentity', 'type': 'bool'},
        'is_picklist': {'key': 'isPicklist', 'type': 'bool'},
        'is_picklist_suggested': {'key': 'isPicklistSuggested', 'type': 'bool'},
        'is_queryable': {'key': 'isQueryable', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'picklist_id': {'key': 'picklistId', 'type': 'str'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'supported_operations': {'key': 'supportedOperations', 'type': '[WorkItemFieldOperation]'},
        'type': {'key': 'type', 'type': 'object'},
        'usage': {'key': 'usage', 'type': 'object'}
    }

    def __init__(self, url=None, _links=None, can_sort_by=None, description=None, is_deleted=None, is_identity=None, is_picklist=None, is_picklist_suggested=None, is_queryable=None, name=None, picklist_id=None, read_only=None, reference_name=None, supported_operations=None, type=None, usage=None):
        super(WorkItemField, self).__init__(url=url, _links=_links)
        self.can_sort_by = can_sort_by
        self.description = description
        self.is_deleted = is_deleted
        self.is_identity = is_identity
        self.is_picklist = is_picklist
        self.is_picklist_suggested = is_picklist_suggested
        self.is_queryable = is_queryable
        self.name = name
        self.picklist_id = picklist_id
        self.read_only = read_only
        self.reference_name = reference_name
        self.supported_operations = supported_operations
        self.type = type
        self.usage = usage


class WorkItemHistory(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'rev': {'key': 'rev', 'type': 'int'},
        'revised_by': {'key': 'revisedBy', 'type': 'IdentityReference'},
        'revised_date': {'key': 'revisedDate', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, rev=None, revised_by=None, revised_date=None, value=None):
        super(WorkItemHistory, self).__init__(url=url, _links=_links)
        self.rev = rev
        self.revised_by = revised_by
        self.revised_date = revised_date
        self.value = value


class WorkItemTemplateReference(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, description=None, id=None, name=None, work_item_type_name=None):
        super(WorkItemTemplateReference, self).__init__(url=url, _links=_links)
        self.description = description
        self.id = id
        self.name = name
        self.work_item_type_name = work_item_type_name


class WorkItemTrackingReference(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, name=None, reference_name=None):
        super(WorkItemTrackingReference, self).__init__(url=url, _links=_links)
        self.name = name
        self.reference_name = reference_name


class WorkItemRelationType(WorkItemTrackingReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': '{object}'}
    }

    def __init__(self, url=None, _links=None, name=None, reference_name=None, attributes=None):
        super(WorkItemRelationType, self).__init__(url=url, _links=_links, name=name, reference_name=reference_name)
        self.attributes = attributes


class WorkItemTemplate(WorkItemTemplateReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '{str}'}
    }

    def __init__(self, url=None, _links=None, description=None, id=None, name=None, work_item_type_name=None, fields=None):
        super(WorkItemTemplate, self).__init__(url=url, _links=_links, description=description, id=id, name=name, work_item_type_name=work_item_type_name)
        self.fields = fields


__all__ = [
    'AccountMyWorkResult',
    'AccountRecentActivityWorkItemModelBase',
    'AccountRecentMentionWorkItemModel',
    'AccountWorkWorkItemModel',
    'ArtifactUriQuery',
    'ArtifactUriQueryResult',
    'AttachmentReference',
    'CommentCreate',
    'CommentUpdate',
    'ExternalDeployment',
    'ExternalEnvironment',
    'ExternalPipeline',
    'GraphSubjectBase',
    'IdentityRef',
    'IdentityReference',
    'JsonPatchOperation',
    'Link',
    'ProcessIdModel',
    'ProcessMigrationResultModel',
    'ProjectWorkItemStateColors',
    'ProvisioningResult',
    'QueryBatchGetRequest',
    'QueryHierarchyItemsResult',
    'ReferenceLinks',
    'ReportingWorkItemRevisionsFilter',
    'StreamedBatch',
    'TeamContext',
    'UpdateWorkItemField',
    'Wiql',
    'WorkArtifactLink',
    'WorkItemBatchGetRequest',
    'WorkItemDeleteReference',
    'WorkItemDeleteShallowReference',
    'WorkItemDeleteUpdate',
    'WorkItemFieldOperation',
    'WorkItemFieldReference',
    'WorkItemFieldUpdate',
    'WorkItemIcon',
    'WorkItemLink',
    'WorkItemNextStateOnTransition',
    'WorkItemQueryClause',
    'WorkItemQueryResult',
    'WorkItemQuerySortColumn',
    'WorkItemReference',
    'WorkItemRelation',
    'WorkItemRelationUpdates',
    'WorkItemStateColor',
    'WorkItemStateTransition',
    'WorkItemTagDefinition',
    'WorkItemTrackingResourceReference',
    'WorkItemTypeColor',
    'WorkItemTypeColorAndIcon',
    'WorkItemTypeFieldInstanceBase',
    'WorkItemTypeFieldWithReferences',
    'WorkItemTypeReference',
    'WorkItemTypeStateColors',
    'WorkItemTypeTemplate',
    'WorkItemTypeTemplateUpdateModel',
    'AccountRecentActivityWorkItemModel',
    'AccountRecentActivityWorkItemModel2',
    'ReportingWorkItemLinksBatch',
    'ReportingWorkItemRevisionsBatch',
    'WorkItemCommentVersionRef',
    'WorkItemDelete',
    'WorkItemTrackingResource',
    'WorkItemType',
    'WorkItemTypeCategory',
    'WorkItemTypeFieldInstance',
    'WorkItemUpdate',
    'Comment',
    'CommentList',
    'CommentMention',
    'CommentReaction',
    'CommentVersion',
    'FieldDependentRule',
    'QueryHierarchyItem',
    'WorkItem',
    'WorkItemClassificationNode',
    'WorkItemComment',
    'WorkItemComments',
    'WorkItemField',
    'WorkItemHistory',
    'WorkItemTemplateReference',
    'WorkItemTrackingReference',
    'WorkItemRelationType',
    'WorkItemTemplate',
]
