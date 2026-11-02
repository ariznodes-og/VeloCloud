# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ClientTraceEvent(Model):

    _attribute_map = {
        'area': {'key': 'area', 'type': 'str'},
        'component': {'key': 'component', 'type': 'str'},
        'exception_type': {'key': 'exceptionType', 'type': 'str'},
        'feature': {'key': 'feature', 'type': 'str'},
        'level': {'key': 'level', 'type': 'object'},
        'message': {'key': 'message', 'type': 'str'},
        'method': {'key': 'method', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, area=None, component=None, exception_type=None, feature=None, level=None, message=None, method=None, properties=None):
        super(ClientTraceEvent, self).__init__()
        self.area = area
        self.component = component
        self.exception_type = exception_type
        self.feature = feature
        self.level = level
        self.message = message
        self.method = method
        self.properties = properties


__all__ = [
    'ClientTraceEvent',
]
