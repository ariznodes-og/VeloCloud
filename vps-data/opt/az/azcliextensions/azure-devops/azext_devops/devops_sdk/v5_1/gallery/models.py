# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AcquisitionOperation(Model):

    _attribute_map = {
        'operation_state': {'key': 'operationState', 'type': 'object'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'str'}
    }

    def __init__(self, operation_state=None, operation_type=None, reason=None):
        super(AcquisitionOperation, self).__init__()
        self.operation_state = operation_state
        self.operation_type = operation_type
        self.reason = reason


class AcquisitionOptions(Model):

    _attribute_map = {
        'default_operation': {'key': 'defaultOperation', 'type': 'AcquisitionOperation'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'operations': {'key': 'operations', 'type': '[AcquisitionOperation]'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, default_operation=None, item_id=None, operations=None, target=None):
        super(AcquisitionOptions, self).__init__()
        self.default_operation = default_operation
        self.item_id = item_id
        self.operations = operations
        self.target = target


class Answers(Model):

    _attribute_map = {
        'vs_marketplace_extension_name': {'key': 'vsMarketplaceExtensionName', 'type': 'str'},
        'vs_marketplace_publisher_name': {'key': 'vsMarketplacePublisherName', 'type': 'str'}
    }

    def __init__(self, vs_marketplace_extension_name=None, vs_marketplace_publisher_name=None):
        super(Answers, self).__init__()
        self.vs_marketplace_extension_name = vs_marketplace_extension_name
        self.vs_marketplace_publisher_name = vs_marketplace_publisher_name


class AssetDetails(Model):

    _attribute_map = {
        'answers': {'key': 'answers', 'type': 'Answers'},
        'publisher_natural_identifier': {'key': 'publisherNaturalIdentifier', 'type': 'str'}
    }

    def __init__(self, answers=None, publisher_natural_identifier=None):
        super(AssetDetails, self).__init__()
        self.answers = answers
        self.publisher_natural_identifier = publisher_natural_identifier


class AzurePublisher(Model):

    _attribute_map = {
        'azure_publisher_id': {'key': 'azurePublisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, azure_publisher_id=None, publisher_name=None):
        super(AzurePublisher, self).__init__()
        self.azure_publisher_id = azure_publisher_id
        self.publisher_name = publisher_name


class AzureRestApiRequestModel(Model):

    _attribute_map = {
        'asset_details': {'key': 'assetDetails', 'type': 'AssetDetails'},
        'asset_id': {'key': 'assetId', 'type': 'str'},
        'asset_version': {'key': 'assetVersion', 'type': 'long'},
        'customer_support_email': {'key': 'customerSupportEmail', 'type': 'str'},
        'integration_contact_email': {'key': 'integrationContactEmail', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, asset_details=None, asset_id=None, asset_version=None, customer_support_email=None, integration_contact_email=None, operation=None, plan_id=None, publisher_id=None, type=None):
        super(AzureRestApiRequestModel, self).__init__()
        self.asset_details = asset_details
        self.asset_id = asset_id
        self.asset_version = asset_version
        self.customer_support_email = customer_support_email
        self.integration_contact_email = integration_contact_email
        self.operation = operation
        self.plan_id = plan_id
        self.publisher_id = publisher_id
        self.type = type


class CategoriesResult(Model):

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[ExtensionCategory]'}
    }

    def __init__(self, categories=None):
        super(CategoriesResult, self).__init__()
        self.categories = categories


class CategoryLanguageTitle(Model):

    _attribute_map = {
        'lang': {'key': 'lang', 'type': 'str'},
        'lcid': {'key': 'lcid', 'type': 'int'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, lang=None, lcid=None, title=None):
        super(CategoryLanguageTitle, self).__init__()
        self.lang = lang
        self.lcid = lcid
        self.title = title


class EventCounts(Model):

    _attribute_map = {
        'average_rating': {'key': 'averageRating', 'type': 'int'},
        'buy_count': {'key': 'buyCount', 'type': 'int'},
        'connected_buy_count': {'key': 'connectedBuyCount', 'type': 'int'},
        'connected_install_count': {'key': 'connectedInstallCount', 'type': 'int'},
        'install_count': {'key': 'installCount', 'type': 'long'},
        'try_count': {'key': 'tryCount', 'type': 'int'},
        'uninstall_count': {'key': 'uninstallCount', 'type': 'int'},
        'web_download_count': {'key': 'webDownloadCount', 'type': 'long'},
        'web_page_views': {'key': 'webPageViews', 'type': 'long'}
    }

    def __init__(self, average_rating=None, buy_count=None, connected_buy_count=None, connected_install_count=None, install_count=None, try_count=None, uninstall_count=None, web_download_count=None, web_page_views=None):
        super(EventCounts, self).__init__()
        self.average_rating = average_rating
        self.buy_count = buy_count
        self.connected_buy_count = connected_buy_count
        self.connected_install_count = connected_install_count
        self.install_count = install_count
        self.try_count = try_count
        self.uninstall_count = uninstall_count
        self.web_download_count = web_download_count
        self.web_page_views = web_page_views


class ExtensionAcquisitionRequest(Model):

    _attribute_map = {
        'assignment_type': {'key': 'assignmentType', 'type': 'object'},
        'billing_id': {'key': 'billingId', 'type': 'str'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'properties': {'key': 'properties', 'type': 'object'},
        'quantity': {'key': 'quantity', 'type': 'int'},
        'targets': {'key': 'targets', 'type': '[str]'}
    }

    def __init__(self, assignment_type=None, billing_id=None, item_id=None, operation_type=None, properties=None, quantity=None, targets=None):
        super(ExtensionAcquisitionRequest, self).__init__()
        self.assignment_type = assignment_type
        self.billing_id = billing_id
        self.item_id = item_id
        self.operation_type = operation_type
        self.properties = properties
        self.quantity = quantity
        self.targets = targets


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


class ExtensionCategory(Model):

    _attribute_map = {
        'associated_products': {'key': 'associatedProducts', 'type': '[str]'},
        'category_id': {'key': 'categoryId', 'type': 'int'},
        'category_name': {'key': 'categoryName', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'language_titles': {'key': 'languageTitles', 'type': '[CategoryLanguageTitle]'},
        'parent_category_name': {'key': 'parentCategoryName', 'type': 'str'}
    }

    def __init__(self, associated_products=None, category_id=None, category_name=None, language=None, language_titles=None, parent_category_name=None):
        super(ExtensionCategory, self).__init__()
        self.associated_products = associated_products
        self.category_id = category_id
        self.category_name = category_name
        self.language = language
        self.language_titles = language_titles
        self.parent_category_name = parent_category_name


class ExtensionDailyStat(Model):

    _attribute_map = {
        'counts': {'key': 'counts', 'type': 'EventCounts'},
        'extended_stats': {'key': 'extendedStats', 'type': '{object}'},
        'statistic_date': {'key': 'statisticDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, counts=None, extended_stats=None, statistic_date=None, version=None):
        super(ExtensionDailyStat, self).__init__()
        self.counts = counts
        self.extended_stats = extended_stats
        self.statistic_date = statistic_date
        self.version = version


class ExtensionDailyStats(Model):

    _attribute_map = {
        'daily_stats': {'key': 'dailyStats', 'type': '[ExtensionDailyStat]'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'stat_count': {'key': 'statCount', 'type': 'int'}
    }

    def __init__(self, daily_stats=None, extension_id=None, extension_name=None, publisher_name=None, stat_count=None):
        super(ExtensionDailyStats, self).__init__()
        self.daily_stats = daily_stats
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.publisher_name = publisher_name
        self.stat_count = stat_count


class ExtensionDraft(Model):

    _attribute_map = {
        'assets': {'key': 'assets', 'type': '[ExtensionDraftAsset]'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'draft_state': {'key': 'draftState', 'type': 'object'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'payload': {'key': 'payload', 'type': 'ExtensionPayload'},
        'product': {'key': 'product', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'validation_errors': {'key': 'validationErrors', 'type': '[{ key: str; value: str }]'},
        'validation_warnings': {'key': 'validationWarnings', 'type': '[{ key: str; value: str }]'}
    }

    def __init__(self, assets=None, created_date=None, draft_state=None, extension_name=None, id=None, last_updated=None, payload=None, product=None, publisher_name=None, validation_errors=None, validation_warnings=None):
        super(ExtensionDraft, self).__init__()
        self.assets = assets
        self.created_date = created_date
        self.draft_state = draft_state
        self.extension_name = extension_name
        self.id = id
        self.last_updated = last_updated
        self.payload = payload
        self.product = product
        self.publisher_name = publisher_name
        self.validation_errors = validation_errors
        self.validation_warnings = validation_warnings


class ExtensionDraftPatch(Model):

    _attribute_map = {
        'extension_data': {'key': 'extensionData', 'type': 'UnpackagedExtensionData'},
        'operation': {'key': 'operation', 'type': 'object'}
    }

    def __init__(self, extension_data=None, operation=None):
        super(ExtensionDraftPatch, self).__init__()
        self.extension_data = extension_data
        self.operation = operation


class ExtensionEvent(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'long'},
        'properties': {'key': 'properties', 'type': 'object'},
        'statistic_date': {'key': 'statisticDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, properties=None, statistic_date=None, version=None):
        super(ExtensionEvent, self).__init__()
        self.id = id
        self.properties = properties
        self.statistic_date = statistic_date
        self.version = version


class ExtensionEvents(Model):

    _attribute_map = {
        'events': {'key': 'events', 'type': '{[ExtensionEvent]}'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, events=None, extension_id=None, extension_name=None, publisher_name=None):
        super(ExtensionEvents, self).__init__()
        self.events = events
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.publisher_name = publisher_name


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


class ExtensionFilterResult(Model):

    _attribute_map = {
        'extensions': {'key': 'extensions', 'type': '[PublishedExtension]'},
        'paging_token': {'key': 'pagingToken', 'type': 'str'},
        'result_metadata': {'key': 'resultMetadata', 'type': '[ExtensionFilterResultMetadata]'}
    }

    def __init__(self, extensions=None, paging_token=None, result_metadata=None):
        super(ExtensionFilterResult, self).__init__()
        self.extensions = extensions
        self.paging_token = paging_token
        self.result_metadata = result_metadata


class ExtensionFilterResultMetadata(Model):

    _attribute_map = {
        'metadata_items': {'key': 'metadataItems', 'type': '[MetadataItem]'},
        'metadata_type': {'key': 'metadataType', 'type': 'str'}
    }

    def __init__(self, metadata_items=None, metadata_type=None):
        super(ExtensionFilterResultMetadata, self).__init__()
        self.metadata_items = metadata_items
        self.metadata_type = metadata_type


class ExtensionPackage(Model):

    _attribute_map = {
        'extension_manifest': {'key': 'extensionManifest', 'type': 'str'}
    }

    def __init__(self, extension_manifest=None):
        super(ExtensionPackage, self).__init__()
        self.extension_manifest = extension_manifest


class ExtensionPayload(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'installation_targets': {'key': 'installationTargets', 'type': '[InstallationTarget]'},
        'is_preview': {'key': 'isPreview', 'type': 'bool'},
        'is_signed_by_microsoft': {'key': 'isSignedByMicrosoft', 'type': 'bool'},
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'metadata': {'key': 'metadata', 'type': '[{ key: str; value: str }]'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, display_name=None, file_name=None, installation_targets=None, is_preview=None, is_signed_by_microsoft=None, is_valid=None, metadata=None, type=None):
        super(ExtensionPayload, self).__init__()
        self.description = description
        self.display_name = display_name
        self.file_name = file_name
        self.installation_targets = installation_targets
        self.is_preview = is_preview
        self.is_signed_by_microsoft = is_signed_by_microsoft
        self.is_valid = is_valid
        self.metadata = metadata
        self.type = type


class ExtensionQuery(Model):

    _attribute_map = {
        'asset_types': {'key': 'assetTypes', 'type': '[str]'},
        'filters': {'key': 'filters', 'type': '[QueryFilter]'},
        'flags': {'key': 'flags', 'type': 'object'}
    }

    def __init__(self, asset_types=None, filters=None, flags=None):
        super(ExtensionQuery, self).__init__()
        self.asset_types = asset_types
        self.filters = filters
        self.flags = flags


class ExtensionQueryResult(Model):

    _attribute_map = {
        'results': {'key': 'results', 'type': '[ExtensionFilterResult]'}
    }

    def __init__(self, results=None):
        super(ExtensionQueryResult, self).__init__()
        self.results = results


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


class ExtensionStatisticUpdate(Model):

    _attribute_map = {
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'object'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'statistic': {'key': 'statistic', 'type': 'ExtensionStatistic'}
    }

    def __init__(self, extension_name=None, operation=None, publisher_name=None, statistic=None):
        super(ExtensionStatisticUpdate, self).__init__()
        self.extension_name = extension_name
        self.operation = operation
        self.publisher_name = publisher_name
        self.statistic = statistic


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


class FilterCriteria(Model):

    _attribute_map = {
        'filter_type': {'key': 'filterType', 'type': 'int'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, filter_type=None, value=None):
        super(FilterCriteria, self).__init__()
        self.filter_type = filter_type
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


class MetadataItem(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, count=None, name=None):
        super(MetadataItem, self).__init__()
        self.count = count
        self.name = name


class NotificationsData(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': '{object}'},
        'identities': {'key': 'identities', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, data=None, identities=None, type=None):
        super(NotificationsData, self).__init__()
        self.data = data
        self.identities = identities
        self.type = type


class ProductCategoriesResult(Model):

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[ProductCategory]'}
    }

    def __init__(self, categories=None):
        super(ProductCategoriesResult, self).__init__()
        self.categories = categories


class ProductCategory(Model):

    _attribute_map = {
        'children': {'key': 'children', 'type': '[ProductCategory]'},
        'has_children': {'key': 'hasChildren', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, children=None, has_children=None, id=None, title=None):
        super(ProductCategory, self).__init__()
        self.children = children
        self.has_children = has_children
        self.id = id
        self.title = title


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


class PublisherBase(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': '[str]'},
        'extensions': {'key': 'extensions', 'type': '[PublishedExtension]'},
        'flags': {'key': 'flags', 'type': 'object'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'long_description': {'key': 'longDescription', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'short_description': {'key': 'shortDescription', 'type': 'str'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, display_name=None, email_address=None, extensions=None, flags=None, last_updated=None, long_description=None, publisher_id=None, publisher_name=None, short_description=None, state=None):
        super(PublisherBase, self).__init__()
        self.display_name = display_name
        self.email_address = email_address
        self.extensions = extensions
        self.flags = flags
        self.last_updated = last_updated
        self.long_description = long_description
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        self.short_description = short_description
        self.state = state


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


class PublisherFilterResult(Model):

    _attribute_map = {
        'publishers': {'key': 'publishers', 'type': '[Publisher]'}
    }

    def __init__(self, publishers=None):
        super(PublisherFilterResult, self).__init__()
        self.publishers = publishers


class PublisherQuery(Model):

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '[QueryFilter]'},
        'flags': {'key': 'flags', 'type': 'object'}
    }

    def __init__(self, filters=None, flags=None):
        super(PublisherQuery, self).__init__()
        self.filters = filters
        self.flags = flags


class PublisherQueryResult(Model):

    _attribute_map = {
        'results': {'key': 'results', 'type': '[PublisherFilterResult]'}
    }

    def __init__(self, results=None):
        super(PublisherQueryResult, self).__init__()
        self.results = results


class PublisherRoleAssignment(Model):

    _attribute_map = {
        'access': {'key': 'access', 'type': 'object'},
        'access_display_name': {'key': 'accessDisplayName', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'IdentityRef'},
        'role': {'key': 'role', 'type': 'PublisherSecurityRole'}
    }

    def __init__(self, access=None, access_display_name=None, identity=None, role=None):
        super(PublisherRoleAssignment, self).__init__()
        self.access = access
        self.access_display_name = access_display_name
        self.identity = identity
        self.role = role


class PublisherSecurityRole(Model):

    _attribute_map = {
        'allow_permissions': {'key': 'allowPermissions', 'type': 'int'},
        'deny_permissions': {'key': 'denyPermissions', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'}
    }

    def __init__(self, allow_permissions=None, deny_permissions=None, description=None, display_name=None, identifier=None, name=None, scope=None):
        super(PublisherSecurityRole, self).__init__()
        self.allow_permissions = allow_permissions
        self.deny_permissions = deny_permissions
        self.description = description
        self.display_name = display_name
        self.identifier = identifier
        self.name = name
        self.scope = scope


class PublisherUserRoleAssignmentRef(Model):

    _attribute_map = {
        'role_name': {'key': 'roleName', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, role_name=None, unique_name=None, user_id=None):
        super(PublisherUserRoleAssignmentRef, self).__init__()
        self.role_name = role_name
        self.unique_name = unique_name
        self.user_id = user_id


class QnAItem(Model):

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'status': {'key': 'status', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'UserIdentityRef'}
    }

    def __init__(self, created_date=None, id=None, status=None, text=None, updated_date=None, user=None):
        super(QnAItem, self).__init__()
        self.created_date = created_date
        self.id = id
        self.status = status
        self.text = text
        self.updated_date = updated_date
        self.user = user


class QueryFilter(Model):

    _attribute_map = {
        'criteria': {'key': 'criteria', 'type': '[FilterCriteria]'},
        'direction': {'key': 'direction', 'type': 'object'},
        'page_number': {'key': 'pageNumber', 'type': 'int'},
        'page_size': {'key': 'pageSize', 'type': 'int'},
        'paging_token': {'key': 'pagingToken', 'type': 'str'},
        'sort_by': {'key': 'sortBy', 'type': 'int'},
        'sort_order': {'key': 'sortOrder', 'type': 'int'}
    }

    def __init__(self, criteria=None, direction=None, page_number=None, page_size=None, paging_token=None, sort_by=None, sort_order=None):
        super(QueryFilter, self).__init__()
        self.criteria = criteria
        self.direction = direction
        self.page_number = page_number
        self.page_size = page_size
        self.paging_token = paging_token
        self.sort_by = sort_by
        self.sort_order = sort_order


class Question(QnAItem):

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'status': {'key': 'status', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'UserIdentityRef'},
        'responses': {'key': 'responses', 'type': '[Response]'}
    }

    def __init__(self, created_date=None, id=None, status=None, text=None, updated_date=None, user=None, responses=None):
        super(Question, self).__init__(created_date=created_date, id=id, status=status, text=text, updated_date=updated_date, user=user)
        self.responses = responses


class QuestionsResult(Model):

    _attribute_map = {
        'has_more_questions': {'key': 'hasMoreQuestions', 'type': 'bool'},
        'questions': {'key': 'questions', 'type': '[Question]'}
    }

    def __init__(self, has_more_questions=None, questions=None):
        super(QuestionsResult, self).__init__()
        self.has_more_questions = has_more_questions
        self.questions = questions


class RatingCountPerRating(Model):

    _attribute_map = {
        'rating': {'key': 'rating', 'type': 'str'},
        'rating_count': {'key': 'ratingCount', 'type': 'long'}
    }

    def __init__(self, rating=None, rating_count=None):
        super(RatingCountPerRating, self).__init__()
        self.rating = rating
        self.rating_count = rating_count


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class Response(QnAItem):

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'status': {'key': 'status', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'UserIdentityRef'},
    }

    def __init__(self, created_date=None, id=None, status=None, text=None, updated_date=None, user=None):
        super(Response, self).__init__(created_date=created_date, id=id, status=status, text=text, updated_date=updated_date, user=user)


class Review(Model):

    _attribute_map = {
        'admin_reply': {'key': 'adminReply', 'type': 'ReviewReply'},
        'id': {'key': 'id', 'type': 'long'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_ignored': {'key': 'isIgnored', 'type': 'bool'},
        'product_version': {'key': 'productVersion', 'type': 'str'},
        'rating': {'key': 'rating', 'type': 'str'},
        'reply': {'key': 'reply', 'type': 'ReviewReply'},
        'text': {'key': 'text', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user_display_name': {'key': 'userDisplayName', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, admin_reply=None, id=None, is_deleted=None, is_ignored=None, product_version=None, rating=None, reply=None, text=None, title=None, updated_date=None, user_display_name=None, user_id=None):
        super(Review, self).__init__()
        self.admin_reply = admin_reply
        self.id = id
        self.is_deleted = is_deleted
        self.is_ignored = is_ignored
        self.product_version = product_version
        self.rating = rating
        self.reply = reply
        self.text = text
        self.title = title
        self.updated_date = updated_date
        self.user_display_name = user_display_name
        self.user_id = user_id


class ReviewPatch(Model):

    _attribute_map = {
        'operation': {'key': 'operation', 'type': 'object'},
        'reported_concern': {'key': 'reportedConcern', 'type': 'UserReportedConcern'},
        'review_item': {'key': 'reviewItem', 'type': 'Review'}
    }

    def __init__(self, operation=None, reported_concern=None, review_item=None):
        super(ReviewPatch, self).__init__()
        self.operation = operation
        self.reported_concern = reported_concern
        self.review_item = review_item


class ReviewReply(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'long'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'product_version': {'key': 'productVersion', 'type': 'str'},
        'reply_text': {'key': 'replyText', 'type': 'str'},
        'review_id': {'key': 'reviewId', 'type': 'long'},
        'title': {'key': 'title', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, id=None, is_deleted=None, product_version=None, reply_text=None, review_id=None, title=None, updated_date=None, user_id=None):
        super(ReviewReply, self).__init__()
        self.id = id
        self.is_deleted = is_deleted
        self.product_version = product_version
        self.reply_text = reply_text
        self.review_id = review_id
        self.title = title
        self.updated_date = updated_date
        self.user_id = user_id


class ReviewsResult(Model):

    _attribute_map = {
        'has_more_reviews': {'key': 'hasMoreReviews', 'type': 'bool'},
        'reviews': {'key': 'reviews', 'type': '[Review]'},
        'total_review_count': {'key': 'totalReviewCount', 'type': 'long'}
    }

    def __init__(self, has_more_reviews=None, reviews=None, total_review_count=None):
        super(ReviewsResult, self).__init__()
        self.has_more_reviews = has_more_reviews
        self.reviews = reviews
        self.total_review_count = total_review_count


class ReviewSummary(Model):

    _attribute_map = {
        'average_rating': {'key': 'averageRating', 'type': 'int'},
        'rating_count': {'key': 'ratingCount', 'type': 'long'},
        'rating_split': {'key': 'ratingSplit', 'type': '[RatingCountPerRating]'}
    }

    def __init__(self, average_rating=None, rating_count=None, rating_split=None):
        super(ReviewSummary, self).__init__()
        self.average_rating = average_rating
        self.rating_count = rating_count
        self.rating_split = rating_split


class UnpackagedExtensionData(Model):

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'draft_id': {'key': 'draftId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'installation_targets': {'key': 'installationTargets', 'type': '[InstallationTarget]'},
        'is_converted_to_markdown': {'key': 'isConvertedToMarkdown', 'type': 'bool'},
        'is_preview': {'key': 'isPreview', 'type': 'bool'},
        'pricing_category': {'key': 'pricingCategory', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'qn_aEnabled': {'key': 'qnAEnabled', 'type': 'bool'},
        'referral_url': {'key': 'referralUrl', 'type': 'str'},
        'repository_url': {'key': 'repositoryUrl', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'version': {'key': 'version', 'type': 'str'},
        'vsix_id': {'key': 'vsixId', 'type': 'str'}
    }

    def __init__(self, categories=None, description=None, display_name=None, draft_id=None, extension_name=None, installation_targets=None, is_converted_to_markdown=None, is_preview=None, pricing_category=None, product=None, publisher_name=None, qn_aEnabled=None, referral_url=None, repository_url=None, tags=None, version=None, vsix_id=None):
        super(UnpackagedExtensionData, self).__init__()
        self.categories = categories
        self.description = description
        self.display_name = display_name
        self.draft_id = draft_id
        self.extension_name = extension_name
        self.installation_targets = installation_targets
        self.is_converted_to_markdown = is_converted_to_markdown
        self.is_preview = is_preview
        self.pricing_category = pricing_category
        self.product = product
        self.publisher_name = publisher_name
        self.qn_aEnabled = qn_aEnabled
        self.referral_url = referral_url
        self.repository_url = repository_url
        self.tags = tags
        self.version = version
        self.vsix_id = vsix_id


class UserIdentityRef(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None):
        super(UserIdentityRef, self).__init__()
        self.display_name = display_name
        self.id = id


class UserReportedConcern(Model):

    _attribute_map = {
        'category': {'key': 'category', 'type': 'object'},
        'concern_text': {'key': 'concernText', 'type': 'str'},
        'review_id': {'key': 'reviewId', 'type': 'long'},
        'submitted_date': {'key': 'submittedDate', 'type': 'iso-8601'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, category=None, concern_text=None, review_id=None, submitted_date=None, user_id=None):
        super(UserReportedConcern, self).__init__()
        self.category = category
        self.concern_text = concern_text
        self.review_id = review_id
        self.submitted_date = submitted_date
        self.user_id = user_id


class Concern(QnAItem):

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'status': {'key': 'status', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'UserIdentityRef'},
        'category': {'key': 'category', 'type': 'object'}
    }

    def __init__(self, created_date=None, id=None, status=None, text=None, updated_date=None, user=None, category=None):
        super(Concern, self).__init__(created_date=created_date, id=id, status=status, text=text, updated_date=updated_date, user=user)
        self.category = category


class ExtensionDraftAsset(ExtensionFile):

    _attribute_map = {
        'asset_type': {'key': 'assetType', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
    }

    def __init__(self, asset_type=None, language=None, source=None):
        super(ExtensionDraftAsset, self).__init__(asset_type=asset_type, language=language, source=source)


class Publisher(PublisherBase):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': '[str]'},
        'extensions': {'key': 'extensions', 'type': '[PublishedExtension]'},
        'flags': {'key': 'flags', 'type': 'object'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'long_description': {'key': 'longDescription', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'short_description': {'key': 'shortDescription', 'type': 'str'},
        'state': {'key': 'state', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'}
    }

    def __init__(self, display_name=None, email_address=None, extensions=None, flags=None, last_updated=None, long_description=None, publisher_id=None, publisher_name=None, short_description=None, state=None, _links=None):
        super(Publisher, self).__init__(display_name=display_name, email_address=email_address, extensions=extensions, flags=flags, last_updated=last_updated, long_description=long_description, publisher_id=publisher_id, publisher_name=publisher_name, short_description=short_description, state=state)
        self._links = _links


__all__ = [
    'AcquisitionOperation',
    'AcquisitionOptions',
    'Answers',
    'AssetDetails',
    'AzurePublisher',
    'AzureRestApiRequestModel',
    'CategoriesResult',
    'CategoryLanguageTitle',
    'EventCounts',
    'ExtensionAcquisitionRequest',
    'ExtensionBadge',
    'ExtensionCategory',
    'ExtensionDailyStat',
    'ExtensionDailyStats',
    'ExtensionDraft',
    'ExtensionDraftPatch',
    'ExtensionEvent',
    'ExtensionEvents',
    'ExtensionFile',
    'ExtensionFilterResult',
    'ExtensionFilterResultMetadata',
    'ExtensionPackage',
    'ExtensionPayload',
    'ExtensionQuery',
    'ExtensionQueryResult',
    'ExtensionShare',
    'ExtensionStatistic',
    'ExtensionStatisticUpdate',
    'ExtensionVersion',
    'FilterCriteria',
    'GraphSubjectBase',
    'IdentityRef',
    'InstallationTarget',
    'MetadataItem',
    'NotificationsData',
    'ProductCategoriesResult',
    'ProductCategory',
    'PublishedExtension',
    'PublisherBase',
    'PublisherFacts',
    'PublisherFilterResult',
    'PublisherQuery',
    'PublisherQueryResult',
    'PublisherRoleAssignment',
    'PublisherSecurityRole',
    'PublisherUserRoleAssignmentRef',
    'QnAItem',
    'QueryFilter',
    'Question',
    'QuestionsResult',
    'RatingCountPerRating',
    'ReferenceLinks',
    'Response',
    'Review',
    'ReviewPatch',
    'ReviewReply',
    'ReviewsResult',
    'ReviewSummary',
    'UnpackagedExtensionData',
    'UserIdentityRef',
    'UserReportedConcern',
    'Concern',
    'ExtensionDraftAsset',
    'Publisher',
]
