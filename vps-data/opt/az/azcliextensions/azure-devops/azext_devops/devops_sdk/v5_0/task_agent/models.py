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
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'name': {'key': 'name', 'type': 'str'},
        'resource_url': {'key': 'resourceUrl', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'}
    }

    def __init__(self, authentication_scheme=None, endpoint_url=None, headers=None, name=None, resource_url=None, result_selector=None):
        super(DataSource, self).__init__()
        self.authentication_scheme = authentication_scheme
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.name = name
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
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target


class DataSourceDetails(Model):

    _attribute_map = {
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'data_source_url': {'key': 'dataSourceUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'resource_url': {'key': 'resourceUrl', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'}
    }

    def __init__(self, data_source_name=None, data_source_url=None, headers=None, parameters=None, resource_url=None, result_selector=None):
        super(DataSourceDetails, self).__init__()
        self.data_source_name = data_source_name
        self.data_source_url = data_source_url
        self.headers = headers
        self.parameters = parameters
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


class DeploymentGroupCreateParameter(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'DeploymentGroupCreateParameterPoolProperty'},
        'pool_id': {'key': 'poolId', 'type': 'int'}
    }

    def __init__(self, description=None, name=None, pool=None, pool_id=None):
        super(DeploymentGroupCreateParameter, self).__init__()
        self.description = description
        self.name = name
        self.pool = pool
        self.pool_id = pool_id


class DeploymentGroupCreateParameterPoolProperty(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(DeploymentGroupCreateParameterPoolProperty, self).__init__()
        self.id = id


class DeploymentGroupMetrics(Model):

    _attribute_map = {
        'columns_header': {'key': 'columnsHeader', 'type': 'MetricsColumnsHeader'},
        'deployment_group': {'key': 'deploymentGroup', 'type': 'DeploymentGroupReference'},
        'rows': {'key': 'rows', 'type': '[MetricsRow]'}
    }

    def __init__(self, columns_header=None, deployment_group=None, rows=None):
        super(DeploymentGroupMetrics, self).__init__()
        self.columns_header = columns_header
        self.deployment_group = deployment_group
        self.rows = rows


class DeploymentGroupReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project': {'key': 'project', 'type': 'ProjectReference'}
    }

    def __init__(self, id=None, name=None, pool=None, project=None):
        super(DeploymentGroupReference, self).__init__()
        self.id = id
        self.name = name
        self.pool = pool
        self.project = project


class DeploymentGroupUpdateParameter(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(DeploymentGroupUpdateParameter, self).__init__()
        self.description = description
        self.name = name


class DeploymentMachine(Model):

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgent'},
        'id': {'key': 'id', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, agent=None, id=None, tags=None):
        super(DeploymentMachine, self).__init__()
        self.agent = agent
        self.id = id
        self.tags = tags


class DeploymentMachineGroupReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project': {'key': 'project', 'type': 'ProjectReference'}
    }

    def __init__(self, id=None, name=None, pool=None, project=None):
        super(DeploymentMachineGroupReference, self).__init__()
        self.id = id
        self.name = name
        self.pool = pool
        self.project = project


