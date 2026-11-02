# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AadOauthTokenRequest(Model):

    _attribute_map = {
        'refresh': {'key': 'refresh', 'type': 'bool'},
        'resource': {'key': 'resource', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'}
    }

    def __init__(self, refresh=None, resource=None, tenant_id=None, token=None):
        super(AadOauthTokenRequest, self).__init__()
        self.refresh = refresh
        self.resource = resource
        self.tenant_id = tenant_id
        self.token = token


class AadOauthTokenResult(Model):

    _attribute_map = {
        'access_token': {'key': 'accessToken', 'type': 'str'},
        'refresh_token_cache': {'key': 'refreshTokenCache', 'type': 'str'}
    }

    def __init__(self, access_token=None, refresh_token_cache=None):
        super(AadOauthTokenResult, self).__init__()
        self.access_token = access_token
        self.refresh_token_cache = refresh_token_cache


class AuthenticationSchemeReference(Model):

    _attribute_map = {
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, inputs=None, type=None):
        super(AuthenticationSchemeReference, self).__init__()
        self.inputs = inputs
        self.type = type


class AuthorizationHeader(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(AuthorizationHeader, self).__init__()
        self.name = name
        self.value = value


class AzureManagementGroup(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, name=None, tenant_id=None):
        super(AzureManagementGroup, self).__init__()
        self.display_name = display_name
        self.id = id
        self.name = name
        self.tenant_id = tenant_id


class AzureManagementGroupQueryResult(Model):

    _attribute_map = {
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'value': {'key': 'value', 'type': '[AzureManagementGroup]'}
    }

    def __init__(self, error_message=None, value=None):
        super(AzureManagementGroupQueryResult, self).__init__()
        self.error_message = error_message
        self.value = value


class AzureSubscription(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'subscription_tenant_id': {'key': 'subscriptionTenantId', 'type': 'str'},
        'subscription_tenant_name': {'key': 'subscriptionTenantName', 'type': 'str'}
    }

    def __init__(self, display_name=None, subscription_id=None, subscription_tenant_id=None, subscription_tenant_name=None):
        super(AzureSubscription, self).__init__()
        self.display_name = display_name
        self.subscription_id = subscription_id
        self.subscription_tenant_id = subscription_tenant_id
        self.subscription_tenant_name = subscription_tenant_name


class AzureSubscriptionQueryResult(Model):

    _attribute_map = {
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'value': {'key': 'value', 'type': '[AzureSubscription]'}
    }

    def __init__(self, error_message=None, value=None):
        super(AzureSubscriptionQueryResult, self).__init__()
        self.error_message = error_message
        self.value = value


class ClientCertificate(Model):

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, value=None):
        super(ClientCertificate, self).__init__()
        self.value = value


class DataSource(Model):

    _attribute_map = {
        'authentication_scheme': {'key': 'authenticationScheme', 'type': 'AuthenticationSchemeReference'},
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'resource_url': {'key': 'resourceUrl', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'}
    }

    def __init__(self, authentication_scheme=None, callback_context_template=None, callback_required_template=None, endpoint_url=None, headers=None, initial_context_template=None, name=None, request_content=None, request_verb=None, resource_url=None, result_selector=None):
        super(DataSource, self).__init__()
        self.authentication_scheme = authentication_scheme
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.name = name
        self.request_content = request_content
        self.request_verb = request_verb
        self.resource_url = resource_url
        self.result_selector = result_selector


class DataSourceBindingBase(Model):

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, request_content=None, request_verb=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.request_content = request_content
        self.request_verb = request_verb
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target


class DataSourceDetails(Model):

    _attribute_map = {
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'data_source_url': {'key': 'dataSourceUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'resource_url': {'key': 'resourceUrl', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'}
    }

    def __init__(self, data_source_name=None, data_source_url=None, headers=None, initial_context_template=None, parameters=None, request_content=None, request_verb=None, resource_url=None, result_selector=None):
        super(DataSourceDetails, self).__init__()
        self.data_source_name = data_source_name
        self.data_source_url = data_source_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.request_content = request_content
        self.request_verb = request_verb
        self.resource_url = resource_url
        self.result_selector = result_selector


class DependencyBinding(Model):

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, key=None, value=None):
        super(DependencyBinding, self).__init__()
        self.key = key
        self.value = value


class DependencyData(Model):

    _attribute_map = {
        'input': {'key': 'input', 'type': 'str'},
        'map': {'key': 'map', 'type': '[{ key: str; value: [{ key: str; value: str }] }]'}
    }

    def __init__(self, input=None, map=None):
        super(DependencyData, self).__init__()
        self.input = input
        self.map = map


class DependsOn(Model):

    _attribute_map = {
        'input': {'key': 'input', 'type': 'str'},
        'map': {'key': 'map', 'type': '[DependencyBinding]'}
    }

    def __init__(self, input=None, map=None):
        super(DependsOn, self).__init__()
        self.input = input
        self.map = map


class EndpointAuthorization(Model):

    _attribute_map = {
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'scheme': {'key': 'scheme', 'type': 'str'}
    }

    def __init__(self, parameters=None, scheme=None):
        super(EndpointAuthorization, self).__init__()
        self.parameters = parameters
        self.scheme = scheme


class EndpointUrl(Model):

    _attribute_map = {
        'depends_on': {'key': 'dependsOn', 'type': 'DependsOn'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'format': {'key': 'format', 'type': 'str'},
        'help_text': {'key': 'helpText', 'type': 'str'},
        'is_visible': {'key': 'isVisible', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, depends_on=None, display_name=None, format=None, help_text=None, is_visible=None, value=None):
        super(EndpointUrl, self).__init__()
        self.depends_on = depends_on
        self.display_name = display_name
        self.format = format
        self.help_text = help_text
        self.is_visible = is_visible
        self.value = value


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


class HelpLink(Model):

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, text=None, url=None):
        super(HelpLink, self).__init__()
        self.text = text
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


class OAuthConfiguration(Model):

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, client_id=None, client_secret=None, created_by=None, created_on=None, endpoint_type=None, id=None, modified_by=None, modified_on=None, name=None, url=None):
        super(OAuthConfiguration, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.created_by = created_by
        self.created_on = created_on
        self.endpoint_type = endpoint_type
        self.id = id
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.url = url


class OAuthConfigurationParams(Model):

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, client_id=None, client_secret=None, endpoint_type=None, name=None, url=None):
        super(OAuthConfigurationParams, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.endpoint_type = endpoint_type
        self.name = name
        self.url = url


class ProjectReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class RefreshAuthenticationParameters(Model):

    _attribute_map = {
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'scope': {'key': 'scope', 'type': '[int]'},
        'token_validity_in_minutes': {'key': 'tokenValidityInMinutes', 'type': 'int'}
    }

    def __init__(self, endpoint_id=None, scope=None, token_validity_in_minutes=None):
        super(RefreshAuthenticationParameters, self).__init__()
        self.endpoint_id = endpoint_id
        self.scope = scope
        self.token_validity_in_minutes = token_validity_in_minutes


class ResultTransformationDetails(Model):

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, result_template=None):
        super(ResultTransformationDetails, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.result_template = result_template


class ServiceEndpoint(Model):

    _attribute_map = {
        'administrators_group': {'key': 'administratorsGroup', 'type': 'IdentityRef'},
        'authorization': {'key': 'authorization', 'type': 'EndpointAuthorization'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'data': {'key': 'data', 'type': '{str}'},
        'description': {'key': 'description', 'type': 'str'},
        'group_scope_id': {'key': 'groupScopeId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_ready': {'key': 'isReady', 'type': 'bool'},
        'is_shared': {'key': 'isShared', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'owner': {'key': 'owner', 'type': 'str'},
        'readers_group': {'key': 'readersGroup', 'type': 'IdentityRef'},
        'service_endpoint_project_references': {'key': 'serviceEndpointProjectReferences', 'type': '[ServiceEndpointProjectReference]'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, administrators_group=None, authorization=None, created_by=None, data=None, description=None, group_scope_id=None, id=None, is_ready=None, is_shared=None, name=None, operation_status=None, owner=None, readers_group=None, service_endpoint_project_references=None, type=None, url=None):
        super(ServiceEndpoint, self).__init__()
        self.administrators_group = administrators_group
        self.authorization = authorization
        self.created_by = created_by
        self.data = data
        self.description = description
        self.group_scope_id = group_scope_id
        self.id = id
        self.is_ready = is_ready
        self.is_shared = is_shared
        self.name = name
        self.operation_status = operation_status
        self.owner = owner
        self.readers_group = readers_group
        self.service_endpoint_project_references = service_endpoint_project_references
        self.type = type
        self.url = url


class ServiceEndpointAuthenticationScheme(Model):

    _attribute_map = {
        'authorization_headers': {'key': 'authorizationHeaders', 'type': '[AuthorizationHeader]'},
        'authorization_url': {'key': 'authorizationUrl', 'type': 'str'},
        'client_certificates': {'key': 'clientCertificates', 'type': '[ClientCertificate]'},
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBinding]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'requires_oAuth2_configuration': {'key': 'requiresOAuth2Configuration', 'type': 'bool'},
        'scheme': {'key': 'scheme', 'type': 'str'}
    }

    def __init__(self, authorization_headers=None, authorization_url=None, client_certificates=None, data_source_bindings=None, display_name=None, input_descriptors=None, properties=None, requires_oAuth2_configuration=None, scheme=None):
        super(ServiceEndpointAuthenticationScheme, self).__init__()
        self.authorization_headers = authorization_headers
        self.authorization_url = authorization_url
        self.client_certificates = client_certificates
        self.data_source_bindings = data_source_bindings
        self.display_name = display_name
        self.input_descriptors = input_descriptors
        self.properties = properties
        self.requires_oAuth2_configuration = requires_oAuth2_configuration
        self.scheme = scheme


class ServiceEndpointDetails(Model):

    _attribute_map = {
        'authorization': {'key': 'authorization', 'type': 'EndpointAuthorization'},
        'data': {'key': 'data', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, authorization=None, data=None, type=None, url=None):
        super(ServiceEndpointDetails, self).__init__()
        self.authorization = authorization
        self.data = data
        self.type = type
        self.url = url


class ServiceEndpointExecutionData(Model):

    _attribute_map = {
        'definition': {'key': 'definition', 'type': 'ServiceEndpointExecutionOwner'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'ServiceEndpointExecutionOwner'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'}
    }

    def __init__(self, definition=None, finish_time=None, id=None, owner=None, plan_type=None, result=None, start_time=None):
        super(ServiceEndpointExecutionData, self).__init__()
        self.definition = definition
        self.finish_time = finish_time
        self.id = id
        self.owner = owner
        self.plan_type = plan_type
        self.result = result
        self.start_time = start_time


class ServiceEndpointExecutionOwner(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None):
        super(ServiceEndpointExecutionOwner, self).__init__()
        self._links = _links
        self.id = id
        self.name = name


class ServiceEndpointExecutionRecord(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': 'ServiceEndpointExecutionData'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'}
    }

    def __init__(self, data=None, endpoint_id=None):
        super(ServiceEndpointExecutionRecord, self).__init__()
        self.data = data
        self.endpoint_id = endpoint_id


class ServiceEndpointExecutionRecordsInput(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': 'ServiceEndpointExecutionData'},
        'endpoint_ids': {'key': 'endpointIds', 'type': '[str]'}
    }

    def __init__(self, data=None, endpoint_ids=None):
        super(ServiceEndpointExecutionRecordsInput, self).__init__()
        self.data = data
        self.endpoint_ids = endpoint_ids


class ServiceEndpointProjectReference(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'}
    }

    def __init__(self, description=None, name=None, project_reference=None):
        super(ServiceEndpointProjectReference, self).__init__()
        self.description = description
        self.name = name
        self.project_reference = project_reference


class ServiceEndpointRequest(Model):

    _attribute_map = {
        'data_source_details': {'key': 'dataSourceDetails', 'type': 'DataSourceDetails'},
        'result_transformation_details': {'key': 'resultTransformationDetails', 'type': 'ResultTransformationDetails'},
        'service_endpoint_details': {'key': 'serviceEndpointDetails', 'type': 'ServiceEndpointDetails'}
    }

    def __init__(self, data_source_details=None, result_transformation_details=None, service_endpoint_details=None):
        super(ServiceEndpointRequest, self).__init__()
        self.data_source_details = data_source_details
        self.result_transformation_details = result_transformation_details
        self.service_endpoint_details = service_endpoint_details


class ServiceEndpointRequestResult(Model):

    _attribute_map = {
        'callback_context_parameters': {'key': 'callbackContextParameters', 'type': '{str}'},
        'callback_required': {'key': 'callbackRequired', 'type': 'bool'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'status_code': {'key': 'statusCode', 'type': 'object'}
    }

    def __init__(self, callback_context_parameters=None, callback_required=None, error_message=None, result=None, status_code=None):
        super(ServiceEndpointRequestResult, self).__init__()
        self.callback_context_parameters = callback_context_parameters
        self.callback_required = callback_required
        self.error_message = error_message
        self.result = result
        self.status_code = status_code


class ServiceEndpointType(Model):

    _attribute_map = {
        'authentication_schemes': {'key': 'authenticationSchemes', 'type': '[ServiceEndpointAuthenticationScheme]'},
        'data_sources': {'key': 'dataSources', 'type': '[DataSource]'},
        'dependency_data': {'key': 'dependencyData', 'type': '[DependencyData]'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'EndpointUrl'},
        'help_link': {'key': 'helpLink', 'type': 'HelpLink'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'trusted_hosts': {'key': 'trustedHosts', 'type': '[str]'},
        'ui_contribution_id': {'key': 'uiContributionId', 'type': 'str'}
    }

    def __init__(self, authentication_schemes=None, data_sources=None, dependency_data=None, description=None, display_name=None, endpoint_url=None, help_link=None, help_mark_down=None, icon_url=None, input_descriptors=None, name=None, trusted_hosts=None, ui_contribution_id=None):
        super(ServiceEndpointType, self).__init__()
        self.authentication_schemes = authentication_schemes
        self.data_sources = data_sources
        self.dependency_data = dependency_data
        self.description = description
        self.display_name = display_name
        self.endpoint_url = endpoint_url
        self.help_link = help_link
        self.help_mark_down = help_mark_down
        self.icon_url = icon_url
        self.input_descriptors = input_descriptors
        self.name = name
        self.trusted_hosts = trusted_hosts
        self.ui_contribution_id = ui_contribution_id


class DataSourceBinding(DataSourceBindingBase):

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, request_content=None, request_verb=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBinding, self).__init__(callback_context_template=callback_context_template, callback_required_template=callback_required_template, data_source_name=data_source_name, endpoint_id=endpoint_id, endpoint_url=endpoint_url, headers=headers, initial_context_template=initial_context_template, parameters=parameters, request_content=request_content, request_verb=request_verb, result_selector=result_selector, result_template=result_template, target=target)


__all__ = [
    'AadOauthTokenRequest',
    'AadOauthTokenResult',
    'AuthenticationSchemeReference',
    'AuthorizationHeader',
    'AzureManagementGroup',
    'AzureManagementGroupQueryResult',
    'AzureSubscription',
    'AzureSubscriptionQueryResult',
    'ClientCertificate',
    'DataSource',
    'DataSourceBindingBase',
    'DataSourceDetails',
    'DependencyBinding',
    'DependencyData',
    'DependsOn',
    'EndpointAuthorization',
    'EndpointUrl',
    'GraphSubjectBase',
    'HelpLink',
    'IdentityRef',
    'InputDescriptor',
    'InputValidation',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'OAuthConfiguration',
    'OAuthConfigurationParams',
    'ProjectReference',
    'ReferenceLinks',
    'RefreshAuthenticationParameters',
    'ResultTransformationDetails',
    'ServiceEndpoint',
    'ServiceEndpointAuthenticationScheme',
    'ServiceEndpointDetails',
    'ServiceEndpointExecutionData',
    'ServiceEndpointExecutionOwner',
    'ServiceEndpointExecutionRecord',
    'ServiceEndpointExecutionRecordsInput',
    'ServiceEndpointProjectReference',
    'ServiceEndpointRequest',
    'ServiceEndpointRequestResult',
    'ServiceEndpointType',
    'DataSourceBinding',
]
