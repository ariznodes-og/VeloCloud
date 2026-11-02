# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CodeResult(Model):

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'Collection'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'matches': {'key': 'matches', 'type': '{[Hit]}'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'Project'},
        'repository': {'key': 'repository', 'type': 'Repository'},
        'versions': {'key': 'versions', 'type': '[Version]'}
    }

    def __init__(self, collection=None, content_id=None, file_name=None, matches=None, path=None, project=None, repository=None, versions=None):
        super(CodeResult, self).__init__()
        self.collection = collection
        self.content_id = content_id
        self.file_name = file_name
        self.matches = matches
        self.path = path
        self.project = project
        self.repository = repository
        self.versions = versions


class Collection(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(Collection, self).__init__()
        self.name = name


class EntitySearchRequestBase(Model):

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'}
    }

    def __init__(self, filters=None, search_text=None):
        super(EntitySearchRequestBase, self).__init__()
        self.filters = filters
        self.search_text = search_text


class EntitySearchResponse(Model):

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'}
    }

    def __init__(self, facets=None, info_code=None):
        super(EntitySearchResponse, self).__init__()
        self.facets = facets
        self.info_code = info_code


class FeedInfo(Model):

    _attribute_map = {
        'collection_id': {'key': 'collectionId', 'type': 'str'},
        'collection_name': {'key': 'collectionName', 'type': 'str'},
        'feed_id': {'key': 'feedId', 'type': 'str'},
        'feed_name': {'key': 'feedName', 'type': 'str'},
        'latest_matched_version': {'key': 'latestMatchedVersion', 'type': 'str'},
        'latest_version': {'key': 'latestVersion', 'type': 'str'},
        'package_url': {'key': 'packageUrl', 'type': 'str'},
        'views': {'key': 'views', 'type': '[str]'}
    }

    def __init__(self, collection_id=None, collection_name=None, feed_id=None, feed_name=None, latest_matched_version=None, latest_version=None, package_url=None, views=None):
        super(FeedInfo, self).__init__()
        self.collection_id = collection_id
        self.collection_name = collection_name
        self.feed_id = feed_id
        self.feed_name = feed_name
        self.latest_matched_version = latest_matched_version
        self.latest_version = latest_version
        self.package_url = package_url
        self.views = views


class Filter(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'result_count': {'key': 'resultCount', 'type': 'int'}
    }

    def __init__(self, id=None, name=None, result_count=None):
        super(Filter, self).__init__()
        self.id = id
        self.name = name
        self.result_count = result_count


class Hit(Model):

    _attribute_map = {
        'char_offset': {'key': 'charOffset', 'type': 'int'},
        'length': {'key': 'length', 'type': 'int'}
    }

    def __init__(self, char_offset=None, length=None):
        super(Hit, self).__init__()
        self.char_offset = char_offset
        self.length = length


class PackageHit(Model):

    _attribute_map = {
        'field_reference_name': {'key': 'fieldReferenceName', 'type': 'str'},
        'highlights': {'key': 'highlights', 'type': '[str]'}
    }

    def __init__(self, field_reference_name=None, highlights=None):
        super(PackageHit, self).__init__()
        self.field_reference_name = field_reference_name
        self.highlights = highlights


