# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


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


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class WorkItemCommentCreateRequest(Model):

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, text=None):
        super(WorkItemCommentCreateRequest, self).__init__()
        self.text = text


class WorkItemCommentUpdateRequest(Model):

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, text=None):
        super(WorkItemCommentUpdateRequest, self).__init__()
        self.text = text


class WorkItemTrackingResourceReference(Model):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, url=None):
        super(WorkItemTrackingResourceReference, self).__init__()
        self.url = url


class WorkItemTrackingResource(WorkItemTrackingResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'}
    }

    def __init__(self, url=None, _links=None):
        super(WorkItemTrackingResource, self).__init__(url=url)
        self._links = _links


class WorkItemCommentReactionResponse(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'is_current_user_engaged': {'key': 'isCurrentUserEngaged', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, url=None, _links=None, comment_id=None, count=None, is_current_user_engaged=None, type=None):
        super(WorkItemCommentReactionResponse, self).__init__(url=url, _links=_links)
        self.comment_id = comment_id
        self.count = count
        self.is_current_user_engaged = is_current_user_engaged
        self.type = type


class WorkItemCommentResponse(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_on_behalf_date': {'key': 'createdOnBehalfDate', 'type': 'iso-8601'},
        'created_on_behalf_of': {'key': 'createdOnBehalfOf', 'type': 'IdentityRef'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'reactions': {'key': 'reactions', 'type': '[WorkItemCommentReactionResponse]'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'},
        'work_item_id': {'key': 'workItemId', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comment_id=None, created_by=None, created_date=None, created_on_behalf_date=None, created_on_behalf_of=None, is_deleted=None, modified_by=None, modified_date=None, reactions=None, text=None, version=None, work_item_id=None):
        super(WorkItemCommentResponse, self).__init__(url=url, _links=_links)
        self.comment_id = comment_id
        self.created_by = created_by
        self.created_date = created_date
        self.created_on_behalf_date = created_on_behalf_date
        self.created_on_behalf_of = created_on_behalf_of
        self.is_deleted = is_deleted
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.reactions = reactions
        self.text = text
        self.version = version
        self.work_item_id = work_item_id


class WorkItemCommentsResponse(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[WorkItemCommentResponse]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'next_page': {'key': 'nextPage', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comments=None, continuation_token=None, count=None, next_page=None, total_count=None):
        super(WorkItemCommentsResponse, self).__init__(url=url, _links=_links)
        self.comments = comments
        self.continuation_token = continuation_token
        self.count = count
        self.next_page = next_page
        self.total_count = total_count


class WorkItemCommentVersionResponse(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_on_behalf_date': {'key': 'createdOnBehalfDate', 'type': 'iso-8601'},
        'created_on_behalf_of': {'key': 'createdOnBehalfOf', 'type': 'IdentityRef'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'rendered_text': {'key': 'renderedText', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comment_id=None, created_by=None, created_date=None, created_on_behalf_date=None, created_on_behalf_of=None, is_deleted=None, modified_by=None, modified_date=None, rendered_text=None, text=None, version=None):
        super(WorkItemCommentVersionResponse, self).__init__(url=url, _links=_links)
        self.comment_id = comment_id
        self.created_by = created_by
        self.created_date = created_date
        self.created_on_behalf_date = created_on_behalf_date
        self.created_on_behalf_of = created_on_behalf_of
        self.is_deleted = is_deleted
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.rendered_text = rendered_text
        self.text = text
        self.version = version


class WorkItemCommentsReportingResponse(WorkItemCommentsResponse):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[WorkItemCommentResponse]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'next_page': {'key': 'nextPage', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'},
        'is_last_batch': {'key': 'isLastBatch', 'type': 'bool'}
    }

    def __init__(self, url=None, _links=None, comments=None, continuation_token=None, count=None, next_page=None, total_count=None, is_last_batch=None):
        super(WorkItemCommentsReportingResponse, self).__init__(url=url, _links=_links, comments=comments, continuation_token=continuation_token, count=count, next_page=next_page, total_count=total_count)
        self.is_last_batch = is_last_batch


__all__ = [
    'GraphSubjectBase',
    'IdentityRef',
    'ReferenceLinks',
    'WorkItemCommentCreateRequest',
    'WorkItemCommentUpdateRequest',
    'WorkItemTrackingResourceReference',
    'WorkItemTrackingResource',
    'WorkItemCommentReactionResponse',
    'WorkItemCommentResponse',
    'WorkItemCommentsResponse',
    'WorkItemCommentVersionResponse',
    'WorkItemCommentsReportingResponse',
]
