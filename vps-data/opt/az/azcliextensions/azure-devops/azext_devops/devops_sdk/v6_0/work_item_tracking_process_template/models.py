# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AdminBehavior(Model):

    _attribute_map = {
        'abstract': {'key': 'abstract', 'type': 'bool'},
        'color': {'key': 'color', 'type': 'str'},
        'custom': {'key': 'custom', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '[AdminBehaviorField]'},
        'id': {'key': 'id', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'overriden': {'key': 'overriden', 'type': 'bool'},
        'rank': {'key': 'rank', 'type': 'int'}
    }

    def __init__(self, abstract=None, color=None, custom=None, description=None, fields=None, id=None, inherits=None, name=None, overriden=None, rank=None):
        super(AdminBehavior, self).__init__()
        self.abstract = abstract
        self.color = color
        self.custom = custom
        self.description = description
        self.fields = fields
        self.id = id
        self.inherits = inherits
        self.name = name
        self.overriden = overriden
        self.rank = rank


class AdminBehaviorField(Model):

    _attribute_map = {
        'behavior_field_id': {'key': 'behaviorFieldId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, behavior_field_id=None, id=None, name=None):
        super(AdminBehaviorField, self).__init__()
        self.behavior_field_id = behavior_field_id
        self.id = id
        self.name = name


class CheckTemplateExistenceResult(Model):

    _attribute_map = {
        'does_template_exist': {'key': 'doesTemplateExist', 'type': 'bool'},
        'existing_template_name': {'key': 'existingTemplateName', 'type': 'str'},
        'existing_template_type_id': {'key': 'existingTemplateTypeId', 'type': 'str'},
        'requested_template_name': {'key': 'requestedTemplateName', 'type': 'str'}
    }

    def __init__(self, does_template_exist=None, existing_template_name=None, existing_template_type_id=None, requested_template_name=None):
        super(CheckTemplateExistenceResult, self).__init__()
        self.does_template_exist = does_template_exist
        self.existing_template_name = existing_template_name
        self.existing_template_type_id = existing_template_type_id
        self.requested_template_name = requested_template_name


class ProcessImportResult(Model):

    _attribute_map = {
        'check_existence_result': {'key': 'checkExistenceResult', 'type': 'CheckTemplateExistenceResult'},
        'help_url': {'key': 'helpUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_new': {'key': 'isNew', 'type': 'bool'},
        'promote_job_id': {'key': 'promoteJobId', 'type': 'str'},
        'validation_results': {'key': 'validationResults', 'type': '[ValidationIssue]'}
    }

    def __init__(self, check_existence_result=None, help_url=None, id=None, is_new=None, promote_job_id=None, validation_results=None):
        super(ProcessImportResult, self).__init__()
        self.check_existence_result = check_existence_result
        self.help_url = help_url
        self.id = id
        self.is_new = is_new
        self.promote_job_id = promote_job_id
        self.validation_results = validation_results


class ProcessPromoteStatus(Model):

    _attribute_map = {
        'complete': {'key': 'complete', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'pending': {'key': 'pending', 'type': 'int'},
        'remaining_retries': {'key': 'remainingRetries', 'type': 'int'},
        'successful': {'key': 'successful', 'type': 'bool'}
    }

    def __init__(self, complete=None, id=None, message=None, pending=None, remaining_retries=None, successful=None):
        super(ProcessPromoteStatus, self).__init__()
        self.complete = complete
        self.id = id
        self.message = message
        self.pending = pending
        self.remaining_retries = remaining_retries
        self.successful = successful


class ValidationIssue(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'file': {'key': 'file', 'type': 'str'},
        'help_link': {'key': 'helpLink', 'type': 'str'},
        'issue_type': {'key': 'issueType', 'type': 'object'},
        'line': {'key': 'line', 'type': 'int'}
    }

    def __init__(self, description=None, file=None, help_link=None, issue_type=None, line=None):
        super(ValidationIssue, self).__init__()
        self.description = description
        self.file = file
        self.help_link = help_link
        self.issue_type = issue_type
        self.line = line


__all__ = [
    'AdminBehavior',
    'AdminBehaviorField',
    'CheckTemplateExistenceResult',
    'ProcessImportResult',
    'ProcessPromoteStatus',
    'ValidationIssue',
]
