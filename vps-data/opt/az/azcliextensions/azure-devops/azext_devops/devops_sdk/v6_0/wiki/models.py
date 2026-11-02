# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CommentCreateParameters(Model):

    _attribute_map = {
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, parent_id=None, text=None):
        super(CommentCreateParameters, self).__init__()
        self.parent_id = parent_id
        self.text = text


class CommentResourceReference(Model):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, url=None):
        super(CommentResourceReference, self).__init__()
        self.url = url


class CommentUpdateParameters(Model):

    _attribute_map = {
        'state': {'key': 'state', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, state=None, text=None):
        super(CommentUpdateParameters, self).__init__()
        self.state = state
        self.text = text


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


class WikiAttachment(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, name=None, path=None):
        super(WikiAttachment, self).__init__()
        self.name = name
        self.path = path


class WikiAttachmentResponse(Model):

    _attribute_map = {
        'attachment': {'key': 'attachment', 'type': 'WikiAttachment'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, attachment=None, eTag=None):
        super(WikiAttachmentResponse, self).__init__()
        self.attachment = attachment
        self.eTag = eTag


class WikiCreateBaseParameters(Model):

    _attribute_map = {
        'mapped_path': {'key': 'mappedPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, mapped_path=None, name=None, project_id=None, repository_id=None, type=None):
        super(WikiCreateBaseParameters, self).__init__()
        self.mapped_path = mapped_path
        self.name = name
        self.project_id = project_id
        self.repository_id = repository_id
        self.type = type


class WikiCreateParametersV2(WikiCreateBaseParameters):

    _attribute_map = {
        'mapped_path': {'key': 'mappedPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'version': {'key': 'version', 'type': 'GitVersionDescriptor'}
    }

    def __init__(self, mapped_path=None, name=None, project_id=None, repository_id=None, type=None, version=None):
        super(WikiCreateParametersV2, self).__init__(mapped_path=mapped_path, name=name, project_id=project_id, repository_id=repository_id, type=type)
        self.version = version


class WikiPageCreateOrUpdateParameters(Model):

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'}
    }

    def __init__(self, content=None):
        super(WikiPageCreateOrUpdateParameters, self).__init__()
        self.content = content


class WikiPageDetail(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'view_stats': {'key': 'viewStats', 'type': '[WikiPageStat]'}
    }

    def __init__(self, id=None, path=None, view_stats=None):
        super(WikiPageDetail, self).__init__()
        self.id = id
        self.path = path
        self.view_stats = view_stats


class WikiPageMoveParameters(Model):

    _attribute_map = {
        'new_order': {'key': 'newOrder', 'type': 'int'},
        'new_path': {'key': 'newPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, new_order=None, new_path=None, path=None):
        super(WikiPageMoveParameters, self).__init__()
        self.new_order = new_order
        self.new_path = new_path
        self.path = path


class WikiPageMoveResponse(Model):

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'page_move': {'key': 'pageMove', 'type': 'WikiPageMove'}
    }

    def __init__(self, eTag=None, page_move=None):
        super(WikiPageMoveResponse, self).__init__()
        self.eTag = eTag
        self.page_move = page_move


class WikiPageResponse(Model):

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'page': {'key': 'page', 'type': 'WikiPage'}
    }

    def __init__(self, eTag=None, page=None):
        super(WikiPageResponse, self).__init__()
        self.eTag = eTag
        self.page = page


class WikiPagesBatchRequest(Model):

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'page_views_for_days': {'key': 'pageViewsForDays', 'type': 'int'},
        'top': {'key': 'top', 'type': 'int'}
    }

    def __init__(self, continuation_token=None, page_views_for_days=None, top=None):
        super(WikiPagesBatchRequest, self).__init__()
        self.continuation_token = continuation_token
        self.page_views_for_days = page_views_for_days
        self.top = top


class WikiPageStat(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'day': {'key': 'day', 'type': 'iso-8601'}
    }

    def __init__(self, count=None, day=None):
        super(WikiPageStat, self).__init__()
        self.count = count
        self.day = day


class WikiPageViewStats(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'last_viewed_time': {'key': 'lastViewedTime', 'type': 'iso-8601'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, count=None, last_viewed_time=None, path=None):
        super(WikiPageViewStats, self).__init__()
        self.count = count
        self.last_viewed_time = last_viewed_time
        self.path = path


class WikiUpdateParameters(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[GitVersionDescriptor]'}
    }

    def __init__(self, name=None, versions=None):
        super(WikiUpdateParameters, self).__init__()
        self.name = name
        self.versions = versions


class WikiV2(WikiCreateBaseParameters):

    _attribute_map = {
        'mapped_path': {'key': 'mappedPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[GitVersionDescriptor]'}
    }

    def __init__(self, mapped_path=None, name=None, project_id=None, repository_id=None, type=None, id=None, properties=None, remote_url=None, url=None, versions=None):
        super(WikiV2, self).__init__(mapped_path=mapped_path, name=name, project_id=project_id, repository_id=repository_id, type=type)
        self.id = id
        self.properties = properties
        self.remote_url = remote_url
        self.url = url
        self.versions = versions


class Comment(CommentResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'mentions': {'key': 'mentions', 'type': '[CommentMention]'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'reactions': {'key': 'reactions', 'type': '[CommentReaction]'},
        'rendered_text': {'key': 'renderedText', 'type': 'str'},
        'replies': {'key': 'replies', 'type': 'CommentList'},
        'state': {'key': 'state', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, url=None, artifact_id=None, created_by=None, created_date=None, id=None, is_deleted=None, mentions=None, modified_by=None, modified_date=None, parent_id=None, reactions=None, rendered_text=None, replies=None, state=None, text=None, version=None):
        super(Comment, self).__init__(url=url)
        self.artifact_id = artifact_id
        self.created_by = created_by
        self.created_date = created_date
        self.id = id
        self.is_deleted = is_deleted
        self.mentions = mentions
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.parent_id = parent_id
        self.reactions = reactions
        self.rendered_text = rendered_text
        self.replies = replies
        self.state = state
        self.text = text
        self.version = version


class CommentAttachment(CommentResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, url=None, created_by=None, created_date=None, id=None):
        super(CommentAttachment, self).__init__(url=url)
        self.created_by = created_by
        self.created_date = created_date
        self.id = id


class CommentList(CommentResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'next_page': {'key': 'nextPage', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, url=None, comments=None, continuation_token=None, count=None, next_page=None, total_count=None):
        super(CommentList, self).__init__(url=url)
        self.comments = comments
        self.continuation_token = continuation_token
        self.count = count
        self.next_page = next_page
        self.total_count = total_count


class CommentMention(CommentResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'mentioned_artifact': {'key': 'mentionedArtifact', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, url=None, artifact_id=None, comment_id=None, mentioned_artifact=None, type=None):
        super(CommentMention, self).__init__(url=url)
        self.artifact_id = artifact_id
        self.comment_id = comment_id
        self.mentioned_artifact = mentioned_artifact
        self.type = type


class CommentReaction(CommentResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'is_current_user_engaged': {'key': 'isCurrentUserEngaged', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, url=None, comment_id=None, count=None, is_current_user_engaged=None, type=None):
        super(CommentReaction, self).__init__(url=url)
        self.comment_id = comment_id
        self.count = count
        self.is_current_user_engaged = is_current_user_engaged
        self.type = type


class WikiPage(WikiPageCreateOrUpdateParameters):

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'git_item_path': {'key': 'gitItemPath', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_non_conformant': {'key': 'isNonConformant', 'type': 'bool'},
        'is_parent_page': {'key': 'isParentPage', 'type': 'bool'},
        'order': {'key': 'order', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'sub_pages': {'key': 'subPages', 'type': '[WikiPage]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, content=None, git_item_path=None, id=None, is_non_conformant=None, is_parent_page=None, order=None, path=None, remote_url=None, sub_pages=None, url=None):
        super(WikiPage, self).__init__(content=content)
        self.git_item_path = git_item_path
        self.id = id
        self.is_non_conformant = is_non_conformant
        self.is_parent_page = is_parent_page
        self.order = order
        self.path = path
        self.remote_url = remote_url
        self.sub_pages = sub_pages
        self.url = url


class WikiPageMove(WikiPageMoveParameters):

    _attribute_map = {
        'new_order': {'key': 'newOrder', 'type': 'int'},
        'new_path': {'key': 'newPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'page': {'key': 'page', 'type': 'WikiPage'}
    }

    def __init__(self, new_order=None, new_path=None, path=None, page=None):
        super(WikiPageMove, self).__init__(new_order=new_order, new_path=new_path, path=path)
        self.page = page


__all__ = [
    'CommentCreateParameters',
    'CommentResourceReference',
    'CommentUpdateParameters',
    'GitRepository',
    'GitRepositoryRef',
    'GitVersionDescriptor',
    'GraphSubjectBase',
    'IdentityRef',
    'ReferenceLinks',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'WikiAttachment',
    'WikiAttachmentResponse',
    'WikiCreateBaseParameters',
    'WikiCreateParametersV2',
    'WikiPageCreateOrUpdateParameters',
    'WikiPageDetail',
    'WikiPageMoveParameters',
    'WikiPageMoveResponse',
    'WikiPageResponse',
    'WikiPagesBatchRequest',
    'WikiPageStat',
    'WikiPageViewStats',
    'WikiUpdateParameters',
    'WikiV2',
    'Comment',
    'CommentAttachment',
    'CommentList',
    'CommentMention',
    'CommentReaction',
    'WikiPage',
    'WikiPageMove',
]
