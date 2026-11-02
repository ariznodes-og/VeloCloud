# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class TestResultsClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(TestResultsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'c83eaf52-edf3-4034-ae11-17d38f25404c'

    def query_test_results_meta_data(self, test_case_reference_ids, project, details_to_include=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        content = self._serialize.body(test_case_reference_ids, '[str]')
        response = self._send(http_method='POST',
                              location_id='b72ff4c0-4341-4213-ba27-f517cf341c95',
                              version='6.0-preview.4',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[TestResultMetaData]', self._unwrap_collection(response))

    def update_test_results_meta_data(self, test_result_meta_data_update_input, project, test_case_reference_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_case_reference_id is not None:
            route_values['testCaseReferenceId'] = self._serialize.url('test_case_reference_id', test_case_reference_id, 'int')
        content = self._serialize.body(test_result_meta_data_update_input, 'TestResultMetaDataUpdateInput')
        response = self._send(http_method='PATCH',
                              location_id='b72ff4c0-4341-4213-ba27-f517cf341c95',
                              version='6.0-preview.4',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultMetaData', response)

    def get_test_result_logs(self, project, run_id, result_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='714caaac-ae1e-4869-8323-9bc0f5120dbf',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[TestLog]', self._unwrap_collection(response))

    def get_test_sub_result_logs(self, project, run_id, result_id, sub_result_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='714caaac-ae1e-4869-8323-9bc0f5120dbf',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[TestLog]', self._unwrap_collection(response))

    def get_test_run_logs(self, project, run_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='5b47b946-e875-4c9a-acdc-2a20996caebe',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[TestLog]', self._unwrap_collection(response))

    def get_test_log_store_endpoint_details_for_result_log(self, project, run_id, result_id, type, file_path):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def get_test_log_store_endpoint_details_for_sub_result_log(self, project, run_id, result_id, sub_result_id, type, file_path):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def test_log_store_endpoint_details_for_result(self, project, run_id, result_id, sub_result_id, file_path, type):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='POST',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def get_test_log_store_endpoint_details_for_run_log(self, project, run_id, type, file_path):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='67eb3f92-6c97-4fd9-8b63-6cbdc7e526ea',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def test_log_store_endpoint_details_for_run(self, project, run_id, test_log_store_operation_type, file_path=None, type=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if test_log_store_operation_type is not None:
            query_parameters['testLogStoreOperationType'] = self._serialize.query('test_log_store_operation_type', test_log_store_operation_type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='POST',
                              location_id='67eb3f92-6c97-4fd9-8b63-6cbdc7e526ea',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

