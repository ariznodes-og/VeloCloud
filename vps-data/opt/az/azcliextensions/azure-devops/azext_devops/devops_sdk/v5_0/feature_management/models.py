# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ContributedFeature(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'default_state': {'key': 'defaultState', 'type': 'bool'},
        'default_value_rules': {'key': 'defaultValueRules', 'type': '[ContributedFeatureValueRule]'},
        'description': {'key': 'description', 'type': 'str'},
        'feature_properties': {'key': 'featureProperties', 'type': '{object}'},
        'feature_state_changed_listeners': {'key': 'featureStateChangedListeners', 'type': '[ContributedFeatureListener]'},
        'id': {'key': 'id', 'type': 'str'},
        'include_as_claim': {'key': 'includeAsClaim', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'override_rules': {'key': 'overrideRules', 'type': '[ContributedFeatureValueRule]'},
        'scopes': {'key': 'scopes', 'type': '[ContributedFeatureSettingScope]'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, _links=None, default_state=None, default_value_rules=None, description=None, feature_properties=None, feature_state_changed_listeners=None, id=None, include_as_claim=None, name=None, order=None, override_rules=None, scopes=None, service_instance_type=None, tags=None):
        super(ContributedFeature, self).__init__()
        self._links = _links
        self.default_state = default_state
        self.default_value_rules = default_value_rules
        self.description = description
        self.feature_properties = feature_properties
        self.feature_state_changed_listeners = feature_state_changed_listeners
        self.id = id
        self.include_as_claim = include_as_claim
        self.name = name
        self.order = order
        self.override_rules = override_rules
        self.scopes = scopes
        self.service_instance_type = service_instance_type
        self.tags = tags


class ContributedFeatureHandlerSettings(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, name=None, properties=None):
        super(ContributedFeatureHandlerSettings, self).__init__()
        self.name = name
        self.properties = properties


class ContributedFeatureListener(ContributedFeatureHandlerSettings):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
    }

    def __init__(self, name=None, properties=None):
        super(ContributedFeatureListener, self).__init__(name=name, properties=properties)


class ContributedFeatureSettingScope(Model):

    _attribute_map = {
        'setting_scope': {'key': 'settingScope', 'type': 'str'},
        'user_scoped': {'key': 'userScoped', 'type': 'bool'}
    }

    def __init__(self, setting_scope=None, user_scoped=None):
        super(ContributedFeatureSettingScope, self).__init__()
        self.setting_scope = setting_scope
        self.user_scoped = user_scoped


class ContributedFeatureState(Model):

    _attribute_map = {
        'feature_id': {'key': 'featureId', 'type': 'str'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'ContributedFeatureSettingScope'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, feature_id=None, overridden=None, reason=None, scope=None, state=None):
        super(ContributedFeatureState, self).__init__()
        self.feature_id = feature_id
        self.overridden = overridden
        self.reason = reason
        self.scope = scope
        self.state = state


class ContributedFeatureStateQuery(Model):

    _attribute_map = {
        'feature_ids': {'key': 'featureIds', 'type': '[str]'},
        'feature_states': {'key': 'featureStates', 'type': '{ContributedFeatureState}'},
        'scope_values': {'key': 'scopeValues', 'type': '{str}'}
    }

    def __init__(self, feature_ids=None, feature_states=None, scope_values=None):
        super(ContributedFeatureStateQuery, self).__init__()
        self.feature_ids = feature_ids
        self.feature_states = feature_states
        self.scope_values = scope_values


class ContributedFeatureValueRule(ContributedFeatureHandlerSettings):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
    }

    def __init__(self, name=None, properties=None):
        super(ContributedFeatureValueRule, self).__init__(name=name, properties=properties)


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


__all__ = [
    'ContributedFeature',
    'ContributedFeatureHandlerSettings',
    'ContributedFeatureListener',
    'ContributedFeatureSettingScope',
    'ContributedFeatureState',
    'ContributedFeatureStateQuery',
    'ContributedFeatureValueRule',
    'ReferenceLinks',
]
