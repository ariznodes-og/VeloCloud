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
        'versions': {'key': 'versions', 'type': '[str]'}
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


class SortOption(Model):

    _attribute_map = {
        'field': {'key': 'field', 'type': 'str'},
        'sort_order': {'key': 'sortOrder', 'type': 'str'}
    }

    def __init__(self, field=None, sort_order=None):
        super(SortOption, self).__init__()
        self.field = field
        self.sort_order = sort_order


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
    'Filter',
    'Hit',
    'Project',
    'ProjectReference',
    'Repository',
    'SortOption',
    'Wiki',
    'WikiHit',
    'WikiResult',
    'WikiSearchResponse',
    'WorkItemHit',
    'WorkItemResult',
    'WorkItemSearchResponse',
    'CodeSearchResponse',
    'EntitySearchRequest',
    'WikiSearchRequest',
    'WorkItemSearchRequest',
    'CodeSearchRequest',
]
