# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class FeatureFlag(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'effective_state': {'key': 'effectiveState', 'type': 'str'},
        'explicit_state': {'key': 'explicitState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, description=None, effective_state=None, explicit_state=None, name=None, uri=None):
        super(FeatureFlag, self).__init__()
        self.description = description
        self.effective_state = effective_state
        self.explicit_state = explicit_state
        self.name = name
        self.uri = uri


class FeatureFlagPatch(Model):

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, state=None):
        super(FeatureFlagPatch, self).__init__()
        self.state = state


__all__ = [
    'FeatureFlag',
    'FeatureFlagPatch',
]
