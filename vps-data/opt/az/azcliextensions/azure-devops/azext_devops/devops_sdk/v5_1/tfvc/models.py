# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AssociatedWorkItem(Model):

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, id=None, state=None, title=None, url=None, web_url=None, work_item_type=None):
        super(AssociatedWorkItem, self).__init__()
        self.assigned_to = assigned_to
        self.id = id
        self.state = state
        self.title = title
        self.url = url
        self.web_url = web_url
        self.work_item_type = work_item_type


class Change(Model):

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'item': {'key': 'item', 'type': 'object'},
        'new_content': {'key': 'newContent', 'type': 'ItemContent'},
        'source_server_item': {'key': 'sourceServerItem', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, change_type=None, item=None, new_content=None, source_server_item=None, url=None):
        super(Change, self).__init__()
        self.change_type = change_type
        self.item = item
        self.new_content = new_content
        self.source_server_item = source_server_item
        self.url = url


class CheckinNote(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(CheckinNote, self).__init__()
        self.name = name
        self.value = value


class FileContentMetadata(Model):

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'encoding': {'key': 'encoding', 'type': 'int'},
        'extension': {'key': 'extension', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'is_binary': {'key': 'isBinary', 'type': 'bool'},
        'is_image': {'key': 'isImage', 'type': 'bool'},
        'vs_link': {'key': 'vsLink', 'type': 'str'}
    }

    def __init__(self, content_type=None, encoding=None, extension=None, file_name=None, is_binary=None, is_image=None, vs_link=None):
        super(FileContentMetadata, self).__init__()
        self.content_type = content_type
        self.encoding = encoding
        self.extension = extension
        self.file_name = file_name
        self.is_binary = is_binary
        self.is_image = is_image
        self.vs_link = vs_link


class GitRepository(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_fork': {'key': 'isFork', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_repository': {'key': 'parentRepository', 'type': 'GitRepositoryRef'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'ssh_url': {'key': 'sshUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'valid_remote_urls': {'key': 'validRemoteUrls', 'type': '[str]'},
        'web_url': {'key': 'webUrl', 'type': 'str'}
    }

    def __init__(self, _links=None, default_branch=None, id=None, is_fork=None, name=None, parent_repository=None, project=None, remote_url=None, size=None, ssh_url=None, url=None, valid_remote_urls=None, web_url=None):
        super(GitRepository, self).__init__()
        self._links = _links
        self.default_branch = default_branch
        self.id = id
        self.is_fork = is_fork
        self.name = name
        self.parent_repository = parent_repository
        self.project = project
        self.remote_url = remote_url
        self.size = size
        self.ssh_url = ssh_url
        self.url = url
        self.valid_remote_urls = valid_remote_urls
        self.web_url = web_url


class GitRepositoryRef(Model):

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'TeamProjectCollectionReference'},
        'id': {'key': 'id', 'type': 'str'},
        'is_fork': {'key': 'isFork', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'ssh_url': {'key': 'sshUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, collection=None, id=None, is_fork=None, name=None, project=None, remote_url=None, ssh_url=None, url=None):
        super(GitRepositoryRef, self).__init__()
        self.collection = collection
        self.id = id
        self.is_fork = is_fork
        self.name = name
        self.project = project
        self.remote_url = remote_url
        self.ssh_url = ssh_url
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


class ItemContent(Model):

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'object'}
    }

    def __init__(self, content=None, content_type=None):
        super(ItemContent, self).__init__()
        self.content = content
        self.content_type = content_type


class ItemModel(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'content': {'key': 'content', 'type': 'str'},
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, content=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None):
        super(ItemModel, self).__init__()
        self._links = _links
        self.content = content
        self.content_metadata = content_metadata
        self.is_folder = is_folder
        self.is_sym_link = is_sym_link
        self.path = path
        self.url = url


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class TeamProjectCollectionReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(TeamProjectCollectionReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class TeamProjectReference(Model):

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.default_team_image_url = default_team_image_url
        self.description = description
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility


class TfvcBranchMapping(Model):

    _attribute_map = {
        'depth': {'key': 'depth', 'type': 'str'},
        'server_item': {'key': 'serverItem', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, depth=None, server_item=None, type=None):
        super(TfvcBranchMapping, self).__init__()
        self.depth = depth
        self.server_item = server_item
        self.type = type


class TfvcChange(Change):

    _attribute_map = {
        'merge_sources': {'key': 'mergeSources', 'type': '[TfvcMergeSource]'},
        'pending_version': {'key': 'pendingVersion', 'type': 'int'}
    }

    def __init__(self, merge_sources=None, pending_version=None):
        super(TfvcChange, self).__init__()
        self.merge_sources = merge_sources
        self.pending_version = pending_version


class TfvcChangesetRef(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'changeset_id': {'key': 'changesetId', 'type': 'int'},
        'checked_in_by': {'key': 'checkedInBy', 'type': 'IdentityRef'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, changeset_id=None, checked_in_by=None, comment=None, comment_truncated=None, created_date=None, url=None):
        super(TfvcChangesetRef, self).__init__()
        self._links = _links
        self.author = author
        self.changeset_id = changeset_id
        self.checked_in_by = checked_in_by
        self.comment = comment
        self.comment_truncated = comment_truncated
        self.created_date = created_date
        self.url = url


class TfvcChangesetSearchCriteria(Model):

    _attribute_map = {
        'author': {'key': 'author', 'type': 'str'},
        'follow_renames': {'key': 'followRenames', 'type': 'bool'},
        'from_date': {'key': 'fromDate', 'type': 'str'},
        'from_id': {'key': 'fromId', 'type': 'int'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_path': {'key': 'itemPath', 'type': 'str'},
        'mappings': {'key': 'mappings', 'type': '[TfvcMappingFilter]'},
        'to_date': {'key': 'toDate', 'type': 'str'},
        'to_id': {'key': 'toId', 'type': 'int'}
    }

    def __init__(self, author=None, follow_renames=None, from_date=None, from_id=None, include_links=None, item_path=None, mappings=None, to_date=None, to_id=None):
        super(TfvcChangesetSearchCriteria, self).__init__()
        self.author = author
        self.follow_renames = follow_renames
        self.from_date = from_date
        self.from_id = from_id
        self.include_links = include_links
        self.item_path = item_path
        self.mappings = mappings
        self.to_date = to_date
        self.to_id = to_id


class TfvcChangesetsRequestData(Model):

    _attribute_map = {
        'changeset_ids': {'key': 'changesetIds', 'type': '[int]'},
        'comment_length': {'key': 'commentLength', 'type': 'int'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'}
    }

    def __init__(self, changeset_ids=None, comment_length=None, include_links=None):
        super(TfvcChangesetsRequestData, self).__init__()
        self.changeset_ids = changeset_ids
        self.comment_length = comment_length
        self.include_links = include_links


class TfvcItem(ItemModel):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'content': {'key': 'content', 'type': 'str'},
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'change_date': {'key': 'changeDate', 'type': 'iso-8601'},
        'deletion_id': {'key': 'deletionId', 'type': 'int'},
        'encoding': {'key': 'encoding', 'type': 'int'},
        'hash_value': {'key': 'hashValue', 'type': 'str'},
        'is_branch': {'key': 'isBranch', 'type': 'bool'},
        'is_pending_change': {'key': 'isPendingChange', 'type': 'bool'},
        'size': {'key': 'size', 'type': 'long'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, _links=None, content=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None, change_date=None, deletion_id=None, encoding=None, hash_value=None, is_branch=None, is_pending_change=None, size=None, version=None):
        super(TfvcItem, self).__init__(_links=_links, content=content, content_metadata=content_metadata, is_folder=is_folder, is_sym_link=is_sym_link, path=path, url=url)
        self.change_date = change_date
        self.deletion_id = deletion_id
        self.encoding = encoding
        self.hash_value = hash_value
        self.is_branch = is_branch
        self.is_pending_change = is_pending_change
        self.size = size
        self.version = version


class TfvcItemDescriptor(Model):

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'recursion_level': {'key': 'recursionLevel', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'},
        'version_option': {'key': 'versionOption', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, path=None, recursion_level=None, version=None, version_option=None, version_type=None):
        super(TfvcItemDescriptor, self).__init__()
        self.path = path
        self.recursion_level = recursion_level
        self.version = version
        self.version_option = version_option
        self.version_type = version_type


class TfvcItemRequestData(Model):

    _attribute_map = {
        'include_content_metadata': {'key': 'includeContentMetadata', 'type': 'bool'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_descriptors': {'key': 'itemDescriptors', 'type': '[TfvcItemDescriptor]'}
    }

    def __init__(self, include_content_metadata=None, include_links=None, item_descriptors=None):
        super(TfvcItemRequestData, self).__init__()
        self.include_content_metadata = include_content_metadata
        self.include_links = include_links
        self.item_descriptors = item_descriptors


class TfvcLabelRef(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'label_scope': {'key': 'labelScope', 'type': 'str'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, description=None, id=None, label_scope=None, modified_date=None, name=None, owner=None, url=None):
        super(TfvcLabelRef, self).__init__()
        self._links = _links
        self.description = description
        self.id = id
        self.label_scope = label_scope
        self.modified_date = modified_date
        self.name = name
        self.owner = owner
        self.url = url


class TfvcLabelRequestData(Model):

    _attribute_map = {
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_label_filter': {'key': 'itemLabelFilter', 'type': 'str'},
        'label_scope': {'key': 'labelScope', 'type': 'str'},
        'max_item_count': {'key': 'maxItemCount', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'}
    }

    def __init__(self, include_links=None, item_label_filter=None, label_scope=None, max_item_count=None, name=None, owner=None):
        super(TfvcLabelRequestData, self).__init__()
        self.include_links = include_links
        self.item_label_filter = item_label_filter
        self.label_scope = label_scope
        self.max_item_count = max_item_count
        self.name = name
        self.owner = owner


class TfvcMappingFilter(Model):

    _attribute_map = {
        'exclude': {'key': 'exclude', 'type': 'bool'},
        'server_path': {'key': 'serverPath', 'type': 'str'}
    }

    def __init__(self, exclude=None, server_path=None):
        super(TfvcMappingFilter, self).__init__()
        self.exclude = exclude
        self.server_path = server_path


class TfvcMergeSource(Model):

    _attribute_map = {
        'is_rename': {'key': 'isRename', 'type': 'bool'},
        'server_item': {'key': 'serverItem', 'type': 'str'},
        'version_from': {'key': 'versionFrom', 'type': 'int'},
        'version_to': {'key': 'versionTo', 'type': 'int'}
    }

    def __init__(self, is_rename=None, server_item=None, version_from=None, version_to=None):
        super(TfvcMergeSource, self).__init__()
        self.is_rename = is_rename
        self.server_item = server_item
        self.version_from = version_from
        self.version_to = version_to


class TfvcPolicyFailureInfo(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'policy_name': {'key': 'policyName', 'type': 'str'}
    }

    def __init__(self, message=None, policy_name=None):
        super(TfvcPolicyFailureInfo, self).__init__()
        self.message = message
        self.policy_name = policy_name


class TfvcPolicyOverrideInfo(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'policy_failures': {'key': 'policyFailures', 'type': '[TfvcPolicyFailureInfo]'}
    }

    def __init__(self, comment=None, policy_failures=None):
        super(TfvcPolicyOverrideInfo, self).__init__()
        self.comment = comment
        self.policy_failures = policy_failures


class TfvcShallowBranchRef(Model):

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, path=None):
        super(TfvcShallowBranchRef, self).__init__()
        self.path = path


class TfvcShelvesetRef(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, comment=None, comment_truncated=None, created_date=None, id=None, name=None, owner=None, url=None):
        super(TfvcShelvesetRef, self).__init__()
        self._links = _links
        self.comment = comment
        self.comment_truncated = comment_truncated
        self.created_date = created_date
        self.id = id
        self.name = name
        self.owner = owner
        self.url = url


class TfvcShelvesetRequestData(Model):

    _attribute_map = {
        'include_details': {'key': 'includeDetails', 'type': 'bool'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'include_work_items': {'key': 'includeWorkItems', 'type': 'bool'},
        'max_change_count': {'key': 'maxChangeCount', 'type': 'int'},
        'max_comment_length': {'key': 'maxCommentLength', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'}
    }

    def __init__(self, include_details=None, include_links=None, include_work_items=None, max_change_count=None, max_comment_length=None, name=None, owner=None):
        super(TfvcShelvesetRequestData, self).__init__()
        self.include_details = include_details
        self.include_links = include_links
        self.include_work_items = include_work_items
        self.max_change_count = max_change_count
        self.max_comment_length = max_comment_length
        self.name = name
        self.owner = owner


class TfvcStatistics(Model):

    _attribute_map = {
        'changeset_id': {'key': 'changesetId', 'type': 'int'},
        'file_count_total': {'key': 'fileCountTotal', 'type': 'long'}
    }

    def __init__(self, changeset_id=None, file_count_total=None):
        super(TfvcStatistics, self).__init__()
        self.changeset_id = changeset_id
        self.file_count_total = file_count_total


class TfvcVersionDescriptor(Model):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_option': {'key': 'versionOption', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_option=None, version_type=None):
        super(TfvcVersionDescriptor, self).__init__()
        self.version = version
        self.version_option = version_option
        self.version_type = version_type


class VersionControlProjectInfo(Model):

    _attribute_map = {
        'default_source_control_type': {'key': 'defaultSourceControlType', 'type': 'object'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'supports_git': {'key': 'supportsGit', 'type': 'bool'},
        'supports_tFVC': {'key': 'supportsTFVC', 'type': 'bool'}
    }

    def __init__(self, default_source_control_type=None, project=None, supports_git=None, supports_tFVC=None):
        super(VersionControlProjectInfo, self).__init__()
        self.default_source_control_type = default_source_control_type
        self.project = project
        self.supports_git = supports_git
        self.supports_tFVC = supports_tFVC


class VstsInfo(Model):

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'TeamProjectCollectionReference'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'server_url': {'key': 'serverUrl', 'type': 'str'}
    }

    def __init__(self, collection=None, repository=None, server_url=None):
        super(VstsInfo, self).__init__()
        self.collection = collection
        self.repository = repository
        self.server_url = server_url


class TfvcBranchRef(TfvcShallowBranchRef):

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, path=None, _links=None, created_date=None, description=None, is_deleted=None, owner=None, url=None):
        super(TfvcBranchRef, self).__init__(path=path)
        self._links = _links
        self.created_date = created_date
        self.description = description
        self.is_deleted = is_deleted
        self.owner = owner
        self.url = url


class TfvcChangeset(TfvcChangesetRef):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'changeset_id': {'key': 'changesetId', 'type': 'int'},
        'checked_in_by': {'key': 'checkedInBy', 'type': 'IdentityRef'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
        'changes': {'key': 'changes', 'type': '[TfvcChange]'},
        'checkin_notes': {'key': 'checkinNotes', 'type': '[CheckinNote]'},
        'collection_id': {'key': 'collectionId', 'type': 'str'},
        'has_more_changes': {'key': 'hasMoreChanges', 'type': 'bool'},
        'policy_override': {'key': 'policyOverride', 'type': 'TfvcPolicyOverrideInfo'},
        'team_project_ids': {'key': 'teamProjectIds', 'type': '[str]'},
        'work_items': {'key': 'workItems', 'type': '[AssociatedWorkItem]'}
    }

    def __init__(self, _links=None, author=None, changeset_id=None, checked_in_by=None, comment=None, comment_truncated=None, created_date=None, url=None, account_id=None, changes=None, checkin_notes=None, collection_id=None, has_more_changes=None, policy_override=None, team_project_ids=None, work_items=None):
        super(TfvcChangeset, self).__init__(_links=_links, author=author, changeset_id=changeset_id, checked_in_by=checked_in_by, comment=comment, comment_truncated=comment_truncated, created_date=created_date, url=url)
        self.account_id = account_id
        self.changes = changes
        self.checkin_notes = checkin_notes
        self.collection_id = collection_id
        self.has_more_changes = has_more_changes
        self.policy_override = policy_override
        self.team_project_ids = team_project_ids
        self.work_items = work_items


class TfvcLabel(TfvcLabelRef):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'label_scope': {'key': 'labelScope', 'type': 'str'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'items': {'key': 'items', 'type': '[TfvcItem]'}
    }

    def __init__(self, _links=None, description=None, id=None, label_scope=None, modified_date=None, name=None, owner=None, url=None, items=None):
        super(TfvcLabel, self).__init__(_links=_links, description=description, id=id, label_scope=label_scope, modified_date=modified_date, name=name, owner=owner, url=url)
        self.items = items


class TfvcShelveset(TfvcShelvesetRef):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'changes': {'key': 'changes', 'type': '[TfvcChange]'},
        'notes': {'key': 'notes', 'type': '[CheckinNote]'},
        'policy_override': {'key': 'policyOverride', 'type': 'TfvcPolicyOverrideInfo'},
        'work_items': {'key': 'workItems', 'type': '[AssociatedWorkItem]'}
    }

    def __init__(self, _links=None, comment=None, comment_truncated=None, created_date=None, id=None, name=None, owner=None, url=None, changes=None, notes=None, policy_override=None, work_items=None):
        super(TfvcShelveset, self).__init__(_links=_links, comment=comment, comment_truncated=comment_truncated, created_date=created_date, id=id, name=name, owner=owner, url=url)
        self.changes = changes
        self.notes = notes
        self.policy_override = policy_override
        self.work_items = work_items


class TfvcBranch(TfvcBranchRef):

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'children': {'key': 'children', 'type': '[TfvcBranch]'},
        'mappings': {'key': 'mappings', 'type': '[TfvcBranchMapping]'},
        'parent': {'key': 'parent', 'type': 'TfvcShallowBranchRef'},
        'related_branches': {'key': 'relatedBranches', 'type': '[TfvcShallowBranchRef]'}
    }

    def __init__(self, path=None, _links=None, created_date=None, description=None, is_deleted=None, owner=None, url=None, children=None, mappings=None, parent=None, related_branches=None):
        super(TfvcBranch, self).__init__(path=path, _links=_links, created_date=created_date, description=description, is_deleted=is_deleted, owner=owner, url=url)
        self.children = children
        self.mappings = mappings
        self.parent = parent
        self.related_branches = related_branches


__all__ = [
    'AssociatedWorkItem',
    'Change',
    'CheckinNote',
    'FileContentMetadata',
    'GitRepository',
    'GitRepositoryRef',
    'GraphSubjectBase',
    'IdentityRef',
    'ItemContent',
    'ItemModel',
    'ReferenceLinks',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'TfvcBranchMapping',
    'TfvcChange',
    'TfvcChangesetRef',
    'TfvcChangesetSearchCriteria',
    'TfvcChangesetsRequestData',
    'TfvcItem',
    'TfvcItemDescriptor',
    'TfvcItemRequestData',
    'TfvcLabelRef',
    'TfvcLabelRequestData',
    'TfvcMappingFilter',
    'TfvcMergeSource',
    'TfvcPolicyFailureInfo',
    'TfvcPolicyOverrideInfo',
    'TfvcShallowBranchRef',
    'TfvcShelvesetRef',
    'TfvcShelvesetRequestData',
    'TfvcStatistics',
    'TfvcVersionDescriptor',
    'VersionControlProjectInfo',
    'VstsInfo',
    'TfvcBranchRef',
    'TfvcChangeset',
    'TfvcLabel',
    'TfvcShelveset',
    'TfvcBranch',
]
