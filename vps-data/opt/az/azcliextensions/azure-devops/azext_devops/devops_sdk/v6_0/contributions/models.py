# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ClientContribution(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'includes': {'key': 'includes', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, includes=None, properties=None, targets=None, type=None):
        super(ClientContribution, self).__init__()
        self.description = description
        self.id = id
        self.includes = includes
        self.properties = properties
        self.targets = targets
        self.type = type


class ClientContributionNode(Model):

    _attribute_map = {
        'children': {'key': 'children', 'type': '[str]'},
        'contribution': {'key': 'contribution', 'type': 'ClientContribution'},
        'parents': {'key': 'parents', 'type': '[str]'}
    }

    def __init__(self, children=None, contribution=None, parents=None):
        super(ClientContributionNode, self).__init__()
        self.children = children
        self.contribution = contribution
        self.parents = parents


class ClientContributionProviderDetails(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, display_name=None, name=None, properties=None, version=None):
        super(ClientContributionProviderDetails, self).__init__()
        self.display_name = display_name
        self.name = name
        self.properties = properties
        self.version = version


class ContributionBase(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'visible_to': {'key': 'visibleTo', 'type': '[str]'}
    }

    def __init__(self, description=None, id=None, visible_to=None):
        super(ContributionBase, self).__init__()
        self.description = description
        self.id = id
        self.visible_to = visible_to


