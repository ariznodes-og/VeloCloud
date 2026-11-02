# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AccessLevel(Model):

    _attribute_map = {
        'account_license_type': {'key': 'accountLicenseType', 'type': 'object'},
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'license_display_name': {'key': 'licenseDisplayName', 'type': 'str'},
        'licensing_source': {'key': 'licensingSource', 'type': 'object'},
        'msdn_license_type': {'key': 'msdnLicenseType', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'},
        'status_message': {'key': 'statusMessage', 'type': 'str'}
    }

    def __init__(self, account_license_type=None, assignment_source=None, license_display_name=None, licensing_source=None, msdn_license_type=None, status=None, status_message=None):
        super(AccessLevel, self).__init__()
        self.account_license_type = account_license_type
        self.assignment_source = assignment_source
        self.license_display_name = license_display_name
        self.licensing_source = licensing_source
        self.msdn_license_type = msdn_license_type
        self.status = status
        self.status_message = status_message


class BaseOperationResult(Model):

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'}
    }

    def __init__(self, errors=None, is_success=None):
        super(BaseOperationResult, self).__init__()
        self.errors = errors
        self.is_success = is_success


class Extension(Model):

    _attribute_map = {
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'source': {'key': 'source', 'type': 'object'}
    }

    def __init__(self, assignment_source=None, id=None, name=None, source=None):
        super(Extension, self).__init__()
        self.assignment_source = assignment_source
        self.id = id
        self.name = name
        self.source = source


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


class Group(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'group_type': {'key': 'groupType', 'type': 'object'}
    }

    def __init__(self, display_name=None, group_type=None):
        super(Group, self).__init__()
        self.display_name = display_name
        self.group_type = group_type


class GroupEntitlement(Model):

    _attribute_map = {
        'extension_rules': {'key': 'extensionRules', 'type': '[Extension]'},
        'group': {'key': 'group', 'type': 'GraphGroup'},
        'id': {'key': 'id', 'type': 'str'},
        'last_executed': {'key': 'lastExecuted', 'type': 'iso-8601'},
        'license_rule': {'key': 'licenseRule', 'type': 'AccessLevel'},
        'members': {'key': 'members', 'type': '[UserEntitlement]'},
        'project_entitlements': {'key': 'projectEntitlements', 'type': '[ProjectEntitlement]'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, extension_rules=None, group=None, id=None, last_executed=None, license_rule=None, members=None, project_entitlements=None, status=None):
        super(GroupEntitlement, self).__init__()
        self.extension_rules = extension_rules
        self.group = group
        self.id = id
        self.last_executed = last_executed
        self.license_rule = license_rule
        self.members = members
        self.project_entitlements = project_entitlements
        self.status = status


class GroupOperationResult(BaseOperationResult):

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'result': {'key': 'result', 'type': 'GroupEntitlement'}
    }

    def __init__(self, errors=None, is_success=None, group_id=None, result=None):
        super(GroupOperationResult, self).__init__(errors=errors, is_success=is_success)
        self.group_id = group_id
        self.result = result


class GroupOption(Model):

    _attribute_map = {
        'access_level': {'key': 'accessLevel', 'type': 'AccessLevel'},
        'group': {'key': 'group', 'type': 'Group'}
    }

    def __init__(self, access_level=None, group=None):
        super(GroupOption, self).__init__()
        self.access_level = access_level
        self.group = group


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


class MemberEntitlementsResponseBase(Model):

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'}
    }

    def __init__(self, is_success=None, member_entitlement=None):
        super(MemberEntitlementsResponseBase, self).__init__()
        self.is_success = is_success
        self.member_entitlement = member_entitlement


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


class OperationResult(Model):

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_id': {'key': 'memberId', 'type': 'str'},
        'result': {'key': 'result', 'type': 'MemberEntitlement'}
    }

    def __init__(self, errors=None, is_success=None, member_id=None, result=None):
        super(OperationResult, self).__init__()
        self.errors = errors
        self.is_success = is_success
        self.member_id = member_id
        self.result = result


