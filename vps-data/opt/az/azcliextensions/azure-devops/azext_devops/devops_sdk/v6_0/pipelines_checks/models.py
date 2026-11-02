# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ApprovalConfig(Model):

    _attribute_map = {
        'approvers': {'key': 'approvers', 'type': '[IdentityRef]'},
        'blocked_approvers': {'key': 'blockedApprovers', 'type': '[IdentityRef]'},
        'execution_order': {'key': 'executionOrder', 'type': 'object'},
        'instructions': {'key': 'instructions', 'type': 'str'},
        'min_required_approvers': {'key': 'minRequiredApprovers', 'type': 'int'}
    }

    def __init__(self, approvers=None, blocked_approvers=None, execution_order=None, instructions=None, min_required_approvers=None):
        super(ApprovalConfig, self).__init__()
        self.approvers = approvers
        self.blocked_approvers = blocked_approvers
        self.execution_order = execution_order
        self.instructions = instructions
        self.min_required_approvers = min_required_approvers


class ApprovalConfigSettings(ApprovalConfig):

    _attribute_map = {
        'approvers': {'key': 'approvers', 'type': '[IdentityRef]'},
        'blocked_approvers': {'key': 'blockedApprovers', 'type': '[IdentityRef]'},
        'execution_order': {'key': 'executionOrder', 'type': 'object'},
        'instructions': {'key': 'instructions', 'type': 'str'},
        'min_required_approvers': {'key': 'minRequiredApprovers', 'type': 'int'},
        'requester_cannot_be_approver': {'key': 'requesterCannotBeApprover', 'type': 'bool'}
    }

    def __init__(self, approvers=None, blocked_approvers=None, execution_order=None, instructions=None, min_required_approvers=None, requester_cannot_be_approver=None):
        super(ApprovalConfigSettings, self).__init__(approvers=approvers, blocked_approvers=blocked_approvers, execution_order=execution_order, instructions=instructions, min_required_approvers=min_required_approvers)
        self.requester_cannot_be_approver = requester_cannot_be_approver


class CheckConfigurationRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'resource': {'key': 'resource', 'type': 'Resource'},
        'type': {'key': 'type', 'type': 'CheckType'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, resource=None, type=None, url=None):
        super(CheckConfigurationRef, self).__init__()
        self.id = id
        self.resource = resource
        self.type = type
        self.url = url


class CheckRunResult(Model):

    _attribute_map = {
        'result_message': {'key': 'resultMessage', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, result_message=None, status=None):
        super(CheckRunResult, self).__init__()
        self.result_message = result_message
        self.status = status


class CheckSuiteRef(Model):

    _attribute_map = {
        'context': {'key': 'context', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, context=None, id=None):
        super(CheckSuiteRef, self).__init__()
        self.context = context
        self.id = id


class CheckSuiteRequest(Model):

    _attribute_map = {
        'context': {'key': 'context', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[Resource]'}
    }

    def __init__(self, context=None, id=None, resources=None):
        super(CheckSuiteRequest, self).__init__()
        self.context = context
        self.id = id
        self.resources = resources


class CheckType(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(CheckType, self).__init__()
        self.id = id
        self.name = name


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


class TaskCheckConfig(Model):

    _attribute_map = {
        'definition_ref': {'key': 'definitionRef', 'type': 'TaskCheckDefinitionReference'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'linked_variable_group': {'key': 'linkedVariableGroup', 'type': 'str'},
        'retry_interval': {'key': 'retryInterval', 'type': 'int'}
    }

    def __init__(self, definition_ref=None, display_name=None, inputs=None, linked_variable_group=None, retry_interval=None):
        super(TaskCheckConfig, self).__init__()
        self.definition_ref = definition_ref
        self.display_name = display_name
        self.inputs = inputs
        self.linked_variable_group = linked_variable_group
        self.retry_interval = retry_interval


class TaskCheckDefinitionReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, version=None):
        super(TaskCheckDefinitionReference, self).__init__()
        self.id = id
        self.name = name
        self.version = version


class CheckConfiguration(CheckConfigurationRef):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'resource': {'key': 'resource', 'type': 'Resource'},
        'type': {'key': 'type', 'type': 'CheckType'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'timeout': {'key': 'timeout', 'type': 'int'}
    }

    def __init__(self, id=None, resource=None, type=None, url=None, _links=None, created_by=None, created_on=None, modified_by=None, modified_on=None, timeout=None):
        super(CheckConfiguration, self).__init__(id=id, resource=resource, type=type, url=url)
        self._links = _links
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.timeout = timeout


class CheckRun(CheckRunResult):

    _attribute_map = {
        'result_message': {'key': 'resultMessage', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'check_configuration_ref': {'key': 'checkConfigurationRef', 'type': 'CheckConfigurationRef'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, result_message=None, status=None, check_configuration_ref=None, completed_date=None, created_date=None, id=None):
        super(CheckRun, self).__init__(result_message=result_message, status=status)
        self.check_configuration_ref = check_configuration_ref
        self.completed_date = completed_date
        self.created_date = created_date
        self.id = id


class CheckSuite(CheckSuiteRef):

    _attribute_map = {
        'context': {'key': 'context', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'check_runs': {'key': 'checkRuns', 'type': '[CheckRun]'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, context=None, id=None, _links=None, check_runs=None, completed_date=None, message=None, status=None):
        super(CheckSuite, self).__init__(context=context, id=id)
        self._links = _links
        self.check_runs = check_runs
        self.completed_date = completed_date
        self.message = message
        self.status = status


__all__ = [
    'ApprovalConfig',
    'ApprovalConfigSettings',
    'CheckConfigurationRef',
    'CheckRunResult',
    'CheckSuiteRef',
    'CheckSuiteRequest',
    'CheckType',
    'GraphSubjectBase',
    'IdentityRef',
    'ReferenceLinks',
    'Resource',
    'TaskCheckConfig',
    'TaskCheckDefinitionReference',
    'CheckConfiguration',
    'CheckRun',
    'CheckSuite',
]
