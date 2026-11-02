# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AuditLogEntry(Model):

    _attribute_map = {
        'action_id': {'key': 'actionId', 'type': 'str'},
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'actor_cUID': {'key': 'actorCUID', 'type': 'str'},
        'actor_user_id': {'key': 'actorUserId', 'type': 'str'},
        'authentication_mechanism': {'key': 'authenticationMechanism', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'data': {'key': 'data', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'user_agent': {'key': 'userAgent', 'type': 'str'}
    }

    def __init__(self, action_id=None, activity_id=None, actor_cUID=None, actor_user_id=None, authentication_mechanism=None, correlation_id=None, data=None, id=None, ip_address=None, scope_id=None, scope_type=None, timestamp=None, user_agent=None):
        super(AuditLogEntry, self).__init__()
        self.action_id = action_id
        self.activity_id = activity_id
        self.actor_cUID = actor_cUID
        self.actor_user_id = actor_user_id
        self.authentication_mechanism = authentication_mechanism
        self.correlation_id = correlation_id
        self.data = data
        self.id = id
        self.ip_address = ip_address
        self.scope_id = scope_id
        self.scope_type = scope_type
        self.timestamp = timestamp
        self.user_agent = user_agent


class AuditLogQueryResult(Model):

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'decorated_audit_log_entries': {'key': 'decoratedAuditLogEntries', 'type': '[DecoratedAuditLogEntry]'},
        'has_more': {'key': 'hasMore', 'type': 'bool'}
    }

    def __init__(self, continuation_token=None, decorated_audit_log_entries=None, has_more=None):
        super(AuditLogQueryResult, self).__init__()
        self.continuation_token = continuation_token
        self.decorated_audit_log_entries = decorated_audit_log_entries
        self.has_more = has_more


class DecoratedAuditLogEntry(Model):

    _attribute_map = {
        'action_id': {'key': 'actionId', 'type': 'str'},
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'actor_cUID': {'key': 'actorCUID', 'type': 'str'},
        'actor_display_name': {'key': 'actorDisplayName', 'type': 'str'},
        'actor_image_url': {'key': 'actorImageUrl', 'type': 'str'},
        'actor_user_id': {'key': 'actorUserId', 'type': 'str'},
        'area': {'key': 'area', 'type': 'str'},
        'authentication_mechanism': {'key': 'authenticationMechanism', 'type': 'str'},
        'category': {'key': 'category', 'type': 'object'},
        'category_display_name': {'key': 'categoryDisplayName', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'data': {'key': 'data', 'type': '{object}'},
        'details': {'key': 'details', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'scope_display_name': {'key': 'scopeDisplayName', 'type': 'str'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'user_agent': {'key': 'userAgent', 'type': 'str'}
    }

    def __init__(self, action_id=None, activity_id=None, actor_cUID=None, actor_display_name=None, actor_image_url=None, actor_user_id=None, area=None, authentication_mechanism=None, category=None, category_display_name=None, correlation_id=None, data=None, details=None, id=None, ip_address=None, scope_display_name=None, scope_id=None, scope_type=None, timestamp=None, user_agent=None):
        super(DecoratedAuditLogEntry, self).__init__()
        self.action_id = action_id
        self.activity_id = activity_id
        self.actor_cUID = actor_cUID
        self.actor_display_name = actor_display_name
        self.actor_image_url = actor_image_url
        self.actor_user_id = actor_user_id
        self.area = area
        self.authentication_mechanism = authentication_mechanism
        self.category = category
        self.category_display_name = category_display_name
        self.correlation_id = correlation_id
        self.data = data
        self.details = details
        self.id = id
        self.ip_address = ip_address
        self.scope_display_name = scope_display_name
        self.scope_id = scope_id
        self.scope_type = scope_type
        self.timestamp = timestamp
        self.user_agent = user_agent


__all__ = [
    'AuditLogEntry',
    'AuditLogQueryResult',
    'DecoratedAuditLogEntry',
]