class PackageResult(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'feeds': {'key': 'feeds', 'type': '[FeedInfo]'},
        'hits': {'key': 'hits', 'type': '[PackageHit]'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'protocol_type': {'key': 'protocolType', 'type': 'str'}
    }

    def __init__(self, description=None, feeds=None, hits=None, id=None, name=None, protocol_type=None):
        super(PackageResult, self).__init__()
        self.description = description
        self.feeds = feeds
        self.hits = hits
        self.id = id
        self.name = name
        self.protocol_type = protocol_type


class PackageSearchResponse(Model):

    _attribute_map = {
        'activity_id': {'key': 'activityId', 'type': '[str]'},
        'content': {'key': 'content', 'type': 'PackageSearchResponseContent'}
    }

    def __init__(self, activity_id=None, content=None):
        super(PackageSearchResponse, self).__init__()
        self.activity_id = activity_id
        self.content = content


class PackageSearchResponseContent(EntitySearchResponse):

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[PackageResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(PackageSearchResponseContent, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class Project(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(Project, self).__init__()
        self.id = id
        self.name = name


class ProjectReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, visibility=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name
        self.visibility = visibility


class Repository(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(Repository, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class ScrollSearchRequest(EntitySearchRequestBase):

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'scroll_id': {'key': '$scrollId', 'type': 'str'},
        'scroll_size': {'key': '$scrollSize', 'type': 'int'}
    }

    def __init__(self, filters=None, search_text=None, scroll_id=None, scroll_size=None):
        super(ScrollSearchRequest, self).__init__(filters=filters, search_text=search_text)
        self.scroll_id = scroll_id
        self.scroll_size = scroll_size


class SortOption(Model):

    _attribute_map = {
        'field': {'key': 'field', 'type': 'str'},
        'sort_order': {'key': 'sortOrder', 'type': 'str'}
    }

    def __init__(self, field=None, sort_order=None):
        super(SortOption, self).__init__()
        self.field = field
        self.sort_order = sort_order


class Version(Model):

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'change_id': {'key': 'changeId', 'type': 'str'}
    }

    def __init__(self, branch_name=None, change_id=None):
        super(Version, self).__init__()
        self.branch_name = branch_name
        self.change_id = change_id


class Wiki(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'mapped_path': {'key': 'mappedPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, mapped_path=None, name=None, version=None):
        super(Wiki, self).__init__()
        self.id = id
        self.mapped_path = mapped_path
        self.name = name
        self.version = version


class WikiHit(Model):

    _attribute_map = {
        'field_reference_name': {'key': 'fieldReferenceName', 'type': 'str'},
        'highlights': {'key': 'highlights', 'type': '[str]'}
    }

    def __init__(self, field_reference_name=None, highlights=None):
        super(WikiHit, self).__init__()
        self.field_reference_name = field_reference_name
        self.highlights = highlights


class WikiResult(Model):

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'Collection'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'hits': {'key': 'hits', 'type': '[WikiHit]'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'wiki': {'key': 'wiki', 'type': 'Wiki'}
    }

    def __init__(self, collection=None, content_id=None, file_name=None, hits=None, path=None, project=None, wiki=None):
        super(WikiResult, self).__init__()
        self.collection = collection
        self.content_id = content_id
        self.file_name = file_name
        self.hits = hits
        self.path = path
        self.project = project
        self.wiki = wiki


class WikiSearchResponse(EntitySearchResponse):

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[WikiResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(WikiSearchResponse, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class WorkItemHit(Model):

    _attribute_map = {
        'field_reference_name': {'key': 'fieldReferenceName', 'type': 'str'},
        'highlights': {'key': 'highlights', 'type': '[str]'}
    }

    def __init__(self, field_reference_name=None, highlights=None):
        super(WorkItemHit, self).__init__()
        self.field_reference_name = field_reference_name
        self.highlights = highlights


class WorkItemResult(Model):

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '{str}'},
        'hits': {'key': 'hits', 'type': '[WorkItemHit]'},
        'project': {'key': 'project', 'type': 'Project'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, fields=None, hits=None, project=None, url=None):
        super(WorkItemResult, self).__init__()
        self.fields = fields
        self.hits = hits
        self.project = project
        self.url = url


class WorkItemSearchResponse(EntitySearchResponse):

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[WorkItemResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(WorkItemSearchResponse, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class CodeSearchResponse(EntitySearchResponse):

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[CodeResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(CodeSearchResponse, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class EntitySearchRequest(EntitySearchRequestBase):

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'}
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(EntitySearchRequest, self).__init__(filters=filters, search_text=search_text)
        self.order_by = order_by
        self.skip = skip
        self.top = top
        self.include_facets = include_facets


class PackageSearchRequest(EntitySearchRequest):

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(PackageSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


class WikiSearchRequest(EntitySearchRequest):

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(WikiSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


class WorkItemSearchRequest(EntitySearchRequest):

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(WorkItemSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


class CodeSearchRequest(EntitySearchRequest):

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(CodeSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


__all__ = [
    'CodeResult',
    'Collection',
    'EntitySearchRequestBase',
    'EntitySearchResponse',
    'FeedInfo',
    'Filter',
    'Hit',
    'PackageHit',
    'PackageResult',
    'PackageSearchResponse',
    'PackageSearchResponseContent',
    'Project',
    'ProjectReference',
    'Repository',
    'ScrollSearchRequest',
    'SortOption',
    'Version',
    'Wiki',
    'WikiHit',
    'WikiResult',
    'WikiSearchResponse',
    'WorkItemHit',
    'WorkItemResult',
    'WorkItemSearchResponse',
    'CodeSearchResponse',
    'EntitySearchRequest',
    'PackageSearchRequest',
    'WikiSearchRequest',
    'WorkItemSearchRequest',
    'CodeSearchRequest',
]
