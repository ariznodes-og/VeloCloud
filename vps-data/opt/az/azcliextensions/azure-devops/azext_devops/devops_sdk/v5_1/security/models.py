# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AccessControlEntry(Model):

    _attribute_map = {
        'allow': {'key': 'allow', 'type': 'int'},
        'deny': {'key': 'deny', 'type': 'int'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'extended_info': {'key': 'extendedInfo', 'type': 'AceExtendedInformation'}
    }

    def __init__(self, allow=None, deny=None, descriptor=None, extended_info=None):
        super(AccessControlEntry, self).__init__()
        self.allow = allow
        self.deny = deny
        self.descriptor = descriptor
        self.extended_info = extended_info


class AccessControlList(Model):

    _attribute_map = {
        'aces_dictionary': {'key': 'acesDictionary', 'type': '{AccessControlEntry}'},
        'include_extended_info': {'key': 'includeExtendedInfo', 'type': 'bool'},
        'inherit_permissions': {'key': 'inheritPermissions', 'type': 'bool'},
        'token': {'key': 'token', 'type': 'str'}
    }

    def __init__(self, aces_dictionary=None, include_extended_info=None, inherit_permissions=None, token=None):
        super(AccessControlList, self).__init__()
        self.aces_dictionary = aces_dictionary
        self.include_extended_info = include_extended_info
        self.inherit_permissions = inherit_permissions
        self.token = token


class AccessControlListsCollection(Model):

    _attribute_map = {
    }

    def __init__(self):
        super(AccessControlListsCollection, self).__init__()


class AceExtendedInformation(Model):

    _attribute_map = {
        'effective_allow': {'key': 'effectiveAllow', 'type': 'int'},
        'effective_deny': {'key': 'effectiveDeny', 'type': 'int'},
        'inherited_allow': {'key': 'inheritedAllow', 'type': 'int'},
        'inherited_deny': {'key': 'inheritedDeny', 'type': 'int'}
    }

    def __init__(self, effective_allow=None, effective_deny=None, inherited_allow=None, inherited_deny=None):
        super(AceExtendedInformation, self).__init__()
        self.effective_allow = effective_allow
        self.effective_deny = effective_deny
        self.inherited_allow = inherited_allow
        self.inherited_deny = inherited_deny


class ActionDefinition(Model):

    _attribute_map = {
        'bit': {'key': 'bit', 'type': 'int'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'namespace_id': {'key': 'namespaceId', 'type': 'str'}
    }

    def __init__(self, bit=None, display_name=None, name=None, namespace_id=None):
        super(ActionDefinition, self).__init__()
        self.bit = bit
        self.display_name = display_name
        self.name = name
        self.namespace_id = namespace_id


class PermissionEvaluation(Model):

    _attribute_map = {
        'permissions': {'key': 'permissions', 'type': 'int'},
        'security_namespace_id': {'key': 'securityNamespaceId', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'value': {'key': 'value', 'type': 'bool'}
    }

    def __init__(self, permissions=None, security_namespace_id=None, token=None, value=None):
        super(PermissionEvaluation, self).__init__()
        self.permissions = permissions
        self.security_namespace_id = security_namespace_id
        self.token = token
        self.value = value


class PermissionEvaluationBatch(Model):

    _attribute_map = {
        'always_allow_administrators': {'key': 'alwaysAllowAdministrators', 'type': 'bool'},
        'evaluations': {'key': 'evaluations', 'type': '[PermissionEvaluation]'}
    }

    def __init__(self, always_allow_administrators=None, evaluations=None):
        super(PermissionEvaluationBatch, self).__init__()
        self.always_allow_administrators = always_allow_administrators
        self.evaluations = evaluations


class SecurityNamespaceDescription(Model):

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[ActionDefinition]'},
        'dataspace_category': {'key': 'dataspaceCategory', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'element_length': {'key': 'elementLength', 'type': 'int'},
        'extension_type': {'key': 'extensionType', 'type': 'str'},
        'is_remotable': {'key': 'isRemotable', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'namespace_id': {'key': 'namespaceId', 'type': 'str'},
        'read_permission': {'key': 'readPermission', 'type': 'int'},
        'separator_value': {'key': 'separatorValue', 'type': 'str'},
        'structure_value': {'key': 'structureValue', 'type': 'int'},
        'system_bit_mask': {'key': 'systemBitMask', 'type': 'int'},
        'use_token_translator': {'key': 'useTokenTranslator', 'type': 'bool'},
        'write_permission': {'key': 'writePermission', 'type': 'int'}
    }

    def __init__(self, actions=None, dataspace_category=None, display_name=None, element_length=None, extension_type=None, is_remotable=None, name=None, namespace_id=None, read_permission=None, separator_value=None, structure_value=None, system_bit_mask=None, use_token_translator=None, write_permission=None):
        super(SecurityNamespaceDescription, self).__init__()
        self.actions = actions
        self.dataspace_category = dataspace_category
        self.display_name = display_name
        self.element_length = element_length
        self.extension_type = extension_type
        self.is_remotable = is_remotable
        self.name = name
        self.namespace_id = namespace_id
        self.read_permission = read_permission
        self.separator_value = separator_value
        self.structure_value = structure_value
        self.system_bit_mask = system_bit_mask
        self.use_token_translator = use_token_translator
        self.write_permission = write_permission


__all__ = [
    'AccessControlEntry',
    'AccessControlList',
    'AccessControlListsCollection',
    'AceExtendedInformation',
    'ActionDefinition',
    'PermissionEvaluation',
    'PermissionEvaluationBatch',
    'SecurityNamespaceDescription',
]