class PagedList(Model):

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'items': {'key': 'items', 'type': '[object]'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, continuation_token=None, items=None, total_count=None):
        super(PagedList, self).__init__()
        self.continuation_token = continuation_token
        self.items = items
        self.total_count = total_count


class ProjectEntitlement(Model):

    _attribute_map = {
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'group': {'key': 'group', 'type': 'Group'},
        'is_project_permission_inherited': {'key': 'isProjectPermissionInherited', 'type': 'bool'},
        'project_permission_inherited': {'key': 'projectPermissionInherited', 'type': 'object'},
        'project_ref': {'key': 'projectRef', 'type': 'ProjectRef'},
        'team_refs': {'key': 'teamRefs', 'type': '[TeamRef]'}
    }

    def __init__(self, assignment_source=None, group=None, is_project_permission_inherited=None, project_permission_inherited=None, project_ref=None, team_refs=None):
        super(ProjectEntitlement, self).__init__()
        self.assignment_source = assignment_source
        self.group = group
        self.is_project_permission_inherited = is_project_permission_inherited
        self.project_permission_inherited = project_permission_inherited
        self.project_ref = project_ref
        self.team_refs = team_refs


class ProjectRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectRef, self).__init__()
        self.id = id
        self.name = name


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class SummaryData(Model):

    _attribute_map = {
        'assigned': {'key': 'assigned', 'type': 'int'},
        'available': {'key': 'available', 'type': 'int'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'}
    }

    def __init__(self, assigned=None, available=None, included_quantity=None, total=None):
        super(SummaryData, self).__init__()
        self.assigned = assigned
        self.available = available
        self.included_quantity = included_quantity
        self.total = total


class TeamRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TeamRef, self).__init__()
        self.id = id
        self.name = name


