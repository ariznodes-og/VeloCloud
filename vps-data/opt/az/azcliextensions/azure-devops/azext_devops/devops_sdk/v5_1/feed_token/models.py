# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class FeedSessionToken(Model):

    _attribute_map = {
        'token': {'key': 'token', 'type': 'str'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'}
    }

    def __init__(self, token=None, valid_to=None):
        super(FeedSessionToken, self).__init__()
        self.token = token
        self.valid_to = valid_to


__all__ = [
    'FeedSessionToken',
]
