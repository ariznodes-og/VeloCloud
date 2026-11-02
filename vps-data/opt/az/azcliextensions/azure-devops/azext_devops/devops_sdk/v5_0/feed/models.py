# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class FeedBatchData(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': 'FeedBatchOperationData'},
        'operation': {'key': 'operation', 'type': 'object'}
    }

    def __init__(self, data=None, operation=None):
        super(FeedBatchData, self).__init__()
        self.data = data
        self.operation = operation


class FeedBatchOperationData(Model):

    _attribute_map = {
    }

    def __init__(self):
        super(FeedBatchOperationData, self).__init__()


class FeedChange(Model):

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'feed': {'key': 'feed', 'type': 'Feed'},
        'feed_continuation_token': {'key': 'feedContinuationToken', 'type': 'long'},
        'latest_package_continuation_token': {'key': 'latestPackageContinuationToken', 'type': 'long'}
    }

    def __init__(self, change_type=None, feed=None, feed_continuation_token=None, latest_package_continuation_token=None):
        super(FeedChange, self).__init__()
        self.change_type = change_type
        self.feed = feed
        self.feed_continuation_token = feed_continuation_token
        self.latest_package_continuation_token = latest_package_continuation_token


class FeedChangesResponse(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'count': {'key': 'count', 'type': 'int'},
        'feed_changes': {'key': 'feedChanges', 'type': '[FeedChange]'},
        'next_feed_continuation_token': {'key': 'nextFeedContinuationToken', 'type': 'long'}
    }

    def __init__(self, _links=None, count=None, feed_changes=None, next_feed_continuation_token=None):
        super(FeedChangesResponse, self).__init__()
        self._links = _links
        self.count = count
        self.feed_changes = feed_changes
        self.next_feed_continuation_token = next_feed_continuation_token


