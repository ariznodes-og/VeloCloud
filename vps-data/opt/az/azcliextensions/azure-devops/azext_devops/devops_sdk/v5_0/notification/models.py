# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BaseSubscriptionFilter(Model):

    _attribute_map = {
        'event_type': {'key': 'eventType', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, event_type=None, type=None):
        super(BaseSubscriptionFilter, self).__init__()
        self.event_type = event_type
        self.type = type


class BatchNotificationOperation(Model):

    _attribute_map = {
        'notification_operation': {'key': 'notificationOperation', 'type': 'object'},
        'notification_query_conditions': {'key': 'notificationQueryConditions', 'type': '[NotificationQueryCondition]'}
    }

    def __init__(self, notification_operation=None, notification_query_conditions=None):
        super(BatchNotificationOperation, self).__init__()
        self.notification_operation = notification_operation
        self.notification_query_conditions = notification_query_conditions


class EventActor(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'role': {'key': 'role', 'type': 'str'}
    }

    def __init__(self, id=None, role=None):
        super(EventActor, self).__init__()
        self.id = id
        self.role = role


class EventScope(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(EventScope, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class EventsEvaluationResult(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'matched_count': {'key': 'matchedCount', 'type': 'int'}
    }

    def __init__(self, count=None, matched_count=None):
        super(EventsEvaluationResult, self).__init__()
        self.count = count
        self.matched_count = matched_count


class EventTransformRequest(Model):

    _attribute_map = {
        'event_payload': {'key': 'eventPayload', 'type': 'str'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'system_inputs': {'key': 'systemInputs', 'type': '{str}'}
    }

    def __init__(self, event_payload=None, event_type=None, system_inputs=None):
        super(EventTransformRequest, self).__init__()
        self.event_payload = event_payload
        self.event_type = event_type
        self.system_inputs = system_inputs


class EventTransformResult(Model):

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'system_inputs': {'key': 'systemInputs', 'type': '{str}'}
    }

    def __init__(self, content=None, data=None, system_inputs=None):
        super(EventTransformResult, self).__init__()
        self.content = content
        self.data = data
        self.system_inputs = system_inputs


class ExpressionFilterClause(Model):

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'index': {'key': 'index', 'type': 'int'},
        'logical_operator': {'key': 'logicalOperator', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, field_name=None, index=None, logical_operator=None, operator=None, value=None):
        super(ExpressionFilterClause, self).__init__()
        self.field_name = field_name
        self.index = index
        self.logical_operator = logical_operator
        self.operator = operator
        self.value = value


class ExpressionFilterGroup(Model):

    _attribute_map = {
        'end': {'key': 'end', 'type': 'int'},
        'level': {'key': 'level', 'type': 'int'},
        'start': {'key': 'start', 'type': 'int'}
    }

    def __init__(self, end=None, level=None, start=None):
        super(ExpressionFilterGroup, self).__init__()
        self.end = end
        self.level = level
        self.start = start


class ExpressionFilterModel(Model):

    _attribute_map = {
        'clauses': {'key': 'clauses', 'type': '[ExpressionFilterClause]'},
        'groups': {'key': 'groups', 'type': '[ExpressionFilterGroup]'},
        'max_group_level': {'key': 'maxGroupLevel', 'type': 'int'}
    }

    def __init__(self, clauses=None, groups=None, max_group_level=None):
        super(ExpressionFilterModel, self).__init__()
        self.clauses = clauses
        self.groups = groups
        self.max_group_level = max_group_level


class GraphSubjectBase(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class IdentityRef(GraphSubjectBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


class INotificationDiagnosticLog(Model):

    _attribute_map = {
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'log_type': {'key': 'logType', 'type': 'str'},
        'messages': {'key': 'messages', 'type': '[NotificationDiagnosticLogMessage]'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'source': {'key': 'source', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'}
    }

    def __init__(self, activity_id=None, description=None, end_time=None, id=None, log_type=None, messages=None, properties=None, source=None, start_time=None):
        super(INotificationDiagnosticLog, self).__init__()
        self.activity_id = activity_id
        self.description = description
        self.end_time = end_time
        self.id = id
        self.log_type = log_type
        self.messages = messages
        self.properties = properties
        self.source = source
        self.start_time = start_time


class InputValue(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': '{object}'},
        'display_value': {'key': 'displayValue', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, data=None, display_value=None, value=None):
        super(InputValue, self).__init__()
        self.data = data
        self.display_value = display_value
        self.value = value


class InputValues(Model):

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'error': {'key': 'error', 'type': 'InputValuesError'},
        'input_id': {'key': 'inputId', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'is_limited_to_possible_values': {'key': 'isLimitedToPossibleValues', 'type': 'bool'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'possible_values': {'key': 'possibleValues', 'type': '[InputValue]'}
    }

    def __init__(self, default_value=None, error=None, input_id=None, is_disabled=None, is_limited_to_possible_values=None, is_read_only=None, possible_values=None):
        super(InputValues, self).__init__()
        self.default_value = default_value
        self.error = error
        self.input_id = input_id
        self.is_disabled = is_disabled
        self.is_limited_to_possible_values = is_limited_to_possible_values
        self.is_read_only = is_read_only
        self.possible_values = possible_values


class InputValuesError(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, message=None):
        super(InputValuesError, self).__init__()
        self.message = message


class InputValuesQuery(Model):

    _attribute_map = {
        'current_values': {'key': 'currentValues', 'type': '{str}'},
        'input_values': {'key': 'inputValues', 'type': '[InputValues]'},
        'resource': {'key': 'resource', 'type': 'object'}
    }

    def __init__(self, current_values=None, input_values=None, resource=None):
        super(InputValuesQuery, self).__init__()
        self.current_values = current_values
        self.input_values = input_values
        self.resource = resource


class ISubscriptionChannel(Model):

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, type=None):
        super(ISubscriptionChannel, self).__init__()
        self.type = type


class ISubscriptionFilter(Model):

    _attribute_map = {
        'event_type': {'key': 'eventType', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, event_type=None, type=None):
        super(ISubscriptionFilter, self).__init__()
        self.event_type = event_type
        self.type = type


class NotificationAdminSettings(Model):

    _attribute_map = {
        'default_group_delivery_preference': {'key': 'defaultGroupDeliveryPreference', 'type': 'object'}
    }

    def __init__(self, default_group_delivery_preference=None):
        super(NotificationAdminSettings, self).__init__()
        self.default_group_delivery_preference = default_group_delivery_preference


class NotificationAdminSettingsUpdateParameters(Model):

    _attribute_map = {
        'default_group_delivery_preference': {'key': 'defaultGroupDeliveryPreference', 'type': 'object'}
    }

    def __init__(self, default_group_delivery_preference=None):
        super(NotificationAdminSettingsUpdateParameters, self).__init__()
        self.default_group_delivery_preference = default_group_delivery_preference


class NotificationDiagnosticLogMessage(Model):

    _attribute_map = {
        'level': {'key': 'level', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'time': {'key': 'time', 'type': 'object'}
    }

    def __init__(self, level=None, message=None, time=None):
        super(NotificationDiagnosticLogMessage, self).__init__()
        self.level = level
        self.message = message
        self.time = time


class NotificationEventField(Model):

    _attribute_map = {
        'field_type': {'key': 'fieldType', 'type': 'NotificationEventFieldType'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[str]'}
    }

    def __init__(self, field_type=None, id=None, name=None, path=None, supported_scopes=None):
        super(NotificationEventField, self).__init__()
        self.field_type = field_type
        self.id = id
        self.name = name
        self.path = path
        self.supported_scopes = supported_scopes


class NotificationEventFieldOperator(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None):
        super(NotificationEventFieldOperator, self).__init__()
        self.display_name = display_name
        self.id = id


class NotificationEventFieldType(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'operator_constraints': {'key': 'operatorConstraints', 'type': '[OperatorConstraint]'},
        'operators': {'key': 'operators', 'type': '[NotificationEventFieldOperator]'},
        'subscription_field_type': {'key': 'subscriptionFieldType', 'type': 'object'},
        'value': {'key': 'value', 'type': 'ValueDefinition'}
    }

    def __init__(self, id=None, operator_constraints=None, operators=None, subscription_field_type=None, value=None):
        super(NotificationEventFieldType, self).__init__()
        self.id = id
        self.operator_constraints = operator_constraints
        self.operators = operators
        self.subscription_field_type = subscription_field_type
        self.value = value


class NotificationEventPublisher(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_management_info': {'key': 'subscriptionManagementInfo', 'type': 'SubscriptionManagement'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, subscription_management_info=None, url=None):
        super(NotificationEventPublisher, self).__init__()
        self.id = id
        self.subscription_management_info = subscription_management_info
        self.url = url


class NotificationEventRole(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'supports_groups': {'key': 'supportsGroups', 'type': 'bool'}
    }

    def __init__(self, id=None, name=None, supports_groups=None):
        super(NotificationEventRole, self).__init__()
        self.id = id
        self.name = name
        self.supports_groups = supports_groups


class NotificationEventType(Model):

    _attribute_map = {
        'category': {'key': 'category', 'type': 'NotificationEventTypeCategory'},
        'color': {'key': 'color', 'type': 'str'},
        'custom_subscriptions_allowed': {'key': 'customSubscriptionsAllowed', 'type': 'bool'},
        'event_publisher': {'key': 'eventPublisher', 'type': 'NotificationEventPublisher'},
        'fields': {'key': 'fields', 'type': '{NotificationEventField}'},
        'has_initiator': {'key': 'hasInitiator', 'type': 'bool'},
        'icon': {'key': 'icon', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[NotificationEventRole]'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, category=None, color=None, custom_subscriptions_allowed=None, event_publisher=None, fields=None, has_initiator=None, icon=None, id=None, name=None, roles=None, supported_scopes=None, url=None):
        super(NotificationEventType, self).__init__()
        self.category = category
        self.color = color
        self.custom_subscriptions_allowed = custom_subscriptions_allowed
        self.event_publisher = event_publisher
        self.fields = fields
        self.has_initiator = has_initiator
        self.icon = icon
        self.id = id
        self.name = name
        self.roles = roles
        self.supported_scopes = supported_scopes
        self.url = url


class NotificationEventTypeCategory(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(NotificationEventTypeCategory, self).__init__()
        self.id = id
        self.name = name


class NotificationQueryCondition(Model):

    _attribute_map = {
        'event_initiator': {'key': 'eventInitiator', 'type': 'str'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'subscriber': {'key': 'subscriber', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'}
    }

    def __init__(self, event_initiator=None, event_type=None, subscriber=None, subscription_id=None):
        super(NotificationQueryCondition, self).__init__()
        self.event_initiator = event_initiator
        self.event_type = event_type
        self.subscriber = subscriber
        self.subscription_id = subscription_id


class NotificationReason(Model):

    _attribute_map = {
        'notification_reason_type': {'key': 'notificationReasonType', 'type': 'object'},
        'target_identities': {'key': 'targetIdentities', 'type': '[IdentityRef]'}
    }

    def __init__(self, notification_reason_type=None, target_identities=None):
        super(NotificationReason, self).__init__()
        self.notification_reason_type = notification_reason_type
        self.target_identities = target_identities


class NotificationsEvaluationResult(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'}
    }

    def __init__(self, count=None):
        super(NotificationsEvaluationResult, self).__init__()
        self.count = count


class NotificationStatistic(Model):

    _attribute_map = {
        'date': {'key': 'date', 'type': 'iso-8601'},
        'hit_count': {'key': 'hitCount', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'user': {'key': 'user', 'type': 'IdentityRef'}
    }

    def __init__(self, date=None, hit_count=None, path=None, type=None, user=None):
        super(NotificationStatistic, self).__init__()
        self.date = date
        self.hit_count = hit_count
        self.path = path
        self.type = type
        self.user = user


class NotificationStatisticsQuery(Model):

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[NotificationStatisticsQueryConditions]'}
    }

    def __init__(self, conditions=None):
        super(NotificationStatisticsQuery, self).__init__()
        self.conditions = conditions


class NotificationStatisticsQueryConditions(Model):

    _attribute_map = {
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'hit_count_minimum': {'key': 'hitCountMinimum', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'object'},
        'user': {'key': 'user', 'type': 'IdentityRef'}
    }

    def __init__(self, end_date=None, hit_count_minimum=None, path=None, start_date=None, type=None, user=None):
        super(NotificationStatisticsQueryConditions, self).__init__()
        self.end_date = end_date
        self.hit_count_minimum = hit_count_minimum
        self.path = path
        self.start_date = start_date
        self.type = type
        self.user = user


class NotificationSubscriber(Model):

    _attribute_map = {
        'delivery_preference': {'key': 'deliveryPreference', 'type': 'object'},
        'flags': {'key': 'flags', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'preferred_email_address': {'key': 'preferredEmailAddress', 'type': 'str'}
    }

    def __init__(self, delivery_preference=None, flags=None, id=None, preferred_email_address=None):
        super(NotificationSubscriber, self).__init__()
        self.delivery_preference = delivery_preference
        self.flags = flags
        self.id = id
        self.preferred_email_address = preferred_email_address


class NotificationSubscriberUpdateParameters(Model):

    _attribute_map = {
        'delivery_preference': {'key': 'deliveryPreference', 'type': 'object'},
        'preferred_email_address': {'key': 'preferredEmailAddress', 'type': 'str'}
    }

    def __init__(self, delivery_preference=None, preferred_email_address=None):
        super(NotificationSubscriberUpdateParameters, self).__init__()
        self.delivery_preference = delivery_preference
        self.preferred_email_address = preferred_email_address


class NotificationSubscription(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'admin_settings': {'key': 'adminSettings', 'type': 'SubscriptionAdminSettings'},
        'channel': {'key': 'channel', 'type': 'ISubscriptionChannel'},
        'description': {'key': 'description', 'type': 'str'},
        'diagnostics': {'key': 'diagnostics', 'type': 'SubscriptionDiagnostics'},
        'extended_properties': {'key': 'extendedProperties', 'type': '{str}'},
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'flags': {'key': 'flags', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'permissions': {'key': 'permissions', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'SubscriptionScope'},
        'status': {'key': 'status', 'type': 'object'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
        'subscriber': {'key': 'subscriber', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'user_settings': {'key': 'userSettings', 'type': 'SubscriptionUserSettings'}
    }

    def __init__(self, _links=None, admin_settings=None, channel=None, description=None, diagnostics=None, extended_properties=None, filter=None, flags=None, id=None, last_modified_by=None, modified_date=None, permissions=None, scope=None, status=None, status_message=None, subscriber=None, url=None, user_settings=None):
        super(NotificationSubscription, self).__init__()
        self._links = _links
        self.admin_settings = admin_settings
        self.channel = channel
        self.description = description
        self.diagnostics = diagnostics
        self.extended_properties = extended_properties
        self.filter = filter
        self.flags = flags
        self.id = id
        self.last_modified_by = last_modified_by
        self.modified_date = modified_date
        self.permissions = permissions
        self.scope = scope
        self.status = status
        self.status_message = status_message
        self.subscriber = subscriber
        self.url = url
        self.user_settings = user_settings


class NotificationSubscriptionCreateParameters(Model):

    _attribute_map = {
        'channel': {'key': 'channel', 'type': 'ISubscriptionChannel'},
        'description': {'key': 'description', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'scope': {'key': 'scope', 'type': 'SubscriptionScope'},
        'subscriber': {'key': 'subscriber', 'type': 'IdentityRef'}
    }

    def __init__(self, channel=None, description=None, filter=None, scope=None, subscriber=None):
        super(NotificationSubscriptionCreateParameters, self).__init__()
        self.channel = channel
        self.description = description
        self.filter = filter
        self.scope = scope
        self.subscriber = subscriber


class NotificationSubscriptionTemplate(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'id': {'key': 'id', 'type': 'str'},
        'notification_event_information': {'key': 'notificationEventInformation', 'type': 'NotificationEventType'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, filter=None, id=None, notification_event_information=None, type=None):
        super(NotificationSubscriptionTemplate, self).__init__()
        self.description = description
        self.filter = filter
        self.id = id
        self.notification_event_information = notification_event_information
        self.type = type


class NotificationSubscriptionUpdateParameters(Model):

    _attribute_map = {
        'admin_settings': {'key': 'adminSettings', 'type': 'SubscriptionAdminSettings'},
        'channel': {'key': 'channel', 'type': 'ISubscriptionChannel'},
        'description': {'key': 'description', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'scope': {'key': 'scope', 'type': 'SubscriptionScope'},
        'status': {'key': 'status', 'type': 'object'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
        'user_settings': {'key': 'userSettings', 'type': 'SubscriptionUserSettings'}
    }

    def __init__(self, admin_settings=None, channel=None, description=None, filter=None, scope=None, status=None, status_message=None, user_settings=None):
        super(NotificationSubscriptionUpdateParameters, self).__init__()
        self.admin_settings = admin_settings
        self.channel = channel
        self.description = description
        self.filter = filter
        self.scope = scope
        self.status = status
        self.status_message = status_message
        self.user_settings = user_settings


class OperatorConstraint(Model):

    _attribute_map = {
        'operator': {'key': 'operator', 'type': 'str'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[str]'}
    }

    def __init__(self, operator=None, supported_scopes=None):
        super(OperatorConstraint, self).__init__()
        self.operator = operator
        self.supported_scopes = supported_scopes


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class SubscriptionAdminSettings(Model):

    _attribute_map = {
        'block_user_opt_out': {'key': 'blockUserOptOut', 'type': 'bool'}
    }

    def __init__(self, block_user_opt_out=None):
        super(SubscriptionAdminSettings, self).__init__()
        self.block_user_opt_out = block_user_opt_out


class SubscriptionChannelWithAddress(Model):

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'use_custom_address': {'key': 'useCustomAddress', 'type': 'bool'}
    }

    def __init__(self, address=None, type=None, use_custom_address=None):
        super(SubscriptionChannelWithAddress, self).__init__()
        self.address = address
        self.type = type
        self.use_custom_address = use_custom_address


class SubscriptionDiagnostics(Model):

    _attribute_map = {
        'delivery_results': {'key': 'deliveryResults', 'type': 'SubscriptionTracing'},
        'delivery_tracing': {'key': 'deliveryTracing', 'type': 'SubscriptionTracing'},
        'evaluation_tracing': {'key': 'evaluationTracing', 'type': 'SubscriptionTracing'}
    }

    def __init__(self, delivery_results=None, delivery_tracing=None, evaluation_tracing=None):
        super(SubscriptionDiagnostics, self).__init__()
        self.delivery_results = delivery_results
        self.delivery_tracing = delivery_tracing
        self.evaluation_tracing = evaluation_tracing


class SubscriptionEvaluationRequest(Model):

    _attribute_map = {
        'min_events_created_date': {'key': 'minEventsCreatedDate', 'type': 'iso-8601'},
        'subscription_create_parameters': {'key': 'subscriptionCreateParameters', 'type': 'NotificationSubscriptionCreateParameters'}
    }

    def __init__(self, min_events_created_date=None, subscription_create_parameters=None):
        super(SubscriptionEvaluationRequest, self).__init__()
        self.min_events_created_date = min_events_created_date
        self.subscription_create_parameters = subscription_create_parameters


class SubscriptionEvaluationResult(Model):

    _attribute_map = {
        'evaluation_job_status': {'key': 'evaluationJobStatus', 'type': 'object'},
        'events': {'key': 'events', 'type': 'EventsEvaluationResult'},
        'id': {'key': 'id', 'type': 'str'},
        'notifications': {'key': 'notifications', 'type': 'NotificationsEvaluationResult'}
    }

    def __init__(self, evaluation_job_status=None, events=None, id=None, notifications=None):
        super(SubscriptionEvaluationResult, self).__init__()
        self.evaluation_job_status = evaluation_job_status
        self.events = events
        self.id = id
        self.notifications = notifications


class SubscriptionEvaluationSettings(Model):

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'interval': {'key': 'interval', 'type': 'int'},
        'threshold': {'key': 'threshold', 'type': 'int'},
        'time_out': {'key': 'timeOut', 'type': 'int'}
    }

    def __init__(self, enabled=None, interval=None, threshold=None, time_out=None):
        super(SubscriptionEvaluationSettings, self).__init__()
        self.enabled = enabled
        self.interval = interval
        self.threshold = threshold
        self.time_out = time_out


class SubscriptionManagement(Model):

    _attribute_map = {
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, service_instance_type=None, url=None):
        super(SubscriptionManagement, self).__init__()
        self.service_instance_type = service_instance_type
        self.url = url


class SubscriptionQuery(Model):

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[SubscriptionQueryCondition]'},
        'query_flags': {'key': 'queryFlags', 'type': 'object'}
    }

    def __init__(self, conditions=None, query_flags=None):
        super(SubscriptionQuery, self).__init__()
        self.conditions = conditions
        self.query_flags = query_flags


class SubscriptionQueryCondition(Model):

    _attribute_map = {
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'flags': {'key': 'flags', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'str'},
        'subscriber_id': {'key': 'subscriberId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'}
    }

    def __init__(self, filter=None, flags=None, scope=None, subscriber_id=None, subscription_id=None):
        super(SubscriptionQueryCondition, self).__init__()
        self.filter = filter
        self.flags = flags
        self.scope = scope
        self.subscriber_id = subscriber_id
        self.subscription_id = subscription_id


class SubscriptionScope(EventScope):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, type=None):
        super(SubscriptionScope, self).__init__(id=id, name=name, type=type)


class SubscriptionTracing(Model):

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'max_traced_entries': {'key': 'maxTracedEntries', 'type': 'int'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'traced_entries': {'key': 'tracedEntries', 'type': 'int'}
    }

    def __init__(self, enabled=None, end_date=None, max_traced_entries=None, start_date=None, traced_entries=None):
        super(SubscriptionTracing, self).__init__()
        self.enabled = enabled
        self.end_date = end_date
        self.max_traced_entries = max_traced_entries
        self.start_date = start_date
        self.traced_entries = traced_entries


class SubscriptionUserSettings(Model):

    _attribute_map = {
        'opted_out': {'key': 'optedOut', 'type': 'bool'}
    }

    def __init__(self, opted_out=None):
        super(SubscriptionUserSettings, self).__init__()
        self.opted_out = opted_out


class UpdateSubscripitonDiagnosticsParameters(Model):

    _attribute_map = {
        'delivery_results': {'key': 'deliveryResults', 'type': 'UpdateSubscripitonTracingParameters'},
        'delivery_tracing': {'key': 'deliveryTracing', 'type': 'UpdateSubscripitonTracingParameters'},
        'evaluation_tracing': {'key': 'evaluationTracing', 'type': 'UpdateSubscripitonTracingParameters'}
    }

    def __init__(self, delivery_results=None, delivery_tracing=None, evaluation_tracing=None):
        super(UpdateSubscripitonDiagnosticsParameters, self).__init__()
        self.delivery_results = delivery_results
        self.delivery_tracing = delivery_tracing
        self.evaluation_tracing = evaluation_tracing


class UpdateSubscripitonTracingParameters(Model):

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'}
    }

    def __init__(self, enabled=None):
        super(UpdateSubscripitonTracingParameters, self).__init__()
        self.enabled = enabled


class ValueDefinition(Model):

    _attribute_map = {
        'data_source': {'key': 'dataSource', 'type': '[InputValue]'},
        'end_point': {'key': 'endPoint', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'}
    }

    def __init__(self, data_source=None, end_point=None, result_template=None):
        super(ValueDefinition, self).__init__()
        self.data_source = data_source
        self.end_point = end_point
        self.result_template = result_template


class VssNotificationEvent(Model):

    _attribute_map = {
        'actors': {'key': 'actors', 'type': '[EventActor]'},
        'artifact_uris': {'key': 'artifactUris', 'type': '[str]'},
        'data': {'key': 'data', 'type': 'object'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'expires_in': {'key': 'expiresIn', 'type': 'object'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'process_delay': {'key': 'processDelay', 'type': 'object'},
        'scopes': {'key': 'scopes', 'type': '[EventScope]'},
        'source_event_created_time': {'key': 'sourceEventCreatedTime', 'type': 'iso-8601'}
    }

    def __init__(self, actors=None, artifact_uris=None, data=None, event_type=None, expires_in=None, item_id=None, process_delay=None, scopes=None, source_event_created_time=None):
        super(VssNotificationEvent, self).__init__()
        self.actors = actors
        self.artifact_uris = artifact_uris
        self.data = data
        self.event_type = event_type
        self.expires_in = expires_in
        self.item_id = item_id
        self.process_delay = process_delay
        self.scopes = scopes
        self.source_event_created_time = source_event_created_time


class ArtifactFilter(BaseSubscriptionFilter):

    _attribute_map = {
        'event_type': {'key': 'eventType', 'type': 'str'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'artifact_type': {'key': 'artifactType', 'type': 'str'},
        'artifact_uri': {'key': 'artifactUri', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, event_type=None, artifact_id=None, artifact_type=None, artifact_uri=None, type=None):
        super(ArtifactFilter, self).__init__(event_type=event_type)
        self.artifact_id = artifact_id
        self.artifact_type = artifact_type
        self.artifact_uri = artifact_uri
        self.type = type


class FieldInputValues(InputValues):

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'error': {'key': 'error', 'type': 'InputValuesError'},
        'input_id': {'key': 'inputId', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'is_limited_to_possible_values': {'key': 'isLimitedToPossibleValues', 'type': 'bool'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'possible_values': {'key': 'possibleValues', 'type': '[InputValue]'},
        'operators': {'key': 'operators', 'type': 'str'}
    }

    def __init__(self, default_value=None, error=None, input_id=None, is_disabled=None, is_limited_to_possible_values=None, is_read_only=None, possible_values=None, operators=None):
        super(FieldInputValues, self).__init__(default_value=default_value, error=error, input_id=input_id, is_disabled=is_disabled, is_limited_to_possible_values=is_limited_to_possible_values, is_read_only=is_read_only, possible_values=possible_values)
        self.operators = operators


class FieldValuesQuery(InputValuesQuery):

    _attribute_map = {
        'current_values': {'key': 'currentValues', 'type': '{str}'},
        'resource': {'key': 'resource', 'type': 'object'},
        'input_values': {'key': 'inputValues', 'type': '[FieldInputValues]'},
        'scope': {'key': 'scope', 'type': 'str'}
    }

    def __init__(self, current_values=None, resource=None, input_values=None, scope=None):
        super(FieldValuesQuery, self).__init__(current_values=current_values, resource=resource)
        self.input_values = input_values
        self.scope = scope


__all__ = [
    'BaseSubscriptionFilter',
    'BatchNotificationOperation',
    'EventActor',
    'EventScope',
    'EventsEvaluationResult',
    'EventTransformRequest',
    'EventTransformResult',
    'ExpressionFilterClause',
    'ExpressionFilterGroup',
    'ExpressionFilterModel',
    'GraphSubjectBase',
    'IdentityRef',
    'INotificationDiagnosticLog',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'InputValuesQuery',
    'ISubscriptionChannel',
    'ISubscriptionFilter',
    'NotificationAdminSettings',
    'NotificationAdminSettingsUpdateParameters',
    'NotificationDiagnosticLogMessage',
    'NotificationEventField',
    'NotificationEventFieldOperator',
    'NotificationEventFieldType',
    'NotificationEventPublisher',
    'NotificationEventRole',
    'NotificationEventType',
    'NotificationEventTypeCategory',
    'NotificationQueryCondition',
    'NotificationReason',
    'NotificationsEvaluationResult',
    'NotificationStatistic',
    'NotificationStatisticsQuery',
    'NotificationStatisticsQueryConditions',
    'NotificationSubscriber',
    'NotificationSubscriberUpdateParameters',
    'NotificationSubscription',
    'NotificationSubscriptionCreateParameters',
    'NotificationSubscriptionTemplate',
    'NotificationSubscriptionUpdateParameters',
    'OperatorConstraint',
    'ReferenceLinks',
    'SubscriptionAdminSettings',
    'SubscriptionChannelWithAddress',
    'SubscriptionDiagnostics',
    'SubscriptionEvaluationRequest',
    'SubscriptionEvaluationResult',
    'SubscriptionEvaluationSettings',
    'SubscriptionManagement',
    'SubscriptionQuery',
    'SubscriptionQueryCondition',
    'SubscriptionScope',
    'SubscriptionTracing',
    'SubscriptionUserSettings',
    'UpdateSubscripitonDiagnosticsParameters',
    'UpdateSubscripitonTracingParameters',
    'ValueDefinition',
    'VssNotificationEvent',
    'ArtifactFilter',
    'FieldInputValues',
    'FieldValuesQuery',
]
