# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class ProjectAnalysisClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(ProjectAnalysisClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '7658fa33-b1bf-4580-990f-fac5896773d3'

    def get_project_language_analytics(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='5b02a779-1867-433f-90b7-d23ed5e33e57',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ProjectLanguageAnalytics', response)

    def get_project_activity_metrics(self, project, from_date, aggregation_type):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if from_date is not None:
            query_parameters['fromDate'] = self._serialize.query('from_date', from_date, 'iso-8601')
        if aggregation_type is not None:
            query_parameters['aggregationType'] = self._serialize.query('aggregation_type', aggregation_type, 'str')
        response = self._send(http_method='GET',
                              location_id='e40ae584-9ea6-4f06-a7c7-6284651b466b',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProjectActivityMetrics', response)

    def get_git_repositories_activity_metrics(self, project, from_date, aggregation_type, skip, top):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if from_date is not None:
            query_parameters['fromDate'] = self._serialize.query('from_date', from_date, 'iso-8601')
        if aggregation_type is not None:
            query_parameters['aggregationType'] = self._serialize.query('aggregation_type', aggregation_type, 'str')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='df7fbbca-630a-40e3-8aa3-7a3faf66947e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[RepositoryActivityMetrics]', self._unwrap_collection(response))

    def get_repository_activity_metrics(self, project, repository_id, from_date, aggregation_type):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if from_date is not None:
            query_parameters['fromDate'] = self._serialize.query('from_date', from_date, 'iso-8601')
        if aggregation_type is not None:
            query_parameters['aggregationType'] = self._serialize.query('aggregation_type', aggregation_type, 'str')
        response = self._send(http_method='GET',
                              location_id='df7fbbca-630a-40e3-8aa3-7a3faf66947e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('RepositoryActivityMetrics', response)