class FeedCore(Model):

    _attribute_map = {
        'allow_upstream_name_conflict': {'key': 'allowUpstreamNameConflict', 'type': 'bool'},
        'capabilities': {'key': 'capabilities', 'type': 'object'},
        'fully_qualified_id': {'key': 'fullyQualifiedId', 'type': 'str'},
        'fully_qualified_name': {'key': 'fullyQualifiedName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'upstream_enabled': {'key': 'upstreamEnabled', 'type': 'bool'},
        'upstream_sources': {'key': 'upstreamSources', 'type': '[UpstreamSource]'},
        'view': {'key': 'view', 'type': 'FeedView'},
        'view_id': {'key': 'viewId', 'type': 'str'},
        'view_name': {'key': 'viewName', 'type': 'str'}
    }

    def __init__(self, allow_upstream_name_conflict=None, capabilities=None, fully_qualified_id=None, fully_qualified_name=None, id=None, is_read_only=None, name=None, upstream_enabled=None, upstream_sources=None, view=None, view_id=None, view_name=None):
        super(FeedCore, self).__init__()
        self.allow_upstream_name_conflict = allow_upstream_name_conflict
        self.capabilities = capabilities
        self.fully_qualified_id = fully_qualified_id
        self.fully_qualified_name = fully_qualified_name
        self.id = id
        self.is_read_only = is_read_only
        self.name = name
        self.upstream_enabled = upstream_enabled
        self.upstream_sources = upstream_sources
        self.view = view
        self.view_id = view_id
        self.view_name = view_name


class FeedPermission(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identity_descriptor': {'key': 'identityDescriptor', 'type': 'str'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'role': {'key': 'role', 'type': 'object'}
    }

    def __init__(self, display_name=None, identity_descriptor=None, identity_id=None, role=None):
        super(FeedPermission, self).__init__()
        self.display_name = display_name
        self.identity_descriptor = identity_descriptor
        self.identity_id = identity_id
        self.role = role


class FeedRetentionPolicy(Model):

    _attribute_map = {
        'age_limit_in_days': {'key': 'ageLimitInDays', 'type': 'int'},
        'count_limit': {'key': 'countLimit', 'type': 'int'}
    }

    def __init__(self, age_limit_in_days=None, count_limit=None):
        super(FeedRetentionPolicy, self).__init__()
        self.age_limit_in_days = age_limit_in_days
        self.count_limit = count_limit


class FeedUpdate(Model):

    _attribute_map = {
        'allow_upstream_name_conflict': {'key': 'allowUpstreamNameConflict', 'type': 'bool'},
        'badges_enabled': {'key': 'badgesEnabled', 'type': 'bool'},
        'default_view_id': {'key': 'defaultViewId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'hide_deleted_package_versions': {'key': 'hideDeletedPackageVersions', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'upstream_enabled': {'key': 'upstreamEnabled', 'type': 'bool'},
        'upstream_sources': {'key': 'upstreamSources', 'type': '[UpstreamSource]'}
    }

    def __init__(self, allow_upstream_name_conflict=None, badges_enabled=None, default_view_id=None, description=None, hide_deleted_package_versions=None, id=None, name=None, upstream_enabled=None, upstream_sources=None):
        super(FeedUpdate, self).__init__()
        self.allow_upstream_name_conflict = allow_upstream_name_conflict
        self.badges_enabled = badges_enabled
        self.default_view_id = default_view_id
        self.description = description
        self.hide_deleted_package_versions = hide_deleted_package_versions
        self.id = id
        self.name = name
        self.upstream_enabled = upstream_enabled
        self.upstream_sources = upstream_sources


class FeedView(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, _links=None, id=None, name=None, type=None, url=None, visibility=None):
        super(FeedView, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.type = type
        self.url = url
        self.visibility = visibility


class GlobalPermission(Model):

    _attribute_map = {
        'identity_descriptor': {'key': 'identityDescriptor', 'type': 'str'},
        'role': {'key': 'role', 'type': 'object'}
    }

    def __init__(self, identity_descriptor=None, role=None):
        super(GlobalPermission, self).__init__()
        self.identity_descriptor = identity_descriptor
        self.role = role


class JsonPatchOperation(Model):

    _attribute_map = {
        'from_': {'key': 'from', 'type': 'str'},
        'op': {'key': 'op', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, from_=None, op=None, path=None, value=None):
        super(JsonPatchOperation, self).__init__()
        self.from_ = from_
        self.op = op
        self.path = path
        self.value = value


class MinimalPackageVersion(Model):

    _attribute_map = {
        'direct_upstream_source_id': {'key': 'directUpstreamSourceId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_cached_version': {'key': 'isCachedVersion', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_latest': {'key': 'isLatest', 'type': 'bool'},
        'is_listed': {'key': 'isListed', 'type': 'bool'},
        'normalized_version': {'key': 'normalizedVersion', 'type': 'str'},
        'package_description': {'key': 'packageDescription', 'type': 'str'},
        'publish_date': {'key': 'publishDate', 'type': 'iso-8601'},
        'storage_id': {'key': 'storageId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'views': {'key': 'views', 'type': '[FeedView]'}
    }

    def __init__(self, direct_upstream_source_id=None, id=None, is_cached_version=None, is_deleted=None, is_latest=None, is_listed=None, normalized_version=None, package_description=None, publish_date=None, storage_id=None, version=None, views=None):
        super(MinimalPackageVersion, self).__init__()
        self.direct_upstream_source_id = direct_upstream_source_id
        self.id = id
        self.is_cached_version = is_cached_version
        self.is_deleted = is_deleted
        self.is_latest = is_latest
        self.is_listed = is_listed
        self.normalized_version = normalized_version
        self.package_description = package_description
        self.publish_date = publish_date
        self.storage_id = storage_id
        self.version = version
        self.views = views


class Package(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'str'},
        'is_cached': {'key': 'isCached', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'normalized_name': {'key': 'normalizedName', 'type': 'str'},
        'protocol_type': {'key': 'protocolType', 'type': 'str'},
        'star_count': {'key': 'starCount', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[MinimalPackageVersion]'}
    }

    def __init__(self, _links=None, id=None, is_cached=None, name=None, normalized_name=None, protocol_type=None, star_count=None, url=None, versions=None):
        super(Package, self).__init__()
        self._links = _links
        self.id = id
        self.is_cached = is_cached
        self.name = name
        self.normalized_name = normalized_name
        self.protocol_type = protocol_type
        self.star_count = star_count
        self.url = url
        self.versions = versions


class PackageChange(Model):

    _attribute_map = {
        'package': {'key': 'package', 'type': 'Package'},
        'package_version_change': {'key': 'packageVersionChange', 'type': 'PackageVersionChange'}
    }

    def __init__(self, package=None, package_version_change=None):
        super(PackageChange, self).__init__()
        self.package = package
        self.package_version_change = package_version_change


class PackageChangesResponse(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'count': {'key': 'count', 'type': 'int'},
        'next_package_continuation_token': {'key': 'nextPackageContinuationToken', 'type': 'long'},
        'package_changes': {'key': 'packageChanges', 'type': '[PackageChange]'}
    }

    def __init__(self, _links=None, count=None, next_package_continuation_token=None, package_changes=None):
        super(PackageChangesResponse, self).__init__()
        self._links = _links
        self.count = count
        self.next_package_continuation_token = next_package_continuation_token
        self.package_changes = package_changes


class PackageDependency(Model):

    _attribute_map = {
        'group': {'key': 'group', 'type': 'str'},
        'package_name': {'key': 'packageName', 'type': 'str'},
        'version_range': {'key': 'versionRange', 'type': 'str'}
    }

    def __init__(self, group=None, package_name=None, version_range=None):
        super(PackageDependency, self).__init__()
        self.group = group
        self.package_name = package_name
        self.version_range = version_range


class PackageDownloadMetricsQuery(Model):

    _attribute_map = {
        'package_ids': {'key': 'packageIds', 'type': '[str]'}
    }

    def __init__(self, package_ids=None):
        super(PackageDownloadMetricsQuery, self).__init__()
        self.package_ids = package_ids


class PackageFile(Model):

    _attribute_map = {
        'children': {'key': 'children', 'type': '[PackageFile]'},
        'name': {'key': 'name', 'type': 'str'},
        'protocol_metadata': {'key': 'protocolMetadata', 'type': 'ProtocolMetadata'}
    }

    def __init__(self, children=None, name=None, protocol_metadata=None):
        super(PackageFile, self).__init__()
        self.children = children
        self.name = name
        self.protocol_metadata = protocol_metadata


class PackageIdMetrics(Model):

    _attribute_map = {
        'download_count': {'key': 'downloadCount', 'type': 'float'},
        'download_unique_users': {'key': 'downloadUniqueUsers', 'type': 'float'},
        'last_downloaded': {'key': 'lastDownloaded', 'type': 'iso-8601'},
        'package_id': {'key': 'packageId', 'type': 'str'}
    }

    def __init__(self, download_count=None, download_unique_users=None, last_downloaded=None, package_id=None):
        super(PackageIdMetrics, self).__init__()
        self.download_count = download_count
        self.download_unique_users = download_unique_users
        self.last_downloaded = last_downloaded
        self.package_id = package_id


class PackageVersion(MinimalPackageVersion):

    _attribute_map = {
        'direct_upstream_source_id': {'key': 'directUpstreamSourceId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_cached_version': {'key': 'isCachedVersion', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_latest': {'key': 'isLatest', 'type': 'bool'},
        'is_listed': {'key': 'isListed', 'type': 'bool'},
        'normalized_version': {'key': 'normalizedVersion', 'type': 'str'},
        'package_description': {'key': 'packageDescription', 'type': 'str'},
        'publish_date': {'key': 'publishDate', 'type': 'iso-8601'},
        'storage_id': {'key': 'storageId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'views': {'key': 'views', 'type': '[FeedView]'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'dependencies': {'key': 'dependencies', 'type': '[PackageDependency]'},
        'description': {'key': 'description', 'type': 'str'},
        'files': {'key': 'files', 'type': '[PackageFile]'},
        'other_versions': {'key': 'otherVersions', 'type': '[MinimalPackageVersion]'},
        'protocol_metadata': {'key': 'protocolMetadata', 'type': 'ProtocolMetadata'},
        'source_chain': {'key': 'sourceChain', 'type': '[UpstreamSource]'},
        'summary': {'key': 'summary', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, direct_upstream_source_id=None, id=None, is_cached_version=None, is_deleted=None, is_latest=None, is_listed=None, normalized_version=None, package_description=None, publish_date=None, storage_id=None, version=None, views=None, _links=None, author=None, deleted_date=None, dependencies=None, description=None, files=None, other_versions=None, protocol_metadata=None, source_chain=None, summary=None, tags=None, url=None):
        super(PackageVersion, self).__init__(direct_upstream_source_id=direct_upstream_source_id, id=id, is_cached_version=is_cached_version, is_deleted=is_deleted, is_latest=is_latest, is_listed=is_listed, normalized_version=normalized_version, package_description=package_description, publish_date=publish_date, storage_id=storage_id, version=version, views=views)
        self._links = _links
        self.author = author
        self.deleted_date = deleted_date
        self.dependencies = dependencies
        self.description = description
        self.files = files
        self.other_versions = other_versions
        self.protocol_metadata = protocol_metadata
        self.source_chain = source_chain
        self.summary = summary
        self.tags = tags
        self.url = url


class PackageVersionChange(Model):

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'continuation_token': {'key': 'continuationToken', 'type': 'long'},
        'package_version': {'key': 'packageVersion', 'type': 'PackageVersion'}
    }

    def __init__(self, change_type=None, continuation_token=None, package_version=None):
        super(PackageVersionChange, self).__init__()
        self.change_type = change_type
        self.continuation_token = continuation_token
        self.package_version = package_version


class PackageVersionDownloadMetricsQuery(Model):

    _attribute_map = {
        'package_version_ids': {'key': 'packageVersionIds', 'type': '[str]'}
    }

    def __init__(self, package_version_ids=None):
        super(PackageVersionDownloadMetricsQuery, self).__init__()
        self.package_version_ids = package_version_ids


class PackageVersionMetrics(Model):

    _attribute_map = {
        'download_count': {'key': 'downloadCount', 'type': 'float'},
        'download_unique_users': {'key': 'downloadUniqueUsers', 'type': 'float'},
        'last_downloaded': {'key': 'lastDownloaded', 'type': 'iso-8601'},
        'package_id': {'key': 'packageId', 'type': 'str'},
        'package_version_id': {'key': 'packageVersionId', 'type': 'str'}
    }

    def __init__(self, download_count=None, download_unique_users=None, last_downloaded=None, package_id=None, package_version_id=None):
        super(PackageVersionMetrics, self).__init__()
        self.download_count = download_count
        self.download_unique_users = download_unique_users
        self.last_downloaded = last_downloaded
        self.package_id = package_id
        self.package_version_id = package_version_id


class PackageVersionProvenance(Model):

    _attribute_map = {
        'feed_id': {'key': 'feedId', 'type': 'str'},
        'package_id': {'key': 'packageId', 'type': 'str'},
        'package_version_id': {'key': 'packageVersionId', 'type': 'str'},
        'provenance': {'key': 'provenance', 'type': 'Provenance'}
    }

    def __init__(self, feed_id=None, package_id=None, package_version_id=None, provenance=None):
        super(PackageVersionProvenance, self).__init__()
        self.feed_id = feed_id
        self.package_id = package_id
        self.package_version_id = package_version_id
        self.provenance = provenance


class ProtocolMetadata(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': 'object'},
        'schema_version': {'key': 'schemaVersion', 'type': 'int'}
    }

    def __init__(self, data=None, schema_version=None):
        super(ProtocolMetadata, self).__init__()
        self.data = data
        self.schema_version = schema_version


class Provenance(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': '{str}'},
        'provenance_source': {'key': 'provenanceSource', 'type': 'str'},
        'publisher_user_identity': {'key': 'publisherUserIdentity', 'type': 'str'},
        'user_agent': {'key': 'userAgent', 'type': 'str'}
    }

    def __init__(self, data=None, provenance_source=None, publisher_user_identity=None, user_agent=None):
        super(Provenance, self).__init__()
        self.data = data
        self.provenance_source = provenance_source
        self.publisher_user_identity = publisher_user_identity
        self.user_agent = user_agent


class RecycleBinPackageVersion(PackageVersion):

    _attribute_map = {
        'direct_upstream_source_id': {'key': 'directUpstreamSourceId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_cached_version': {'key': 'isCachedVersion', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_latest': {'key': 'isLatest', 'type': 'bool'},
        'is_listed': {'key': 'isListed', 'type': 'bool'},
        'normalized_version': {'key': 'normalizedVersion', 'type': 'str'},
        'package_description': {'key': 'packageDescription', 'type': 'str'},
        'publish_date': {'key': 'publishDate', 'type': 'iso-8601'},
        'storage_id': {'key': 'storageId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'views': {'key': 'views', 'type': '[FeedView]'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'dependencies': {'key': 'dependencies', 'type': '[PackageDependency]'},
        'description': {'key': 'description', 'type': 'str'},
        'files': {'key': 'files', 'type': '[PackageFile]'},
        'other_versions': {'key': 'otherVersions', 'type': '[MinimalPackageVersion]'},
        'protocol_metadata': {'key': 'protocolMetadata', 'type': 'ProtocolMetadata'},
        'source_chain': {'key': 'sourceChain', 'type': '[UpstreamSource]'},
        'summary': {'key': 'summary', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'},
        'scheduled_permanent_delete_date': {'key': 'scheduledPermanentDeleteDate', 'type': 'iso-8601'}
    }

    def __init__(self, direct_upstream_source_id=None, id=None, is_cached_version=None, is_deleted=None, is_latest=None, is_listed=None, normalized_version=None, package_description=None, publish_date=None, storage_id=None, version=None, views=None, _links=None, author=None, deleted_date=None, dependencies=None, description=None, files=None, other_versions=None, protocol_metadata=None, source_chain=None, summary=None, tags=None, url=None, scheduled_permanent_delete_date=None):
        super(RecycleBinPackageVersion, self).__init__(direct_upstream_source_id=direct_upstream_source_id, id=id, is_cached_version=is_cached_version, is_deleted=is_deleted, is_latest=is_latest, is_listed=is_listed, normalized_version=normalized_version, package_description=package_description, publish_date=publish_date, storage_id=storage_id, version=version, views=views, _links=_links, author=author, deleted_date=deleted_date, dependencies=dependencies, description=description, files=files, other_versions=other_versions, protocol_metadata=protocol_metadata, source_chain=source_chain, summary=summary, tags=tags, url=url)
        self.scheduled_permanent_delete_date = scheduled_permanent_delete_date


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class UpstreamSource(Model):

    _attribute_map = {
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'internal_upstream_collection_id': {'key': 'internalUpstreamCollectionId', 'type': 'str'},
        'internal_upstream_feed_id': {'key': 'internalUpstreamFeedId', 'type': 'str'},
        'internal_upstream_view_id': {'key': 'internalUpstreamViewId', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'protocol': {'key': 'protocol', 'type': 'str'},
        'upstream_source_type': {'key': 'upstreamSourceType', 'type': 'object'}
    }

    def __init__(self, deleted_date=None, id=None, internal_upstream_collection_id=None, internal_upstream_feed_id=None, internal_upstream_view_id=None, location=None, name=None, protocol=None, upstream_source_type=None):
        super(UpstreamSource, self).__init__()
        self.deleted_date = deleted_date
        self.id = id
        self.internal_upstream_collection_id = internal_upstream_collection_id
        self.internal_upstream_feed_id = internal_upstream_feed_id
        self.internal_upstream_view_id = internal_upstream_view_id
        self.location = location
        self.name = name
        self.protocol = protocol
        self.upstream_source_type = upstream_source_type


class Feed(FeedCore):

    _attribute_map = {
        'allow_upstream_name_conflict': {'key': 'allowUpstreamNameConflict', 'type': 'bool'},
        'capabilities': {'key': 'capabilities', 'type': 'object'},
        'fully_qualified_id': {'key': 'fullyQualifiedId', 'type': 'str'},
        'fully_qualified_name': {'key': 'fullyQualifiedName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'upstream_enabled': {'key': 'upstreamEnabled', 'type': 'bool'},
        'upstream_sources': {'key': 'upstreamSources', 'type': '[UpstreamSource]'},
        'view': {'key': 'view', 'type': 'FeedView'},
        'view_id': {'key': 'viewId', 'type': 'str'},
        'view_name': {'key': 'viewName', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'badges_enabled': {'key': 'badgesEnabled', 'type': 'bool'},
        'default_view_id': {'key': 'defaultViewId', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'hide_deleted_package_versions': {'key': 'hideDeletedPackageVersions', 'type': 'bool'},
        'permissions': {'key': 'permissions', 'type': '[FeedPermission]'},
        'upstream_enabled_changed_date': {'key': 'upstreamEnabledChangedDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, allow_upstream_name_conflict=None, capabilities=None, fully_qualified_id=None, fully_qualified_name=None, id=None, is_read_only=None, name=None, upstream_enabled=None, upstream_sources=None, view=None, view_id=None, view_name=None, _links=None, badges_enabled=None, default_view_id=None, deleted_date=None, description=None, hide_deleted_package_versions=None, permissions=None, upstream_enabled_changed_date=None, url=None):
        super(Feed, self).__init__(allow_upstream_name_conflict=allow_upstream_name_conflict, capabilities=capabilities, fully_qualified_id=fully_qualified_id, fully_qualified_name=fully_qualified_name, id=id, is_read_only=is_read_only, name=name, upstream_enabled=upstream_enabled, upstream_sources=upstream_sources, view=view, view_id=view_id, view_name=view_name)
        self._links = _links
        self.badges_enabled = badges_enabled
        self.default_view_id = default_view_id
        self.deleted_date = deleted_date
        self.description = description
        self.hide_deleted_package_versions = hide_deleted_package_versions
        self.permissions = permissions
        self.upstream_enabled_changed_date = upstream_enabled_changed_date
        self.url = url


__all__ = [
    'FeedBatchData',
    'FeedBatchOperationData',
    'FeedChange',
    'FeedChangesResponse',
    'FeedCore',
    'FeedPermission',
    'FeedRetentionPolicy',
    'FeedUpdate',
    'FeedView',
    'GlobalPermission',
    'JsonPatchOperation',
    'MinimalPackageVersion',
    'Package',
    'PackageChange',
    'PackageChangesResponse',
    'PackageDependency',
    'PackageDownloadMetricsQuery',
    'PackageFile',
    'PackageIdMetrics',
    'PackageVersion',
    'PackageVersionChange',
    'PackageVersionDownloadMetricsQuery',
    'PackageVersionMetrics',
    'PackageVersionProvenance',
    'ProtocolMetadata',
    'Provenance',
    'RecycleBinPackageVersion',
    'ReferenceLinks',
    'UpstreamSource',
    'Feed',
]
