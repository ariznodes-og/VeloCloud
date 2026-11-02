# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AccountEntitlement(Model):

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'str'},
        'assignment_date': {'key': 'assignmentDate', 'type': 'iso-8601'},
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'last_accessed_date': {'key': 'lastAccessedDate', 'type': 'iso-8601'},
        'license': {'key': 'license', 'type': 'License'},
        'origin': {'key': 'origin', 'type': 'object'},
        'rights': {'key': 'rights', 'type': 'AccountRights'},
        'status': {'key': 'status', 'type': 'object'},
        'user': {'key': 'user', 'type': 'IdentityRef'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, account_id=None, assignment_date=None, assignment_source=None, date_created=None, last_accessed_date=None, license=None, origin=None, rights=None, status=None, user=None, user_id=None):
        super(AccountEntitlement, self).__init__()
        self.account_id = account_id
        self.assignment_date = assignment_date
        self.assignment_source = assignment_source
        self.date_created = date_created
        self.last_accessed_date = last_accessed_date
        self.license = license
        self.origin = origin
        self.rights = rights
        self.status = status
        self.user = user
        self.user_id = user_id


class AccountEntitlementUpdateModel(Model):

    _attribute_map = {
        'license': {'key': 'license', 'type': 'License'}
    }

    def __init__(self, license=None):
        super(AccountEntitlementUpdateModel, self).__init__()
        self.license = license


class AccountLicenseExtensionUsage(Model):

    _attribute_map = {
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'int'},
        'is_trial': {'key': 'isTrial', 'type': 'bool'},
        'minimum_license_required': {'key': 'minimumLicenseRequired', 'type': 'object'},
        'msdn_used_count': {'key': 'msdnUsedCount', 'type': 'int'},
        'provisioned_count': {'key': 'provisionedCount', 'type': 'int'},
        'remaining_trial_days': {'key': 'remainingTrialDays', 'type': 'int'},
        'trial_expiry_date': {'key': 'trialExpiryDate', 'type': 'iso-8601'},
        'used_count': {'key': 'usedCount', 'type': 'int'}
    }

    def __init__(self, extension_id=None, extension_name=None, included_quantity=None, is_trial=None, minimum_license_required=None, msdn_used_count=None, provisioned_count=None, remaining_trial_days=None, trial_expiry_date=None, used_count=None):
        super(AccountLicenseExtensionUsage, self).__init__()
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.included_quantity = included_quantity
        self.is_trial = is_trial
        self.minimum_license_required = minimum_license_required
        self.msdn_used_count = msdn_used_count
        self.provisioned_count = provisioned_count
        self.remaining_trial_days = remaining_trial_days
        self.trial_expiry_date = trial_expiry_date
        self.used_count = used_count


class AccountLicenseUsage(Model):

    _attribute_map = {
        'disabled_count': {'key': 'disabledCount', 'type': 'int'},
        'license': {'key': 'license', 'type': 'AccountUserLicense'},
        'pending_provisioned_count': {'key': 'pendingProvisionedCount', 'type': 'int'},
        'provisioned_count': {'key': 'provisionedCount', 'type': 'int'},
        'used_count': {'key': 'usedCount', 'type': 'int'}
    }

    def __init__(self, disabled_count=None, license=None, pending_provisioned_count=None, provisioned_count=None, used_count=None):
        super(AccountLicenseUsage, self).__init__()
        self.disabled_count = disabled_count
        self.license = license
        self.pending_provisioned_count = pending_provisioned_count
        self.provisioned_count = provisioned_count
        self.used_count = used_count


class AccountRights(Model):

    _attribute_map = {
        'level': {'key': 'level', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'str'}
    }

    def __init__(self, level=None, reason=None):
        super(AccountRights, self).__init__()
        self.level = level
        self.reason = reason


class AccountUserLicense(Model):

    _attribute_map = {
        'license': {'key': 'license', 'type': 'int'},
        'source': {'key': 'source', 'type': 'object'}
    }

    def __init__(self, license=None, source=None):
        super(AccountUserLicense, self).__init__()
        self.license = license
        self.source = source


