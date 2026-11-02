# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class SearchClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(SearchClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'ea48a0a1-269c-42d8-b8ad-ddc8fcdcf578'

    def fetch_scroll_code_search_results(self, request, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'ScrollSearchRequest')
        response = self._send(http_method='POST',
                              location_id='852dac94-e8f7-45a2-9910-927ae35766a2',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CodeSearchResponse', response)

    def fetch_code_search_results(self, request, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'CodeSearchRequest')
        response = self._send(http_method='POST',
                              location_id='e7f29993-5b82-4fca-9386-f5cfe683d524',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CodeSearchResponse', response)

    def fetch_package_search_results(self, request):
        content = self._serialize.body(request, 'PackageSearchRequest')
        response = self._send(http_method='POST',
                              location_id='f62ada48-eedc-4c8e-93f0-de870e4ecce0',
                              version='5.1-preview.1',
                              content=content)
        response_object = models.PackageSearchResponse()
        response_object.content = self._deserialize('PackageSearchResponseContent', response)
        response_object.activity_id = response.headers.get('ActivityId')
        return response_object

    def fetch_wiki_search_results(self, request, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'WikiSearchRequest')
        response = self._send(http_method='POST',
                              location_id='e90e7664-7049-4100-9a86-66b161d81080',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiSearchResponse', response)

    def fetch_work_item_search_results(self, request, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'WorkItemSearchRequest')
        response = self._send(http_method='POST',
                              location_id='73b2c9e2-ff9e-4447-8cda-5f5b21ff7cae',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemSearchResponse', response)

