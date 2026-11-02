# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GraphCachePolicies(Model):

    _attribute_map = {
        'cache_size': {'key': 'cacheSize', 'type': 'int'}
    }

    def __init__(self, cache_size=None):
        super(GraphCachePolicies, self).__init__()
        self.cache_size = cache_size


class GraphDescriptorResult(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, _links=None, value=None):
        super(GraphDescriptorResult, self).__init__()
        self._links = _links
        self.value = value


class GraphFederatedProviderData(Model):

    _attribute_map = {
        'access_token': {'key': 'accessToken', 'type': 'str'},
        'can_query_access_token': {'key': 'canQueryAccessToken', 'type': 'bool'},
        'provider_name': {'key': 'providerName', 'type': 'str'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'version': {'key': 'version', 'type': 'long'}
    }

    def __init__(self, access_token=None, can_query_access_token=None, provider_name=None, subject_descriptor=None, version=None):
        super(GraphFederatedProviderData, self).__init__()
        self.access_token = access_token
        self.can_query_access_token = can_query_access_token
        self.provider_name = provider_name
        self.subject_descriptor = subject_descriptor
        self.version = version


class GraphGlobalExtendedPropertyBatch(Model):

    _attribute_map = {
        'property_name_filters': {'key': 'propertyNameFilters', 'type': '[str]'},
        'subject_descriptors': {'key': 'subjectDescriptors', 'type': '[str]'}
    }

    def __init__(self, property_name_filters=None, subject_descriptors=None):
        super(GraphGlobalExtendedPropertyBatch, self).__init__()
        self.property_name_filters = property_name_filters
        self.subject_descriptors = subject_descriptors


class GraphGroupCreationContext(Model):

    _attribute_map = {
        'storage_key': {'key': 'storageKey', 'type': 'str'}
    }

    def __init__(self, storage_key=None):
        super(GraphGroupCreationContext, self).__init__()
        self.storage_key = storage_key


class GraphMembership(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'container_descriptor': {'key': 'containerDescriptor', 'type': 'str'},
        'member_descriptor': {'key': 'memberDescriptor', 'type': 'str'}
    }

    def __init__(self, _links=None, container_descriptor=None, member_descriptor=None):
        super(GraphMembership, self).__init__()
        self._links = _links
        self.container_descriptor = container_descriptor
        self.member_descriptor = member_descriptor


class GraphMembershipState(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'active': {'key': 'active', 'type': 'bool'}
    }

    def __init__(self, _links=None, active=None):
        super(GraphMembershipState, self).__init__()
        self._links = _links
        self.active = active


class GraphMembershipTraversal(Model):

    _attribute_map = {
        'incompleteness_reason': {'key': 'incompletenessReason', 'type': 'str'},
        'is_complete': {'key': 'isComplete', 'type': 'bool'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'traversed_subject_ids': {'key': 'traversedSubjectIds', 'type': '[str]'},
        'traversed_subjects': {'key': 'traversedSubjects', 'type': '[str]'}
    }

    def __init__(self, incompleteness_reason=None, is_complete=None, subject_descriptor=None, traversed_subject_ids=None, traversed_subjects=None):
        super(GraphMembershipTraversal, self).__init__()
        self.incompleteness_reason = incompleteness_reason
        self.is_complete = is_complete
        self.subject_descriptor = subject_descriptor
        self.traversed_subject_ids = traversed_subject_ids
        self.traversed_subjects = traversed_subjects


class GraphProviderInfo(Model):

    _attribute_map = {
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'}
    }

    def __init__(self, descriptor=None, domain=None, origin=None, origin_id=None):
        super(GraphProviderInfo, self).__init__()
        self.descriptor = descriptor
        self.domain = domain
        self.origin = origin
        self.origin_id = origin_id


class GraphScopeCreationContext(Model):

    _attribute_map = {
        'admin_group_description': {'key': 'adminGroupDescription', 'type': 'str'},
        'admin_group_name': {'key': 'adminGroupName', 'type': 'str'},
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'storage_key': {'key': 'storageKey', 'type': 'str'}
    }

    def __init__(self, admin_group_description=None, admin_group_name=None, creator_id=None, name=None, scope_type=None, storage_key=None):
        super(GraphScopeCreationContext, self).__init__()
        self.admin_group_description = admin_group_description
        self.admin_group_name = admin_group_name
        self.creator_id = creator_id
        self.name = name
        self.scope_type = scope_type
        self.storage_key = storage_key


class GraphStorageKeyResult(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, _links=None, value=None):
        super(GraphStorageKeyResult, self).__init__()
        self._links = _links
        self.value = value


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


class GraphSubjectLookup(Model):

    _attribute_map = {
        'lookup_keys': {'key': 'lookupKeys', 'type': '[GraphSubjectLookupKey]'}
    }

    def __init__(self, lookup_keys=None):
        super(GraphSubjectLookup, self).__init__()
        self.lookup_keys = lookup_keys


class GraphSubjectLookupKey(Model):

    _attribute_map = {
        'descriptor': {'key': 'descriptor', 'type': 'str'}
    }

    def __init__(self, descriptor=None):
        super(GraphSubjectLookupKey, self).__init__()
        self.descriptor = descriptor


class GraphUserCreationContext(Model):

    _attribute_map = {
        'storage_key': {'key': 'storageKey', 'type': 'str'}
    }

    def __init__(self, storage_key=None):
        super(GraphUserCreationContext, self).__init__()
        self.storage_key = storage_key


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


class PagedGraphGroups(Model):

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': '[str]'},
        'graph_groups': {'key': 'graphGroups', 'type': '[GraphGroup]'}
    }

    def __init__(self, continuation_token=None, graph_groups=None):
        super(PagedGraphGroups, self).__init__()
        self.continuation_token = continuation_token
        self.graph_groups = graph_groups


class PagedGraphUsers(Model):

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': '[str]'},
        'graph_users': {'key': 'graphUsers', 'type': '[GraphUser]'}
    }

    def __init__(self, continuation_token=None, graph_users=None):
        super(PagedGraphUsers, self).__init__()
        self.continuation_token = continuation_token
        self.graph_users = graph_users


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class GraphSubject(GraphSubjectBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None):
        super(GraphSubject, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.legacy_descriptor = legacy_descriptor
        self.origin = origin
        self.origin_id = origin_id
        self.subject_kind = subject_kind


class GraphMember(GraphSubject):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, domain=None, mail_address=None, principal_name=None):
        super(GraphMember, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind)
        self.domain = domain
        self.mail_address = mail_address
        self.principal_name = principal_name