class ClientRightsContainer(Model):

    _attribute_map = {
        'certificate_bytes': {'key': 'certificateBytes', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'}
    }

    def __init__(self, certificate_bytes=None, token=None):
        super(ClientRightsContainer, self).__init__()
        self.certificate_bytes = certificate_bytes
        self.token = token


class ExtensionAssignment(Model):

    _attribute_map = {
        'extension_gallery_id': {'key': 'extensionGalleryId', 'type': 'str'},
        'is_auto_assignment': {'key': 'isAutoAssignment', 'type': 'bool'},
        'licensing_source': {'key': 'licensingSource', 'type': 'object'},
        'user_ids': {'key': 'userIds', 'type': '[str]'}
    }

    def __init__(self, extension_gallery_id=None, is_auto_assignment=None, licensing_source=None, user_ids=None):
        super(ExtensionAssignment, self).__init__()
        self.extension_gallery_id = extension_gallery_id
        self.is_auto_assignment = is_auto_assignment
        self.licensing_source = licensing_source
        self.user_ids = user_ids


class ExtensionAssignmentDetails(Model):

    _attribute_map = {
        'assignment_status': {'key': 'assignmentStatus', 'type': 'object'},
        'source_collection_name': {'key': 'sourceCollectionName', 'type': 'str'}
    }

    def __init__(self, assignment_status=None, source_collection_name=None):
        super(ExtensionAssignmentDetails, self).__init__()
        self.assignment_status = assignment_status
        self.source_collection_name = source_collection_name


class ExtensionLicenseData(Model):

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'is_free': {'key': 'isFree', 'type': 'bool'},
        'minimum_required_access_level': {'key': 'minimumRequiredAccessLevel', 'type': 'object'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, created_date=None, extension_id=None, is_free=None, minimum_required_access_level=None, updated_date=None):
        super(ExtensionLicenseData, self).__init__()
        self.created_date = created_date
        self.extension_id = extension_id
        self.is_free = is_free
        self.minimum_required_access_level = minimum_required_access_level
        self.updated_date = updated_date


class ExtensionOperationResult(Model):

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'str'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'object'},
        'result': {'key': 'result', 'type': 'object'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, account_id=None, extension_id=None, message=None, operation=None, result=None, user_id=None):
        super(ExtensionOperationResult, self).__init__()
        self.account_id = account_id
        self.extension_id = extension_id
        self.message = message
        self.operation = operation
        self.result = result
        self.user_id = user_id


class ExtensionRightsResult(Model):

    _attribute_map = {
        'entitled_extensions': {'key': 'entitledExtensions', 'type': '[str]'},
        'host_id': {'key': 'hostId', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'reason_code': {'key': 'reasonCode', 'type': 'object'},
        'result_code': {'key': 'resultCode', 'type': 'object'}
    }

    def __init__(self, entitled_extensions=None, host_id=None, reason=None, reason_code=None, result_code=None):
        super(ExtensionRightsResult, self).__init__()
        self.entitled_extensions = entitled_extensions
        self.host_id = host_id
        self.reason = reason
        self.reason_code = reason_code
        self.result_code = result_code


class ExtensionSource(Model):

    _attribute_map = {
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'extension_gallery_id': {'key': 'extensionGalleryId', 'type': 'str'},
        'licensing_source': {'key': 'licensingSource', 'type': 'object'}
    }

    def __init__(self, assignment_source=None, extension_gallery_id=None, licensing_source=None):
        super(ExtensionSource, self).__init__()
        self.assignment_source = assignment_source
        self.extension_gallery_id = extension_gallery_id
        self.licensing_source = licensing_source


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
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'unique_user_id': {'key': 'uniqueUserId', 'type': 'int'}
    }

    def __init__(self, custom_display_name=None, descriptor=None, id=None, is_active=None, is_container=None, master_id=None, member_ids=None, member_of=None, members=None, meta_type_id=None, properties=None, provider_display_name=None, resource_version=None, subject_descriptor=None, unique_user_id=None):
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
        self.subject_descriptor = subject_descriptor
        self.unique_user_id = unique_user_id


