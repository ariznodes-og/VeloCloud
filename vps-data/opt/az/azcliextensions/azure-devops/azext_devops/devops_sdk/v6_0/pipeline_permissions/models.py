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


class Permission(Model):

    _attribute_map = {
        'authorized': {'key': 'authorized', 'type': 'bool'},
        'authorized_by': {'key': 'authorizedBy', 'type': 'IdentityRef'},
        'authorized_on': {'key': 'authorizedOn', 'type': 'iso-8601'}
    }

    def __init__(self, authorized=None, authorized_by=None, authorized_on=None):
        super(Permission, self).__init__()
        self.authorized = authorized
        self.authorized_by = authorized_by
        self.authorized_on = authorized_on


class PipelinePermission(Permission):

    _attribute_map = {
        'authorized': {'key': 'authorized', 'type': 'bool'},
        'authorized_by': {'key': 'authorizedBy', 'type': 'IdentityRef'},
        'authorized_on': {'key': 'authorizedOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, authorized=None, authorized_by=None, authorized_on=None, id=None):
        super(PipelinePermission, self).__init__(authorized=authorized, authorized_by=authorized_by, authorized_on=authorized_on)
        self.id = id


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class Resource(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(Resource, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class ResourcePipelinePermissions(Model):

    _attribute_map = {
        'all_pipelines': {'key': 'allPipelines', 'type': 'Permission'},
        'pipelines': {'key': 'pipelines', 'type': '[PipelinePermission]'},
        'resource': {'key': 'resource', 'type': 'Resource'}
    }

    def __init__(self, all_pipelines=None, pipelines=None, resource=None):
        super(ResourcePipelinePermissions, self).__init__()
        self.all_pipelines = all_pipelines
        self.pipelines = pipelines
        self.resource = resource


__all__ = [
    'GraphSubjectBase',
    'IdentityRef',
    'Permission',
    'PipelinePermission',
    'ReferenceLinks',
    'Resource',
    'ResourcePipelinePermissions',
]