class UserEntitlement(Model):

    _attribute_map = {
        'access_level': {'key': 'accessLevel', 'type': 'AccessLevel'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'extensions': {'key': 'extensions', 'type': '[Extension]'},
        'group_assignments': {'key': 'groupAssignments', 'type': '[GroupEntitlement]'},
        'id': {'key': 'id', 'type': 'str'},
        'last_accessed_date': {'key': 'lastAccessedDate', 'type': 'iso-8601'},
        'project_entitlements': {'key': 'projectEntitlements', 'type': '[ProjectEntitlement]'},
        'user': {'key': 'user', 'type': 'GraphUser'}
    }

    def __init__(self, access_level=None, date_created=None, extensions=None, group_assignments=None, id=None, last_accessed_date=None, project_entitlements=None, user=None):
        super(UserEntitlement, self).__init__()
        self.access_level = access_level
        self.date_created = date_created
        self.extensions = extensions
        self.group_assignments = group_assignments
        self.id = id
        self.last_accessed_date = last_accessed_date
        self.project_entitlements = project_entitlements
        self.user = user


class UserEntitlementOperationReference(OperationReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[UserEntitlementOperationResult]'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(UserEntitlementOperationReference, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results


class UserEntitlementOperationResult(Model):

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'result': {'key': 'result', 'type': 'UserEntitlement'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, errors=None, is_success=None, result=None, user_id=None):
        super(UserEntitlementOperationResult, self).__init__()
        self.errors = errors
        self.is_success = is_success
        self.result = result
        self.user_id = user_id


class UserEntitlementsResponseBase(Model):

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'user_entitlement': {'key': 'userEntitlement', 'type': 'UserEntitlement'}
    }

    def __init__(self, is_success=None, user_entitlement=None):
        super(UserEntitlementsResponseBase, self).__init__()
        self.is_success = is_success
        self.user_entitlement = user_entitlement


class UsersSummary(Model):

    _attribute_map = {
        'available_access_levels': {'key': 'availableAccessLevels', 'type': '[AccessLevel]'},
        'extensions': {'key': 'extensions', 'type': '[ExtensionSummaryData]'},
        'group_options': {'key': 'groupOptions', 'type': '[GroupOption]'},
        'licenses': {'key': 'licenses', 'type': '[LicenseSummaryData]'},
        'project_refs': {'key': 'projectRefs', 'type': '[ProjectRef]'}
    }

    def __init__(self, available_access_levels=None, extensions=None, group_options=None, licenses=None, project_refs=None):
        super(UsersSummary, self).__init__()
        self.available_access_levels = available_access_levels
        self.extensions = extensions
        self.group_options = group_options
        self.licenses = licenses
        self.project_refs = project_refs


class ExtensionSummaryData(SummaryData):

    _attribute_map = {
        'assigned': {'key': 'assigned', 'type': 'int'},
        'available': {'key': 'available', 'type': 'int'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'},
        'assigned_through_subscription': {'key': 'assignedThroughSubscription', 'type': 'int'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'is_trial_version': {'key': 'isTrialVersion', 'type': 'bool'},
        'minimum_license_required': {'key': 'minimumLicenseRequired', 'type': 'object'},
        'remaining_trial_days': {'key': 'remainingTrialDays', 'type': 'int'},
        'trial_expiry_date': {'key': 'trialExpiryDate', 'type': 'iso-8601'}
    }

    def __init__(self, assigned=None, available=None, included_quantity=None, total=None, assigned_through_subscription=None, extension_id=None, extension_name=None, is_trial_version=None, minimum_license_required=None, remaining_trial_days=None, trial_expiry_date=None):
        super(ExtensionSummaryData, self).__init__(assigned=assigned, available=available, included_quantity=included_quantity, total=total)
        self.assigned_through_subscription = assigned_through_subscription
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.is_trial_version = is_trial_version
        self.minimum_license_required = minimum_license_required
        self.remaining_trial_days = remaining_trial_days
        self.trial_expiry_date = trial_expiry_date


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


class GroupEntitlementOperationReference(OperationReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[GroupOperationResult]'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(GroupEntitlementOperationReference, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results


class LicenseSummaryData(SummaryData):

    _attribute_map = {
        'assigned': {'key': 'assigned', 'type': 'int'},
        'available': {'key': 'available', 'type': 'int'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'},
        'account_license_type': {'key': 'accountLicenseType', 'type': 'object'},
        'disabled': {'key': 'disabled', 'type': 'int'},
        'is_purchasable': {'key': 'isPurchasable', 'type': 'bool'},
        'license_name': {'key': 'licenseName', 'type': 'str'},
        'msdn_license_type': {'key': 'msdnLicenseType', 'type': 'object'},
        'next_billing_date': {'key': 'nextBillingDate', 'type': 'iso-8601'},
        'source': {'key': 'source', 'type': 'object'},
        'total_after_next_billing_date': {'key': 'totalAfterNextBillingDate', 'type': 'int'}
    }

    def __init__(self, assigned=None, available=None, included_quantity=None, total=None, account_license_type=None, disabled=None, is_purchasable=None, license_name=None, msdn_license_type=None, next_billing_date=None, source=None, total_after_next_billing_date=None):
        super(LicenseSummaryData, self).__init__(assigned=assigned, available=available, included_quantity=included_quantity, total=total)
        self.account_license_type = account_license_type
        self.disabled = disabled
        self.is_purchasable = is_purchasable
        self.license_name = license_name
        self.msdn_license_type = msdn_license_type
        self.next_billing_date = next_billing_date
        self.source = source
        self.total_after_next_billing_date = total_after_next_billing_date


class MemberEntitlement(UserEntitlement):

    _attribute_map = {
        'access_level': {'key': 'accessLevel', 'type': 'AccessLevel'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'extensions': {'key': 'extensions', 'type': '[Extension]'},
        'group_assignments': {'key': 'groupAssignments', 'type': '[GroupEntitlement]'},
        'id': {'key': 'id', 'type': 'str'},
        'last_accessed_date': {'key': 'lastAccessedDate', 'type': 'iso-8601'},
        'project_entitlements': {'key': 'projectEntitlements', 'type': '[ProjectEntitlement]'},
        'user': {'key': 'user', 'type': 'GraphUser'},
        'member': {'key': 'member', 'type': 'GraphMember'}
    }

    def __init__(self, access_level=None, date_created=None, extensions=None, group_assignments=None, id=None, last_accessed_date=None, project_entitlements=None, user=None, member=None):
        super(MemberEntitlement, self).__init__(access_level=access_level, date_created=date_created, extensions=extensions, group_assignments=group_assignments, id=id, last_accessed_date=last_accessed_date, project_entitlements=project_entitlements, user=user)
        self.member = member


class MemberEntitlementOperationReference(OperationReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[OperationResult]'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(MemberEntitlementOperationReference, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results


class MemberEntitlementsPatchResponse(MemberEntitlementsResponseBase):

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'},
        'operation_results': {'key': 'operationResults', 'type': '[OperationResult]'}
    }

    def __init__(self, is_success=None, member_entitlement=None, operation_results=None):
        super(MemberEntitlementsPatchResponse, self).__init__(is_success=is_success, member_entitlement=member_entitlement)
        self.operation_results = operation_results


class MemberEntitlementsPostResponse(MemberEntitlementsResponseBase):

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'},
        'operation_result': {'key': 'operationResult', 'type': 'OperationResult'}
    }

    def __init__(self, is_success=None, member_entitlement=None, operation_result=None):
        super(MemberEntitlementsPostResponse, self).__init__(is_success=is_success, member_entitlement=member_entitlement)
        self.operation_result = operation_result


class PagedGraphMemberList(PagedList):

    _attribute_map = {
        'members': {'key': 'members', 'type': '[UserEntitlement]'}
    }

    def __init__(self, members=None):
        super(PagedGraphMemberList, self).__init__()
        self.members = members


class UserEntitlementsPatchResponse(UserEntitlementsResponseBase):

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'user_entitlement': {'key': 'userEntitlement', 'type': 'UserEntitlement'},
        'operation_results': {'key': 'operationResults', 'type': '[UserEntitlementOperationResult]'}
    }

    def __init__(self, is_success=None, user_entitlement=None, operation_results=None):
        super(UserEntitlementsPatchResponse, self).__init__(is_success=is_success, user_entitlement=user_entitlement)
        self.operation_results = operation_results


class UserEntitlementsPostResponse(UserEntitlementsResponseBase):

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'user_entitlement': {'key': 'userEntitlement', 'type': 'UserEntitlement'},
        'operation_result': {'key': 'operationResult', 'type': 'UserEntitlementOperationResult'}
    }

    def __init__(self, is_success=None, user_entitlement=None, operation_result=None):
        super(UserEntitlementsPostResponse, self).__init__(is_success=is_success, user_entitlement=user_entitlement)
        self.operation_result = operation_result


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
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'metadata_update_date': {'key': 'metadataUpdateDate', 'type': 'iso-8601'},
        'meta_type': {'key': 'metaType', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, domain=None, mail_address=None, principal_name=None, directory_alias=None, is_deleted_in_origin=None, metadata_update_date=None, meta_type=None):
        super(GraphUser, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.directory_alias = directory_alias
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
    'AccessLevel',
    'BaseOperationResult',
    'Extension',
    'GraphSubjectBase',
    'Group',
    'GroupEntitlement',
    'GroupOperationResult',
    'GroupOption',
    'JsonPatchOperation',
    'MemberEntitlementsResponseBase',
    'OperationReference',
    'OperationResult',
    'PagedList',
    'ProjectEntitlement',
    'ProjectRef',
    'ReferenceLinks',
    'SummaryData',
    'TeamRef',
    'UserEntitlement',
    'UserEntitlementOperationReference',
    'UserEntitlementOperationResult',
    'UserEntitlementsResponseBase',
    'UsersSummary',
    'ExtensionSummaryData',
    'GraphSubject',
    'GroupEntitlementOperationReference',
    'LicenseSummaryData',
    'MemberEntitlement',
    'MemberEntitlementOperationReference',
    'MemberEntitlementsPatchResponse',
    'MemberEntitlementsPostResponse',
    'PagedGraphMemberList',
    'UserEntitlementsPatchResponse',
    'UserEntitlementsPostResponse',
    'GraphMember',
    'GraphUser',
    'GraphGroup',
]