class IdentityMapping(Model):

    _attribute_map = {
        'source_identity': {'key': 'sourceIdentity', 'type': 'Identity'},
        'target_identity': {'key': 'targetIdentity', 'type': 'Identity'}
    }

    def __init__(self, source_identity=None, target_identity=None):
        super(IdentityMapping, self).__init__()
        self.source_identity = source_identity
        self.target_identity = target_identity


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


class License(Model):

    _attribute_map = {
        'source': {'key': 'source', 'type': 'object'}
    }

    def __init__(self, source=None):
        super(License, self).__init__()
        self.source = source


class MsdnEntitlement(Model):

    _attribute_map = {
        'entitlement_code': {'key': 'entitlementCode', 'type': 'str'},
        'entitlement_name': {'key': 'entitlementName', 'type': 'str'},
        'entitlement_type': {'key': 'entitlementType', 'type': 'str'},
        'is_activated': {'key': 'isActivated', 'type': 'bool'},
        'is_entitlement_available': {'key': 'isEntitlementAvailable', 'type': 'bool'},
        'subscription_channel': {'key': 'subscriptionChannel', 'type': 'str'},
        'subscription_expiration_date': {'key': 'subscriptionExpirationDate', 'type': 'iso-8601'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'subscription_level_code': {'key': 'subscriptionLevelCode', 'type': 'str'},
        'subscription_level_name': {'key': 'subscriptionLevelName', 'type': 'str'},
        'subscription_status': {'key': 'subscriptionStatus', 'type': 'str'}
    }

    def __init__(self, entitlement_code=None, entitlement_name=None, entitlement_type=None, is_activated=None, is_entitlement_available=None, subscription_channel=None, subscription_expiration_date=None, subscription_id=None, subscription_level_code=None, subscription_level_name=None, subscription_status=None):
        super(MsdnEntitlement, self).__init__()
        self.entitlement_code = entitlement_code
        self.entitlement_name = entitlement_name
        self.entitlement_type = entitlement_type
        self.is_activated = is_activated
        self.is_entitlement_available = is_entitlement_available
        self.subscription_channel = subscription_channel
        self.subscription_expiration_date = subscription_expiration_date
        self.subscription_id = subscription_id
        self.subscription_level_code = subscription_level_code
        self.subscription_level_name = subscription_level_name
        self.subscription_status = subscription_status


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


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
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'unique_user_id': {'key': 'uniqueUserId', 'type': 'int'},
    }

    def __init__(self, custom_display_name=None, descriptor=None, id=None, is_active=None, is_container=None, master_id=None, member_ids=None, member_of=None, members=None, meta_type_id=None, properties=None, provider_display_name=None, resource_version=None, subject_descriptor=None, unique_user_id=None):
        super(Identity, self).__init__(custom_display_name=custom_display_name, descriptor=descriptor, id=id, is_active=is_active, is_container=is_container, master_id=master_id, member_ids=member_ids, member_of=member_of, members=members, meta_type_id=meta_type_id, properties=properties, provider_display_name=provider_display_name, resource_version=resource_version, subject_descriptor=subject_descriptor, unique_user_id=unique_user_id)


__all__ = [
    'AccountEntitlement',
    'AccountEntitlementUpdateModel',
    'AccountLicenseExtensionUsage',
    'AccountLicenseUsage',
    'AccountRights',
    'AccountUserLicense',
    'ClientRightsContainer',
    'ExtensionAssignment',
    'ExtensionAssignmentDetails',
    'ExtensionLicenseData',
    'ExtensionOperationResult',
    'ExtensionRightsResult',
    'ExtensionSource',
    'GraphSubjectBase',
    'IdentityBase',
    'IdentityMapping',
    'IdentityRef',
    'License',
    'MsdnEntitlement',
    'ReferenceLinks',
    'Identity',
]
