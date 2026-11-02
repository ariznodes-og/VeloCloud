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


class IdentityBase(Model):

    _attribute_map = {
        'custom_display_name': {'key': 'customDisplayName', 'type': 'str'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'master_id': {'key': 'masterId', 'type': 'str'},
        'member_ids': {'key': 'memberIds', 'type': '[str]'},
        'member_of': {'key': 'memberOf', 'type': '[str]'},
        'members': {'key': 'members', 'type': '[str]'},
        'meta_type_id': {'key': 'metaTypeId', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'},
        'provider_display_name': {'key': 'providerDisplayName', 'type': 'str'},
        'resource_version': {'key': 'resourceVersion', 'type': 'int'},
        'social_descriptor': {'key': 'socialDescriptor', 'type': 'str'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'unique_user_id': {'key': 'uniqueUserId', 'type': 'int'}
    }

    def __init__(self, custom_display_name=None, descriptor=None, id=None, is_active=None, is_container=None, master_id=None, member_ids=None, member_of=None, members=None, meta_type_id=None, properties=None, provider_display_name=None, resource_version=None, social_descriptor=None, subject_descriptor=None, unique_user_id=None):
        super(IdentityBase, self).__init__()
        self.custom_display_name = custom_display_name
        self.descriptor = descriptor
        self.id = id
        self.is_active = is_active
        self.is_container = is_container
        self.master_id = master_id
        self.member_ids = member_ids
        self.member_of = member_of
        self.members = members
        self.meta_type_id = meta_type_id
        self.properties = properties
        self.provider_display_name = provider_display_name
        self.resource_version = resource_version
        self.social_descriptor = social_descriptor
        self.subject_descriptor = subject_descriptor
        self.unique_user_id = unique_user_id


class IdentityData(Model):

    _attribute_map = {
        'identity_ids': {'key': 'identityIds', 'type': '[str]'}
    }

    def __init__(self, identity_ids=None):
        super(IdentityData, self).__init__()
        self.identity_ids = identity_ids


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


class OperationReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None):
        super(OperationReference, self).__init__()
        self.id = id
        self.plugin_id = plugin_id
        self.status = status
        self.url = url


class ProcessReference(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, url=None):
        super(ProcessReference, self).__init__()
        self.name = name
        self.url = url


class ProjectAvatar(Model):

    _attribute_map = {
        'image': {'key': 'image', 'type': 'str'}
    }

    def __init__(self, image=None):
        super(ProjectAvatar, self).__init__()
        self.image = image


class ProjectInfo(Model):

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[ProjectProperty]'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'version': {'key': 'version', 'type': 'long'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, description=None, id=None, last_update_time=None, name=None, properties=None, revision=None, state=None, uri=None, version=None, visibility=None):
        super(ProjectInfo, self).__init__()
        self.abbreviation = abbreviation
        self.description = description
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.properties = properties
        self.revision = revision
        self.state = state
        self.uri = uri
        self.version = version
        self.visibility = visibility


class ProjectProperties(Model):

    _attribute_map = {
        'project_id': {'key': 'projectId', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[ProjectProperty]'}
    }

    def __init__(self, project_id=None, properties=None):
        super(ProjectProperties, self).__init__()
        self.project_id = project_id
        self.properties = properties


class ProjectProperty(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, name=None, value=None):
        super(ProjectProperty, self).__init__()
        self.name = name
        self.value = value


class Proxy(Model):

    _attribute_map = {
        'authorization': {'key': 'authorization', 'type': 'ProxyAuthorization'},
        'description': {'key': 'description', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'global_default': {'key': 'globalDefault', 'type': 'bool'},
        'site': {'key': 'site', 'type': 'str'},
        'site_default': {'key': 'siteDefault', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, authorization=None, description=None, friendly_name=None, global_default=None, site=None, site_default=None, url=None):
        super(Proxy, self).__init__()
        self.authorization = authorization
        self.description = description
        self.friendly_name = friendly_name
        self.global_default = global_default
        self.site = site
        self.site_default = site_default
        self.url = url


class ProxyAuthorization(Model):

    _attribute_map = {
        'authorization_url': {'key': 'authorizationUrl', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'str'},
        'public_key': {'key': 'publicKey', 'type': 'PublicKey'}
    }

    def __init__(self, authorization_url=None, client_id=None, identity=None, public_key=None):
        super(ProxyAuthorization, self).__init__()
        self.authorization_url = authorization_url
        self.client_id = client_id
        self.identity = identity
        self.public_key = public_key


class PublicKey(Model):

    _attribute_map = {
        'exponent': {'key': 'exponent', 'type': 'str'},
        'modulus': {'key': 'modulus', 'type': 'str'}
    }

    def __init__(self, exponent=None, modulus=None):
        super(PublicKey, self).__init__()
        self.exponent = exponent
        self.modulus = modulus


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class TeamMember(Model):

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'IdentityRef'},
        'is_team_admin': {'key': 'isTeamAdmin', 'type': 'bool'}
    }

    def __init__(self, identity=None, is_team_admin=None):
        super(TeamMember, self).__init__()
        self.identity = identity
        self.is_team_admin = is_team_admin


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


class WebApiConnectedServiceRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WebApiConnectedServiceRef, self).__init__()
        self.id = id
        self.url = url


class WebApiTeamRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(WebApiTeamRef, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class Identity(IdentityBase):

    _attribute_map = {
        'custom_display_name': {'key': 'customDisplayName', 'type': 'str'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'master_id': {'key': 'masterId', 'type': 'str'},
        'member_ids': {'key': 'memberIds', 'type': '[str]'},
        'member_of': {'key': 'memberOf', 'type': '[str]'},
        'members': {'key': 'members', 'type': '[str]'},
        'meta_type_id': {'key': 'metaTypeId', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'},
        'provider_display_name': {'key': 'providerDisplayName', 'type': 'str'},
        'resource_version': {'key': 'resourceVersion', 'type': 'int'},
        'social_descriptor': {'key': 'socialDescriptor', 'type': 'str'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'unique_user_id': {'key': 'uniqueUserId', 'type': 'int'},
    }

    def __init__(self, custom_display_name=None, descriptor=None, id=None, is_active=None, is_container=None, master_id=None, member_ids=None, member_of=None, members=None, meta_type_id=None, properties=None, provider_display_name=None, resource_version=None, social_descriptor=None, subject_descriptor=None, unique_user_id=None):
        super(Identity, self).__init__(custom_display_name=custom_display_name, descriptor=descriptor, id=id, is_active=is_active, is_container=is_container, master_id=master_id, member_ids=member_ids, member_of=member_of, members=members, meta_type_id=meta_type_id, properties=properties, provider_display_name=provider_display_name, resource_version=resource_version, social_descriptor=social_descriptor, subject_descriptor=subject_descriptor, unique_user_id=unique_user_id)


class Process(ProcessReference):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, name=None, url=None, _links=None, description=None, id=None, is_default=None, type=None):
        super(Process, self).__init__(name=name, url=url)
        self._links = _links
        self.description = description
        self.id = id
        self.is_default = is_default
        self.type = type


class TeamProject(TeamProjectReference):

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
        'visibility': {'key': 'visibility', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'capabilities': {'key': 'capabilities', 'type': '{{str}}'},
        'default_team': {'key': 'defaultTeam', 'type': 'WebApiTeamRef'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None, _links=None, capabilities=None, default_team=None):
        super(TeamProject, self).__init__(abbreviation=abbreviation, default_team_image_url=default_team_image_url, description=description, id=id, last_update_time=last_update_time, name=name, revision=revision, state=state, url=url, visibility=visibility)
        self._links = _links
        self.capabilities = capabilities
        self.default_team = default_team


class TeamProjectCollection(TeamProjectCollectionReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'process_customization_type': {'key': 'processCustomizationType', 'type': 'object'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None, _links=None, description=None, process_customization_type=None, state=None):
        super(TeamProjectCollection, self).__init__(id=id, name=name, url=url)
        self._links = _links
        self.description = description
        self.process_customization_type = process_customization_type
        self.state = state


class WebApiConnectedService(WebApiConnectedServiceRef):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'authenticated_by': {'key': 'authenticatedBy', 'type': 'IdentityRef'},
        'description': {'key': 'description', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'}
    }

    def __init__(self, url=None, authenticated_by=None, description=None, friendly_name=None, id=None, kind=None, project=None, service_uri=None):
        super(WebApiConnectedService, self).__init__(url=url)
        self.authenticated_by = authenticated_by
        self.description = description
        self.friendly_name = friendly_name
        self.id = id
        self.kind = kind
        self.project = project
        self.service_uri = service_uri


class WebApiConnectedServiceDetails(WebApiConnectedServiceRef):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'connected_service_meta_data': {'key': 'connectedServiceMetaData', 'type': 'WebApiConnectedService'},
        'credentials_xml': {'key': 'credentialsXml', 'type': 'str'},
        'end_point': {'key': 'endPoint', 'type': 'str'}
    }

    def __init__(self, id=None, url=None, connected_service_meta_data=None, credentials_xml=None, end_point=None):
        super(WebApiConnectedServiceDetails, self).__init__(id=id, url=url)
        self.connected_service_meta_data = connected_service_meta_data
        self.credentials_xml = credentials_xml
        self.end_point = end_point


class WebApiTeam(WebApiTeamRef):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'identity_url': {'key': 'identityUrl', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'project_name': {'key': 'projectName', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None, description=None, identity=None, identity_url=None, project_id=None, project_name=None):
        super(WebApiTeam, self).__init__(id=id, name=name, url=url)
        self.description = description
        self.identity = identity
        self.identity_url = identity_url
        self.project_id = project_id
        self.project_name = project_name


__all__ = [
    'GraphSubjectBase',
    'IdentityBase',
    'IdentityData',
    'IdentityRef',
    'JsonPatchOperation',
    'OperationReference',
    'ProcessReference',
    'ProjectAvatar',
    'ProjectInfo',
    'ProjectProperties',
    'ProjectProperty',
    'Proxy',
    'ProxyAuthorization',
    'PublicKey',
    'ReferenceLinks',
    'TeamMember',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'WebApiConnectedServiceRef',
    'WebApiTeamRef',
    'Identity',
    'Process',
    'TeamProject',
    'TeamProjectCollection',
    'WebApiConnectedService',
    'WebApiConnectedServiceDetails',
    'WebApiTeam',
]
