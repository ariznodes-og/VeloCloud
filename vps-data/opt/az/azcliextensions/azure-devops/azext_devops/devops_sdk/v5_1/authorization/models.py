# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AuthorizedDefinitions(Model):

    _attribute_map = {
        'authorized': {'key': 'authorized', 'type': 'bool'},
        'authorized_by': {'key': 'authorizedBy', 'type': 'IdentityRef'},
        'authorized_on': {'key': 'authorizedOn', 'type': 'iso-8601'},
        'definition_id': {'key': 'definitionId', 'type': 'int'}
    }

    def __init__(self, authorized=None, authorized_by=None, authorized_on=None, definition_id=None):
        super(AuthorizedDefinitions, self).__init__()
        self.authorized = authorized
        self.authorized_by = authorized_by
        self.authorized_on = authorized_on
        self.definition_id = definition_id


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


class ResourceAuthorizedDefinitions(Model):

    _attribute_map = {
        'definitions': {'key': 'definitions', 'type': '[AuthorizedDefinitions]'},
        'id': {'key': 'id', 'type': 'str'},
        'is_authorized_for_all_definitions': {'key': 'isAuthorizedForAllDefinitions', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, definitions=None, id=None, is_authorized_for_all_definitions=None, type=None):
        super(ResourceAuthorizedDefinitions, self).__init__()
        self.definitions = definitions
        self.id = id
        self.is_authorized_for_all_definitions = is_authorized_for_all_definitions
        self.type = type


__all__ = [
    'AuthorizedDefinitions',
    'GraphSubjectBase',
    'IdentityRef',
    'ReferenceLinks',
    'ResourceAuthorizedDefinitions',
]
