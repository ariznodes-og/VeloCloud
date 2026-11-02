# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AccessMapping(Model):

    _attribute_map = {
        'access_point': {'key': 'accessPoint', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'moniker': {'key': 'moniker', 'type': 'str'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'},
        'virtual_directory': {'key': 'virtualDirectory', 'type': 'str'}
    }

    def __init__(self, access_point=None, display_name=None, moniker=None, service_owner=None, virtual_directory=None):
        super(AccessMapping, self).__init__()
        self.access_point = access_point
        self.display_name = display_name
        self.moniker = moniker
        self.service_owner = service_owner
        self.virtual_directory = virtual_directory


class ConnectionData(Model):

    _attribute_map = {
        'authenticated_user': {'key': 'authenticatedUser', 'type': 'Identity'},
        'authorized_user': {'key': 'authorizedUser', 'type': 'Identity'},
        'deployment_id': {'key': 'deploymentId', 'type': 'str'},
        'deployment_type': {'key': 'deploymentType', 'type': 'object'},
        'instance_id': {'key': 'instanceId', 'type': 'str'},
        'last_user_access': {'key': 'lastUserAccess', 'type': 'iso-8601'},
        'location_service_data': {'key': 'locationServiceData', 'type': 'LocationServiceData'},
        'web_application_relative_directory': {'key': 'webApplicationRelativeDirectory', 'type': 'str'}
    }

    def __init__(self, authenticated_user=None, authorized_user=None, deployment_id=None, deployment_type=None, instance_id=None, last_user_access=None, location_service_data=None, web_application_relative_directory=None):
        super(ConnectionData, self).__init__()
        self.authenticated_user = authenticated_user
        self.authorized_user = authorized_user
        self.deployment_id = deployment_id
        self.deployment_type = deployment_type
        self.instance_id = instance_id
        self.last_user_access = last_user_access
        self.location_service_data = location_service_data
        self.web_application_relative_directory = web_application_relative_directory


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


class LocationMapping(Model):

    _attribute_map = {
        'access_mapping_moniker': {'key': 'accessMappingMoniker', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'}
    }

    def __init__(self, access_mapping_moniker=None, location=None):
        super(LocationMapping, self).__init__()
        self.access_mapping_moniker = access_mapping_moniker
        self.location = location


class LocationServiceData(Model):

    _attribute_map = {
        'access_mappings': {'key': 'accessMappings', 'type': '[AccessMapping]'},
        'client_cache_fresh': {'key': 'clientCacheFresh', 'type': 'bool'},
        'client_cache_time_to_live': {'key': 'clientCacheTimeToLive', 'type': 'int'},
        'default_access_mapping_moniker': {'key': 'defaultAccessMappingMoniker', 'type': 'str'},
        'last_change_id': {'key': 'lastChangeId', 'type': 'int'},
        'last_change_id64': {'key': 'lastChangeId64', 'type': 'long'},
        'service_definitions': {'key': 'serviceDefinitions', 'type': '[ServiceDefinition]'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'}
    }

    def __init__(self, access_mappings=None, client_cache_fresh=None, client_cache_time_to_live=None, default_access_mapping_moniker=None, last_change_id=None, last_change_id64=None, service_definitions=None, service_owner=None):
        super(LocationServiceData, self).__init__()
        self.access_mappings = access_mappings
        self.client_cache_fresh = client_cache_fresh
        self.client_cache_time_to_live = client_cache_time_to_live
        self.default_access_mapping_moniker = default_access_mapping_moniker
        self.last_change_id = last_change_id
        self.last_change_id64 = last_change_id64
        self.service_definitions = service_definitions
        self.service_owner = service_owner


class ResourceAreaInfo(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location_url': {'key': 'locationUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, location_url=None, name=None):
        super(ResourceAreaInfo, self).__init__()
        self.id = id
        self.location_url = location_url
        self.name = name


class ServiceDefinition(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'inherit_level': {'key': 'inheritLevel', 'type': 'object'},
        'location_mappings': {'key': 'locationMappings', 'type': '[LocationMapping]'},
        'max_version': {'key': 'maxVersion', 'type': 'str'},
        'min_version': {'key': 'minVersion', 'type': 'str'},
        'parent_identifier': {'key': 'parentIdentifier', 'type': 'str'},
        'parent_service_type': {'key': 'parentServiceType', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'relative_to_setting': {'key': 'relativeToSetting', 'type': 'object'},
        'released_version': {'key': 'releasedVersion', 'type': 'str'},
        'resource_version': {'key': 'resourceVersion', 'type': 'int'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'},
        'service_type': {'key': 'serviceType', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'tool_id': {'key': 'toolId', 'type': 'str'}
    }

    def __init__(self, description=None, display_name=None, identifier=None, inherit_level=None, location_mappings=None, max_version=None, min_version=None, parent_identifier=None, parent_service_type=None, properties=None, relative_path=None, relative_to_setting=None, released_version=None, resource_version=None, service_owner=None, service_type=None, status=None, tool_id=None):
        super(ServiceDefinition, self).__init__()
        self.description = description
        self.display_name = display_name
        self.identifier = identifier
        self.inherit_level = inherit_level
        self.location_mappings = location_mappings
        self.max_version = max_version
        self.min_version = min_version
        self.parent_identifier = parent_identifier
        self.parent_service_type = parent_service_type
        self.properties = properties
        self.relative_path = relative_path
        self.relative_to_setting = relative_to_setting
        self.released_version = released_version
        self.resource_version = resource_version
        self.service_owner = service_owner
        self.service_type = service_type
        self.status = status
        self.tool_id = tool_id


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


__all__ = [
    'AccessMapping',
    'ConnectionData',
    'IdentityBase',
    'LocationMapping',
    'LocationServiceData',
    'ResourceAreaInfo',
    'ServiceDefinition',
    'Identity',
]
