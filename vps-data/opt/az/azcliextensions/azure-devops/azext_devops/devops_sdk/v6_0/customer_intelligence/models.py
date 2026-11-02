# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CustomerIntelligenceEvent(Model):

    _attribute_map = {
        'area': {'key': 'area', 'type': 'str'},
        'feature': {'key': 'feature', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, area=None, feature=None, properties=None):
        super(CustomerIntelligenceEvent, self).__init__()
        self.area = area
        self.feature = feature
        self.properties = properties


__all__ = [
    'CustomerIntelligenceEvent',
]
