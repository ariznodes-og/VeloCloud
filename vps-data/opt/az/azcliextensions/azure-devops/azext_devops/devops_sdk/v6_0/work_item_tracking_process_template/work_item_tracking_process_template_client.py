# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class WorkItemTrackingProcessTemplateClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(WorkItemTrackingProcessTemplateClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '5264459e-e5e0-4bd8-b118-0985e68a4ec5'

    def get_behavior(self, process_id, behavior_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        query_parameters = {}
        if behavior_ref_name is not None:
            query_parameters['behaviorRefName'] = self._serialize.query('behavior_ref_name', behavior_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='90bf9317-3571-487b-bc8c-a523ba0e05d7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('AdminBehavior', response)

    def get_behaviors(self, process_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        response = self._send(http_method='GET',
                              location_id='90bf9317-3571-487b-bc8c-a523ba0e05d7',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[AdminBehavior]', self._unwrap_collection(response))

    def export_process_template(self, id, **kwargs):
        route_values = {}
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        route_values['action'] = 'Export'
        response = self._send(http_method='GET',
                              location_id='29e1f38d-9e9c-4358-86a5-cdf9896a5759',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def import_process_template(self, upload_stream, ignore_warnings=None, replace_existing_template=None, **kwargs):
        route_values = {}
        route_values['action'] = 'Import'
        query_parameters = {}
        if ignore_warnings is not None:
            query_parameters['ignoreWarnings'] = self._serialize.query('ignore_warnings', ignore_warnings, 'bool')
        if replace_existing_template is not None:
            query_parameters['replaceExistingTemplate'] = self._serialize.query('replace_existing_template', replace_existing_template, 'bool')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='29e1f38d-9e9c-4358-86a5-cdf9896a5759',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ProcessImportResult', response)

    def import_process_template_status(self, id):
        route_values = {}
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        route_values['action'] = 'Status'
        response = self._send(http_method='GET',
                              location_id='29e1f38d-9e9c-4358-86a5-cdf9896a5759',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ProcessPromoteStatus', response)

