# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Consumer(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'actions': {'key': 'actions', 'type': '[ConsumerAction]'},
        'authentication_type': {'key': 'authenticationType', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'external_configuration': {'key': 'externalConfiguration', 'type': 'ExternalConfigurationDescriptor'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'information_url': {'key': 'informationUrl', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, actions=None, authentication_type=None, description=None, external_configuration=None, id=None, image_url=None, information_url=None, input_descriptors=None, name=None, url=None):
        super(Consumer, self).__init__()
        self._links = _links
        self.actions = actions
        self.authentication_type = authentication_type
        self.description = description
        self.external_configuration = external_configuration
        self.id = id
        self.image_url = image_url
        self.information_url = information_url
        self.input_descriptors = input_descriptors
        self.name = name
        self.url = url


class ConsumerAction(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allow_resource_version_override': {'key': 'allowResourceVersionOverride', 'type': 'bool'},
        'consumer_id': {'key': 'consumerId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'supported_event_types': {'key': 'supportedEventTypes', 'type': '[str]'},
        'supported_resource_versions': {'key': 'supportedResourceVersions', 'type': '{[str]}'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, allow_resource_version_override=None, consumer_id=None, description=None, id=None, input_descriptors=None, name=None, supported_event_types=None, supported_resource_versions=None, url=None):
        super(ConsumerAction, self).__init__()
        self._links = _links
        self.allow_resource_version_override = allow_resource_version_override
        self.consumer_id = consumer_id
        self.description = description
        self.id = id
        self.input_descriptors = input_descriptors
        self.name = name
        self.supported_event_types = supported_event_types
        self.supported_resource_versions = supported_resource_versions
        self.url = url


class Event(Model):

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'detailed_message': {'key': 'detailedMessage', 'type': 'FormattedEventMessage'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'message': {'key': 'message', 'type': 'FormattedEventMessage'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'object'},
        'resource_containers': {'key': 'resourceContainers', 'type': '{ResourceContainer}'},
        'resource_version': {'key': 'resourceVersion', 'type': 'str'},
        'session_token': {'key': 'sessionToken', 'type': 'SessionToken'}
    }

    def __init__(self, created_date=None, detailed_message=None, event_type=None, id=None, message=None, publisher_id=None, resource=None, resource_containers=None, resource_version=None, session_token=None):
        super(Event, self).__init__()
        self.created_date = created_date
        self.detailed_message = detailed_message
        self.event_type = event_type
        self.id = id
        self.message = message
        self.publisher_id = publisher_id
        self.resource = resource
        self.resource_containers = resource_containers
        self.resource_version = resource_version
        self.session_token = session_token


class EventTypeDescriptor(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'supported_resource_versions': {'key': 'supportedResourceVersions', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, input_descriptors=None, name=None, publisher_id=None, supported_resource_versions=None, url=None):
        super(EventTypeDescriptor, self).__init__()
        self.description = description
        self.id = id
        self.input_descriptors = input_descriptors
        self.name = name
        self.publisher_id = publisher_id
        self.supported_resource_versions = supported_resource_versions
        self.url = url


class ExternalConfigurationDescriptor(Model):

    _attribute_map = {
        'create_subscription_url': {'key': 'createSubscriptionUrl', 'type': 'str'},
        'edit_subscription_property_name': {'key': 'editSubscriptionPropertyName', 'type': 'str'},
        'hosted_only': {'key': 'hostedOnly', 'type': 'bool'}
    }

    def __init__(self, create_subscription_url=None, edit_subscription_property_name=None, hosted_only=None):
        super(ExternalConfigurationDescriptor, self).__init__()
        self.create_subscription_url = create_subscription_url
        self.edit_subscription_property_name = edit_subscription_property_name
        self.hosted_only = hosted_only


class FormattedEventMessage(Model):

    _attribute_map = {
        'html': {'key': 'html', 'type': 'str'},
        'markdown': {'key': 'markdown', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, html=None, markdown=None, text=None):
        super(FormattedEventMessage, self).__init__()
        self.html = html
        self.markdown = markdown
        self.text = text


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


class InputDescriptor(Model):

    _attribute_map = {
        'dependency_input_ids': {'key': 'dependencyInputIds', 'type': '[str]'},
        'description': {'key': 'description', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'has_dynamic_value_information': {'key': 'hasDynamicValueInformation', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'input_mode': {'key': 'inputMode', 'type': 'object'},
        'is_confidential': {'key': 'isConfidential', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'use_in_default_description': {'key': 'useInDefaultDescription', 'type': 'bool'},
        'validation': {'key': 'validation', 'type': 'InputValidation'},
        'value_hint': {'key': 'valueHint', 'type': 'str'},
        'values': {'key': 'values', 'type': 'InputValues'}
    }

    def __init__(self, dependency_input_ids=None, description=None, group_name=None, has_dynamic_value_information=None, id=None, input_mode=None, is_confidential=None, name=None, properties=None, type=None, use_in_default_description=None, validation=None, value_hint=None, values=None):
        super(InputDescriptor, self).__init__()
        self.dependency_input_ids = dependency_input_ids
        self.description = description
        self.group_name = group_name
        self.has_dynamic_value_information = has_dynamic_value_information
        self.id = id
        self.input_mode = input_mode
        self.is_confidential = is_confidential
        self.name = name
        self.properties = properties
        self.type = type
        self.use_in_default_description = use_in_default_description
        self.validation = validation
        self.value_hint = value_hint
        self.values = values


class InputFilter(Model):

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[InputFilterCondition]'}
    }

    def __init__(self, conditions=None):
        super(InputFilter, self).__init__()
        self.conditions = conditions


class InputFilterCondition(Model):

    _attribute_map = {
        'case_sensitive': {'key': 'caseSensitive', 'type': 'bool'},
        'input_id': {'key': 'inputId', 'type': 'str'},
        'input_value': {'key': 'inputValue', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'object'}
    }

    def __init__(self, case_sensitive=None, input_id=None, input_value=None, operator=None):
        super(InputFilterCondition, self).__init__()
        self.case_sensitive = case_sensitive
        self.input_id = input_id
        self.input_value = input_value
        self.operator = operator


class InputValidation(Model):

    _attribute_map = {
        'data_type': {'key': 'dataType', 'type': 'object'},
        'is_required': {'key': 'isRequired', 'type': 'bool'},
        'max_length': {'key': 'maxLength', 'type': 'int'},
        'max_value': {'key': 'maxValue', 'type': 'decimal'},
        'min_length': {'key': 'minLength', 'type': 'int'},
        'min_value': {'key': 'minValue', 'type': 'decimal'},
        'pattern': {'key': 'pattern', 'type': 'str'},
        'pattern_mismatch_error_message': {'key': 'patternMismatchErrorMessage', 'type': 'str'}
    }

    def __init__(self, data_type=None, is_required=None, max_length=None, max_value=None, min_length=None, min_value=None, pattern=None, pattern_mismatch_error_message=None):
        super(InputValidation, self).__init__()
        self.data_type = data_type
        self.is_required = is_required
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.pattern = pattern
        self.pattern_mismatch_error_message = pattern_mismatch_error_message


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


class Notification(Model):

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'details': {'key': 'details', 'type': 'NotificationDetails'},
        'event_id': {'key': 'eventId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'result': {'key': 'result', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'},
        'subscriber_id': {'key': 'subscriberId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'}
    }

    def __init__(self, created_date=None, details=None, event_id=None, id=None, modified_date=None, result=None, status=None, subscriber_id=None, subscription_id=None):
        super(Notification, self).__init__()
        self.created_date = created_date
        self.details = details
        self.event_id = event_id
        self.id = id
        self.modified_date = modified_date
        self.result = result
        self.status = status
        self.subscriber_id = subscriber_id
        self.subscription_id = subscription_id


class NotificationDetails(Model):

    _attribute_map = {
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'consumer_action_id': {'key': 'consumerActionId', 'type': 'str'},
        'consumer_id': {'key': 'consumerId', 'type': 'str'},
        'consumer_inputs': {'key': 'consumerInputs', 'type': '{str}'},
        'dequeued_date': {'key': 'dequeuedDate', 'type': 'iso-8601'},
        'error_detail': {'key': 'errorDetail', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'event': {'key': 'event', 'type': 'Event'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'processed_date': {'key': 'processedDate', 'type': 'iso-8601'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_inputs': {'key': 'publisherInputs', 'type': '{str}'},
        'queued_date': {'key': 'queuedDate', 'type': 'iso-8601'},
        'request': {'key': 'request', 'type': 'str'},
        'request_attempts': {'key': 'requestAttempts', 'type': 'int'},
        'request_duration': {'key': 'requestDuration', 'type': 'float'},
        'response': {'key': 'response', 'type': 'str'}
    }

    def __init__(self, completed_date=None, consumer_action_id=None, consumer_id=None, consumer_inputs=None, dequeued_date=None, error_detail=None, error_message=None, event=None, event_type=None, processed_date=None, publisher_id=None, publisher_inputs=None, queued_date=None, request=None, request_attempts=None, request_duration=None, response=None):
        super(NotificationDetails, self).__init__()
        self.completed_date = completed_date
        self.consumer_action_id = consumer_action_id
        self.consumer_id = consumer_id
        self.consumer_inputs = consumer_inputs
        self.dequeued_date = dequeued_date
        self.error_detail = error_detail
        self.error_message = error_message
        self.event = event
        self.event_type = event_type
        self.processed_date = processed_date
        self.publisher_id = publisher_id
        self.publisher_inputs = publisher_inputs
        self.queued_date = queued_date
        self.request = request
        self.request_attempts = request_attempts
        self.request_duration = request_duration
        self.response = response


class NotificationResultsSummaryDetail(Model):

    _attribute_map = {
        'notification_count': {'key': 'notificationCount', 'type': 'int'},
        'result': {'key': 'result', 'type': 'object'}
    }

    def __init__(self, notification_count=None, result=None):
        super(NotificationResultsSummaryDetail, self).__init__()
        self.notification_count = notification_count
        self.result = result


class NotificationsQuery(Model):

    _attribute_map = {
        'associated_subscriptions': {'key': 'associatedSubscriptions', 'type': '[Subscription]'},
        'include_details': {'key': 'includeDetails', 'type': 'bool'},
        'max_created_date': {'key': 'maxCreatedDate', 'type': 'iso-8601'},
        'max_results': {'key': 'maxResults', 'type': 'int'},
        'max_results_per_subscription': {'key': 'maxResultsPerSubscription', 'type': 'int'},
        'min_created_date': {'key': 'minCreatedDate', 'type': 'iso-8601'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'results': {'key': 'results', 'type': '[Notification]'},
        'result_type': {'key': 'resultType', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'},
        'subscription_ids': {'key': 'subscriptionIds', 'type': '[str]'},
        'summary': {'key': 'summary', 'type': '[NotificationSummary]'}
    }

    def __init__(self, associated_subscriptions=None, include_details=None, max_created_date=None, max_results=None, max_results_per_subscription=None, min_created_date=None, publisher_id=None, results=None, result_type=None, status=None, subscription_ids=None, summary=None):
        super(NotificationsQuery, self).__init__()
        self.associated_subscriptions = associated_subscriptions
        self.include_details = include_details
        self.max_created_date = max_created_date
        self.max_results = max_results
        self.max_results_per_subscription = max_results_per_subscription
        self.min_created_date = min_created_date
        self.publisher_id = publisher_id
        self.results = results
        self.result_type = result_type
        self.status = status
        self.subscription_ids = subscription_ids
        self.summary = summary


class NotificationSummary(Model):

    _attribute_map = {
        'results': {'key': 'results', 'type': '[NotificationResultsSummaryDetail]'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'}
    }

    def __init__(self, results=None, subscription_id=None):
        super(NotificationSummary, self).__init__()
        self.results = results
        self.subscription_id = subscription_id


class Publisher(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'},
        'supported_events': {'key': 'supportedEvents', 'type': '[EventTypeDescriptor]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, description=None, id=None, input_descriptors=None, name=None, service_instance_type=None, supported_events=None, url=None):
        super(Publisher, self).__init__()
        self._links = _links
        self.description = description
        self.id = id
        self.input_descriptors = input_descriptors
        self.name = name
        self.service_instance_type = service_instance_type
        self.supported_events = supported_events
        self.url = url


class PublisherEvent(Model):

    _attribute_map = {
        'diagnostics': {'key': 'diagnostics', 'type': '{str}'},
        'event': {'key': 'event', 'type': 'Event'},
        'is_filtered_event': {'key': 'isFilteredEvent', 'type': 'bool'},
        'notification_data': {'key': 'notificationData', 'type': '{str}'},
        'other_resource_versions': {'key': 'otherResourceVersions', 'type': '[VersionedResource]'},
        'publisher_input_filters': {'key': 'publisherInputFilters', 'type': '[InputFilter]'},
        'subscription': {'key': 'subscription', 'type': 'Subscription'}
    }

    def __init__(self, diagnostics=None, event=None, is_filtered_event=None, notification_data=None, other_resource_versions=None, publisher_input_filters=None, subscription=None):
        super(PublisherEvent, self).__init__()
        self.diagnostics = diagnostics
        self.event = event
        self.is_filtered_event = is_filtered_event
        self.notification_data = notification_data
        self.other_resource_versions = other_resource_versions
        self.publisher_input_filters = publisher_input_filters
        self.subscription = subscription


class PublishersQuery(Model):

    _attribute_map = {
        'publisher_ids': {'key': 'publisherIds', 'type': '[str]'},
        'publisher_inputs': {'key': 'publisherInputs', 'type': '{str}'},
        'results': {'key': 'results', 'type': '[Publisher]'}
    }

    def __init__(self, publisher_ids=None, publisher_inputs=None, results=None):
        super(PublishersQuery, self).__init__()
        self.publisher_ids = publisher_ids
        self.publisher_inputs = publisher_inputs
        self.results = results


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ResourceContainer(Model):

    _attribute_map = {
        'base_url': {'key': 'baseUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, base_url=None, id=None, name=None, url=None):
        super(ResourceContainer, self).__init__()
        self.base_url = base_url
        self.id = id
        self.name = name
        self.url = url


class SessionToken(Model):

    _attribute_map = {
        'error': {'key': 'error', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'}
    }

    def __init__(self, error=None, token=None, valid_to=None):
        super(SessionToken, self).__init__()
        self.error = error
        self.token = token
        self.valid_to = valid_to


class Subscription(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'action_description': {'key': 'actionDescription', 'type': 'str'},
        'consumer_action_id': {'key': 'consumerActionId', 'type': 'str'},
        'consumer_id': {'key': 'consumerId', 'type': 'str'},
        'consumer_inputs': {'key': 'consumerInputs', 'type': '{str}'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'event_description': {'key': 'eventDescription', 'type': 'str'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'probation_retries': {'key': 'probationRetries', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_inputs': {'key': 'publisherInputs', 'type': '{str}'},
        'resource_version': {'key': 'resourceVersion', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'subscriber': {'key': 'subscriber', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, action_description=None, consumer_action_id=None, consumer_id=None, consumer_inputs=None, created_by=None, created_date=None, event_description=None, event_type=None, id=None, modified_by=None, modified_date=None, probation_retries=None, publisher_id=None, publisher_inputs=None, resource_version=None, status=None, subscriber=None, url=None):
        super(Subscription, self).__init__()
        self._links = _links
        self.action_description = action_description
        self.consumer_action_id = consumer_action_id
        self.consumer_id = consumer_id
        self.consumer_inputs = consumer_inputs
        self.created_by = created_by
        self.created_date = created_date
        self.event_description = event_description
        self.event_type = event_type
        self.id = id
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.probation_retries = probation_retries
        self.publisher_id = publisher_id
        self.publisher_inputs = publisher_inputs
        self.resource_version = resource_version
        self.status = status
        self.subscriber = subscriber
        self.url = url


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


class SubscriptionsQuery(Model):

    _attribute_map = {
        'consumer_action_id': {'key': 'consumerActionId', 'type': 'str'},
        'consumer_id': {'key': 'consumerId', 'type': 'str'},
        'consumer_input_filters': {'key': 'consumerInputFilters', 'type': '[InputFilter]'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_input_filters': {'key': 'publisherInputFilters', 'type': '[InputFilter]'},
        'results': {'key': 'results', 'type': '[Subscription]'},
        'subscriber_id': {'key': 'subscriberId', 'type': 'str'}
    }

    def __init__(self, consumer_action_id=None, consumer_id=None, consumer_input_filters=None, event_type=None, publisher_id=None, publisher_input_filters=None, results=None, subscriber_id=None):
        super(SubscriptionsQuery, self).__init__()
        self.consumer_action_id = consumer_action_id
        self.consumer_id = consumer_id
        self.consumer_input_filters = consumer_input_filters
        self.event_type = event_type
        self.publisher_id = publisher_id
        self.publisher_input_filters = publisher_input_filters
        self.results = results
        self.subscriber_id = subscriber_id


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


class VersionedResource(Model):

    _attribute_map = {
        'compatible_with': {'key': 'compatibleWith', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'object'},
        'resource_version': {'key': 'resourceVersion', 'type': 'str'}
    }

    def __init__(self, compatible_with=None, resource=None, resource_version=None):
        super(VersionedResource, self).__init__()
        self.compatible_with = compatible_with
        self.resource = resource
        self.resource_version = resource_version


__all__ = [
    'Consumer',
    'ConsumerAction',
    'Event',
    'EventTypeDescriptor',
    'ExternalConfigurationDescriptor',
    'FormattedEventMessage',
    'GraphSubjectBase',
    'IdentityRef',
    'InputDescriptor',
    'InputFilter',
    'InputFilterCondition',
    'InputValidation',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'InputValuesQuery',
    'Notification',
    'NotificationDetails',
    'NotificationResultsSummaryDetail',
    'NotificationsQuery',
    'NotificationSummary',
    'Publisher',
    'PublisherEvent',
    'PublishersQuery',
    'ReferenceLinks',
    'ResourceContainer',
    'SessionToken',
    'Subscription',
    'SubscriptionDiagnostics',
    'SubscriptionsQuery',
    'SubscriptionTracing',
    'UpdateSubscripitonDiagnosticsParameters',
    'UpdateSubscripitonTracingParameters',
    'VersionedResource',
]
