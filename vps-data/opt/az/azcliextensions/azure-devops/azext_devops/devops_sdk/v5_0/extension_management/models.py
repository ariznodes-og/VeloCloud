# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AcquisitionOperation(Model):

    _attribute_map = {
        'operation_state': {'key': 'operationState', 'type': 'object'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'str'},
        'reasons': {'key': 'reasons', 'type': '[AcquisitionOperationDisallowReason]'}
    }

    def __init__(self, operation_state=None, operation_type=None, reason=None, reasons=None):
        super(AcquisitionOperation, self).__init__()
        self.operation_state = operation_state
        self.operation_type = operation_type
        self.reason = reason
        self.reasons = reasons


class AcquisitionOperationDisallowReason(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, message=None, type=None):
        super(AcquisitionOperationDisallowReason, self).__init__()
        self.message = message
        self.type = type


class AcquisitionOptions(Model):

    _attribute_map = {
        'default_operation': {'key': 'defaultOperation', 'type': 'AcquisitionOperation'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'operations': {'key': 'operations', 'type': '[AcquisitionOperation]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, default_operation=None, item_id=None, operations=None, properties=None, target=None):
        super(AcquisitionOptions, self).__init__()
        self.default_operation = default_operation
        self.item_id = item_id
        self.operations = operations
        self.properties = properties
        self.target = target


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


class ExtensionAcquisitionRequest(Model):

    _attribute_map = {
        'assignment_type': {'key': 'assignmentType', 'type': 'object'},
        'billing_id': {'key': 'billingId', 'type': 'str'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'properties': {'key': 'properties', 'type': 'object'},
        'quantity': {'key': 'quantity', 'type': 'int'}
    }

    def __init__(self, assignment_type=None, billing_id=None, item_id=None, operation_type=None, properties=None, quantity=None):
        super(ExtensionAcquisitionRequest, self).__init__()
        self.assignment_type = assignment_type
        self.billing_id = billing_id
        self.item_id = item_id
        self.operation_type = operation_type
        self.properties = properties
        self.quantity = quantity


class ExtensionAuthorization(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'scopes': {'key': 'scopes', 'type': '[str]'}
    }

    def __init__(self, id=None, scopes=None):
        super(ExtensionAuthorization, self).__init__()
        self.id = id
        self.scopes = scopes


class ExtensionBadge(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'img_uri': {'key': 'imgUri', 'type': 'str'},
        'link': {'key': 'link', 'type': 'str'}
    }

    def __init__(self, description=None, img_uri=None, link=None):
        super(ExtensionBadge, self).__init__()
        self.description = description
        self.img_uri = img_uri
        self.link = link


class ExtensionDataCollection(Model):

    _attribute_map = {
        'collection_name': {'key': 'collectionName', 'type': 'str'},
        'documents': {'key': 'documents', 'type': '[object]'},
        'scope_type': {'key': 'scopeType', 'type': 'str'},
        'scope_value': {'key': 'scopeValue', 'type': 'str'}
    }

    def __init__(self, collection_name=None, documents=None, scope_type=None, scope_value=None):
        super(ExtensionDataCollection, self).__init__()
        self.collection_name = collection_name
        self.documents = documents
        self.scope_type = scope_type
        self.scope_value = scope_value


class ExtensionDataCollectionQuery(Model):

    _attribute_map = {
        'collections': {'key': 'collections', 'type': '[ExtensionDataCollection]'}
    }

    def __init__(self, collections=None):
        super(ExtensionDataCollectionQuery, self).__init__()
        self.collections = collections


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


class ExtensionIdentifier(Model):

    _attribute_map = {
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, extension_name=None, publisher_name=None):
        super(ExtensionIdentifier, self).__init__()
        self.extension_name = extension_name
        self.publisher_name = publisher_name


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


class ExtensionPolicy(Model):

    _attribute_map = {
        'install': {'key': 'install', 'type': 'object'},
        'request': {'key': 'request', 'type': 'object'}
    }

    def __init__(self, install=None, request=None):
        super(ExtensionPolicy, self).__init__()
        self.install = install
        self.request = request


class ExtensionRequest(Model):

    _attribute_map = {
        'reject_message': {'key': 'rejectMessage', 'type': 'str'},
        'request_date': {'key': 'requestDate', 'type': 'iso-8601'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'request_message': {'key': 'requestMessage', 'type': 'str'},
        'request_state': {'key': 'requestState', 'type': 'object'},
        'resolve_date': {'key': 'resolveDate', 'type': 'iso-8601'},
        'resolved_by': {'key': 'resolvedBy', 'type': 'IdentityRef'}
    }

    def __init__(self, reject_message=None, request_date=None, requested_by=None, request_message=None, request_state=None, resolve_date=None, resolved_by=None):
        super(ExtensionRequest, self).__init__()
        self.reject_message = reject_message
        self.request_date = request_date
        self.requested_by = requested_by
        self.request_message = request_message
        self.request_state = request_state
        self.resolve_date = resolve_date
        self.resolved_by = resolved_by


class ExtensionShare(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_org': {'key': 'isOrg', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, id=None, is_org=None, name=None, type=None):
        super(ExtensionShare, self).__init__()
        self.id = id
        self.is_org = is_org
        self.name = name
        self.type = type


class ExtensionStatistic(Model):

    _attribute_map = {
        'statistic_name': {'key': 'statisticName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'}
    }

    def __init__(self, statistic_name=None, value=None):
        super(ExtensionStatistic, self).__init__()
        self.statistic_name = statistic_name
        self.value = value


class ExtensionVersion(Model):

    _attribute_map = {
        'asset_uri': {'key': 'assetUri', 'type': 'str'},
        'badges': {'key': 'badges', 'type': '[ExtensionBadge]'},
        'fallback_asset_uri': {'key': 'fallbackAssetUri', 'type': 'str'},
        'files': {'key': 'files', 'type': '[ExtensionFile]'},
        'flags': {'key': 'flags', 'type': 'object'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': '[{ key: str; value: str }]'},
        'validation_result_message': {'key': 'validationResultMessage', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'version_description': {'key': 'versionDescription', 'type': 'str'}
    }

    def __init__(self, asset_uri=None, badges=None, fallback_asset_uri=None, files=None, flags=None, last_updated=None, properties=None, validation_result_message=None, version=None, version_description=None):
        super(ExtensionVersion, self).__init__()
        self.asset_uri = asset_uri
        self.badges = badges
        self.fallback_asset_uri = fallback_asset_uri
        self.files = files
        self.flags = flags
        self.last_updated = last_updated
        self.properties = properties
        self.validation_result_message = validation_result_message
        self.version = version
        self.version_description = version_description


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


class InstallationTarget(Model):

    _attribute_map = {
        'target': {'key': 'target', 'type': 'str'},
        'target_version': {'key': 'targetVersion', 'type': 'str'}
    }

    def __init__(self, target=None, target_version=None):
        super(InstallationTarget, self).__init__()
        self.target = target
        self.target_version = target_version


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


class InstalledExtensionQuery(Model):

    _attribute_map = {
        'asset_types': {'key': 'assetTypes', 'type': '[str]'},
        'monikers': {'key': 'monikers', 'type': '[ExtensionIdentifier]'}
    }

    def __init__(self, asset_types=None, monikers=None):
        super(InstalledExtensionQuery, self).__init__()
        self.asset_types = asset_types
        self.monikers = monikers


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


class PublishedExtension(Model):

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'deployment_type': {'key': 'deploymentType', 'type': 'object'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'flags': {'key': 'flags', 'type': 'object'},
        'installation_targets': {'key': 'installationTargets', 'type': '[InstallationTarget]'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'long_description': {'key': 'longDescription', 'type': 'str'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'publisher': {'key': 'publisher', 'type': 'PublisherFacts'},
        'release_date': {'key': 'releaseDate', 'type': 'iso-8601'},
        'shared_with': {'key': 'sharedWith', 'type': '[ExtensionShare]'},
        'short_description': {'key': 'shortDescription', 'type': 'str'},
        'statistics': {'key': 'statistics', 'type': '[ExtensionStatistic]'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'versions': {'key': 'versions', 'type': '[ExtensionVersion]'}
    }

    def __init__(self, categories=None, deployment_type=None, display_name=None, extension_id=None, extension_name=None, flags=None, installation_targets=None, last_updated=None, long_description=None, published_date=None, publisher=None, release_date=None, shared_with=None, short_description=None, statistics=None, tags=None, versions=None):
        super(PublishedExtension, self).__init__()
        self.categories = categories
        self.deployment_type = deployment_type
        self.display_name = display_name
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.flags = flags
        self.installation_targets = installation_targets
        self.last_updated = last_updated
        self.long_description = long_description
        self.published_date = published_date
        self.publisher = publisher
        self.release_date = release_date
        self.shared_with = shared_with
        self.short_description = short_description
        self.statistics = statistics
        self.tags = tags
        self.versions = versions


class PublisherFacts(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'flags': {'key': 'flags', 'type': 'object'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, display_name=None, flags=None, publisher_id=None, publisher_name=None):
        super(PublisherFacts, self).__init__()
        self.display_name = display_name
        self.flags = flags
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class RequestedExtension(Model):

    _attribute_map = {
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'extension_requests': {'key': 'extensionRequests', 'type': '[ExtensionRequest]'},
        'publisher_display_name': {'key': 'publisherDisplayName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'request_count': {'key': 'requestCount', 'type': 'int'}
    }

    def __init__(self, extension_name=None, extension_requests=None, publisher_display_name=None, publisher_name=None, request_count=None):
        super(RequestedExtension, self).__init__()
        self.extension_name = extension_name
        self.extension_requests = extension_requests
        self.publisher_display_name = publisher_display_name
        self.publisher_name = publisher_name
        self.request_count = request_count


class UserExtensionPolicy(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'ExtensionPolicy'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, display_name=None, permissions=None, user_id=None):
        super(UserExtensionPolicy, self).__init__()
        self.display_name = display_name
        self.permissions = permissions
        self.user_id = user_id


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


class ExtensionState(InstalledExtensionState):

    _attribute_map = {
        'flags': {'key': 'flags', 'type': 'object'},
        'installation_issues': {'key': 'installationIssues', 'type': '[InstalledExtensionStateIssue]'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'last_version_check': {'key': 'lastVersionCheck', 'type': 'iso-8601'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, flags=None, installation_issues=None, last_updated=None, extension_name=None, last_version_check=None, publisher_name=None, version=None):
        super(ExtensionState, self).__init__(flags=flags, installation_issues=installation_issues, last_updated=last_updated)
        self.extension_name = extension_name
        self.last_version_check = last_version_check
        self.publisher_name = publisher_name
        self.version = version


__all__ = [
    'AcquisitionOperation',
    'AcquisitionOperationDisallowReason',
    'AcquisitionOptions',
    'ContributionBase',
    'ContributionConstraint',
    'ContributionPropertyDescription',
    'ContributionType',
    'ExtensionAcquisitionRequest',
    'ExtensionAuthorization',
    'ExtensionBadge',
    'ExtensionDataCollection',
    'ExtensionDataCollectionQuery',
    'ExtensionEventCallback',
    'ExtensionEventCallbackCollection',
    'ExtensionFile',
    'ExtensionIdentifier',
    'ExtensionLicensing',
    'ExtensionManifest',
    'ExtensionPolicy',
    'ExtensionRequest',
    'ExtensionShare',
    'ExtensionStatistic',
    'ExtensionVersion',
    'GraphSubjectBase',
    'IdentityRef',
    'InstallationTarget',
    'InstalledExtension',
    'InstalledExtensionQuery',
    'InstalledExtensionState',
    'InstalledExtensionStateIssue',
    'LicensingOverride',
    'PublishedExtension',
    'PublisherFacts',
    'ReferenceLinks',
    'RequestedExtension',
    'UserExtensionPolicy',
    'Contribution',
    'ExtensionState',
]