class ContributionConstraint(Model):

    _attribute_map = {
        'group': {'key': 'group', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'inverse': {'key': 'inverse', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'relationships': {'key': 'relationships', 'type': '[str]'}
    }

    def __init__(self, group=None, id=None, inverse=None, name=None, properties=None, relationships=None):
        super(ContributionConstraint, self).__init__()
        self.group = group
        self.id = id
        self.inverse = inverse
        self.name = name
        self.properties = properties
        self.relationships = relationships


class ContributionNodeQuery(Model):

    _attribute_map = {
        'contribution_ids': {'key': 'contributionIds', 'type': '[str]'},
        'data_provider_context': {'key': 'dataProviderContext', 'type': 'DataProviderContext'},
        'include_provider_details': {'key': 'includeProviderDetails', 'type': 'bool'},
        'query_options': {'key': 'queryOptions', 'type': 'object'}
    }

    def __init__(self, contribution_ids=None, data_provider_context=None, include_provider_details=None, query_options=None):
        super(ContributionNodeQuery, self).__init__()
        self.contribution_ids = contribution_ids
        self.data_provider_context = data_provider_context
        self.include_provider_details = include_provider_details
        self.query_options = query_options


class ContributionNodeQueryResult(Model):

    _attribute_map = {
        'nodes': {'key': 'nodes', 'type': '{ClientContributionNode}'},
        'provider_details': {'key': 'providerDetails', 'type': '{ClientContributionProviderDetails}'}
    }

    def __init__(self, nodes=None, provider_details=None):
        super(ContributionNodeQueryResult, self).__init__()
        self.nodes = nodes
        self.provider_details = provider_details


class ContributionPropertyDescription(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, name=None, required=None, type=None):
        super(ContributionPropertyDescription, self).__init__()
        self.description = description
        self.name = name
        self.required = required
        self.type = type


class ContributionType(ContributionBase):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'visible_to': {'key': 'visibleTo', 'type': '[str]'},
        'indexed': {'key': 'indexed', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{ContributionPropertyDescription}'}
    }

    def __init__(self, description=None, id=None, visible_to=None, indexed=None, name=None, properties=None):
        super(ContributionType, self).__init__(description=description, id=id, visible_to=visible_to)
        self.indexed = indexed
        self.name = name
        self.properties = properties


class DataProviderContext(Model):

    _attribute_map = {
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, properties=None):
        super(DataProviderContext, self).__init__()
        self.properties = properties


class DataProviderExceptionDetails(Model):

    _attribute_map = {
        'exception_type': {'key': 'exceptionType', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'}
    }

    def __init__(self, exception_type=None, message=None, stack_trace=None):
        super(DataProviderExceptionDetails, self).__init__()
        self.exception_type = exception_type
        self.message = message
        self.stack_trace = stack_trace


class DataProviderQuery(Model):

    _attribute_map = {
        'context': {'key': 'context', 'type': 'DataProviderContext'},
        'contribution_ids': {'key': 'contributionIds', 'type': '[str]'}
    }

    def __init__(self, context=None, contribution_ids=None):
        super(DataProviderQuery, self).__init__()
        self.context = context
        self.contribution_ids = contribution_ids


class DataProviderResult(Model):

    _attribute_map = {
        'client_providers': {'key': 'clientProviders', 'type': '{ClientDataProviderQuery}'},
        'data': {'key': 'data', 'type': '{object}'},
        'exceptions': {'key': 'exceptions', 'type': '{DataProviderExceptionDetails}'},
        'resolved_providers': {'key': 'resolvedProviders', 'type': '[ResolvedDataProvider]'},
        'scope_name': {'key': 'scopeName', 'type': 'str'},
        'scope_value': {'key': 'scopeValue', 'type': 'str'},
        'shared_data': {'key': 'sharedData', 'type': '{object}'}
    }

    def __init__(self, client_providers=None, data=None, exceptions=None, resolved_providers=None, scope_name=None, scope_value=None, shared_data=None):
        super(DataProviderResult, self).__init__()
        self.client_providers = client_providers
        self.data = data
        self.exceptions = exceptions
        self.resolved_providers = resolved_providers
        self.scope_name = scope_name
        self.scope_value = scope_value
        self.shared_data = shared_data


class ExtensionEventCallback(Model):

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, uri=None):
        super(ExtensionEventCallback, self).__init__()
        self.uri = uri


class ExtensionEventCallbackCollection(Model):

    _attribute_map = {
        'post_disable': {'key': 'postDisable', 'type': 'ExtensionEventCallback'},
        'post_enable': {'key': 'postEnable', 'type': 'ExtensionEventCallback'},
        'post_install': {'key': 'postInstall', 'type': 'ExtensionEventCallback'},
        'post_uninstall': {'key': 'postUninstall', 'type': 'ExtensionEventCallback'},
        'post_update': {'key': 'postUpdate', 'type': 'ExtensionEventCallback'},
        'pre_install': {'key': 'preInstall', 'type': 'ExtensionEventCallback'},
        'version_check': {'key': 'versionCheck', 'type': 'ExtensionEventCallback'}
    }

    def __init__(self, post_disable=None, post_enable=None, post_install=None, post_uninstall=None, post_update=None, pre_install=None, version_check=None):
        super(ExtensionEventCallbackCollection, self).__init__()
        self.post_disable = post_disable
        self.post_enable = post_enable
        self.post_install = post_install
        self.post_uninstall = post_uninstall
        self.post_update = post_update
        self.pre_install = pre_install
        self.version_check = version_check


class ExtensionFile(Model):

    _attribute_map = {
        'asset_type': {'key': 'assetType', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'}
    }

    def __init__(self, asset_type=None, language=None, source=None):
        super(ExtensionFile, self).__init__()
        self.asset_type = asset_type
        self.language = language
        self.source = source


class ExtensionLicensing(Model):

    _attribute_map = {
        'overrides': {'key': 'overrides', 'type': '[LicensingOverride]'}
    }

    def __init__(self, overrides=None):
        super(ExtensionLicensing, self).__init__()
        self.overrides = overrides


class ExtensionManifest(Model):

    _attribute_map = {
        'base_uri': {'key': 'baseUri', 'type': 'str'},
        'constraints': {'key': 'constraints', 'type': '[ContributionConstraint]'},
        'contributions': {'key': 'contributions', 'type': '[Contribution]'},
        'contribution_types': {'key': 'contributionTypes', 'type': '[ContributionType]'},
        'demands': {'key': 'demands', 'type': '[str]'},
        'event_callbacks': {'key': 'eventCallbacks', 'type': 'ExtensionEventCallbackCollection'},
        'fallback_base_uri': {'key': 'fallbackBaseUri', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'licensing': {'key': 'licensing', 'type': 'ExtensionLicensing'},
        'manifest_version': {'key': 'manifestVersion', 'type': 'float'},
        'restricted_to': {'key': 'restrictedTo', 'type': '[str]'},
        'scopes': {'key': 'scopes', 'type': '[str]'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'}
    }

    def __init__(self, base_uri=None, constraints=None, contributions=None, contribution_types=None, demands=None, event_callbacks=None, fallback_base_uri=None, language=None, licensing=None, manifest_version=None, restricted_to=None, scopes=None, service_instance_type=None):
        super(ExtensionManifest, self).__init__()
        self.base_uri = base_uri
        self.constraints = constraints
        self.contributions = contributions
        self.contribution_types = contribution_types
        self.demands = demands
        self.event_callbacks = event_callbacks
        self.fallback_base_uri = fallback_base_uri
        self.language = language
        self.licensing = licensing
        self.manifest_version = manifest_version
        self.restricted_to = restricted_to
        self.scopes = scopes
        self.service_instance_type = service_instance_type


class InstalledExtension(ExtensionManifest):

    _attribute_map = {
        'base_uri': {'key': 'baseUri', 'type': 'str'},
        'constraints': {'key': 'constraints', 'type': '[ContributionConstraint]'},
        'contributions': {'key': 'contributions', 'type': '[Contribution]'},
        'contribution_types': {'key': 'contributionTypes', 'type': '[ContributionType]'},
        'demands': {'key': 'demands', 'type': '[str]'},
        'event_callbacks': {'key': 'eventCallbacks', 'type': 'ExtensionEventCallbackCollection'},
        'fallback_base_uri': {'key': 'fallbackBaseUri', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'licensing': {'key': 'licensing', 'type': 'ExtensionLicensing'},
        'manifest_version': {'key': 'manifestVersion', 'type': 'float'},
        'restricted_to': {'key': 'restrictedTo', 'type': '[str]'},
        'scopes': {'key': 'scopes', 'type': '[str]'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'files': {'key': 'files', 'type': '[ExtensionFile]'},
        'flags': {'key': 'flags', 'type': 'object'},
        'install_state': {'key': 'installState', 'type': 'InstalledExtensionState'},
        'last_published': {'key': 'lastPublished', 'type': 'iso-8601'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'registration_id': {'key': 'registrationId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, base_uri=None, constraints=None, contributions=None, contribution_types=None, demands=None, event_callbacks=None, fallback_base_uri=None, language=None, licensing=None, manifest_version=None, restricted_to=None, scopes=None, service_instance_type=None, extension_id=None, extension_name=None, files=None, flags=None, install_state=None, last_published=None, publisher_id=None, publisher_name=None, registration_id=None, version=None):
        super(InstalledExtension, self).__init__(base_uri=base_uri, constraints=constraints, contributions=contributions, contribution_types=contribution_types, demands=demands, event_callbacks=event_callbacks, fallback_base_uri=fallback_base_uri, language=language, licensing=licensing, manifest_version=manifest_version, restricted_to=restricted_to, scopes=scopes, service_instance_type=service_instance_type)
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.files = files
        self.flags = flags
        self.install_state = install_state
        self.last_published = last_published
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        self.registration_id = registration_id
        self.version = version


class InstalledExtensionState(Model):

    _attribute_map = {
        'flags': {'key': 'flags', 'type': 'object'},
        'installation_issues': {'key': 'installationIssues', 'type': '[InstalledExtensionStateIssue]'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'}
    }

    def __init__(self, flags=None, installation_issues=None, last_updated=None):
        super(InstalledExtensionState, self).__init__()
        self.flags = flags
        self.installation_issues = installation_issues
        self.last_updated = last_updated


class InstalledExtensionStateIssue(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, message=None, source=None, type=None):
        super(InstalledExtensionStateIssue, self).__init__()
        self.message = message
        self.source = source
        self.type = type


class LicensingOverride(Model):

    _attribute_map = {
        'behavior': {'key': 'behavior', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, behavior=None, id=None):
        super(LicensingOverride, self).__init__()
        self.behavior = behavior
        self.id = id


class ResolvedDataProvider(Model):

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'float'},
        'error': {'key': 'error', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, duration=None, error=None, id=None):
        super(ResolvedDataProvider, self).__init__()
        self.duration = duration
        self.error = error
        self.id = id


class ClientDataProviderQuery(DataProviderQuery):

    _attribute_map = {
        'context': {'key': 'context', 'type': 'DataProviderContext'},
        'contribution_ids': {'key': 'contributionIds', 'type': '[str]'},
        'query_service_instance_type': {'key': 'queryServiceInstanceType', 'type': 'str'}
    }

    def __init__(self, context=None, contribution_ids=None, query_service_instance_type=None):
        super(ClientDataProviderQuery, self).__init__(context=context, contribution_ids=contribution_ids)
        self.query_service_instance_type = query_service_instance_type


class Contribution(ContributionBase):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'visible_to': {'key': 'visibleTo', 'type': '[str]'},
        'constraints': {'key': 'constraints', 'type': '[ContributionConstraint]'},
        'includes': {'key': 'includes', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'restricted_to': {'key': 'restrictedTo', 'type': '[str]'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, visible_to=None, constraints=None, includes=None, properties=None, restricted_to=None, targets=None, type=None):
        super(Contribution, self).__init__(description=description, id=id, visible_to=visible_to)
        self.constraints = constraints
        self.includes = includes
        self.properties = properties
        self.restricted_to = restricted_to
        self.targets = targets
        self.type = type


__all__ = [
    'ClientContribution',
    'ClientContributionNode',
    'ClientContributionProviderDetails',
    'ContributionBase',
    'ContributionConstraint',
    'ContributionNodeQuery',
    'ContributionNodeQueryResult',
    'ContributionPropertyDescription',
    'ContributionType',
    'DataProviderContext',
    'DataProviderExceptionDetails',
    'DataProviderQuery',
    'DataProviderResult',
    'ExtensionEventCallback',
    'ExtensionEventCallbackCollection',
    'ExtensionFile',
    'ExtensionLicensing',
    'ExtensionManifest',
    'InstalledExtension',
    'InstalledExtensionState',
    'InstalledExtensionStateIssue',
    'LicensingOverride',
    'ResolvedDataProvider',
    'ClientDataProviderQuery',
    'Contribution',
]
