# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AddProcessWorkItemTypeFieldRequest(Model):

    _attribute_map = {
        'allowed_values': {'key': 'allowedValues', 'type': '[str]'},
        'allow_groups': {'key': 'allowGroups', 'type': 'bool'},
        'default_value': {'key': 'defaultValue', 'type': 'object'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'}
    }

    def __init__(self, allowed_values=None, allow_groups=None, default_value=None, read_only=None, reference_name=None, required=None):
        super(AddProcessWorkItemTypeFieldRequest, self).__init__()
        self.allowed_values = allowed_values
        self.allow_groups = allow_groups
        self.default_value = default_value
        self.read_only = read_only
        self.reference_name = reference_name
        self.required = required


class Control(Model):

    _attribute_map = {
        'contribution': {'key': 'contribution', 'type': 'WitContribution'},
        'control_type': {'key': 'controlType', 'type': 'str'},
        'height': {'key': 'height', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'inherited': {'key': 'inherited', 'type': 'bool'},
        'is_contribution': {'key': 'isContribution', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'visible': {'key': 'visible', 'type': 'bool'},
        'watermark': {'key': 'watermark', 'type': 'str'}
    }

    def __init__(self, contribution=None, control_type=None, height=None, id=None, inherited=None, is_contribution=None, label=None, metadata=None, order=None, overridden=None, read_only=None, visible=None, watermark=None):
        super(Control, self).__init__()
        self.contribution = contribution
        self.control_type = control_type
        self.height = height
        self.id = id
        self.inherited = inherited
        self.is_contribution = is_contribution
        self.label = label
        self.metadata = metadata
        self.order = order
        self.overridden = overridden
        self.read_only = read_only
        self.visible = visible
        self.watermark = watermark


class CreateProcessModel(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_process_type_id': {'key': 'parentProcessTypeId', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, parent_process_type_id=None, reference_name=None):
        super(CreateProcessModel, self).__init__()
        self.description = description
        self.name = name
        self.parent_process_type_id = parent_process_type_id
        self.reference_name = reference_name


class CreateProcessRuleRequest(Model):

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[RuleAction]'},
        'conditions': {'key': 'conditions', 'type': '[RuleCondition]'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, actions=None, conditions=None, is_disabled=None, name=None):
        super(CreateProcessRuleRequest, self).__init__()
        self.actions = actions
        self.conditions = conditions
        self.is_disabled = is_disabled
        self.name = name


class CreateProcessWorkItemTypeRequest(Model):

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'inherits_from': {'key': 'inheritsFrom', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, color=None, description=None, icon=None, inherits_from=None, is_disabled=None, name=None):
        super(CreateProcessWorkItemTypeRequest, self).__init__()
        self.color = color
        self.description = description
        self.icon = icon
        self.inherits_from = inherits_from
        self.is_disabled = is_disabled
        self.name = name


class Extension(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, id=None):
        super(Extension, self).__init__()
        self.id = id


class FieldModel(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_identity': {'key': 'isIdentity', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, is_identity=None, name=None, type=None, url=None):
        super(FieldModel, self).__init__()
        self.description = description
        self.id = id
        self.is_identity = is_identity
        self.name = name
        self.type = type
        self.url = url


class FieldRuleModel(Model):

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[RuleActionModel]'},
        'conditions': {'key': 'conditions', 'type': '[RuleConditionModel]'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'is_system': {'key': 'isSystem', 'type': 'bool'}
    }

    def __init__(self, actions=None, conditions=None, friendly_name=None, id=None, is_disabled=None, is_system=None):
        super(FieldRuleModel, self).__init__()
        self.actions = actions
        self.conditions = conditions
        self.friendly_name = friendly_name
        self.id = id
        self.is_disabled = is_disabled
        self.is_system = is_system


class FormLayout(Model):

    _attribute_map = {
        'extensions': {'key': 'extensions', 'type': '[Extension]'},
        'pages': {'key': 'pages', 'type': '[Page]'},
        'system_controls': {'key': 'systemControls', 'type': '[Control]'}
    }

    def __init__(self, extensions=None, pages=None, system_controls=None):
        super(FormLayout, self).__init__()
        self.extensions = extensions
        self.pages = pages
        self.system_controls = system_controls


class Group(Model):

    _attribute_map = {
        'contribution': {'key': 'contribution', 'type': 'WitContribution'},
        'controls': {'key': 'controls', 'type': '[Control]'},
        'height': {'key': 'height', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'inherited': {'key': 'inherited', 'type': 'bool'},
        'is_contribution': {'key': 'isContribution', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'visible': {'key': 'visible', 'type': 'bool'}
    }

    def __init__(self, contribution=None, controls=None, height=None, id=None, inherited=None, is_contribution=None, label=None, order=None, overridden=None, visible=None):
        super(Group, self).__init__()
        self.contribution = contribution
        self.controls = controls
        self.height = height
        self.id = id
        self.inherited = inherited
        self.is_contribution = is_contribution
        self.label = label
        self.order = order
        self.overridden = overridden
        self.visible = visible


class HideStateModel(Model):

    _attribute_map = {
        'hidden': {'key': 'hidden', 'type': 'bool'}
    }

    def __init__(self, hidden=None):
        super(HideStateModel, self).__init__()
        self.hidden = hidden


class Page(Model):

    _attribute_map = {
        'contribution': {'key': 'contribution', 'type': 'WitContribution'},
        'id': {'key': 'id', 'type': 'str'},
        'inherited': {'key': 'inherited', 'type': 'bool'},
        'is_contribution': {'key': 'isContribution', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'locked': {'key': 'locked', 'type': 'bool'},
        'order': {'key': 'order', 'type': 'int'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'page_type': {'key': 'pageType', 'type': 'object'},
        'sections': {'key': 'sections', 'type': '[Section]'},
        'visible': {'key': 'visible', 'type': 'bool'}
    }

    def __init__(self, contribution=None, id=None, inherited=None, is_contribution=None, label=None, locked=None, order=None, overridden=None, page_type=None, sections=None, visible=None):
        super(Page, self).__init__()
        self.contribution = contribution
        self.id = id
        self.inherited = inherited
        self.is_contribution = is_contribution
        self.label = label
        self.locked = locked
        self.order = order
        self.overridden = overridden
        self.page_type = page_type
        self.sections = sections
        self.visible = visible


class PickListMetadata(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_suggested': {'key': 'isSuggested', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, is_suggested=None, name=None, type=None, url=None):
        super(PickListMetadata, self).__init__()
        self.id = id
        self.is_suggested = is_suggested
        self.name = name
        self.type = type
        self.url = url


class ProcessBehavior(Model):

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'customization': {'key': 'customization', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '[ProcessBehaviorField]'},
        'inherits': {'key': 'inherits', 'type': 'ProcessBehaviorReference'},
        'name': {'key': 'name', 'type': 'str'},
        'rank': {'key': 'rank', 'type': 'int'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, color=None, customization=None, description=None, fields=None, inherits=None, name=None, rank=None, reference_name=None, url=None):
        super(ProcessBehavior, self).__init__()
        self.color = color
        self.customization = customization
        self.description = description
        self.fields = fields
        self.inherits = inherits
        self.name = name
        self.rank = rank
        self.reference_name = reference_name
        self.url = url


class ProcessBehaviorCreateRequest(Model):

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'}
    }

    def __init__(self, color=None, inherits=None, name=None, reference_name=None):
        super(ProcessBehaviorCreateRequest, self).__init__()
        self.color = color
        self.inherits = inherits
        self.name = name
        self.reference_name = reference_name


class ProcessBehaviorField(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None, url=None):
        super(ProcessBehaviorField, self).__init__()
        self.name = name
        self.reference_name = reference_name
        self.url = url


class ProcessBehaviorReference(Model):

    _attribute_map = {
        'behavior_ref_name': {'key': 'behaviorRefName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, behavior_ref_name=None, url=None):
        super(ProcessBehaviorReference, self).__init__()
        self.behavior_ref_name = behavior_ref_name
        self.url = url


class ProcessBehaviorUpdateRequest(Model):

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, color=None, name=None):
        super(ProcessBehaviorUpdateRequest, self).__init__()
        self.color = color
        self.name = name


class ProcessInfo(Model):

    _attribute_map = {
        'customization_type': {'key': 'customizationType', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_process_type_id': {'key': 'parentProcessTypeId', 'type': 'str'},
        'projects': {'key': 'projects', 'type': '[ProjectReference]'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'type_id': {'key': 'typeId', 'type': 'str'}
    }

    def __init__(self, customization_type=None, description=None, is_default=None, is_enabled=None, name=None, parent_process_type_id=None, projects=None, reference_name=None, type_id=None):
        super(ProcessInfo, self).__init__()
        self.customization_type = customization_type
        self.description = description
        self.is_default = is_default
        self.is_enabled = is_enabled
        self.name = name
        self.parent_process_type_id = parent_process_type_id
        self.projects = projects
        self.reference_name = reference_name
        self.type_id = type_id


class ProcessModel(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'projects': {'key': 'projects', 'type': '[ProjectReference]'},
        'properties': {'key': 'properties', 'type': 'ProcessProperties'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'type_id': {'key': 'typeId', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, projects=None, properties=None, reference_name=None, type_id=None):
        super(ProcessModel, self).__init__()
        self.description = description
        self.name = name
        self.projects = projects
        self.properties = properties
        self.reference_name = reference_name
        self.type_id = type_id


class ProcessProperties(Model):

    _attribute_map = {
        'class_': {'key': 'class', 'type': 'object'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'parent_process_type_id': {'key': 'parentProcessTypeId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, class_=None, is_default=None, is_enabled=None, parent_process_type_id=None, version=None):
        super(ProcessProperties, self).__init__()
        self.class_ = class_
        self.is_default = is_default
        self.is_enabled = is_enabled
        self.parent_process_type_id = parent_process_type_id
        self.version = version


class ProcessRule(CreateProcessRuleRequest):

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[RuleAction]'},
        'conditions': {'key': 'conditions', 'type': '[RuleCondition]'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'customization_type': {'key': 'customizationType', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, actions=None, conditions=None, is_disabled=None, name=None, customization_type=None, id=None, url=None):
        super(ProcessRule, self).__init__(actions=actions, conditions=conditions, is_disabled=is_disabled, name=name)
        self.customization_type = customization_type
        self.id = id
        self.url = url


class ProcessWorkItemType(Model):

    _attribute_map = {
        'behaviors': {'key': 'behaviors', 'type': '[WorkItemTypeBehavior]'},
        'color': {'key': 'color', 'type': 'str'},
        'customization': {'key': 'customization', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'layout': {'key': 'layout', 'type': 'FormLayout'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'states': {'key': 'states', 'type': '[WorkItemStateResultModel]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, behaviors=None, color=None, customization=None, description=None, icon=None, inherits=None, is_disabled=None, layout=None, name=None, reference_name=None, states=None, url=None):
        super(ProcessWorkItemType, self).__init__()
        self.behaviors = behaviors
        self.color = color
        self.customization = customization
        self.description = description
        self.icon = icon
        self.inherits = inherits
        self.is_disabled = is_disabled
        self.layout = layout
        self.name = name
        self.reference_name = reference_name
        self.states = states
        self.url = url


class ProcessWorkItemTypeField(Model):

    _attribute_map = {
        'allowed_values': {'key': 'allowedValues', 'type': '[object]'},
        'allow_groups': {'key': 'allowGroups', 'type': 'bool'},
        'customization': {'key': 'customization', 'type': 'object'},
        'default_value': {'key': 'defaultValue', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, allowed_values=None, allow_groups=None, customization=None, default_value=None, description=None, name=None, read_only=None, reference_name=None, required=None, type=None, url=None):
        super(ProcessWorkItemTypeField, self).__init__()
        self.allowed_values = allowed_values
        self.allow_groups = allow_groups
        self.customization = customization
        self.default_value = default_value
        self.description = description
        self.name = name
        self.read_only = read_only
        self.reference_name = reference_name
        self.required = required
        self.type = type
        self.url = url


class ProjectReference(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, name=None, url=None):
        super(ProjectReference, self).__init__()
        self.description = description
        self.id = id
        self.name = name
        self.url = url


class RuleAction(Model):

    _attribute_map = {
        'action_type': {'key': 'actionType', 'type': 'object'},
        'target_field': {'key': 'targetField', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, action_type=None, target_field=None, value=None):
        super(RuleAction, self).__init__()
        self.action_type = action_type
        self.target_field = target_field
        self.value = value


class RuleActionModel(Model):

    _attribute_map = {
        'action_type': {'key': 'actionType', 'type': 'str'},
        'target_field': {'key': 'targetField', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, action_type=None, target_field=None, value=None):
        super(RuleActionModel, self).__init__()
        self.action_type = action_type
        self.target_field = target_field
        self.value = value


class RuleCondition(Model):

    _attribute_map = {
        'condition_type': {'key': 'conditionType', 'type': 'object'},
        'field': {'key': 'field', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, condition_type=None, field=None, value=None):
        super(RuleCondition, self).__init__()
        self.condition_type = condition_type
        self.field = field
        self.value = value


class RuleConditionModel(Model):

    _attribute_map = {
        'condition_type': {'key': 'conditionType', 'type': 'str'},
        'field': {'key': 'field', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, condition_type=None, field=None, value=None):
        super(RuleConditionModel, self).__init__()
        self.condition_type = condition_type
        self.field = field
        self.value = value


class Section(Model):

    _attribute_map = {
        'groups': {'key': 'groups', 'type': '[Group]'},
        'id': {'key': 'id', 'type': 'str'},
        'overridden': {'key': 'overridden', 'type': 'bool'}
    }

    def __init__(self, groups=None, id=None, overridden=None):
        super(Section, self).__init__()
        self.groups = groups
        self.id = id
        self.overridden = overridden


class UpdateProcessModel(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, is_default=None, is_enabled=None, name=None):
        super(UpdateProcessModel, self).__init__()
        self.description = description
        self.is_default = is_default
        self.is_enabled = is_enabled
        self.name = name


class UpdateProcessRuleRequest(CreateProcessRuleRequest):

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[RuleAction]'},
        'conditions': {'key': 'conditions', 'type': '[RuleCondition]'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, actions=None, conditions=None, is_disabled=None, name=None, id=None):
        super(UpdateProcessRuleRequest, self).__init__(actions=actions, conditions=conditions, is_disabled=is_disabled, name=name)
        self.id = id


class UpdateProcessWorkItemTypeFieldRequest(Model):

    _attribute_map = {
        'allowed_values': {'key': 'allowedValues', 'type': '[str]'},
        'allow_groups': {'key': 'allowGroups', 'type': 'bool'},
        'default_value': {'key': 'defaultValue', 'type': 'object'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'required': {'key': 'required', 'type': 'bool'}
    }

    def __init__(self, allowed_values=None, allow_groups=None, default_value=None, read_only=None, required=None):
        super(UpdateProcessWorkItemTypeFieldRequest, self).__init__()
        self.allowed_values = allowed_values
        self.allow_groups = allow_groups
        self.default_value = default_value
        self.read_only = read_only
        self.required = required


class UpdateProcessWorkItemTypeRequest(Model):

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'}
    }

    def __init__(self, color=None, description=None, icon=None, is_disabled=None):
        super(UpdateProcessWorkItemTypeRequest, self).__init__()
        self.color = color
        self.description = description
        self.icon = icon
        self.is_disabled = is_disabled


class WitContribution(Model):

    _attribute_map = {
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'height': {'key': 'height', 'type': 'int'},
        'inputs': {'key': 'inputs', 'type': '{object}'},
        'show_on_deleted_work_item': {'key': 'showOnDeletedWorkItem', 'type': 'bool'}
    }

    def __init__(self, contribution_id=None, height=None, inputs=None, show_on_deleted_work_item=None):
        super(WitContribution, self).__init__()
        self.contribution_id = contribution_id
        self.height = height
        self.inputs = inputs
        self.show_on_deleted_work_item = show_on_deleted_work_item


class WorkItemBehavior(Model):

    _attribute_map = {
        'abstract': {'key': 'abstract', 'type': 'bool'},
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '[WorkItemBehaviorField]'},
        'id': {'key': 'id', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'WorkItemBehaviorReference'},
        'name': {'key': 'name', 'type': 'str'},
        'overriden': {'key': 'overriden', 'type': 'bool'},
        'rank': {'key': 'rank', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, abstract=None, color=None, description=None, fields=None, id=None, inherits=None, name=None, overriden=None, rank=None, url=None):
        super(WorkItemBehavior, self).__init__()
        self.abstract = abstract
        self.color = color
        self.description = description
        self.fields = fields
        self.id = id
        self.inherits = inherits
        self.name = name
        self.overriden = overriden
        self.rank = rank
        self.url = url


class WorkItemBehaviorField(Model):

    _attribute_map = {
        'behavior_field_id': {'key': 'behaviorFieldId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, behavior_field_id=None, id=None, url=None):
        super(WorkItemBehaviorField, self).__init__()
        self.behavior_field_id = behavior_field_id
        self.id = id
        self.url = url


class WorkItemBehaviorReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WorkItemBehaviorReference, self).__init__()
        self.id = id
        self.url = url


class WorkItemStateInputModel(Model):

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'state_category': {'key': 'stateCategory', 'type': 'str'}
    }

    def __init__(self, color=None, name=None, order=None, state_category=None):
        super(WorkItemStateInputModel, self).__init__()
        self.color = color
        self.name = name
        self.order = order
        self.state_category = state_category


class WorkItemStateResultModel(Model):

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'customization_type': {'key': 'customizationType', 'type': 'object'},
        'hidden': {'key': 'hidden', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'state_category': {'key': 'stateCategory', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, color=None, customization_type=None, hidden=None, id=None, name=None, order=None, state_category=None, url=None):
        super(WorkItemStateResultModel, self).__init__()
        self.color = color
        self.customization_type = customization_type
        self.hidden = hidden
        self.id = id
        self.name = name
        self.order = order
        self.state_category = state_category
        self.url = url


class WorkItemTypeBehavior(Model):

    _attribute_map = {
        'behavior': {'key': 'behavior', 'type': 'WorkItemBehaviorReference'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, behavior=None, is_default=None, url=None):
        super(WorkItemTypeBehavior, self).__init__()
        self.behavior = behavior
        self.is_default = is_default
        self.url = url


class WorkItemTypeModel(Model):

    _attribute_map = {
        'behaviors': {'key': 'behaviors', 'type': '[WorkItemTypeBehavior]'},
        'class_': {'key': 'class', 'type': 'object'},
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'layout': {'key': 'layout', 'type': 'FormLayout'},
        'name': {'key': 'name', 'type': 'str'},
        'states': {'key': 'states', 'type': '[WorkItemStateResultModel]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, behaviors=None, class_=None, color=None, description=None, icon=None, id=None, inherits=None, is_disabled=None, layout=None, name=None, states=None, url=None):
        super(WorkItemTypeModel, self).__init__()
        self.behaviors = behaviors
        self.class_ = class_
        self.color = color
        self.description = description
        self.icon = icon
        self.id = id
        self.inherits = inherits
        self.is_disabled = is_disabled
        self.layout = layout
        self.name = name
        self.states = states
        self.url = url


class PickList(PickListMetadata):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_suggested': {'key': 'isSuggested', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'items': {'key': 'items', 'type': '[str]'}
    }

    def __init__(self, id=None, is_suggested=None, name=None, type=None, url=None, items=None):
        super(PickList, self).__init__(id=id, is_suggested=is_suggested, name=name, type=type, url=url)
        self.items = items


__all__ = [
    'AddProcessWorkItemTypeFieldRequest',
    'Control',
    'CreateProcessModel',
    'CreateProcessRuleRequest',
    'CreateProcessWorkItemTypeRequest',
    'Extension',
    'FieldModel',
    'FieldRuleModel',
    'FormLayout',
    'Group',
    'HideStateModel',
    'Page',
    'PickListMetadata',
    'ProcessBehavior',
    'ProcessBehaviorCreateRequest',
    'ProcessBehaviorField',
    'ProcessBehaviorReference',
    'ProcessBehaviorUpdateRequest',
    'ProcessInfo',
    'ProcessModel',
    'ProcessProperties',
    'ProcessRule',
    'ProcessWorkItemType',
    'ProcessWorkItemTypeField',
    'ProjectReference',
    'RuleAction',
    'RuleActionModel',
    'RuleCondition',
    'RuleConditionModel',
    'Section',
    'UpdateProcessModel',
    'UpdateProcessRuleRequest',
    'UpdateProcessWorkItemTypeFieldRequest',
    'UpdateProcessWorkItemTypeRequest',
    'WitContribution',
    'WorkItemBehavior',
    'WorkItemBehaviorField',
    'WorkItemBehaviorReference',
    'WorkItemStateInputModel',
    'WorkItemStateResultModel',
    'WorkItemTypeBehavior',
    'WorkItemTypeModel',
    'PickList',
]
