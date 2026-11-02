# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


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


class WikiPage(WikiPageCreateOrUpdateParameters):

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'git_item_path': {'key': 'gitItemPath', 'type': 'str'},
        'is_non_conformant': {'key': 'isNonConformant', 'type': 'bool'},
        'is_parent_page': {'key': 'isParentPage', 'type': 'bool'},
        'order': {'key': 'order', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'sub_pages': {'key': 'subPages', 'type': '[WikiPage]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, content=None, git_item_path=None, is_non_conformant=None, is_parent_page=None, order=None, path=None, remote_url=None, sub_pages=None, url=None):
        super(WikiPage, self).__init__(content=content)
        self.git_item_path = git_item_path
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
    'GitRepository',
    'GitRepositoryRef',
    'GitVersionDescriptor',
    'WikiAttachment',
    'WikiAttachmentResponse',
    'WikiCreateBaseParameters',
    'WikiCreateParametersV2',
    'WikiPageCreateOrUpdateParameters',
    'WikiPageMoveParameters',
    'WikiPageMoveResponse',
    'WikiPageResponse',
    'WikiPageViewStats',
    'WikiUpdateParameters',
    'WikiV2',
    'WikiPage',
    'WikiPageMove',
]