class GraphScope(GraphSubject):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'administrator_descriptor': {'key': 'administratorDescriptor', 'type': 'str'},
        'is_global': {'key': 'isGlobal', 'type': 'bool'},
        'parent_descriptor': {'key': 'parentDescriptor', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'securing_host_descriptor': {'key': 'securingHostDescriptor', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, administrator_descriptor=None, is_global=None, parent_descriptor=None, scope_type=None, securing_host_descriptor=None):
        super(GraphScope, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind)
        self.administrator_descriptor = administrator_descriptor
        self.is_global = is_global
        self.parent_descriptor = parent_descriptor
        self.scope_type = scope_type
        self.securing_host_descriptor = securing_host_descriptor


class GraphUser(GraphMember):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'metadata_update_date': {'key': 'metadataUpdateDate', 'type': 'iso-8601'},
        'meta_type': {'key': 'metaType', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, domain=None, mail_address=None, principal_name=None, is_deleted_in_origin=None, metadata_update_date=None, meta_type=None):
        super(GraphUser, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.is_deleted_in_origin = is_deleted_in_origin
        self.metadata_update_date = metadata_update_date
        self.meta_type = meta_type


class GraphGroup(GraphMember):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_cross_project': {'key': 'isCrossProject', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_global_scope': {'key': 'isGlobalScope', 'type': 'bool'},
        'is_restricted_visible': {'key': 'isRestrictedVisible', 'type': 'bool'},
        'local_scope_id': {'key': 'localScopeId', 'type': 'str'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scope_name': {'key': 'scopeName', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'str'},
        'securing_host_id': {'key': 'securingHostId', 'type': 'str'},
        'special_type': {'key': 'specialType', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, domain=None, mail_address=None, principal_name=None, description=None, is_cross_project=None, is_deleted=None, is_global_scope=None, is_restricted_visible=None, local_scope_id=None, scope_id=None, scope_name=None, scope_type=None, securing_host_id=None, special_type=None):
        super(GraphGroup, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.description = description
        self.is_cross_project = is_cross_project
        self.is_deleted = is_deleted
        self.is_global_scope = is_global_scope
        self.is_restricted_visible = is_restricted_visible
        self.local_scope_id = local_scope_id
        self.scope_id = scope_id
        self.scope_name = scope_name
        self.scope_type = scope_type
        self.securing_host_id = securing_host_id
        self.special_type = special_type


__all__ = [
    'GraphCachePolicies',
    'GraphDescriptorResult',
    'GraphFederatedProviderData',
    'GraphGlobalExtendedPropertyBatch',
    'GraphGroupCreationContext',
    'GraphMembership',
    'GraphMembershipState',
    'GraphMembershipTraversal',
    'GraphProviderInfo',
    'GraphScopeCreationContext',
    'GraphStorageKeyResult',
    'GraphSubjectBase',
    'GraphSubjectLookup',
    'GraphSubjectLookupKey',
    'GraphUserCreationContext',
    'JsonPatchOperation',
    'PagedGraphGroups',
    'PagedGraphUsers',
    'ReferenceLinks',
    'GraphSubject',
    'GraphMember',
    'GraphScope',
    'GraphUser',
    'GraphGroup',
]