class DeploymentPoolSummary(Model):

    _attribute_map = {
        'deployment_groups': {'key': 'deploymentGroups', 'type': '[DeploymentGroupReference]'},
        'offline_agents_count': {'key': 'offlineAgentsCount', 'type': 'int'},
        'online_agents_count': {'key': 'onlineAgentsCount', 'type': 'int'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'}
    }

    def __init__(self, deployment_groups=None, offline_agents_count=None, online_agents_count=None, pool=None):
        super(DeploymentPoolSummary, self).__init__()
        self.deployment_groups = deployment_groups
        self.offline_agents_count = offline_agents_count
        self.online_agents_count = online_agents_count
        self.pool = pool


class DeploymentTargetUpdateParameter(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, id=None, tags=None):
        super(DeploymentTargetUpdateParameter, self).__init__()
        self.id = id
        self.tags = tags


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
        'help_text': {'key': 'helpText', 'type': 'str'},
        'is_visible': {'key': 'isVisible', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, depends_on=None, display_name=None, help_text=None, is_visible=None, value=None):
        super(EndpointUrl, self).__init__()
        self.depends_on = depends_on
        self.display_name = display_name
        self.help_text = help_text
        self.is_visible = is_visible
        self.value = value


class Environment(Model):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'service_groups': {'key': 'serviceGroups', 'type': '[ServiceGroupReference]'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, id=None, last_modified_by=None, last_modified_on=None, name=None, service_groups=None):
        super(Environment, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.name = name
        self.service_groups = service_groups


class EnvironmentCreateParameter(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(EnvironmentCreateParameter, self).__init__()
        self.description = description
        self.name = name


class EnvironmentReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(EnvironmentReference, self).__init__()
        self.id = id
        self.name = name


class EnvironmentUpdateParameter(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(EnvironmentUpdateParameter, self).__init__()
        self.description = description
        self.name = name


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


class InputValidationRequest(Model):

    _attribute_map = {
        'inputs': {'key': 'inputs', 'type': '{ValidationItem}'}
    }

    def __init__(self, inputs=None):
        super(InputValidationRequest, self).__init__()
        self.inputs = inputs


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


class KubernetesServiceGroupCreateParameters(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'}
    }

    def __init__(self, name=None, namespace=None, service_endpoint_id=None):
        super(KubernetesServiceGroupCreateParameters, self).__init__()
        self.name = name
        self.namespace = namespace
        self.service_endpoint_id = service_endpoint_id


class MarketplacePurchasedLicense(Model):

    _attribute_map = {
        'marketplace_name': {'key': 'marketplaceName', 'type': 'str'},
        'purchaser_name': {'key': 'purchaserName', 'type': 'str'},
        'purchase_unit_count': {'key': 'purchaseUnitCount', 'type': 'int'}
    }

    def __init__(self, marketplace_name=None, purchaser_name=None, purchase_unit_count=None):
        super(MarketplacePurchasedLicense, self).__init__()
        self.marketplace_name = marketplace_name
        self.purchaser_name = purchaser_name
        self.purchase_unit_count = purchase_unit_count


class MetricsColumnMetaData(Model):

    _attribute_map = {
        'column_name': {'key': 'columnName', 'type': 'str'},
        'column_value_type': {'key': 'columnValueType', 'type': 'str'}
    }

    def __init__(self, column_name=None, column_value_type=None):
        super(MetricsColumnMetaData, self).__init__()
        self.column_name = column_name
        self.column_value_type = column_value_type


class MetricsColumnsHeader(Model):

    _attribute_map = {
        'dimensions': {'key': 'dimensions', 'type': '[MetricsColumnMetaData]'},
        'metrics': {'key': 'metrics', 'type': '[MetricsColumnMetaData]'}
    }

    def __init__(self, dimensions=None, metrics=None):
        super(MetricsColumnsHeader, self).__init__()
        self.dimensions = dimensions
        self.metrics = metrics


class MetricsRow(Model):

    _attribute_map = {
        'dimensions': {'key': 'dimensions', 'type': '[str]'},
        'metrics': {'key': 'metrics', 'type': '[str]'}
    }

    def __init__(self, dimensions=None, metrics=None):
        super(MetricsRow, self).__init__()
        self.dimensions = dimensions
        self.metrics = metrics


class PackageMetadata(Model):

    _attribute_map = {
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'download_url': {'key': 'downloadUrl', 'type': 'str'},
        'filename': {'key': 'filename', 'type': 'str'},
        'hash_value': {'key': 'hashValue', 'type': 'str'},
        'info_url': {'key': 'infoUrl', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'version': {'key': 'version', 'type': 'PackageVersion'}
    }

    def __init__(self, created_on=None, download_url=None, filename=None, hash_value=None, info_url=None, platform=None, type=None, version=None):
        super(PackageMetadata, self).__init__()
        self.created_on = created_on
        self.download_url = download_url
        self.filename = filename
        self.hash_value = hash_value
        self.info_url = info_url
        self.platform = platform
        self.type = type
        self.version = version


class PackageVersion(Model):

    _attribute_map = {
        'major': {'key': 'major', 'type': 'int'},
        'minor': {'key': 'minor', 'type': 'int'},
        'patch': {'key': 'patch', 'type': 'int'}
    }

    def __init__(self, major=None, minor=None, patch=None):
        super(PackageVersion, self).__init__()
        self.major = major
        self.minor = minor
        self.patch = patch


class ProjectReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name


class PublishTaskGroupMetadata(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'parent_definition_revision': {'key': 'parentDefinitionRevision', 'type': 'int'},
        'preview': {'key': 'preview', 'type': 'bool'},
        'task_group_id': {'key': 'taskGroupId', 'type': 'str'},
        'task_group_revision': {'key': 'taskGroupRevision', 'type': 'int'}
    }

    def __init__(self, comment=None, parent_definition_revision=None, preview=None, task_group_id=None, task_group_revision=None):
        super(PublishTaskGroupMetadata, self).__init__()
        self.comment = comment
        self.parent_definition_revision = parent_definition_revision
        self.preview = preview
        self.task_group_id = task_group_id
        self.task_group_revision = task_group_revision


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ResourceLimit(Model):

    _attribute_map = {
        'failed_to_reach_all_providers': {'key': 'failedToReachAllProviders', 'type': 'bool'},
        'host_id': {'key': 'hostId', 'type': 'str'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'is_premium': {'key': 'isPremium', 'type': 'bool'},
        'parallelism_tag': {'key': 'parallelismTag', 'type': 'str'},
        'resource_limits_data': {'key': 'resourceLimitsData', 'type': '{str}'},
        'total_count': {'key': 'totalCount', 'type': 'int'},
        'total_minutes': {'key': 'totalMinutes', 'type': 'int'}
    }

    def __init__(self, failed_to_reach_all_providers=None, host_id=None, is_hosted=None, is_premium=None, parallelism_tag=None, resource_limits_data=None, total_count=None, total_minutes=None):
        super(ResourceLimit, self).__init__()
        self.failed_to_reach_all_providers = failed_to_reach_all_providers
        self.host_id = host_id
        self.is_hosted = is_hosted
        self.is_premium = is_premium
        self.parallelism_tag = parallelism_tag
        self.resource_limits_data = resource_limits_data
        self.total_count = total_count
        self.total_minutes = total_minutes


class ResourceUsage(Model):

    _attribute_map = {
        'resource_limit': {'key': 'resourceLimit', 'type': 'ResourceLimit'},
        'running_requests': {'key': 'runningRequests', 'type': '[TaskAgentJobRequest]'},
        'used_count': {'key': 'usedCount', 'type': 'int'},
        'used_minutes': {'key': 'usedMinutes', 'type': 'int'}
    }

    def __init__(self, resource_limit=None, running_requests=None, used_count=None, used_minutes=None):
        super(ResourceUsage, self).__init__()
        self.resource_limit = resource_limit
        self.running_requests = running_requests
        self.used_count = used_count
        self.used_minutes = used_minutes


class ResultTransformationDetails(Model):

    _attribute_map = {
        'result_template': {'key': 'resultTemplate', 'type': 'str'}
    }

    def __init__(self, result_template=None):
        super(ResultTransformationDetails, self).__init__()
        self.result_template = result_template


class SecureFile(Model):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'ticket': {'key': 'ticket', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_on=None, id=None, modified_by=None, modified_on=None, name=None, properties=None, ticket=None):
        super(SecureFile, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.id = id
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.properties = properties
        self.ticket = ticket


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
        'readers_group': {'key': 'readersGroup', 'type': 'IdentityRef'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, administrators_group=None, authorization=None, created_by=None, data=None, description=None, group_scope_id=None, id=None, is_ready=None, is_shared=None, name=None, operation_status=None, readers_group=None, type=None, url=None):
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
        self.readers_group = readers_group
        self.type = type
        self.url = url


class ServiceEndpointAuthenticationScheme(Model):

    _attribute_map = {
        'authorization_headers': {'key': 'authorizationHeaders', 'type': '[AuthorizationHeader]'},
        'client_certificates': {'key': 'clientCertificates', 'type': '[ClientCertificate]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'scheme': {'key': 'scheme', 'type': 'str'}
    }

    def __init__(self, authorization_headers=None, client_certificates=None, display_name=None, input_descriptors=None, scheme=None):
        super(ServiceEndpointAuthenticationScheme, self).__init__()
        self.authorization_headers = authorization_headers
        self.client_certificates = client_certificates
        self.display_name = display_name
        self.input_descriptors = input_descriptors
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
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
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
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'status_code': {'key': 'statusCode', 'type': 'object'}
    }

    def __init__(self, error_message=None, result=None, status_code=None):
        super(ServiceEndpointRequestResult, self).__init__()
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


class ServiceGroup(Model):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'environment_reference': {'key': 'environmentReference', 'type': 'EnvironmentReference'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, created_by=None, created_on=None, environment_reference=None, id=None, last_modified_by=None, last_modified_on=None, name=None, type=None):
        super(ServiceGroup, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.environment_reference = environment_reference
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.name = name
        self.type = type


class ServiceGroupReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(ServiceGroupReference, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class TaskAgentAuthorization(Model):

    _attribute_map = {
        'authorization_url': {'key': 'authorizationUrl', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'public_key': {'key': 'publicKey', 'type': 'TaskAgentPublicKey'}
    }

    def __init__(self, authorization_url=None, client_id=None, public_key=None):
        super(TaskAgentAuthorization, self).__init__()
        self.authorization_url = authorization_url
        self.client_id = client_id
        self.public_key = public_key


class TaskAgentCloud(Model):

    _attribute_map = {
        'acquire_agent_endpoint': {'key': 'acquireAgentEndpoint', 'type': 'str'},
        'agent_cloud_id': {'key': 'agentCloudId', 'type': 'int'},
        'get_agent_definition_endpoint': {'key': 'getAgentDefinitionEndpoint', 'type': 'str'},
        'get_agent_request_status_endpoint': {'key': 'getAgentRequestStatusEndpoint', 'type': 'str'},
        'internal': {'key': 'internal', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'release_agent_endpoint': {'key': 'releaseAgentEndpoint', 'type': 'str'},
        'shared_secret': {'key': 'sharedSecret', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, acquire_agent_endpoint=None, agent_cloud_id=None, get_agent_definition_endpoint=None, get_agent_request_status_endpoint=None, internal=None, name=None, release_agent_endpoint=None, shared_secret=None, type=None):
        super(TaskAgentCloud, self).__init__()
        self.acquire_agent_endpoint = acquire_agent_endpoint
        self.agent_cloud_id = agent_cloud_id
        self.get_agent_definition_endpoint = get_agent_definition_endpoint
        self.get_agent_request_status_endpoint = get_agent_request_status_endpoint
        self.internal = internal
        self.name = name
        self.release_agent_endpoint = release_agent_endpoint
        self.shared_secret = shared_secret
        self.type = type


class TaskAgentCloudRequest(Model):

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgentReference'},
        'agent_cloud_id': {'key': 'agentCloudId', 'type': 'int'},
        'agent_connected_time': {'key': 'agentConnectedTime', 'type': 'iso-8601'},
        'agent_data': {'key': 'agentData', 'type': 'object'},
        'agent_specification': {'key': 'agentSpecification', 'type': 'object'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'provisioned_time': {'key': 'provisionedTime', 'type': 'iso-8601'},
        'provision_request_time': {'key': 'provisionRequestTime', 'type': 'iso-8601'},
        'release_request_time': {'key': 'releaseRequestTime', 'type': 'iso-8601'},
        'request_id': {'key': 'requestId', 'type': 'str'}
    }

    def __init__(self, agent=None, agent_cloud_id=None, agent_connected_time=None, agent_data=None, agent_specification=None, pool=None, provisioned_time=None, provision_request_time=None, release_request_time=None, request_id=None):
        super(TaskAgentCloudRequest, self).__init__()
        self.agent = agent
        self.agent_cloud_id = agent_cloud_id
        self.agent_connected_time = agent_connected_time
        self.agent_data = agent_data
        self.agent_specification = agent_specification
        self.pool = pool
        self.provisioned_time = provisioned_time
        self.provision_request_time = provision_request_time
        self.release_request_time = release_request_time
        self.request_id = request_id


class TaskAgentCloudType(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, display_name=None, input_descriptors=None, name=None):
        super(TaskAgentCloudType, self).__init__()
        self.display_name = display_name
        self.input_descriptors = input_descriptors
        self.name = name


class TaskAgentDelaySource(Model):

    _attribute_map = {
        'delays': {'key': 'delays', 'type': '[object]'},
        'task_agent': {'key': 'taskAgent', 'type': 'TaskAgentReference'}
    }

    def __init__(self, delays=None, task_agent=None):
        super(TaskAgentDelaySource, self).__init__()
        self.delays = delays
        self.task_agent = task_agent


class TaskAgentJobRequest(Model):

    _attribute_map = {
        'agent_delays': {'key': 'agentDelays', 'type': '[TaskAgentDelaySource]'},
        'agent_specification': {'key': 'agentSpecification', 'type': 'object'},
        'assign_time': {'key': 'assignTime', 'type': 'iso-8601'},
        'data': {'key': 'data', 'type': '{str}'},
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'expected_duration': {'key': 'expectedDuration', 'type': 'object'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'host_id': {'key': 'hostId', 'type': 'str'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'job_name': {'key': 'jobName', 'type': 'str'},
        'locked_until': {'key': 'lockedUntil', 'type': 'iso-8601'},
        'matched_agents': {'key': 'matchedAgents', 'type': '[TaskAgentReference]'},
        'orchestration_id': {'key': 'orchestrationId', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'pool_id': {'key': 'poolId', 'type': 'int'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'receive_time': {'key': 'receiveTime', 'type': 'iso-8601'},
        'request_id': {'key': 'requestId', 'type': 'long'},
        'reserved_agent': {'key': 'reservedAgent', 'type': 'TaskAgentReference'},
        'result': {'key': 'result', 'type': 'object'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'}
    }

    def __init__(self, agent_delays=None, agent_specification=None, assign_time=None, data=None, definition=None, demands=None, expected_duration=None, finish_time=None, host_id=None, job_id=None, job_name=None, locked_until=None, matched_agents=None, orchestration_id=None, owner=None, plan_group=None, plan_id=None, plan_type=None, pool_id=None, queue_id=None, queue_time=None, receive_time=None, request_id=None, reserved_agent=None, result=None, scope_id=None, service_owner=None):
        super(TaskAgentJobRequest, self).__init__()
        self.agent_delays = agent_delays
        self.agent_specification = agent_specification
        self.assign_time = assign_time
        self.data = data
        self.definition = definition
        self.demands = demands
        self.expected_duration = expected_duration
        self.finish_time = finish_time
        self.host_id = host_id
        self.job_id = job_id
        self.job_name = job_name
        self.locked_until = locked_until
        self.matched_agents = matched_agents
        self.orchestration_id = orchestration_id
        self.owner = owner
        self.plan_group = plan_group
        self.plan_id = plan_id
        self.plan_type = plan_type
        self.pool_id = pool_id
        self.queue_id = queue_id
        self.queue_time = queue_time
        self.receive_time = receive_time
        self.request_id = request_id
        self.reserved_agent = reserved_agent
        self.result = result
        self.scope_id = scope_id
        self.service_owner = service_owner


class TaskAgentMessage(Model):

    _attribute_map = {
        'body': {'key': 'body', 'type': 'str'},
        'iv': {'key': 'iv', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'long'},
        'message_type': {'key': 'messageType', 'type': 'str'}
    }

    def __init__(self, body=None, iv=None, message_id=None, message_type=None):
        super(TaskAgentMessage, self).__init__()
        self.body = body
        self.iv = iv
        self.message_id = message_id
        self.message_type = message_type


class TaskAgentPoolMaintenanceDefinition(Model):

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'job_timeout_in_minutes': {'key': 'jobTimeoutInMinutes', 'type': 'int'},
        'max_concurrent_agents_percentage': {'key': 'maxConcurrentAgentsPercentage', 'type': 'int'},
        'options': {'key': 'options', 'type': 'TaskAgentPoolMaintenanceOptions'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'TaskAgentPoolMaintenanceRetentionPolicy'},
        'schedule_setting': {'key': 'scheduleSetting', 'type': 'TaskAgentPoolMaintenanceSchedule'}
    }

    def __init__(self, enabled=None, id=None, job_timeout_in_minutes=None, max_concurrent_agents_percentage=None, options=None, pool=None, retention_policy=None, schedule_setting=None):
        super(TaskAgentPoolMaintenanceDefinition, self).__init__()
        self.enabled = enabled
        self.id = id
        self.job_timeout_in_minutes = job_timeout_in_minutes
        self.max_concurrent_agents_percentage = max_concurrent_agents_percentage
        self.options = options
        self.pool = pool
        self.retention_policy = retention_policy
        self.schedule_setting = schedule_setting


class TaskAgentPoolMaintenanceJob(Model):

    _attribute_map = {
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'error_count': {'key': 'errorCount', 'type': 'int'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'job_id': {'key': 'jobId', 'type': 'int'},
        'logs_download_url': {'key': 'logsDownloadUrl', 'type': 'str'},
        'orchestration_id': {'key': 'orchestrationId', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'result': {'key': 'result', 'type': 'object'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'target_agents': {'key': 'targetAgents', 'type': '[TaskAgentPoolMaintenanceJobTargetAgent]'},
        'warning_count': {'key': 'warningCount', 'type': 'int'}
    }

    def __init__(self, definition_id=None, error_count=None, finish_time=None, job_id=None, logs_download_url=None, orchestration_id=None, pool=None, queue_time=None, requested_by=None, result=None, start_time=None, status=None, target_agents=None, warning_count=None):
        super(TaskAgentPoolMaintenanceJob, self).__init__()
        self.definition_id = definition_id
        self.error_count = error_count
        self.finish_time = finish_time
        self.job_id = job_id
        self.logs_download_url = logs_download_url
        self.orchestration_id = orchestration_id
        self.pool = pool
        self.queue_time = queue_time
        self.requested_by = requested_by
        self.result = result
        self.start_time = start_time
        self.status = status
        self.target_agents = target_agents
        self.warning_count = warning_count


class TaskAgentPoolMaintenanceJobTargetAgent(Model):

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgentReference'},
        'job_id': {'key': 'jobId', 'type': 'int'},
        'result': {'key': 'result', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, agent=None, job_id=None, result=None, status=None):
        super(TaskAgentPoolMaintenanceJobTargetAgent, self).__init__()
        self.agent = agent
        self.job_id = job_id
        self.result = result
        self.status = status


class TaskAgentPoolMaintenanceOptions(Model):

    _attribute_map = {
        'working_directory_expiration_in_days': {'key': 'workingDirectoryExpirationInDays', 'type': 'int'}
    }

    def __init__(self, working_directory_expiration_in_days=None):
        super(TaskAgentPoolMaintenanceOptions, self).__init__()
        self.working_directory_expiration_in_days = working_directory_expiration_in_days


class TaskAgentPoolMaintenanceRetentionPolicy(Model):

    _attribute_map = {
        'number_of_history_records_to_keep': {'key': 'numberOfHistoryRecordsToKeep', 'type': 'int'}
    }

    def __init__(self, number_of_history_records_to_keep=None):
        super(TaskAgentPoolMaintenanceRetentionPolicy, self).__init__()
        self.number_of_history_records_to_keep = number_of_history_records_to_keep


class TaskAgentPoolMaintenanceSchedule(Model):

    _attribute_map = {
        'days_to_build': {'key': 'daysToBuild', 'type': 'object'},
        'schedule_job_id': {'key': 'scheduleJobId', 'type': 'str'},
        'start_hours': {'key': 'startHours', 'type': 'int'},
        'start_minutes': {'key': 'startMinutes', 'type': 'int'},
        'time_zone_id': {'key': 'timeZoneId', 'type': 'str'}
    }

    def __init__(self, days_to_build=None, schedule_job_id=None, start_hours=None, start_minutes=None, time_zone_id=None):
        super(TaskAgentPoolMaintenanceSchedule, self).__init__()
        self.days_to_build = days_to_build
        self.schedule_job_id = schedule_job_id
        self.start_hours = start_hours
        self.start_minutes = start_minutes
        self.time_zone_id = time_zone_id


class TaskAgentPoolReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'pool_type': {'key': 'poolType', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'}
    }

    def __init__(self, id=None, is_hosted=None, name=None, pool_type=None, scope=None, size=None):
        super(TaskAgentPoolReference, self).__init__()
        self.id = id
        self.is_hosted = is_hosted
        self.name = name
        self.pool_type = pool_type
        self.scope = scope
        self.size = size


class TaskAgentPublicKey(Model):

    _attribute_map = {
        'exponent': {'key': 'exponent', 'type': 'str'},
        'modulus': {'key': 'modulus', 'type': 'str'}
    }

    def __init__(self, exponent=None, modulus=None):
        super(TaskAgentPublicKey, self).__init__()
        self.exponent = exponent
        self.modulus = modulus


class TaskAgentQueue(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project_id': {'key': 'projectId', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, pool=None, project_id=None):
        super(TaskAgentQueue, self).__init__()
        self.id = id
        self.name = name
        self.pool = pool
        self.project_id = project_id


class TaskAgentReference(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'access_point': {'key': 'accessPoint', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'os_description': {'key': 'osDescription', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, _links=None, access_point=None, enabled=None, id=None, name=None, os_description=None, provisioning_state=None, status=None, version=None):
        super(TaskAgentReference, self).__init__()
        self._links = _links
        self.access_point = access_point
        self.enabled = enabled
        self.id = id
        self.name = name
        self.os_description = os_description
        self.provisioning_state = provisioning_state
        self.status = status
        self.version = version


class TaskAgentSession(Model):

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgentReference'},
        'encryption_key': {'key': 'encryptionKey', 'type': 'TaskAgentSessionKey'},
        'owner_name': {'key': 'ownerName', 'type': 'str'},
        'session_id': {'key': 'sessionId', 'type': 'str'},
        'system_capabilities': {'key': 'systemCapabilities', 'type': '{str}'}
    }

    def __init__(self, agent=None, encryption_key=None, owner_name=None, session_id=None, system_capabilities=None):
        super(TaskAgentSession, self).__init__()
        self.agent = agent
        self.encryption_key = encryption_key
        self.owner_name = owner_name
        self.session_id = session_id
        self.system_capabilities = system_capabilities


class TaskAgentSessionKey(Model):

    _attribute_map = {
        'encrypted': {'key': 'encrypted', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, encrypted=None, value=None):
        super(TaskAgentSessionKey, self).__init__()
        self.encrypted = encrypted
        self.value = value


class TaskAgentUpdate(Model):

    _attribute_map = {
        'current_state': {'key': 'currentState', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'TaskAgentUpdateReason'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'request_time': {'key': 'requestTime', 'type': 'iso-8601'},
        'source_version': {'key': 'sourceVersion', 'type': 'PackageVersion'},
        'target_version': {'key': 'targetVersion', 'type': 'PackageVersion'}
    }

    def __init__(self, current_state=None, reason=None, requested_by=None, request_time=None, source_version=None, target_version=None):
        super(TaskAgentUpdate, self).__init__()
        self.current_state = current_state
        self.reason = reason
        self.requested_by = requested_by
        self.request_time = request_time
        self.source_version = source_version
        self.target_version = target_version


class TaskAgentUpdateReason(Model):

    _attribute_map = {
        'code': {'key': 'code', 'type': 'object'}
    }

    def __init__(self, code=None):
        super(TaskAgentUpdateReason, self).__init__()
        self.code = code


class TaskDefinition(Model):

    _attribute_map = {
        'agent_execution': {'key': 'agentExecution', 'type': 'TaskExecution'},
        'author': {'key': 'author', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'contents_uploaded': {'key': 'contentsUploaded', 'type': 'bool'},
        'contribution_identifier': {'key': 'contributionIdentifier', 'type': 'str'},
        'contribution_version': {'key': 'contributionVersion', 'type': 'str'},
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBinding]'},
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deprecated': {'key': 'deprecated', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'disabled': {'key': 'disabled', 'type': 'bool'},
        'execution': {'key': 'execution', 'type': '{object}'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'groups': {'key': 'groups', 'type': '[TaskGroupDefinition]'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'host_type': {'key': 'hostType', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinition]'},
        'instance_name_format': {'key': 'instanceNameFormat', 'type': 'str'},
        'minimum_agent_version': {'key': 'minimumAgentVersion', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'output_variables': {'key': 'outputVariables', 'type': '[TaskOutputVariable]'},
        'package_location': {'key': 'packageLocation', 'type': 'str'},
        'package_type': {'key': 'packageType', 'type': 'str'},
        'post_job_execution': {'key': 'postJobExecution', 'type': '{object}'},
        'pre_job_execution': {'key': 'preJobExecution', 'type': '{object}'},
        'preview': {'key': 'preview', 'type': 'bool'},
        'release_notes': {'key': 'releaseNotes', 'type': 'str'},
        'runs_on': {'key': 'runsOn', 'type': '[str]'},
        'satisfies': {'key': 'satisfies', 'type': '[str]'},
        'server_owned': {'key': 'serverOwned', 'type': 'bool'},
        'show_environment_variables': {'key': 'showEnvironmentVariables', 'type': 'bool'},
        'source_definitions': {'key': 'sourceDefinitions', 'type': '[TaskSourceDefinition]'},
        'source_location': {'key': 'sourceLocation', 'type': 'str'},
        'version': {'key': 'version', 'type': 'TaskVersion'},
        'visibility': {'key': 'visibility', 'type': '[str]'}
    }

    def __init__(self, agent_execution=None, author=None, category=None, contents_uploaded=None, contribution_identifier=None, contribution_version=None, data_source_bindings=None, definition_type=None, demands=None, deprecated=None, description=None, disabled=None, execution=None, friendly_name=None, groups=None, help_mark_down=None, host_type=None, icon_url=None, id=None, inputs=None, instance_name_format=None, minimum_agent_version=None, name=None, output_variables=None, package_location=None, package_type=None, post_job_execution=None, pre_job_execution=None, preview=None, release_notes=None, runs_on=None, satisfies=None, server_owned=None, show_environment_variables=None, source_definitions=None, source_location=None, version=None, visibility=None):
        super(TaskDefinition, self).__init__()
        self.agent_execution = agent_execution
        self.author = author
        self.category = category
        self.contents_uploaded = contents_uploaded
        self.contribution_identifier = contribution_identifier
        self.contribution_version = contribution_version
        self.data_source_bindings = data_source_bindings
        self.definition_type = definition_type
        self.demands = demands
        self.deprecated = deprecated
        self.description = description
        self.disabled = disabled
        self.execution = execution
        self.friendly_name = friendly_name
        self.groups = groups
        self.help_mark_down = help_mark_down
        self.host_type = host_type
        self.icon_url = icon_url
        self.id = id
        self.inputs = inputs
        self.instance_name_format = instance_name_format
        self.minimum_agent_version = minimum_agent_version
        self.name = name
        self.output_variables = output_variables
        self.package_location = package_location
        self.package_type = package_type
        self.post_job_execution = post_job_execution
        self.pre_job_execution = pre_job_execution
        self.preview = preview
        self.release_notes = release_notes
        self.runs_on = runs_on
        self.satisfies = satisfies
        self.server_owned = server_owned
        self.show_environment_variables = show_environment_variables
        self.source_definitions = source_definitions
        self.source_location = source_location
        self.version = version
        self.visibility = visibility


class TaskDefinitionEndpoint(Model):

    _attribute_map = {
        'connection_id': {'key': 'connectionId', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'task_id': {'key': 'taskId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, connection_id=None, key_selector=None, scope=None, selector=None, task_id=None, url=None):
        super(TaskDefinitionEndpoint, self).__init__()
        self.connection_id = connection_id
        self.key_selector = key_selector
        self.scope = scope
        self.selector = selector
        self.task_id = task_id
        self.url = url


class TaskDefinitionReference(Model):

    _attribute_map = {
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'version_spec': {'key': 'versionSpec', 'type': 'str'}
    }

    def __init__(self, definition_type=None, id=None, version_spec=None):
        super(TaskDefinitionReference, self).__init__()
        self.definition_type = definition_type
        self.id = id
        self.version_spec = version_spec


class TaskExecution(Model):

    _attribute_map = {
        'exec_task': {'key': 'execTask', 'type': 'TaskReference'},
        'platform_instructions': {'key': 'platformInstructions', 'type': '{{str}}'}
    }

    def __init__(self, exec_task=None, platform_instructions=None):
        super(TaskExecution, self).__init__()
        self.exec_task = exec_task
        self.platform_instructions = platform_instructions


class TaskGroup(TaskDefinition):

    _attribute_map = {
        'agent_execution': {'key': 'agentExecution', 'type': 'TaskExecution'},
        'author': {'key': 'author', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'contents_uploaded': {'key': 'contentsUploaded', 'type': 'bool'},
        'contribution_identifier': {'key': 'contributionIdentifier', 'type': 'str'},
        'contribution_version': {'key': 'contributionVersion', 'type': 'str'},
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBinding]'},
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deprecated': {'key': 'deprecated', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'disabled': {'key': 'disabled', 'type': 'bool'},
        'execution': {'key': 'execution', 'type': '{object}'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'groups': {'key': 'groups', 'type': '[TaskGroupDefinition]'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'host_type': {'key': 'hostType', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinition]'},
        'instance_name_format': {'key': 'instanceNameFormat', 'type': 'str'},
        'minimum_agent_version': {'key': 'minimumAgentVersion', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'output_variables': {'key': 'outputVariables', 'type': '[TaskOutputVariable]'},
        'package_location': {'key': 'packageLocation', 'type': 'str'},
        'package_type': {'key': 'packageType', 'type': 'str'},
        'post_job_execution': {'key': 'postJobExecution', 'type': '{object}'},
        'pre_job_execution': {'key': 'preJobExecution', 'type': '{object}'},
        'preview': {'key': 'preview', 'type': 'bool'},
        'release_notes': {'key': 'releaseNotes', 'type': 'str'},
        'runs_on': {'key': 'runsOn', 'type': '[str]'},
        'satisfies': {'key': 'satisfies', 'type': '[str]'},
        'server_owned': {'key': 'serverOwned', 'type': 'bool'},
        'show_environment_variables': {'key': 'showEnvironmentVariables', 'type': 'bool'},
        'source_definitions': {'key': 'sourceDefinitions', 'type': '[TaskSourceDefinition]'},
        'source_location': {'key': 'sourceLocation', 'type': 'str'},
        'version': {'key': 'version', 'type': 'TaskVersion'},
        'visibility': {'key': 'visibility', 'type': '[str]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'deleted': {'key': 'deleted', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'str'},
        'parent_definition_id': {'key': 'parentDefinitionId', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'tasks': {'key': 'tasks', 'type': '[TaskGroupStep]'}
    }

    def __init__(self, agent_execution=None, author=None, category=None, contents_uploaded=None, contribution_identifier=None, contribution_version=None, data_source_bindings=None, definition_type=None, demands=None, deprecated=None, description=None, disabled=None, execution=None, friendly_name=None, groups=None, help_mark_down=None, host_type=None, icon_url=None, id=None, inputs=None, instance_name_format=None, minimum_agent_version=None, name=None, output_variables=None, package_location=None, package_type=None, post_job_execution=None, pre_job_execution=None, preview=None, release_notes=None, runs_on=None, satisfies=None, server_owned=None, show_environment_variables=None, source_definitions=None, source_location=None, version=None, visibility=None, comment=None, created_by=None, created_on=None, deleted=None, modified_by=None, modified_on=None, owner=None, parent_definition_id=None, revision=None, tasks=None):
        super(TaskGroup, self).__init__(agent_execution=agent_execution, author=author, category=category, contents_uploaded=contents_uploaded, contribution_identifier=contribution_identifier, contribution_version=contribution_version, data_source_bindings=data_source_bindings, definition_type=definition_type, demands=demands, deprecated=deprecated, description=description, disabled=disabled, execution=execution, friendly_name=friendly_name, groups=groups, help_mark_down=help_mark_down, host_type=host_type, icon_url=icon_url, id=id, inputs=inputs, instance_name_format=instance_name_format, minimum_agent_version=minimum_agent_version, name=name, output_variables=output_variables, package_location=package_location, package_type=package_type, post_job_execution=post_job_execution, pre_job_execution=pre_job_execution, preview=preview, release_notes=release_notes, runs_on=runs_on, satisfies=satisfies, server_owned=server_owned, show_environment_variables=show_environment_variables, source_definitions=source_definitions, source_location=source_location, version=version, visibility=visibility)
        self.comment = comment
        self.created_by = created_by
        self.created_on = created_on
        self.deleted = deleted
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.owner = owner
        self.parent_definition_id = parent_definition_id
        self.revision = revision
        self.tasks = tasks


class TaskGroupCreateParameter(Model):

    _attribute_map = {
        'author': {'key': 'author', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinition]'},
        'instance_name_format': {'key': 'instanceNameFormat', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_definition_id': {'key': 'parentDefinitionId', 'type': 'str'},
        'runs_on': {'key': 'runsOn', 'type': '[str]'},
        'tasks': {'key': 'tasks', 'type': '[TaskGroupStep]'},
        'version': {'key': 'version', 'type': 'TaskVersion'}
    }

    def __init__(self, author=None, category=None, description=None, friendly_name=None, icon_url=None, inputs=None, instance_name_format=None, name=None, parent_definition_id=None, runs_on=None, tasks=None, version=None):
        super(TaskGroupCreateParameter, self).__init__()
        self.author = author
        self.category = category
        self.description = description
        self.friendly_name = friendly_name
        self.icon_url = icon_url
        self.inputs = inputs
        self.instance_name_format = instance_name_format
        self.name = name
        self.parent_definition_id = parent_definition_id
        self.runs_on = runs_on
        self.tasks = tasks
        self.version = version


class TaskGroupDefinition(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_expanded': {'key': 'isExpanded', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, display_name=None, is_expanded=None, name=None, tags=None, visible_rule=None):
        super(TaskGroupDefinition, self).__init__()
        self.display_name = display_name
        self.is_expanded = is_expanded
        self.name = name
        self.tags = tags
        self.visible_rule = visible_rule


class TaskGroupRevision(Model):

    _attribute_map = {
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'file_id': {'key': 'fileId', 'type': 'int'},
        'revision': {'key': 'revision', 'type': 'int'},
        'task_group_id': {'key': 'taskGroupId', 'type': 'str'}
    }

    def __init__(self, changed_by=None, changed_date=None, change_type=None, comment=None, file_id=None, revision=None, task_group_id=None):
        super(TaskGroupRevision, self).__init__()
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.change_type = change_type
        self.comment = comment
        self.file_id = file_id
        self.revision = revision
        self.task_group_id = task_group_id


class TaskGroupStep(Model):

    _attribute_map = {
        'always_run': {'key': 'alwaysRun', 'type': 'bool'},
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'environment': {'key': 'environment', 'type': '{str}'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'task': {'key': 'task', 'type': 'TaskDefinitionReference'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, always_run=None, condition=None, continue_on_error=None, display_name=None, enabled=None, environment=None, inputs=None, task=None, timeout_in_minutes=None):
        super(TaskGroupStep, self).__init__()
        self.always_run = always_run
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.display_name = display_name
        self.enabled = enabled
        self.environment = environment
        self.inputs = inputs
        self.task = task
        self.timeout_in_minutes = timeout_in_minutes


class TaskGroupUpdateParameter(Model):

    _attribute_map = {
        'author': {'key': 'author', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinition]'},
        'instance_name_format': {'key': 'instanceNameFormat', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_definition_id': {'key': 'parentDefinitionId', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'runs_on': {'key': 'runsOn', 'type': '[str]'},
        'tasks': {'key': 'tasks', 'type': '[TaskGroupStep]'},
        'version': {'key': 'version', 'type': 'TaskVersion'}
    }

    def __init__(self, author=None, category=None, comment=None, description=None, friendly_name=None, icon_url=None, id=None, inputs=None, instance_name_format=None, name=None, parent_definition_id=None, revision=None, runs_on=None, tasks=None, version=None):
        super(TaskGroupUpdateParameter, self).__init__()
        self.author = author
        self.category = category
        self.comment = comment
        self.description = description
        self.friendly_name = friendly_name
        self.icon_url = icon_url
        self.id = id
        self.inputs = inputs
        self.instance_name_format = instance_name_format
        self.name = name
        self.parent_definition_id = parent_definition_id
        self.revision = revision
        self.runs_on = runs_on
        self.tasks = tasks
        self.version = version


class TaskHubLicenseDetails(Model):

    _attribute_map = {
        'enterprise_users_count': {'key': 'enterpriseUsersCount', 'type': 'int'},
        'failed_to_reach_all_providers': {'key': 'failedToReachAllProviders', 'type': 'bool'},
        'free_hosted_license_count': {'key': 'freeHostedLicenseCount', 'type': 'int'},
        'free_license_count': {'key': 'freeLicenseCount', 'type': 'int'},
        'has_license_count_ever_updated': {'key': 'hasLicenseCountEverUpdated', 'type': 'bool'},
        'hosted_agent_minutes_free_count': {'key': 'hostedAgentMinutesFreeCount', 'type': 'int'},
        'hosted_agent_minutes_used_count': {'key': 'hostedAgentMinutesUsedCount', 'type': 'int'},
        'hosted_licenses_are_premium': {'key': 'hostedLicensesArePremium', 'type': 'bool'},
        'marketplace_purchased_hosted_licenses': {'key': 'marketplacePurchasedHostedLicenses', 'type': '[MarketplacePurchasedLicense]'},
        'msdn_users_count': {'key': 'msdnUsersCount', 'type': 'int'},
        'purchased_hosted_license_count': {'key': 'purchasedHostedLicenseCount', 'type': 'int'},
        'purchased_license_count': {'key': 'purchasedLicenseCount', 'type': 'int'},
        'total_hosted_license_count': {'key': 'totalHostedLicenseCount', 'type': 'int'},
        'total_license_count': {'key': 'totalLicenseCount', 'type': 'int'},
        'total_private_license_count': {'key': 'totalPrivateLicenseCount', 'type': 'int'}
    }

    def __init__(self, enterprise_users_count=None, failed_to_reach_all_providers=None, free_hosted_license_count=None, free_license_count=None, has_license_count_ever_updated=None, hosted_agent_minutes_free_count=None, hosted_agent_minutes_used_count=None, hosted_licenses_are_premium=None, marketplace_purchased_hosted_licenses=None, msdn_users_count=None, purchased_hosted_license_count=None, purchased_license_count=None, total_hosted_license_count=None, total_license_count=None, total_private_license_count=None):
        super(TaskHubLicenseDetails, self).__init__()
        self.enterprise_users_count = enterprise_users_count
        self.failed_to_reach_all_providers = failed_to_reach_all_providers
        self.free_hosted_license_count = free_hosted_license_count
        self.free_license_count = free_license_count
        self.has_license_count_ever_updated = has_license_count_ever_updated
        self.hosted_agent_minutes_free_count = hosted_agent_minutes_free_count
        self.hosted_agent_minutes_used_count = hosted_agent_minutes_used_count
        self.hosted_licenses_are_premium = hosted_licenses_are_premium
        self.marketplace_purchased_hosted_licenses = marketplace_purchased_hosted_licenses
        self.msdn_users_count = msdn_users_count
        self.purchased_hosted_license_count = purchased_hosted_license_count
        self.purchased_license_count = purchased_license_count
        self.total_hosted_license_count = total_hosted_license_count
        self.total_license_count = total_license_count
        self.total_private_license_count = total_private_license_count


class TaskInputDefinitionBase(Model):

    _attribute_map = {
        'aliases': {'key': 'aliases', 'type': '[str]'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'validation': {'key': 'validation', 'type': 'TaskInputValidation'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, aliases=None, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinitionBase, self).__init__()
        self.aliases = aliases
        self.default_value = default_value
        self.group_name = group_name
        self.help_mark_down = help_mark_down
        self.label = label
        self.name = name
        self.options = options
        self.properties = properties
        self.required = required
        self.type = type
        self.validation = validation
        self.visible_rule = visible_rule


class TaskInputValidation(Model):

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, expression=None, message=None):
        super(TaskInputValidation, self).__init__()
        self.expression = expression
        self.message = message


class TaskOrchestrationOwner(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None):
        super(TaskOrchestrationOwner, self).__init__()
        self._links = _links
        self.id = id
        self.name = name


class TaskOutputVariable(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(TaskOutputVariable, self).__init__()
        self.description = description
        self.name = name


class TaskPackageMetadata(Model):

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, type=None, url=None, version=None):
        super(TaskPackageMetadata, self).__init__()
        self.type = type
        self.url = url
        self.version = version


class TaskReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, inputs=None, name=None, version=None):
        super(TaskReference, self).__init__()
        self.id = id
        self.inputs = inputs
        self.name = name
        self.version = version


class TaskSourceDefinitionBase(Model):

    _attribute_map = {
        'auth_key': {'key': 'authKey', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, auth_key=None, endpoint=None, key_selector=None, selector=None, target=None):
        super(TaskSourceDefinitionBase, self).__init__()
        self.auth_key = auth_key
        self.endpoint = endpoint
        self.key_selector = key_selector
        self.selector = selector
        self.target = target


class TaskVersion(Model):

    _attribute_map = {
        'is_test': {'key': 'isTest', 'type': 'bool'},
        'major': {'key': 'major', 'type': 'int'},
        'minor': {'key': 'minor', 'type': 'int'},
        'patch': {'key': 'patch', 'type': 'int'}
    }

    def __init__(self, is_test=None, major=None, minor=None, patch=None):
        super(TaskVersion, self).__init__()
        self.is_test = is_test
        self.major = major
        self.minor = minor
        self.patch = patch


class ValidationItem(Model):

    _attribute_map = {
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_valid=None, reason=None, type=None, value=None):
        super(ValidationItem, self).__init__()
        self.is_valid = is_valid
        self.reason = reason
        self.type = type
        self.value = value


class VariableGroup(Model):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_shared': {'key': 'isShared', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'provider_data': {'key': 'providerData', 'type': 'VariableGroupProviderData'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, id=None, is_shared=None, modified_by=None, modified_on=None, name=None, provider_data=None, type=None, variables=None):
        super(VariableGroup, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
        self.is_shared = is_shared
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.provider_data = provider_data
        self.type = type
        self.variables = variables


class VariableGroupParameters(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'provider_data': {'key': 'providerData', 'type': 'VariableGroupProviderData'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'}
    }

    def __init__(self, description=None, name=None, provider_data=None, type=None, variables=None):
        super(VariableGroupParameters, self).__init__()
        self.description = description
        self.name = name
        self.provider_data = provider_data
        self.type = type
        self.variables = variables


class VariableGroupProviderData(Model):

    _attribute_map = {
    }

    def __init__(self):
        super(VariableGroupProviderData, self).__init__()


class VariableValue(Model):

    _attribute_map = {
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_secret=None, value=None):
        super(VariableValue, self).__init__()
        self.is_secret = is_secret
        self.value = value


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
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBinding, self).__init__(callback_context_template=callback_context_template, callback_required_template=callback_required_template, data_source_name=data_source_name, endpoint_id=endpoint_id, endpoint_url=endpoint_url, headers=headers, initial_context_template=initial_context_template, parameters=parameters, result_selector=result_selector, result_template=result_template, target=target)


class DeploymentGroup(DeploymentGroupReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'description': {'key': 'description', 'type': 'str'},
        'machine_count': {'key': 'machineCount', 'type': 'int'},
        'machines': {'key': 'machines', 'type': '[DeploymentMachine]'},
        'machine_tags': {'key': 'machineTags', 'type': '[str]'}
    }

    def __init__(self, id=None, name=None, pool=None, project=None, description=None, machine_count=None, machines=None, machine_tags=None):
        super(DeploymentGroup, self).__init__(id=id, name=name, pool=pool, project=project)
        self.description = description
        self.machine_count = machine_count
        self.machines = machines
        self.machine_tags = machine_tags


class DeploymentMachineGroup(DeploymentMachineGroupReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'machines': {'key': 'machines', 'type': '[DeploymentMachine]'},
        'size': {'key': 'size', 'type': 'int'}
    }

    def __init__(self, id=None, name=None, pool=None, project=None, machines=None, size=None):
        super(DeploymentMachineGroup, self).__init__(id=id, name=name, pool=pool, project=project)
        self.machines = machines
        self.size = size


class KubernetesServiceGroup(ServiceGroup):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'environment_reference': {'key': 'environmentReference', 'type': 'EnvironmentReference'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_on=None, environment_reference=None, id=None, last_modified_by=None, last_modified_on=None, name=None, type=None, namespace=None, service_endpoint_id=None):
        super(KubernetesServiceGroup, self).__init__(created_by=created_by, created_on=created_on, environment_reference=environment_reference, id=id, last_modified_by=last_modified_by, last_modified_on=last_modified_on, name=name, type=type)
        self.namespace = namespace
        self.service_endpoint_id = service_endpoint_id


class TaskAgent(TaskAgentReference):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'access_point': {'key': 'accessPoint', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'os_description': {'key': 'osDescription', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'},
        'assigned_agent_cloud_request': {'key': 'assignedAgentCloudRequest', 'type': 'TaskAgentCloudRequest'},
        'assigned_request': {'key': 'assignedRequest', 'type': 'TaskAgentJobRequest'},
        'authorization': {'key': 'authorization', 'type': 'TaskAgentAuthorization'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'last_completed_request': {'key': 'lastCompletedRequest', 'type': 'TaskAgentJobRequest'},
        'max_parallelism': {'key': 'maxParallelism', 'type': 'int'},
        'pending_update': {'key': 'pendingUpdate', 'type': 'TaskAgentUpdate'},
        'properties': {'key': 'properties', 'type': 'object'},
        'status_changed_on': {'key': 'statusChangedOn', 'type': 'iso-8601'},
        'system_capabilities': {'key': 'systemCapabilities', 'type': '{str}'},
        'user_capabilities': {'key': 'userCapabilities', 'type': '{str}'}
    }

    def __init__(self, _links=None, access_point=None, enabled=None, id=None, name=None, os_description=None, provisioning_state=None, status=None, version=None, assigned_agent_cloud_request=None, assigned_request=None, authorization=None, created_on=None, last_completed_request=None, max_parallelism=None, pending_update=None, properties=None, status_changed_on=None, system_capabilities=None, user_capabilities=None):
        super(TaskAgent, self).__init__(_links=_links, access_point=access_point, enabled=enabled, id=id, name=name, os_description=os_description, provisioning_state=provisioning_state, status=status, version=version)
        self.assigned_agent_cloud_request = assigned_agent_cloud_request
        self.assigned_request = assigned_request
        self.authorization = authorization
        self.created_on = created_on
        self.last_completed_request = last_completed_request
        self.max_parallelism = max_parallelism
        self.pending_update = pending_update
        self.properties = properties
        self.status_changed_on = status_changed_on
        self.system_capabilities = system_capabilities
        self.user_capabilities = user_capabilities


class TaskAgentPool(TaskAgentPoolReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'pool_type': {'key': 'poolType', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'},
        'agent_cloud_id': {'key': 'agentCloudId', 'type': 'int'},
        'auto_provision': {'key': 'autoProvision', 'type': 'bool'},
        'auto_size': {'key': 'autoSize', 'type': 'bool'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'properties': {'key': 'properties', 'type': 'object'}
    }

    def __init__(self, id=None, is_hosted=None, name=None, pool_type=None, scope=None, size=None, agent_cloud_id=None, auto_provision=None, auto_size=None, created_by=None, created_on=None, owner=None, properties=None):
        super(TaskAgentPool, self).__init__(id=id, is_hosted=is_hosted, name=name, pool_type=pool_type, scope=scope, size=size)
        self.agent_cloud_id = agent_cloud_id
        self.auto_provision = auto_provision
        self.auto_size = auto_size
        self.created_by = created_by
        self.created_on = created_on
        self.owner = owner
        self.properties = properties


class TaskInputDefinition(TaskInputDefinitionBase):

    _attribute_map = {
        'aliases': {'key': 'aliases', 'type': '[str]'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'validation': {'key': 'validation', 'type': 'TaskInputValidation'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'},
    }

    def __init__(self, aliases=None, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinition, self).__init__(aliases=aliases, default_value=default_value, group_name=group_name, help_mark_down=help_mark_down, label=label, name=name, options=options, properties=properties, required=required, type=type, validation=validation, visible_rule=visible_rule)


class TaskSourceDefinition(TaskSourceDefinitionBase):

    _attribute_map = {
        'auth_key': {'key': 'authKey', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, auth_key=None, endpoint=None, key_selector=None, selector=None, target=None):
        super(TaskSourceDefinition, self).__init__(auth_key=auth_key, endpoint=endpoint, key_selector=key_selector, selector=selector, target=target)


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
    'DeploymentGroupCreateParameter',
    'DeploymentGroupCreateParameterPoolProperty',
    'DeploymentGroupMetrics',
    'DeploymentGroupReference',
    'DeploymentGroupUpdateParameter',
    'DeploymentMachine',
    'DeploymentMachineGroupReference',
    'DeploymentPoolSummary',
    'DeploymentTargetUpdateParameter',
    'EndpointAuthorization',
    'EndpointUrl',
    'Environment',
    'EnvironmentCreateParameter',
    'EnvironmentReference',
    'EnvironmentUpdateParameter',
    'GraphSubjectBase',
    'HelpLink',
    'IdentityRef',
    'InputDescriptor',
    'InputValidation',
    'InputValidationRequest',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'KubernetesServiceGroupCreateParameters',
    'MarketplacePurchasedLicense',
    'MetricsColumnMetaData',
    'MetricsColumnsHeader',
    'MetricsRow',
    'PackageMetadata',
    'PackageVersion',
    'ProjectReference',
    'PublishTaskGroupMetadata',
    'ReferenceLinks',
    'ResourceLimit',
    'ResourceUsage',
    'ResultTransformationDetails',
    'SecureFile',
    'ServiceEndpoint',
    'ServiceEndpointAuthenticationScheme',
    'ServiceEndpointDetails',
    'ServiceEndpointExecutionData',
    'ServiceEndpointExecutionRecord',
    'ServiceEndpointExecutionRecordsInput',
    'ServiceEndpointRequest',
    'ServiceEndpointRequestResult',
    'ServiceEndpointType',
    'ServiceGroup',
    'ServiceGroupReference',
    'TaskAgentAuthorization',
    'TaskAgentCloud',
    'TaskAgentCloudRequest',
    'TaskAgentCloudType',
    'TaskAgentDelaySource',
    'TaskAgentJobRequest',
    'TaskAgentMessage',
    'TaskAgentPoolMaintenanceDefinition',
    'TaskAgentPoolMaintenanceJob',
    'TaskAgentPoolMaintenanceJobTargetAgent',
    'TaskAgentPoolMaintenanceOptions',
    'TaskAgentPoolMaintenanceRetentionPolicy',
    'TaskAgentPoolMaintenanceSchedule',
    'TaskAgentPoolReference',
    'TaskAgentPublicKey',
    'TaskAgentQueue',
    'TaskAgentReference',
    'TaskAgentSession',
    'TaskAgentSessionKey',
    'TaskAgentUpdate',
    'TaskAgentUpdateReason',
    'TaskDefinition',
    'TaskDefinitionEndpoint',
    'TaskDefinitionReference',
    'TaskExecution',
    'TaskGroup',
    'TaskGroupCreateParameter',
    'TaskGroupDefinition',
    'TaskGroupRevision',
    'TaskGroupStep',
    'TaskGroupUpdateParameter',
    'TaskHubLicenseDetails',
    'TaskInputDefinitionBase',
    'TaskInputValidation',
    'TaskOrchestrationOwner',
    'TaskOutputVariable',
    'TaskPackageMetadata',
    'TaskReference',
    'TaskSourceDefinitionBase',
    'TaskVersion',
    'ValidationItem',
    'VariableGroup',
    'VariableGroupParameters',
    'VariableGroupProviderData',
    'VariableValue',
    'DataSourceBinding',
    'DeploymentGroup',
    'DeploymentMachineGroup',
    'KubernetesServiceGroup',
    'TaskAgent',
    'TaskAgentPool',
    'TaskInputDefinition',
    'TaskSourceDefinition',
]
