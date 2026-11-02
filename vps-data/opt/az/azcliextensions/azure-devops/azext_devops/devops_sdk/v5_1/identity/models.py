# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AccessTokenResult(Model):

    _attribute_map = {
        'access_token': {'key': 'accessToken', 'type': 'JsonWebToken'},
        'access_token_error': {'key': 'accessTokenError', 'type': 'object'},
        'authorization_id': {'key': 'authorizationId', 'type': 'str'},
        'error_description': {'key': 'errorDescription', 'type': 'str'},
        'has_error': {'key': 'hasError', 'type': 'bool'},
        'refresh_token': {'key': 'refreshToken', 'type': 'RefreshTokenGrant'},
        'token_type': {'key': 'tokenType', 'type': 'str'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'}
    }

    def __init__(self, access_token=None, access_token_error=None, authorization_id=None, error_description=None, has_error=None, refresh_token=None, token_type=None, valid_to=None):
        super(AccessTokenResult, self).__init__()
        self.access_token = access_token
        self.access_token_error = access_token_error
        self.authorization_id = authorization_id
        self.error_description = error_description
        self.has_error = has_error
        self.refresh_token = refresh_token
        self.token_type = token_type
        self.valid_to = valid_to


class AuthorizationGrant(Model):

    _attribute_map = {
        'grant_type': {'key': 'grantType', 'type': 'object'}
    }

    def __init__(self, grant_type=None):
        super(AuthorizationGrant, self).__init__()
        self.grant_type = grant_type


class ChangedIdentities(Model):

    _attribute_map = {
        'identities': {'key': 'identities', 'type': '[Identity]'},
        'more_data': {'key': 'moreData', 'type': 'bool'},
        'sequence_context': {'key': 'sequenceContext', 'type': 'ChangedIdentitiesContext'}
    }

    def __init__(self, identities=None, more_data=None, sequence_context=None):
        super(ChangedIdentities, self).__init__()
        self.identities = identities
        self.more_data = more_data
        self.sequence_context = sequence_context


class ChangedIdentitiesContext(Model):

    _attribute_map = {
        'group_sequence_id': {'key': 'groupSequenceId', 'type': 'int'},
        'identity_sequence_id': {'key': 'identitySequenceId', 'type': 'int'},
        'organization_identity_sequence_id': {'key': 'organizationIdentitySequenceId', 'type': 'int'},
        'page_size': {'key': 'pageSize', 'type': 'int'}
    }

    def __init__(self, group_sequence_id=None, identity_sequence_id=None, organization_identity_sequence_id=None, page_size=None):
        super(ChangedIdentitiesContext, self).__init__()
        self.group_sequence_id = group_sequence_id
        self.identity_sequence_id = identity_sequence_id
        self.organization_identity_sequence_id = organization_identity_sequence_id
        self.page_size = page_size


class CreateScopeInfo(Model):

    _attribute_map = {
        'admin_group_description': {'key': 'adminGroupDescription', 'type': 'str'},
        'admin_group_name': {'key': 'adminGroupName', 'type': 'str'},
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'parent_scope_id': {'key': 'parentScopeId', 'type': 'str'},
        'scope_name': {'key': 'scopeName', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'}
    }

    def __init__(self, admin_group_description=None, admin_group_name=None, creator_id=None, parent_scope_id=None, scope_name=None, scope_type=None):
        super(CreateScopeInfo, self).__init__()
        self.admin_group_description = admin_group_description
        self.admin_group_name = admin_group_name
        self.creator_id = creator_id
        self.parent_scope_id = parent_scope_id
        self.scope_name = scope_name
        self.scope_type = scope_type


class FrameworkIdentityInfo(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'identity_type': {'key': 'identityType', 'type': 'object'},
        'role': {'key': 'role', 'type': 'str'}
    }

    def __init__(self, display_name=None, identifier=None, identity_type=None, role=None):
        super(FrameworkIdentityInfo, self).__init__()
        self.display_name = display_name
        self.identifier = identifier
        self.identity_type = identity_type
        self.role = role


class GroupMembership(Model):

    _attribute_map = {
        'active': {'key': 'active', 'type': 'bool'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'queried_id': {'key': 'queriedId', 'type': 'str'}
    }

    def __init__(self, active=None, descriptor=None, id=None, queried_id=None):
        super(GroupMembership, self).__init__()
        self.active = active
        self.descriptor = descriptor
        self.id = id
        self.queried_id = queried_id


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


class IdentityBatchInfo(Model):

    _attribute_map = {
        'descriptors': {'key': 'descriptors', 'type': '[str]'},
        'identity_ids': {'key': 'identityIds', 'type': '[str]'},
        'include_restricted_visibility': {'key': 'includeRestrictedVisibility', 'type': 'bool'},
        'property_names': {'key': 'propertyNames', 'type': '[str]'},
        'query_membership': {'key': 'queryMembership', 'type': 'object'},
        'social_descriptors': {'key': 'socialDescriptors', 'type': '[str]'},
        'subject_descriptors': {'key': 'subjectDescriptors', 'type': '[str]'}
    }

    def __init__(self, descriptors=None, identity_ids=None, include_restricted_visibility=None, property_names=None, query_membership=None, social_descriptors=None, subject_descriptors=None):
        super(IdentityBatchInfo, self).__init__()
        self.descriptors = descriptors
        self.identity_ids = identity_ids
        self.include_restricted_visibility = include_restricted_visibility
        self.property_names = property_names
        self.query_membership = query_membership
        self.social_descriptors = social_descriptors
        self.subject_descriptors = subject_descriptors


class IdentityScope(Model):

    _attribute_map = {
        'administrators': {'key': 'administrators', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_global': {'key': 'isGlobal', 'type': 'bool'},
        'local_scope_id': {'key': 'localScopeId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'securing_host_id': {'key': 'securingHostId', 'type': 'str'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'}
    }

    def __init__(self, administrators=None, id=None, is_active=None, is_global=None, local_scope_id=None, name=None, parent_id=None, scope_type=None, securing_host_id=None, subject_descriptor=None):
        super(IdentityScope, self).__init__()
        self.administrators = administrators
        self.id = id
        self.is_active = is_active
        self.is_global = is_global
        self.local_scope_id = local_scope_id
        self.name = name
        self.parent_id = parent_id
        self.scope_type = scope_type
        self.securing_host_id = securing_host_id
        self.subject_descriptor = subject_descriptor


class IdentitySelf(Model):

    _attribute_map = {
        'account_name': {'key': 'accountName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'tenants': {'key': 'tenants', 'type': '[TenantInfo]'}
    }

    def __init__(self, account_name=None, display_name=None, domain=None, id=None, origin=None, origin_id=None, tenants=None):
        super(IdentitySelf, self).__init__()
        self.account_name = account_name
        self.display_name = display_name
        self.domain = domain
        self.id = id
        self.origin = origin
        self.origin_id = origin_id
        self.tenants = tenants


class IdentitySnapshot(Model):

    _attribute_map = {
        'groups': {'key': 'groups', 'type': '[Identity]'},
        'identity_ids': {'key': 'identityIds', 'type': '[str]'},
        'memberships': {'key': 'memberships', 'type': '[GroupMembership]'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scopes': {'key': 'scopes', 'type': '[IdentityScope]'}
    }

    def __init__(self, groups=None, identity_ids=None, memberships=None, scope_id=None, scopes=None):
        super(IdentitySnapshot, self).__init__()
        self.groups = groups
        self.identity_ids = identity_ids
        self.memberships = memberships
        self.scope_id = scope_id
        self.scopes = scopes


class IdentityUpdateData(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'index': {'key': 'index', 'type': 'int'},
        'updated': {'key': 'updated', 'type': 'bool'}
    }

    def __init__(self, id=None, index=None, updated=None):
        super(IdentityUpdateData, self).__init__()
        self.id = id
        self.index = index
        self.updated = updated


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


class JsonWebToken(Model):

    _attribute_map = {
    }

    def __init__(self):
        super(JsonWebToken, self).__init__()


class RefreshTokenGrant(AuthorizationGrant):

    _attribute_map = {
        'grant_type': {'key': 'grantType', 'type': 'object'},
        'jwt': {'key': 'jwt', 'type': 'JsonWebToken'}
    }

    def __init__(self, grant_type=None, jwt=None):
        super(RefreshTokenGrant, self).__init__(grant_type=grant_type)
        self.jwt = jwt


class SwapIdentityInfo(Model):

    _attribute_map = {
        'id1': {'key': 'id1', 'type': 'str'},
        'id2': {'key': 'id2', 'type': 'str'}
    }

    def __init__(self, id1=None, id2=None):
        super(SwapIdentityInfo, self).__init__()
        self.id1 = id1
        self.id2 = id2


class TenantInfo(Model):

    _attribute_map = {
        'home_tenant': {'key': 'homeTenant', 'type': 'bool'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'tenant_name': {'key': 'tenantName', 'type': 'str'},
        'verified_domains': {'key': 'verifiedDomains', 'type': '[str]'}
    }

    def __init__(self, home_tenant=None, tenant_id=None, tenant_name=None, verified_domains=None):
        super(TenantInfo, self).__init__()
        self.home_tenant = home_tenant
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.verified_domains = verified_domains


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
    'AccessTokenResult',
    'AuthorizationGrant',
    'ChangedIdentities',
    'ChangedIdentitiesContext',
    'CreateScopeInfo',
    'FrameworkIdentityInfo',
    'GroupMembership',
    'IdentityBase',
    'IdentityBatchInfo',
    'IdentityScope',
    'IdentitySelf',
    'IdentitySnapshot',
    'IdentityUpdateData',
    'JsonPatchOperation',
    'JsonWebToken',
    'RefreshTokenGrant',
    'SwapIdentityInfo',
    'TenantInfo',
    'Identity',
]
