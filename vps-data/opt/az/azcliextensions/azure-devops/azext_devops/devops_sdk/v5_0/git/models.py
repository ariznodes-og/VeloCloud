# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Attachment(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'content_hash': {'key': 'contentHash', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, content_hash=None, created_date=None, description=None, display_name=None, id=None, properties=None, url=None):
        super(Attachment, self).__init__()
        self._links = _links
        self.author = author
        self.content_hash = content_hash
        self.created_date = created_date
        self.description = description
        self.display_name = display_name
        self.id = id
        self.properties = properties
        self.url = url


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


class Comment(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'comment_type': {'key': 'commentType', 'type': 'object'},
        'content': {'key': 'content', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_content_updated_date': {'key': 'lastContentUpdatedDate', 'type': 'iso-8601'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'parent_comment_id': {'key': 'parentCommentId', 'type': 'int'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'users_liked': {'key': 'usersLiked', 'type': '[IdentityRef]'}
    }

    def __init__(self, _links=None, author=None, comment_type=None, content=None, id=None, is_deleted=None, last_content_updated_date=None, last_updated_date=None, parent_comment_id=None, published_date=None, users_liked=None):
        super(Comment, self).__init__()
        self._links = _links
        self.author = author
        self.comment_type = comment_type
        self.content = content
        self.id = id
        self.is_deleted = is_deleted
        self.last_content_updated_date = last_content_updated_date
        self.last_updated_date = last_updated_date
        self.parent_comment_id = parent_comment_id
        self.published_date = published_date
        self.users_liked = users_liked


class CommentIterationContext(Model):

    _attribute_map = {
        'first_comparing_iteration': {'key': 'firstComparingIteration', 'type': 'int'},
        'second_comparing_iteration': {'key': 'secondComparingIteration', 'type': 'int'}
    }

    def __init__(self, first_comparing_iteration=None, second_comparing_iteration=None):
        super(CommentIterationContext, self).__init__()
        self.first_comparing_iteration = first_comparing_iteration
        self.second_comparing_iteration = second_comparing_iteration


class CommentPosition(Model):

    _attribute_map = {
        'line': {'key': 'line', 'type': 'int'},
        'offset': {'key': 'offset', 'type': 'int'}
    }

    def __init__(self, line=None, offset=None):
        super(CommentPosition, self).__init__()
        self.line = line
        self.offset = offset


class CommentThread(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'id': {'key': 'id', 'type': 'int'},
        'identities': {'key': 'identities', 'type': '{IdentityRef}'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': 'object'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'thread_context': {'key': 'threadContext', 'type': 'CommentThreadContext'}
    }

    def __init__(self, _links=None, comments=None, id=None, identities=None, is_deleted=None, last_updated_date=None, properties=None, published_date=None, status=None, thread_context=None):
        super(CommentThread, self).__init__()
        self._links = _links
        self.comments = comments
        self.id = id
        self.identities = identities
        self.is_deleted = is_deleted
        self.last_updated_date = last_updated_date
        self.properties = properties
        self.published_date = published_date
        self.status = status
        self.thread_context = thread_context


class CommentThreadContext(Model):

    _attribute_map = {
        'file_path': {'key': 'filePath', 'type': 'str'},
        'left_file_end': {'key': 'leftFileEnd', 'type': 'CommentPosition'},
        'left_file_start': {'key': 'leftFileStart', 'type': 'CommentPosition'},
        'right_file_end': {'key': 'rightFileEnd', 'type': 'CommentPosition'},
        'right_file_start': {'key': 'rightFileStart', 'type': 'CommentPosition'}
    }

    def __init__(self, file_path=None, left_file_end=None, left_file_start=None, right_file_end=None, right_file_start=None):
        super(CommentThreadContext, self).__init__()
        self.file_path = file_path
        self.left_file_end = left_file_end
        self.left_file_start = left_file_start
        self.right_file_end = right_file_end
        self.right_file_start = right_file_start


class CommentTrackingCriteria(Model):

    _attribute_map = {
        'first_comparing_iteration': {'key': 'firstComparingIteration', 'type': 'int'},
        'orig_file_path': {'key': 'origFilePath', 'type': 'str'},
        'orig_left_file_end': {'key': 'origLeftFileEnd', 'type': 'CommentPosition'},
        'orig_left_file_start': {'key': 'origLeftFileStart', 'type': 'CommentPosition'},
        'orig_right_file_end': {'key': 'origRightFileEnd', 'type': 'CommentPosition'},
        'orig_right_file_start': {'key': 'origRightFileStart', 'type': 'CommentPosition'},
        'second_comparing_iteration': {'key': 'secondComparingIteration', 'type': 'int'}
    }

    def __init__(self, first_comparing_iteration=None, orig_file_path=None, orig_left_file_end=None, orig_left_file_start=None, orig_right_file_end=None, orig_right_file_start=None, second_comparing_iteration=None):
        super(CommentTrackingCriteria, self).__init__()
        self.first_comparing_iteration = first_comparing_iteration
        self.orig_file_path = orig_file_path
        self.orig_left_file_end = orig_left_file_end
        self.orig_left_file_start = orig_left_file_start
        self.orig_right_file_end = orig_right_file_end
        self.orig_right_file_start = orig_right_file_start
        self.second_comparing_iteration = second_comparing_iteration


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


class FileDiff(Model):

    _attribute_map = {
        'line_diff_blocks': {'key': 'lineDiffBlocks', 'type': '[LineDiffBlock]'},
        'original_path': {'key': 'originalPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, line_diff_blocks=None, original_path=None, path=None):
        super(FileDiff, self).__init__()
        self.line_diff_blocks = line_diff_blocks
        self.original_path = original_path
        self.path = path


class FileDiffParams(Model):

    _attribute_map = {
        'original_path': {'key': 'originalPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, original_path=None, path=None):
        super(FileDiffParams, self).__init__()
        self.original_path = original_path
        self.path = path


class FileDiffsCriteria(Model):

    _attribute_map = {
        'base_version_commit': {'key': 'baseVersionCommit', 'type': 'str'},
        'file_diff_params': {'key': 'fileDiffParams', 'type': '[FileDiffParams]'},
        'target_version_commit': {'key': 'targetVersionCommit', 'type': 'str'}
    }

    def __init__(self, base_version_commit=None, file_diff_params=None, target_version_commit=None):
        super(FileDiffsCriteria, self).__init__()
        self.base_version_commit = base_version_commit
        self.file_diff_params = file_diff_params
        self.target_version_commit = target_version_commit


class GitAnnotatedTag(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'tagged_by': {'key': 'taggedBy', 'type': 'GitUserDate'},
        'tagged_object': {'key': 'taggedObject', 'type': 'GitObject'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, message=None, name=None, object_id=None, tagged_by=None, tagged_object=None, url=None):
        super(GitAnnotatedTag, self).__init__()
        self.message = message
        self.name = name
        self.object_id = object_id
        self.tagged_by = tagged_by
        self.tagged_object = tagged_object
        self.url = url


class GitAsyncRefOperation(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None):
        super(GitAsyncRefOperation, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.parameters = parameters
        self.status = status
        self.url = url


class GitAsyncRefOperationDetail(Model):

    _attribute_map = {
        'conflict': {'key': 'conflict', 'type': 'bool'},
        'current_commit_id': {'key': 'currentCommitId', 'type': 'str'},
        'failure_message': {'key': 'failureMessage', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'float'},
        'status': {'key': 'status', 'type': 'object'},
        'timedout': {'key': 'timedout', 'type': 'bool'}
    }

    def __init__(self, conflict=None, current_commit_id=None, failure_message=None, progress=None, status=None, timedout=None):
        super(GitAsyncRefOperationDetail, self).__init__()
        self.conflict = conflict
        self.current_commit_id = current_commit_id
        self.failure_message = failure_message
        self.progress = progress
        self.status = status
        self.timedout = timedout


class GitAsyncRefOperationParameters(Model):

    _attribute_map = {
        'generated_ref_name': {'key': 'generatedRefName', 'type': 'str'},
        'onto_ref_name': {'key': 'ontoRefName', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'source': {'key': 'source', 'type': 'GitAsyncRefOperationSource'}
    }

    def __init__(self, generated_ref_name=None, onto_ref_name=None, repository=None, source=None):
        super(GitAsyncRefOperationParameters, self).__init__()
        self.generated_ref_name = generated_ref_name
        self.onto_ref_name = onto_ref_name
        self.repository = repository
        self.source = source


class GitAsyncRefOperationSource(Model):

    _attribute_map = {
        'commit_list': {'key': 'commitList', 'type': '[GitCommitRef]'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'}
    }

    def __init__(self, commit_list=None, pull_request_id=None):
        super(GitAsyncRefOperationSource, self).__init__()
        self.commit_list = commit_list
        self.pull_request_id = pull_request_id


class GitBlobRef(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, object_id=None, size=None, url=None):
        super(GitBlobRef, self).__init__()
        self._links = _links
        self.object_id = object_id
        self.size = size
        self.url = url


class GitBranchStats(Model):

    _attribute_map = {
        'ahead_count': {'key': 'aheadCount', 'type': 'int'},
        'behind_count': {'key': 'behindCount', 'type': 'int'},
        'commit': {'key': 'commit', 'type': 'GitCommitRef'},
        'is_base_version': {'key': 'isBaseVersion', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, ahead_count=None, behind_count=None, commit=None, is_base_version=None, name=None):
        super(GitBranchStats, self).__init__()
        self.ahead_count = ahead_count
        self.behind_count = behind_count
        self.commit = commit
        self.is_base_version = is_base_version
        self.name = name


class GitCherryPick(GitAsyncRefOperation):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'cherry_pick_id': {'key': 'cherryPickId', 'type': 'int'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None, cherry_pick_id=None):
        super(GitCherryPick, self).__init__(_links=_links, detailed_status=detailed_status, parameters=parameters, status=status, url=url)
        self.cherry_pick_id = cherry_pick_id


class GitCommitChanges(Model):

    _attribute_map = {
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'}
    }

    def __init__(self, change_counts=None, changes=None):
        super(GitCommitChanges, self).__init__()
        self.change_counts = change_counts
        self.changes = changes


class GitCommitDiffs(Model):

    _attribute_map = {
        'ahead_count': {'key': 'aheadCount', 'type': 'int'},
        'all_changes_included': {'key': 'allChangesIncluded', 'type': 'bool'},
        'base_commit': {'key': 'baseCommit', 'type': 'str'},
        'behind_count': {'key': 'behindCount', 'type': 'int'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'common_commit': {'key': 'commonCommit', 'type': 'str'},
        'target_commit': {'key': 'targetCommit', 'type': 'str'}
    }

    def __init__(self, ahead_count=None, all_changes_included=None, base_commit=None, behind_count=None, change_counts=None, changes=None, common_commit=None, target_commit=None):
        super(GitCommitDiffs, self).__init__()
        self.ahead_count = ahead_count
        self.all_changes_included = all_changes_included
        self.base_commit = base_commit
        self.behind_count = behind_count
        self.change_counts = change_counts
        self.changes = changes
        self.common_commit = common_commit
        self.target_commit = target_commit


class GitCommitRef(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'GitUserDate'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'committer': {'key': 'committer', 'type': 'GitUserDate'},
        'parents': {'key': 'parents', 'type': '[str]'},
        'push': {'key': 'push', 'type': 'GitPushRef'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'work_items': {'key': 'workItems', 'type': '[ResourceRef]'}
    }

    def __init__(self, _links=None, author=None, change_counts=None, changes=None, comment=None, comment_truncated=None, commit_id=None, committer=None, parents=None, push=None, remote_url=None, statuses=None, url=None, work_items=None):
        super(GitCommitRef, self).__init__()
        self._links = _links
        self.author = author
        self.change_counts = change_counts
        self.changes = changes
        self.comment = comment
        self.comment_truncated = comment_truncated
        self.commit_id = commit_id
        self.committer = committer
        self.parents = parents
        self.push = push
        self.remote_url = remote_url
        self.statuses = statuses
        self.url = url
        self.work_items = work_items


class GitConflict(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'conflict_id': {'key': 'conflictId', 'type': 'int'},
        'conflict_path': {'key': 'conflictPath', 'type': 'str'},
        'conflict_type': {'key': 'conflictType', 'type': 'object'},
        'merge_base_commit': {'key': 'mergeBaseCommit', 'type': 'GitCommitRef'},
        'merge_origin': {'key': 'mergeOrigin', 'type': 'GitMergeOriginRef'},
        'merge_source_commit': {'key': 'mergeSourceCommit', 'type': 'GitCommitRef'},
        'merge_target_commit': {'key': 'mergeTargetCommit', 'type': 'GitCommitRef'},
        'resolution_error': {'key': 'resolutionError', 'type': 'object'},
        'resolution_status': {'key': 'resolutionStatus', 'type': 'object'},
        'resolved_by': {'key': 'resolvedBy', 'type': 'IdentityRef'},
        'resolved_date': {'key': 'resolvedDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, conflict_id=None, conflict_path=None, conflict_type=None, merge_base_commit=None, merge_origin=None, merge_source_commit=None, merge_target_commit=None, resolution_error=None, resolution_status=None, resolved_by=None, resolved_date=None, url=None):
        super(GitConflict, self).__init__()
        self._links = _links
        self.conflict_id = conflict_id
        self.conflict_path = conflict_path
        self.conflict_type = conflict_type
        self.merge_base_commit = merge_base_commit
        self.merge_origin = merge_origin
        self.merge_source_commit = merge_source_commit
        self.merge_target_commit = merge_target_commit
        self.resolution_error = resolution_error
        self.resolution_status = resolution_status
        self.resolved_by = resolved_by
        self.resolved_date = resolved_date
        self.url = url


class GitConflictUpdateResult(Model):

    _attribute_map = {
        'conflict_id': {'key': 'conflictId', 'type': 'int'},
        'custom_message': {'key': 'customMessage', 'type': 'str'},
        'updated_conflict': {'key': 'updatedConflict', 'type': 'GitConflict'},
        'update_status': {'key': 'updateStatus', 'type': 'object'}
    }

    def __init__(self, conflict_id=None, custom_message=None, updated_conflict=None, update_status=None):
        super(GitConflictUpdateResult, self).__init__()
        self.conflict_id = conflict_id
        self.custom_message = custom_message
        self.updated_conflict = updated_conflict
        self.update_status = update_status


class GitDeletedRepository(Model):

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'deleted_by': {'key': 'deletedBy', 'type': 'IdentityRef'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, created_date=None, deleted_by=None, deleted_date=None, id=None, name=None, project=None):
        super(GitDeletedRepository, self).__init__()
        self.created_date = created_date
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.id = id
        self.name = name
        self.project = project


class GitFilePathsCollection(Model):

    _attribute_map = {
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'paths': {'key': 'paths', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, commit_id=None, paths=None, url=None):
        super(GitFilePathsCollection, self).__init__()
        self.commit_id = commit_id
        self.paths = paths
        self.url = url


class GitForkOperationStatusDetail(Model):

    _attribute_map = {
        'all_steps': {'key': 'allSteps', 'type': '[str]'},
        'current_step': {'key': 'currentStep', 'type': 'int'},
        'error_message': {'key': 'errorMessage', 'type': 'str'}
    }

    def __init__(self, all_steps=None, current_step=None, error_message=None):
        super(GitForkOperationStatusDetail, self).__init__()
        self.all_steps = all_steps
        self.current_step = current_step
        self.error_message = error_message


class GitForkSyncRequest(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitForkOperationStatusDetail'},
        'operation_id': {'key': 'operationId', 'type': 'int'},
        'source': {'key': 'source', 'type': 'GlobalGitRepositoryKey'},
        'source_to_target_refs': {'key': 'sourceToTargetRefs', 'type': '[SourceToTargetRef]'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, _links=None, detailed_status=None, operation_id=None, source=None, source_to_target_refs=None, status=None):
        super(GitForkSyncRequest, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.operation_id = operation_id
        self.source = source
        self.source_to_target_refs = source_to_target_refs
        self.status = status


class GitForkSyncRequestParameters(Model):

    _attribute_map = {
        'source': {'key': 'source', 'type': 'GlobalGitRepositoryKey'},
        'source_to_target_refs': {'key': 'sourceToTargetRefs', 'type': '[SourceToTargetRef]'}
    }

    def __init__(self, source=None, source_to_target_refs=None):
        super(GitForkSyncRequestParameters, self).__init__()
        self.source = source
        self.source_to_target_refs = source_to_target_refs


class GitImportGitSource(Model):

    _attribute_map = {
        'overwrite': {'key': 'overwrite', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, overwrite=None, url=None):
        super(GitImportGitSource, self).__init__()
        self.overwrite = overwrite
        self.url = url


class GitImportRequest(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitImportStatusDetail'},
        'import_request_id': {'key': 'importRequestId', 'type': 'int'},
        'parameters': {'key': 'parameters', 'type': 'GitImportRequestParameters'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, detailed_status=None, import_request_id=None, parameters=None, repository=None, status=None, url=None):
        super(GitImportRequest, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.import_request_id = import_request_id
        self.parameters = parameters
        self.repository = repository
        self.status = status
        self.url = url


class GitImportRequestParameters(Model):

    _attribute_map = {
        'delete_service_endpoint_after_import_is_done': {'key': 'deleteServiceEndpointAfterImportIsDone', 'type': 'bool'},
        'git_source': {'key': 'gitSource', 'type': 'GitImportGitSource'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'},
        'tfvc_source': {'key': 'tfvcSource', 'type': 'GitImportTfvcSource'}
    }

    def __init__(self, delete_service_endpoint_after_import_is_done=None, git_source=None, service_endpoint_id=None, tfvc_source=None):
        super(GitImportRequestParameters, self).__init__()
        self.delete_service_endpoint_after_import_is_done = delete_service_endpoint_after_import_is_done
        self.git_source = git_source
        self.service_endpoint_id = service_endpoint_id
        self.tfvc_source = tfvc_source


class GitImportStatusDetail(Model):

    _attribute_map = {
        'all_steps': {'key': 'allSteps', 'type': '[str]'},
        'current_step': {'key': 'currentStep', 'type': 'int'},
        'error_message': {'key': 'errorMessage', 'type': 'str'}
    }

    def __init__(self, all_steps=None, current_step=None, error_message=None):
        super(GitImportStatusDetail, self).__init__()
        self.all_steps = all_steps
        self.current_step = current_step
        self.error_message = error_message


class GitImportTfvcSource(Model):

    _attribute_map = {
        'import_history': {'key': 'importHistory', 'type': 'bool'},
        'import_history_duration_in_days': {'key': 'importHistoryDurationInDays', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, import_history=None, import_history_duration_in_days=None, path=None):
        super(GitImportTfvcSource, self).__init__()
        self.import_history = import_history
        self.import_history_duration_in_days = import_history_duration_in_days
        self.path = path


class GitItemDescriptor(Model):

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'recursion_level': {'key': 'recursionLevel', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, path=None, recursion_level=None, version=None, version_options=None, version_type=None):
        super(GitItemDescriptor, self).__init__()
        self.path = path
        self.recursion_level = recursion_level
        self.version = version
        self.version_options = version_options
        self.version_type = version_type


class GitItemRequestData(Model):

    _attribute_map = {
        'include_content_metadata': {'key': 'includeContentMetadata', 'type': 'bool'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_descriptors': {'key': 'itemDescriptors', 'type': '[GitItemDescriptor]'},
        'latest_processed_change': {'key': 'latestProcessedChange', 'type': 'bool'}
    }

    def __init__(self, include_content_metadata=None, include_links=None, item_descriptors=None, latest_processed_change=None):
        super(GitItemRequestData, self).__init__()
        self.include_content_metadata = include_content_metadata
        self.include_links = include_links
        self.item_descriptors = item_descriptors
        self.latest_processed_change = latest_processed_change


class GitMergeOperationStatusDetail(Model):

    _attribute_map = {
        'failure_message': {'key': 'failureMessage', 'type': 'str'},
        'merge_commit_id': {'key': 'mergeCommitId', 'type': 'str'}
    }

    def __init__(self, failure_message=None, merge_commit_id=None):
        super(GitMergeOperationStatusDetail, self).__init__()
        self.failure_message = failure_message
        self.merge_commit_id = merge_commit_id


class GitMergeOriginRef(Model):

    _attribute_map = {
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'}
    }

    def __init__(self, pull_request_id=None):
        super(GitMergeOriginRef, self).__init__()
        self.pull_request_id = pull_request_id


class GitMergeParameters(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'parents': {'key': 'parents', 'type': '[str]'}
    }

    def __init__(self, comment=None, parents=None):
        super(GitMergeParameters, self).__init__()
        self.comment = comment
        self.parents = parents


class GitObject(Model):

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'object'}
    }

    def __init__(self, object_id=None, object_type=None):
        super(GitObject, self).__init__()
        self.object_id = object_id
        self.object_type = object_type


class GitPullRequest(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'auto_complete_set_by': {'key': 'autoCompleteSetBy', 'type': 'IdentityRef'},
        'closed_by': {'key': 'closedBy', 'type': 'IdentityRef'},
        'closed_date': {'key': 'closedDate', 'type': 'iso-8601'},
        'code_review_id': {'key': 'codeReviewId', 'type': 'int'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'completion_options': {'key': 'completionOptions', 'type': 'GitPullRequestCompletionOptions'},
        'completion_queue_time': {'key': 'completionQueueTime', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'fork_source': {'key': 'forkSource', 'type': 'GitForkRef'},
        'is_draft': {'key': 'isDraft', 'type': 'bool'},
        'labels': {'key': 'labels', 'type': '[WebApiTagDefinition]'},
        'last_merge_commit': {'key': 'lastMergeCommit', 'type': 'GitCommitRef'},
        'last_merge_source_commit': {'key': 'lastMergeSourceCommit', 'type': 'GitCommitRef'},
        'last_merge_target_commit': {'key': 'lastMergeTargetCommit', 'type': 'GitCommitRef'},
        'merge_failure_message': {'key': 'mergeFailureMessage', 'type': 'str'},
        'merge_failure_type': {'key': 'mergeFailureType', 'type': 'object'},
        'merge_id': {'key': 'mergeId', 'type': 'str'},
        'merge_options': {'key': 'mergeOptions', 'type': 'GitPullRequestMergeOptions'},
        'merge_status': {'key': 'mergeStatus', 'type': 'object'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'reviewers': {'key': 'reviewers', 'type': '[IdentityRefWithVote]'},
        'source_ref_name': {'key': 'sourceRefName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'supports_iterations': {'key': 'supportsIterations', 'type': 'bool'},
        'target_ref_name': {'key': 'targetRefName', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'work_item_refs': {'key': 'workItemRefs', 'type': '[ResourceRef]'}
    }

    def __init__(self, _links=None, artifact_id=None, auto_complete_set_by=None, closed_by=None, closed_date=None, code_review_id=None, commits=None, completion_options=None, completion_queue_time=None, created_by=None, creation_date=None, description=None, fork_source=None, is_draft=None, labels=None, last_merge_commit=None, last_merge_source_commit=None, last_merge_target_commit=None, merge_failure_message=None, merge_failure_type=None, merge_id=None, merge_options=None, merge_status=None, pull_request_id=None, remote_url=None, repository=None, reviewers=None, source_ref_name=None, status=None, supports_iterations=None, target_ref_name=None, title=None, url=None, work_item_refs=None):
        super(GitPullRequest, self).__init__()
        self._links = _links
        self.artifact_id = artifact_id
        self.auto_complete_set_by = auto_complete_set_by
        self.closed_by = closed_by
        self.closed_date = closed_date
        self.code_review_id = code_review_id
        self.commits = commits
        self.completion_options = completion_options
        self.completion_queue_time = completion_queue_time
        self.created_by = created_by
        self.creation_date = creation_date
        self.description = description
        self.fork_source = fork_source
        self.is_draft = is_draft
        self.labels = labels
        self.last_merge_commit = last_merge_commit
        self.last_merge_source_commit = last_merge_source_commit
        self.last_merge_target_commit = last_merge_target_commit
        self.merge_failure_message = merge_failure_message
        self.merge_failure_type = merge_failure_type
        self.merge_id = merge_id
        self.merge_options = merge_options
        self.merge_status = merge_status
        self.pull_request_id = pull_request_id
        self.remote_url = remote_url
        self.repository = repository
        self.reviewers = reviewers
        self.source_ref_name = source_ref_name
        self.status = status
        self.supports_iterations = supports_iterations
        self.target_ref_name = target_ref_name
        self.title = title
        self.url = url
        self.work_item_refs = work_item_refs


class GitPullRequestChange(Model):

    _attribute_map = {
        'change_tracking_id': {'key': 'changeTrackingId', 'type': 'int'}
    }

    def __init__(self, change_tracking_id=None):
        super(GitPullRequestChange, self).__init__()
        self.change_tracking_id = change_tracking_id


class GitPullRequestCommentThread(CommentThread):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'id': {'key': 'id', 'type': 'int'},
        'identities': {'key': 'identities', 'type': '{IdentityRef}'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': 'object'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'thread_context': {'key': 'threadContext', 'type': 'CommentThreadContext'},
        'pull_request_thread_context': {'key': 'pullRequestThreadContext', 'type': 'GitPullRequestCommentThreadContext'}
    }

    def __init__(self, _links=None, comments=None, id=None, identities=None, is_deleted=None, last_updated_date=None, properties=None, published_date=None, status=None, thread_context=None, pull_request_thread_context=None):
        super(GitPullRequestCommentThread, self).__init__(_links=_links, comments=comments, id=id, identities=identities, is_deleted=is_deleted, last_updated_date=last_updated_date, properties=properties, published_date=published_date, status=status, thread_context=thread_context)
        self.pull_request_thread_context = pull_request_thread_context


class GitPullRequestCommentThreadContext(Model):

    _attribute_map = {
        'change_tracking_id': {'key': 'changeTrackingId', 'type': 'int'},
        'iteration_context': {'key': 'iterationContext', 'type': 'CommentIterationContext'},
        'tracking_criteria': {'key': 'trackingCriteria', 'type': 'CommentTrackingCriteria'}
    }

    def __init__(self, change_tracking_id=None, iteration_context=None, tracking_criteria=None):
        super(GitPullRequestCommentThreadContext, self).__init__()
        self.change_tracking_id = change_tracking_id
        self.iteration_context = iteration_context
        self.tracking_criteria = tracking_criteria


class GitPullRequestCompletionOptions(Model):

    _attribute_map = {
        'bypass_policy': {'key': 'bypassPolicy', 'type': 'bool'},
        'bypass_reason': {'key': 'bypassReason', 'type': 'str'},
        'delete_source_branch': {'key': 'deleteSourceBranch', 'type': 'bool'},
        'merge_commit_message': {'key': 'mergeCommitMessage', 'type': 'str'},
        'squash_merge': {'key': 'squashMerge', 'type': 'bool'},
        'transition_work_items': {'key': 'transitionWorkItems', 'type': 'bool'},
        'triggered_by_auto_complete': {'key': 'triggeredByAutoComplete', 'type': 'bool'}
    }

    def __init__(self, bypass_policy=None, bypass_reason=None, delete_source_branch=None, merge_commit_message=None, squash_merge=None, transition_work_items=None, triggered_by_auto_complete=None):
        super(GitPullRequestCompletionOptions, self).__init__()
        self.bypass_policy = bypass_policy
        self.bypass_reason = bypass_reason
        self.delete_source_branch = delete_source_branch
        self.merge_commit_message = merge_commit_message
        self.squash_merge = squash_merge
        self.transition_work_items = transition_work_items
        self.triggered_by_auto_complete = triggered_by_auto_complete


class GitPullRequestIteration(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'change_list': {'key': 'changeList', 'type': '[GitPullRequestChange]'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'common_ref_commit': {'key': 'commonRefCommit', 'type': 'GitCommitRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'has_more_commits': {'key': 'hasMoreCommits', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'new_target_ref_name': {'key': 'newTargetRefName', 'type': 'str'},
        'old_target_ref_name': {'key': 'oldTargetRefName', 'type': 'str'},
        'push': {'key': 'push', 'type': 'GitPushRef'},
        'reason': {'key': 'reason', 'type': 'object'},
        'source_ref_commit': {'key': 'sourceRefCommit', 'type': 'GitCommitRef'},
        'target_ref_commit': {'key': 'targetRefCommit', 'type': 'GitCommitRef'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, _links=None, author=None, change_list=None, commits=None, common_ref_commit=None, created_date=None, description=None, has_more_commits=None, id=None, new_target_ref_name=None, old_target_ref_name=None, push=None, reason=None, source_ref_commit=None, target_ref_commit=None, updated_date=None):
        super(GitPullRequestIteration, self).__init__()
        self._links = _links
        self.author = author
        self.change_list = change_list
        self.commits = commits
        self.common_ref_commit = common_ref_commit
        self.created_date = created_date
        self.description = description
        self.has_more_commits = has_more_commits
        self.id = id
        self.new_target_ref_name = new_target_ref_name
        self.old_target_ref_name = old_target_ref_name
        self.push = push
        self.reason = reason
        self.source_ref_commit = source_ref_commit
        self.target_ref_commit = target_ref_commit
        self.updated_date = updated_date


class GitPullRequestIterationChanges(Model):

    _attribute_map = {
        'change_entries': {'key': 'changeEntries', 'type': '[GitPullRequestChange]'},
        'next_skip': {'key': 'nextSkip', 'type': 'int'},
        'next_top': {'key': 'nextTop', 'type': 'int'}
    }

    def __init__(self, change_entries=None, next_skip=None, next_top=None):
        super(GitPullRequestIterationChanges, self).__init__()
        self.change_entries = change_entries
        self.next_skip = next_skip
        self.next_top = next_top


class GitPullRequestMergeOptions(Model):

    _attribute_map = {
        'detect_rename_false_positives': {'key': 'detectRenameFalsePositives', 'type': 'bool'},
        'disable_renames': {'key': 'disableRenames', 'type': 'bool'}
    }

    def __init__(self, detect_rename_false_positives=None, disable_renames=None):
        super(GitPullRequestMergeOptions, self).__init__()
        self.detect_rename_false_positives = detect_rename_false_positives
        self.disable_renames = disable_renames


class GitPullRequestQuery(Model):

    _attribute_map = {
        'queries': {'key': 'queries', 'type': '[GitPullRequestQueryInput]'},
        'results': {'key': 'results', 'type': '[{[GitPullRequest]}]'}
    }

    def __init__(self, queries=None, results=None):
        super(GitPullRequestQuery, self).__init__()
        self.queries = queries
        self.results = results


class GitPullRequestQueryInput(Model):

    _attribute_map = {
        'items': {'key': 'items', 'type': '[str]'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, items=None, type=None):
        super(GitPullRequestQueryInput, self).__init__()
        self.items = items
        self.type = type


class GitPullRequestSearchCriteria(Model):

    _attribute_map = {
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'reviewer_id': {'key': 'reviewerId', 'type': 'str'},
        'source_ref_name': {'key': 'sourceRefName', 'type': 'str'},
        'source_repository_id': {'key': 'sourceRepositoryId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'target_ref_name': {'key': 'targetRefName', 'type': 'str'}
    }

    def __init__(self, creator_id=None, include_links=None, repository_id=None, reviewer_id=None, source_ref_name=None, source_repository_id=None, status=None, target_ref_name=None):
        super(GitPullRequestSearchCriteria, self).__init__()
        self.creator_id = creator_id
        self.include_links = include_links
        self.repository_id = repository_id
        self.reviewer_id = reviewer_id
        self.source_ref_name = source_ref_name
        self.source_repository_id = source_repository_id
        self.status = status
        self.target_ref_name = target_ref_name


class GitPushRef(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'date': {'key': 'date', 'type': 'iso-8601'},
        'push_correlation_id': {'key': 'pushCorrelationId', 'type': 'str'},
        'pushed_by': {'key': 'pushedBy', 'type': 'IdentityRef'},
        'push_id': {'key': 'pushId', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, date=None, push_correlation_id=None, pushed_by=None, push_id=None, url=None):
        super(GitPushRef, self).__init__()
        self._links = _links
        self.date = date
        self.push_correlation_id = push_correlation_id
        self.pushed_by = pushed_by
        self.push_id = push_id
        self.url = url


class GitPushSearchCriteria(Model):

    _attribute_map = {
        'from_date': {'key': 'fromDate', 'type': 'iso-8601'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'include_ref_updates': {'key': 'includeRefUpdates', 'type': 'bool'},
        'pusher_id': {'key': 'pusherId', 'type': 'str'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'to_date': {'key': 'toDate', 'type': 'iso-8601'}
    }

    def __init__(self, from_date=None, include_links=None, include_ref_updates=None, pusher_id=None, ref_name=None, to_date=None):
        super(GitPushSearchCriteria, self).__init__()
        self.from_date = from_date
        self.include_links = include_links
        self.include_ref_updates = include_ref_updates
        self.pusher_id = pusher_id
        self.ref_name = ref_name
        self.to_date = to_date


class GitQueryBranchStatsCriteria(Model):

    _attribute_map = {
        'base_commit': {'key': 'baseCommit', 'type': 'GitVersionDescriptor'},
        'target_commits': {'key': 'targetCommits', 'type': '[GitVersionDescriptor]'}
    }

    def __init__(self, base_commit=None, target_commits=None):
        super(GitQueryBranchStatsCriteria, self).__init__()
        self.base_commit = base_commit
        self.target_commits = target_commits


class GitQueryCommitsCriteria(Model):

    _attribute_map = {
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'author': {'key': 'author', 'type': 'str'},
        'compare_version': {'key': 'compareVersion', 'type': 'GitVersionDescriptor'},
        'exclude_deletes': {'key': 'excludeDeletes', 'type': 'bool'},
        'from_commit_id': {'key': 'fromCommitId', 'type': 'str'},
        'from_date': {'key': 'fromDate', 'type': 'str'},
        'history_mode': {'key': 'historyMode', 'type': 'object'},
        'ids': {'key': 'ids', 'type': '[str]'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'include_push_data': {'key': 'includePushData', 'type': 'bool'},
        'include_user_image_url': {'key': 'includeUserImageUrl', 'type': 'bool'},
        'include_work_items': {'key': 'includeWorkItems', 'type': 'bool'},
        'item_path': {'key': 'itemPath', 'type': 'str'},
        'item_version': {'key': 'itemVersion', 'type': 'GitVersionDescriptor'},
        'to_commit_id': {'key': 'toCommitId', 'type': 'str'},
        'to_date': {'key': 'toDate', 'type': 'str'},
        'user': {'key': 'user', 'type': 'str'}
    }

    def __init__(self, skip=None, top=None, author=None, compare_version=None, exclude_deletes=None, from_commit_id=None, from_date=None, history_mode=None, ids=None, include_links=None, include_push_data=None, include_user_image_url=None, include_work_items=None, item_path=None, item_version=None, to_commit_id=None, to_date=None, user=None):
        super(GitQueryCommitsCriteria, self).__init__()
        self.skip = skip
        self.top = top
        self.author = author
        self.compare_version = compare_version
        self.exclude_deletes = exclude_deletes
        self.from_commit_id = from_commit_id
        self.from_date = from_date
        self.history_mode = history_mode
        self.ids = ids
        self.include_links = include_links
        self.include_push_data = include_push_data
        self.include_user_image_url = include_user_image_url
        self.include_work_items = include_work_items
        self.item_path = item_path
        self.item_version = item_version
        self.to_commit_id = to_commit_id
        self.to_date = to_date
        self.user = user


class GitRecycleBinRepositoryDetails(Model):

    _attribute_map = {
        'deleted': {'key': 'deleted', 'type': 'bool'}
    }

    def __init__(self, deleted=None):
        super(GitRecycleBinRepositoryDetails, self).__init__()
        self.deleted = deleted


class GitRef(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'creator': {'key': 'creator', 'type': 'IdentityRef'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'is_locked_by': {'key': 'isLockedBy', 'type': 'IdentityRef'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'peeled_object_id': {'key': 'peeledObjectId', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, creator=None, is_locked=None, is_locked_by=None, name=None, object_id=None, peeled_object_id=None, statuses=None, url=None):
        super(GitRef, self).__init__()
        self._links = _links
        self.creator = creator
        self.is_locked = is_locked
        self.is_locked_by = is_locked_by
        self.name = name
        self.object_id = object_id
        self.peeled_object_id = peeled_object_id
        self.statuses = statuses
        self.url = url


class GitRefFavorite(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, identity_id=None, name=None, repository_id=None, type=None, url=None):
        super(GitRefFavorite, self).__init__()
        self._links = _links
        self.id = id
        self.identity_id = identity_id
        self.name = name
        self.repository_id = repository_id
        self.type = type
        self.url = url


class GitRefUpdate(Model):

    _attribute_map = {
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'new_object_id': {'key': 'newObjectId', 'type': 'str'},
        'old_object_id': {'key': 'oldObjectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, is_locked=None, name=None, new_object_id=None, old_object_id=None, repository_id=None):
        super(GitRefUpdate, self).__init__()
        self.is_locked = is_locked
        self.name = name
        self.new_object_id = new_object_id
        self.old_object_id = old_object_id
        self.repository_id = repository_id


class GitRefUpdateResult(Model):

    _attribute_map = {
        'custom_message': {'key': 'customMessage', 'type': 'str'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'new_object_id': {'key': 'newObjectId', 'type': 'str'},
        'old_object_id': {'key': 'oldObjectId', 'type': 'str'},
        'rejected_by': {'key': 'rejectedBy', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'success': {'key': 'success', 'type': 'bool'},
        'update_status': {'key': 'updateStatus', 'type': 'object'}
    }

    def __init__(self, custom_message=None, is_locked=None, name=None, new_object_id=None, old_object_id=None, rejected_by=None, repository_id=None, success=None, update_status=None):
        super(GitRefUpdateResult, self).__init__()
        self.custom_message = custom_message
        self.is_locked = is_locked
        self.name = name
        self.new_object_id = new_object_id
        self.old_object_id = old_object_id
        self.rejected_by = rejected_by
        self.repository_id = repository_id
        self.success = success
        self.update_status = update_status


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
        'valid_remote_urls': {'key': 'validRemoteUrls', 'type': '[str]'}
    }

    def __init__(self, _links=None, default_branch=None, id=None, is_fork=None, name=None, parent_repository=None, project=None, remote_url=None, size=None, ssh_url=None, url=None, valid_remote_urls=None):
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


class GitRepositoryCreateOptions(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'parent_repository': {'key': 'parentRepository', 'type': 'GitRepositoryRef'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, name=None, parent_repository=None, project=None):
        super(GitRepositoryCreateOptions, self).__init__()
        self.name = name
        self.parent_repository = parent_repository
        self.project = project


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


class GitRepositoryStats(Model):

    _attribute_map = {
        'active_pull_requests_count': {'key': 'activePullRequestsCount', 'type': 'int'},
        'branches_count': {'key': 'branchesCount', 'type': 'int'},
        'commits_count': {'key': 'commitsCount', 'type': 'int'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, active_pull_requests_count=None, branches_count=None, commits_count=None, repository_id=None):
        super(GitRepositoryStats, self).__init__()
        self.active_pull_requests_count = active_pull_requests_count
        self.branches_count = branches_count
        self.commits_count = commits_count
        self.repository_id = repository_id


class GitRevert(GitAsyncRefOperation):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'revert_id': {'key': 'revertId', 'type': 'int'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None, revert_id=None):
        super(GitRevert, self).__init__(_links=_links, detailed_status=detailed_status, parameters=parameters, status=status, url=url)
        self.revert_id = revert_id


class GitStatus(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'context': {'key': 'context', 'type': 'GitStatusContext'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'},
        'target_url': {'key': 'targetUrl', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, _links=None, context=None, created_by=None, creation_date=None, description=None, id=None, state=None, target_url=None, updated_date=None):
        super(GitStatus, self).__init__()
        self._links = _links
        self.context = context
        self.created_by = created_by
        self.creation_date = creation_date
        self.description = description
        self.id = id
        self.state = state
        self.target_url = target_url
        self.updated_date = updated_date


class GitStatusContext(Model):

    _attribute_map = {
        'genre': {'key': 'genre', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, genre=None, name=None):
        super(GitStatusContext, self).__init__()
        self.genre = genre
        self.name = name


class GitSuggestion(Model):

    _attribute_map = {
        'properties': {'key': 'properties', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, properties=None, type=None):
        super(GitSuggestion, self).__init__()
        self.properties = properties
        self.type = type


class GitTemplate(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, name=None, type=None):
        super(GitTemplate, self).__init__()
        self.name = name
        self.type = type


class GitTreeDiff(Model):

    _attribute_map = {
        'base_tree_id': {'key': 'baseTreeId', 'type': 'str'},
        'diff_entries': {'key': 'diffEntries', 'type': '[GitTreeDiffEntry]'},
        'target_tree_id': {'key': 'targetTreeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, base_tree_id=None, diff_entries=None, target_tree_id=None, url=None):
        super(GitTreeDiff, self).__init__()
        self.base_tree_id = base_tree_id
        self.diff_entries = diff_entries
        self.target_tree_id = target_tree_id
        self.url = url


class GitTreeDiffEntry(Model):

    _attribute_map = {
        'base_object_id': {'key': 'baseObjectId', 'type': 'str'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'object_type': {'key': 'objectType', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'target_object_id': {'key': 'targetObjectId', 'type': 'str'}
    }

    def __init__(self, base_object_id=None, change_type=None, object_type=None, path=None, target_object_id=None):
        super(GitTreeDiffEntry, self).__init__()
        self.base_object_id = base_object_id
        self.change_type = change_type
        self.object_type = object_type
        self.path = path
        self.target_object_id = target_object_id


class GitTreeDiffResponse(Model):

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': '[str]'},
        'tree_diff': {'key': 'treeDiff', 'type': 'GitTreeDiff'}
    }

    def __init__(self, continuation_token=None, tree_diff=None):
        super(GitTreeDiffResponse, self).__init__()
        self.continuation_token = continuation_token
        self.tree_diff = tree_diff


class GitTreeEntryRef(Model):

    _attribute_map = {
        'git_object_type': {'key': 'gitObjectType', 'type': 'object'},
        'mode': {'key': 'mode', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, git_object_type=None, mode=None, object_id=None, relative_path=None, size=None, url=None):
        super(GitTreeEntryRef, self).__init__()
        self.git_object_type = git_object_type
        self.mode = mode
        self.object_id = object_id
        self.relative_path = relative_path
        self.size = size
        self.url = url


class GitTreeRef(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'tree_entries': {'key': 'treeEntries', 'type': '[GitTreeEntryRef]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, object_id=None, size=None, tree_entries=None, url=None):
        super(GitTreeRef, self).__init__()
        self._links = _links
        self.object_id = object_id
        self.size = size
        self.tree_entries = tree_entries
        self.url = url


class GitUserDate(Model):

    _attribute_map = {
        'date': {'key': 'date', 'type': 'iso-8601'},
        'email': {'key': 'email', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, date=None, email=None, image_url=None, name=None):
        super(GitUserDate, self).__init__()
        self.date = date
        self.email = email
        self.image_url = image_url
        self.name = name


class GitVersionDescriptor(Model):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None):
        super(GitVersionDescriptor, self).__init__()
        self.version = version
        self.version_options = version_options
        self.version_type = version_type


class GlobalGitRepositoryKey(Model):

    _attribute_map = {
        'collection_id': {'key': 'collectionId', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, collection_id=None, project_id=None, repository_id=None):
        super(GlobalGitRepositoryKey, self).__init__()
        self.collection_id = collection_id
        self.project_id = project_id
        self.repository_id = repository_id


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


class IdentityRefWithVote(IdentityRef):

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
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'is_required': {'key': 'isRequired', 'type': 'bool'},
        'reviewer_url': {'key': 'reviewerUrl', 'type': 'str'},
        'vote': {'key': 'vote', 'type': 'int'},
        'voted_for': {'key': 'votedFor', 'type': '[IdentityRefWithVote]'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None, is_required=None, reviewer_url=None, vote=None, voted_for=None):
        super(IdentityRefWithVote, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, directory_alias=directory_alias, id=id, image_url=image_url, inactive=inactive, is_aad_identity=is_aad_identity, is_container=is_container, is_deleted_in_origin=is_deleted_in_origin, profile_url=profile_url, unique_name=unique_name)
        self.is_required = is_required
        self.reviewer_url = reviewer_url
        self.vote = vote
        self.voted_for = voted_for


class ImportRepositoryValidation(Model):

    _attribute_map = {
        'git_source': {'key': 'gitSource', 'type': 'GitImportGitSource'},
        'password': {'key': 'password', 'type': 'str'},
        'tfvc_source': {'key': 'tfvcSource', 'type': 'GitImportTfvcSource'},
        'username': {'key': 'username', 'type': 'str'}
    }

    def __init__(self, git_source=None, password=None, tfvc_source=None, username=None):
        super(ImportRepositoryValidation, self).__init__()
        self.git_source = git_source
        self.password = password
        self.tfvc_source = tfvc_source
        self.username = username


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


class LineDiffBlock(Model):

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'modified_line_number_start': {'key': 'modifiedLineNumberStart', 'type': 'int'},
        'modified_lines_count': {'key': 'modifiedLinesCount', 'type': 'int'},
        'original_line_number_start': {'key': 'originalLineNumberStart', 'type': 'int'},
        'original_lines_count': {'key': 'originalLinesCount', 'type': 'int'}
    }

    def __init__(self, change_type=None, modified_line_number_start=None, modified_lines_count=None, original_line_number_start=None, original_lines_count=None):
        super(LineDiffBlock, self).__init__()
        self.change_type = change_type
        self.modified_line_number_start = modified_line_number_start
        self.modified_lines_count = modified_lines_count
        self.original_line_number_start = original_line_number_start
        self.original_lines_count = original_lines_count


class PolicyConfigurationRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, type=None, url=None):
        super(PolicyConfigurationRef, self).__init__()
        self.id = id
        self.type = type
        self.url = url


class PolicyTypeRef(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, url=None):
        super(PolicyTypeRef, self).__init__()
        self.display_name = display_name
        self.id = id
        self.url = url


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ResourceRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(ResourceRef, self).__init__()
        self.id = id
        self.url = url


class ShareNotificationContext(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'receivers': {'key': 'receivers', 'type': '[IdentityRef]'}
    }

    def __init__(self, message=None, receivers=None):
        super(ShareNotificationContext, self).__init__()
        self.message = message
        self.receivers = receivers


class SourceToTargetRef(Model):

    _attribute_map = {
        'source_ref': {'key': 'sourceRef', 'type': 'str'},
        'target_ref': {'key': 'targetRef', 'type': 'str'}
    }

    def __init__(self, source_ref=None, target_ref=None):
        super(SourceToTargetRef, self).__init__()
        self.source_ref = source_ref
        self.target_ref = target_ref


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
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.default_team_image_url = default_team_image_url
        self.description = description
        self.id = id
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility


class VersionedPolicyConfigurationRef(PolicyConfigurationRef):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, id=None, type=None, url=None, revision=None):
        super(VersionedPolicyConfigurationRef, self).__init__(id=id, type=type, url=url)
        self.revision = revision


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


class WebApiCreateTagRequestData(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(WebApiCreateTagRequestData, self).__init__()
        self.name = name


class WebApiTagDefinition(Model):

    _attribute_map = {
        'active': {'key': 'active', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, active=None, id=None, name=None, url=None):
        super(WebApiTagDefinition, self).__init__()
        self.active = active
        self.id = id
        self.name = name
        self.url = url


class GitBaseVersionDescriptor(GitVersionDescriptor):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'},
        'base_version': {'key': 'baseVersion', 'type': 'str'},
        'base_version_options': {'key': 'baseVersionOptions', 'type': 'object'},
        'base_version_type': {'key': 'baseVersionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None, base_version=None, base_version_options=None, base_version_type=None):
        super(GitBaseVersionDescriptor, self).__init__(version=version, version_options=version_options, version_type=version_type)
        self.base_version = base_version
        self.base_version_options = base_version_options
        self.base_version_type = base_version_type


class GitCommit(GitCommitRef):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'GitUserDate'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'committer': {'key': 'committer', 'type': 'GitUserDate'},
        'parents': {'key': 'parents', 'type': '[str]'},
        'push': {'key': 'push', 'type': 'GitPushRef'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'work_items': {'key': 'workItems', 'type': '[ResourceRef]'},
        'tree_id': {'key': 'treeId', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, change_counts=None, changes=None, comment=None, comment_truncated=None, commit_id=None, committer=None, parents=None, push=None, remote_url=None, statuses=None, url=None, work_items=None, tree_id=None):
        super(GitCommit, self).__init__(_links=_links, author=author, change_counts=change_counts, changes=changes, comment=comment, comment_truncated=comment_truncated, commit_id=commit_id, committer=committer, parents=parents, push=push, remote_url=remote_url, statuses=statuses, url=url, work_items=work_items)
        self.tree_id = tree_id


class GitForkRef(GitRef):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'creator': {'key': 'creator', 'type': 'IdentityRef'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'is_locked_by': {'key': 'isLockedBy', 'type': 'IdentityRef'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'peeled_object_id': {'key': 'peeledObjectId', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'}
    }

    def __init__(self, _links=None, creator=None, is_locked=None, is_locked_by=None, name=None, object_id=None, peeled_object_id=None, statuses=None, url=None, repository=None):
        super(GitForkRef, self).__init__(_links=_links, creator=creator, is_locked=is_locked, is_locked_by=is_locked_by, name=name, object_id=object_id, peeled_object_id=peeled_object_id, statuses=statuses, url=url)
        self.repository = repository


class GitItem(ItemModel):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'content': {'key': 'content', 'type': 'str'},
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'git_object_type': {'key': 'gitObjectType', 'type': 'object'},
        'latest_processed_change': {'key': 'latestProcessedChange', 'type': 'GitCommitRef'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'original_object_id': {'key': 'originalObjectId', 'type': 'str'}
    }

    def __init__(self, _links=None, content=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None, commit_id=None, git_object_type=None, latest_processed_change=None, object_id=None, original_object_id=None):
        super(GitItem, self).__init__(_links=_links, content=content, content_metadata=content_metadata, is_folder=is_folder, is_sym_link=is_sym_link, path=path, url=url)
        self.commit_id = commit_id
        self.git_object_type = git_object_type
        self.latest_processed_change = latest_processed_change
        self.object_id = object_id
        self.original_object_id = original_object_id


class GitMerge(GitMergeParameters):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'parents': {'key': 'parents', 'type': '[str]'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitMergeOperationStatusDetail'},
        'merge_operation_id': {'key': 'mergeOperationId', 'type': 'int'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, comment=None, parents=None, _links=None, detailed_status=None, merge_operation_id=None, status=None):
        super(GitMerge, self).__init__(comment=comment, parents=parents)
        self._links = _links
        self.detailed_status = detailed_status
        self.merge_operation_id = merge_operation_id
        self.status = status


class GitPullRequestStatus(GitStatus):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'context': {'key': 'context', 'type': 'GitStatusContext'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'},
        'target_url': {'key': 'targetUrl', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'}
    }

    def __init__(self, _links=None, context=None, created_by=None, creation_date=None, description=None, id=None, state=None, target_url=None, updated_date=None, iteration_id=None, properties=None):
        super(GitPullRequestStatus, self).__init__(_links=_links, context=context, created_by=created_by, creation_date=creation_date, description=description, id=id, state=state, target_url=target_url, updated_date=updated_date)
        self.iteration_id = iteration_id
        self.properties = properties


class GitPush(GitPushRef):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'date': {'key': 'date', 'type': 'iso-8601'},
        'push_correlation_id': {'key': 'pushCorrelationId', 'type': 'str'},
        'pushed_by': {'key': 'pushedBy', 'type': 'IdentityRef'},
        'push_id': {'key': 'pushId', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'ref_updates': {'key': 'refUpdates', 'type': '[GitRefUpdate]'},
        'repository': {'key': 'repository', 'type': 'GitRepository'}
    }

    def __init__(self, _links=None, date=None, push_correlation_id=None, pushed_by=None, push_id=None, url=None, commits=None, ref_updates=None, repository=None):
        super(GitPush, self).__init__(_links=_links, date=date, push_correlation_id=push_correlation_id, pushed_by=pushed_by, push_id=push_id, url=url)
        self.commits = commits
        self.ref_updates = ref_updates
        self.repository = repository


class GitTargetVersionDescriptor(GitVersionDescriptor):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'},
        'target_version': {'key': 'targetVersion', 'type': 'str'},
        'target_version_options': {'key': 'targetVersionOptions', 'type': 'object'},
        'target_version_type': {'key': 'targetVersionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None, target_version=None, target_version_options=None, target_version_type=None):
        super(GitTargetVersionDescriptor, self).__init__(version=version, version_options=version_options, version_type=version_type)
        self.target_version = target_version
        self.target_version_options = target_version_options
        self.target_version_type = target_version_type


class PolicyConfiguration(VersionedPolicyConfigurationRef):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'is_blocking': {'key': 'isBlocking', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'settings': {'key': 'settings', 'type': 'object'}
    }

    def __init__(self, id=None, type=None, url=None, revision=None, _links=None, created_by=None, created_date=None, is_blocking=None, is_deleted=None, is_enabled=None, settings=None):
        super(PolicyConfiguration, self).__init__(id=id, type=type, url=url, revision=revision)
        self._links = _links
        self.created_by = created_by
        self.created_date = created_date
        self.is_blocking = is_blocking
        self.is_deleted = is_deleted
        self.is_enabled = is_enabled
        self.settings = settings


__all__ = [
    'Attachment',
    'Change',
    'Comment',
    'CommentIterationContext',
    'CommentPosition',
    'CommentThread',
    'CommentThreadContext',
    'CommentTrackingCriteria',
    'FileContentMetadata',
    'FileDiff',
    'FileDiffParams',
    'FileDiffsCriteria',
    'GitAnnotatedTag',
    'GitAsyncRefOperation',
    'GitAsyncRefOperationDetail',
    'GitAsyncRefOperationParameters',
    'GitAsyncRefOperationSource',
    'GitBlobRef',
    'GitBranchStats',
    'GitCherryPick',
    'GitCommitChanges',
    'GitCommitDiffs',
    'GitCommitRef',
    'GitConflict',
    'GitConflictUpdateResult',
    'GitDeletedRepository',
    'GitFilePathsCollection',
    'GitForkOperationStatusDetail',
    'GitForkSyncRequest',
    'GitForkSyncRequestParameters',
    'GitImportGitSource',
    'GitImportRequest',
    'GitImportRequestParameters',
    'GitImportStatusDetail',
    'GitImportTfvcSource',
    'GitItemDescriptor',
    'GitItemRequestData',
    'GitMergeOperationStatusDetail',
    'GitMergeOriginRef',
    'GitMergeParameters',
    'GitObject',
    'GitPullRequest',
    'GitPullRequestChange',
    'GitPullRequestCommentThread',
    'GitPullRequestCommentThreadContext',
    'GitPullRequestCompletionOptions',
    'GitPullRequestIteration',
    'GitPullRequestIterationChanges',
    'GitPullRequestMergeOptions',
    'GitPullRequestQuery',
    'GitPullRequestQueryInput',
    'GitPullRequestSearchCriteria',
    'GitPushRef',
    'GitPushSearchCriteria',
    'GitQueryBranchStatsCriteria',
    'GitQueryCommitsCriteria',
    'GitRecycleBinRepositoryDetails',
    'GitRef',
    'GitRefFavorite',
    'GitRefUpdate',
    'GitRefUpdateResult',
    'GitRepository',
    'GitRepositoryCreateOptions',
    'GitRepositoryRef',
    'GitRepositoryStats',
    'GitRevert',
    'GitStatus',
    'GitStatusContext',
    'GitSuggestion',
    'GitTemplate',
    'GitTreeDiff',
    'GitTreeDiffEntry',
    'GitTreeDiffResponse',
    'GitTreeEntryRef',
    'GitTreeRef',
    'GitUserDate',
    'GitVersionDescriptor',
    'GlobalGitRepositoryKey',
    'GraphSubjectBase',
    'IdentityRef',
    'IdentityRefWithVote',
    'ImportRepositoryValidation',
    'ItemContent',
    'ItemModel',
    'JsonPatchOperation',
    'LineDiffBlock',
    'PolicyConfigurationRef',
    'PolicyTypeRef',
    'ReferenceLinks',
    'ResourceRef',
    'ShareNotificationContext',
    'SourceToTargetRef',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'VersionedPolicyConfigurationRef',
    'VstsInfo',
    'WebApiCreateTagRequestData',
    'WebApiTagDefinition',
    'GitBaseVersionDescriptor',
    'GitCommit',
    'GitForkRef',
    'GitItem',
    'GitMerge',
    'GitPullRequestStatus',
    'GitPush',
    'GitTargetVersionDescriptor',
    'PolicyConfiguration',
]
