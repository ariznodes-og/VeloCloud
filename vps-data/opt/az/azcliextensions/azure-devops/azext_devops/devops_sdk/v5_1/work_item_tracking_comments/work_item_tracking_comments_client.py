# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class WorkItemTrackingCommentsClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(WorkItemTrackingCommentsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '5264459e-e5e0-4bd8-b118-0985e68a4ec5'

    def add_comment(self, request, project, work_item_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        content = self._serialize.body(request, 'WorkItemCommentCreateRequest')
        response = self._send(http_method='POST',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemCommentResponse', response)

    def delete_comment(self, project, work_item_id, comment_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        response = self._send(http_method='DELETE',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemCommentResponse', response)

    def get_comment(self, project, work_item_id, comment_id, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentResponse', response)

    def get_comments(self, project, work_item_id, top=None, continuation_token=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentsResponse', response)

    def get_comments_batch(self, project, work_item_id, ids, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentsResponse', response)

    def update_comment(self, request, project, work_item_id, comment_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        content = self._serialize.body(request, 'WorkItemCommentUpdateRequest')
        response = self._send(http_method='PATCH',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemCommentResponse', response)

    def read_reporting_comments(self, project, continuation_token=None, top=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='370b8590-9562-42be-b0d8-ac06668fc5dc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentsReportingResponse', response)

    def get_comment_version(self, project, work_item_id, comment_id, version):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'int')
        response = self._send(http_method='GET',
                              location_id='49e03b34-3be0-42e3-8a5d-e8dfb88ac954',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemCommentVersionResponse', response)

    def get_comment_versions(self, project, work_item_id, comment_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='49e03b34-3be0-42e3-8a5d-e8dfb88ac954',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemCommentVersionResponse]', self._unwrap_collection(response))

