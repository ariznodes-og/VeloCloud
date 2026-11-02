# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SessionToken(Model):

    _attribute_map = {
        'access_id': {'key': 'accessId', 'type': 'str'},
        'alternate_token': {'key': 'alternateToken', 'type': 'str'},
        'authorization_id': {'key': 'authorizationId', 'type': 'str'},
        'claims': {'key': 'claims', 'type': '{str}'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'host_authorization_id': {'key': 'hostAuthorizationId', 'type': 'str'},
        'is_public': {'key': 'isPublic', 'type': 'bool'},
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'public_data': {'key': 'publicData', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'target_accounts': {'key': 'targetAccounts', 'type': '[str]'},
        'token': {'key': 'token', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'valid_from': {'key': 'validFrom', 'type': 'iso-8601'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'}
    }

    def __init__(self, access_id=None, alternate_token=None, authorization_id=None, claims=None, client_id=None, display_name=None, host_authorization_id=None, is_public=None, is_valid=None, public_data=None, scope=None, source=None, target_accounts=None, token=None, user_id=None, valid_from=None, valid_to=None):
        super(SessionToken, self).__init__()
        self.access_id = access_id
        self.alternate_token = alternate_token
        self.authorization_id = authorization_id
        self.claims = claims
        self.client_id = client_id
        self.display_name = display_name
        self.host_authorization_id = host_authorization_id
        self.is_public = is_public
        self.is_valid = is_valid
        self.public_data = public_data
        self.scope = scope
        self.source = source
        self.target_accounts = target_accounts
        self.token = token
        self.user_id = user_id
        self.valid_from = valid_from
        self.valid_to = valid_to


class TokenAdministrationRevocation(Model):

    _attribute_map = {
        'audience': {'key': 'audience', 'type': '[str]'},
        'authorization_ids': {'key': 'authorizationIds', 'type': '[str]'}
    }

    def __init__(self, audience=None, authorization_ids=None):
        super(TokenAdministrationRevocation, self).__init__()
        self.audience = audience
        self.authorization_ids = authorization_ids


class TokenAdminPagedSessionTokens(Model):

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'value': {'key': 'value', 'type': '[SessionToken]'}
    }

    def __init__(self, continuation_token=None, value=None):
        super(TokenAdminPagedSessionTokens, self).__init__()
        self.continuation_token = continuation_token
        self.value = value


class TokenAdminRevocation(Model):

    _attribute_map = {
        'authorization_id': {'key': 'authorizationId', 'type': 'str'}
    }

    def __init__(self, authorization_id=None):
        super(TokenAdminRevocation, self).__init__()
        self.authorization_id = authorization_id


__all__ = [
    'SessionToken',
    'TokenAdministrationRevocation',
    'TokenAdminPagedSessionTokens',
    'TokenAdminRevocation',
]
