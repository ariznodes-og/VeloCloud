# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SessionRequest(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': '{str}'},
        'feed': {'key': 'feed', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'}
    }

    def __init__(self, data=None, feed=None, source=None):
        super(SessionRequest, self).__init__()
        self.data = data
        self.feed = feed
        self.source = source


class SessionResponse(Model):

    _attribute_map = {
        'session_id': {'key': 'sessionId', 'type': 'str'},
        'session_name': {'key': 'sessionName', 'type': 'str'}
    }

    def __init__(self, session_id=None, session_name=None):
        super(SessionResponse, self).__init__()
        self.session_id = session_id
        self.session_name = session_name


__all__ = [
    'SessionRequest',
    'SessionResponse',
]
