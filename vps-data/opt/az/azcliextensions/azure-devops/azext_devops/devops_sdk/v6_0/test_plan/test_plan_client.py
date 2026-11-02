# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class TestPlanClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(TestPlanClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def create_test_configuration(self, test_configuration_create_update_parameters, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_configuration_create_update_parameters, 'TestConfigurationCreateUpdateParameters')
        response = self._send(http_method='POST',
                              location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestConfiguration', response)

    def delete_test_confguration(self, project, test_configuartion_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_configuartion_id is not None:
            query_parameters['testConfiguartionId'] = self._serialize.query('test_configuartion_id', test_configuartion_id, 'int')
        self._send(http_method='DELETE',
                   location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                   version='6.0-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_test_configuration_by_id(self, project, test_configuration_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_configuration_id is not None:
            route_values['testConfigurationId'] = self._serialize.url('test_configuration_id', test_configuration_id, 'int')
        response = self._send(http_method='GET',
                              location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('TestConfiguration', response)

    def get_test_configurations(self, project, continuation_token=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestConfiguration]', self._unwrap_collection(response))

    def update_test_configuration(self, test_configuration_create_update_parameters, project, test_configuartion_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_configuartion_id is not None:
            query_parameters['testConfiguartionId'] = self._serialize.query('test_configuartion_id', test_configuartion_id, 'int')
        content = self._serialize.body(test_configuration_create_update_parameters, 'TestConfigurationCreateUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TestConfiguration', response)

    def create_test_plan(self, test_plan_create_params, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_plan_create_params, 'TestPlanCreateParams')
        response = self._send(http_method='POST',
                              location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestPlan', response)

    def delete_test_plan(self, project, plan_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        self._send(http_method='DELETE',
                   location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_test_plan_by_id(self, project, plan_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        response = self._send(http_method='GET',
                              location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('TestPlan', response)

    def get_test_plans(self, project, owner=None, continuation_token=None, include_plan_details=None, filter_active_plans=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if owner is not None:
            query_parameters['owner'] = self._serialize.query('owner', owner, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if include_plan_details is not None:
            query_parameters['includePlanDetails'] = self._serialize.query('include_plan_details', include_plan_details, 'bool')
        if filter_active_plans is not None:
            query_parameters['filterActivePlans'] = self._serialize.query('filter_active_plans', filter_active_plans, 'bool')
        response = self._send(http_method='GET',
                              location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestPlan]', self._unwrap_collection(response))

    def update_test_plan(self, test_plan_update_params, project, plan_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        content = self._serialize.body(test_plan_update_params, 'TestPlanUpdateParams')
        response = self._send(http_method='PATCH',
                              location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestPlan', response)

    def get_suite_entries(self, project, suite_id, suite_entry_type=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if suite_entry_type is not None:
            query_parameters['suiteEntryType'] = self._serialize.query('suite_entry_type', suite_entry_type, 'str')
        response = self._send(http_method='GET',
                              location_id='d6733edf-72f1-4252-925b-c560dfe9b75a',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[SuiteEntry]', self._unwrap_collection(response))

    def reorder_suite_entries(self, suite_entries, project, suite_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(suite_entries, '[SuiteEntryUpdateParams]')
        response = self._send(http_method='PATCH',
                              location_id='d6733edf-72f1-4252-925b-c560dfe9b75a',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[SuiteEntry]', self._unwrap_collection(response))

    def create_test_suite(self, test_suite_create_params, project, plan_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        content = self._serialize.body(test_suite_create_params, 'TestSuiteCreateParams')
        response = self._send(http_method='POST',
                              location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestSuite', response)

    def delete_test_suite(self, project, plan_id, suite_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        self._send(http_method='DELETE',
                   location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_test_suite_by_id(self, project, plan_id, suite_id, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestSuite', response)

    def get_test_suites_for_plan(self, project, plan_id, expand=None, continuation_token=None, as_tree_view=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['expand'] = self._serialize.query('expand', expand, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if as_tree_view is not None:
            query_parameters['asTreeView'] = self._serialize.query('as_tree_view', as_tree_view, 'bool')
        response = self._send(http_method='GET',
                              location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestSuite]', self._unwrap_collection(response))

    def update_test_suite(self, test_suite_update_params, project, plan_id, suite_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(test_suite_update_params, 'TestSuiteUpdateParams')
        response = self._send(http_method='PATCH',
                              location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestSuite', response)

    def get_suites_by_test_case_id(self, test_case_id):
        query_parameters = {}
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'int')
        response = self._send(http_method='GET',
                              location_id='a4080e84-f17b-4fad-84f1-7960b6525bf2',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TestSuite]', self._unwrap_collection(response))

    def add_test_cases_to_suite(self, suite_test_case_create_update_parameters, project, plan_id, suite_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(suite_test_case_create_update_parameters, '[SuiteTestCaseCreateUpdateParameters]')
        response = self._send(http_method='POST',
                              location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCase]', self._unwrap_collection(response))

    def get_test_case(self, project, plan_id, suite_id, test_case_ids, wit_fields=None, return_identity_ref=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if test_case_ids is not None:
            route_values['testCaseIds'] = self._serialize.url('test_case_ids', test_case_ids, 'str')
        query_parameters = {}
        if wit_fields is not None:
            query_parameters['witFields'] = self._serialize.query('wit_fields', wit_fields, 'str')
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        response = self._send(http_method='GET',
                              location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestCase]', self._unwrap_collection(response))

    def get_test_case_list(self, project, plan_id, suite_id, test_ids=None, configuration_ids=None, wit_fields=None, continuation_token=None, return_identity_ref=None, expand=None, exclude_flags=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if test_ids is not None:
            query_parameters['testIds'] = self._serialize.query('test_ids', test_ids, 'str')
        if configuration_ids is not None:
            query_parameters['configurationIds'] = self._serialize.query('configuration_ids', configuration_ids, 'str')
        if wit_fields is not None:
            query_parameters['witFields'] = self._serialize.query('wit_fields', wit_fields, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        if expand is not None:
            query_parameters['expand'] = self._serialize.query('expand', expand, 'bool')
        if exclude_flags is not None:
            query_parameters['excludeFlags'] = self._serialize.query('exclude_flags', exclude_flags, 'str')
        response = self._send(http_method='GET',
                              location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestCase]', self._unwrap_collection(response))

    def remove_test_cases_from_suite(self, project, plan_id, suite_id, test_case_ids):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if test_case_ids is not None:
            route_values['testCaseIds'] = self._serialize.url('test_case_ids', test_case_ids, 'str')
        self._send(http_method='DELETE',
                   location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                   version='6.0-preview.2',
                   route_values=route_values)

    def update_suite_test_cases(self, suite_test_case_create_update_parameters, project, plan_id, suite_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(suite_test_case_create_update_parameters, '[SuiteTestCaseCreateUpdateParameters]')
        response = self._send(http_method='PATCH',
                              location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCase]', self._unwrap_collection(response))

    def clone_test_case(self, clone_request_body, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(clone_request_body, 'CloneTestCaseParams')
        response = self._send(http_method='POST',
                              location_id='529b2b8d-82f4-4893-b1e4-1e74ea534673',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CloneTestCaseOperationInformation', response)

    def get_test_case_clone_information(self, project, clone_operation_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if clone_operation_id is not None:
            route_values['cloneOperationId'] = self._serialize.url('clone_operation_id', clone_operation_id, 'int')
        response = self._send(http_method='GET',
                              location_id='529b2b8d-82f4-4893-b1e4-1e74ea534673',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('CloneTestCaseOperationInformation', response)

    def delete_test_case(self, project, test_case_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_case_id is not None:
            route_values['testCaseId'] = self._serialize.url('test_case_id', test_case_id, 'int')
        self._send(http_method='DELETE',
                   location_id='29006fb5-816b-4ff7-a329-599943569229',
                   version='6.0-preview.1',
                   route_values=route_values)

    def clone_test_plan(self, clone_request_body, project, deep_clone=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if deep_clone is not None:
            query_parameters['deepClone'] = self._serialize.query('deep_clone', deep_clone, 'bool')
        content = self._serialize.body(clone_request_body, 'CloneTestPlanParams')
        response = self._send(http_method='POST',
                              location_id='e65df662-d8a3-46c7-ae1c-14e2d4df57e1',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('CloneTestPlanOperationInformation', response)

    def get_clone_information(self, project, clone_operation_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if clone_operation_id is not None:
            route_values['cloneOperationId'] = self._serialize.url('clone_operation_id', clone_operation_id, 'int')
        response = self._send(http_method='GET',
                              location_id='e65df662-d8a3-46c7-ae1c-14e2d4df57e1',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('CloneTestPlanOperationInformation', response)

    def get_points(self, project, plan_id, suite_id, point_ids, return_identity_ref=None, include_point_details=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if point_ids is not None:
            route_values['pointIds'] = self._serialize.url('point_ids', point_ids, 'str')
        query_parameters = {}
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        if include_point_details is not None:
            query_parameters['includePointDetails'] = self._serialize.query('include_point_details', include_point_details, 'bool')
        response = self._send(http_method='GET',
                              location_id='52df686e-bae4-4334-b0ee-b6cf4e6f6b73',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def get_points_list(self, project, plan_id, suite_id, test_point_ids=None, test_case_id=None, continuation_token=None, return_identity_ref=None, include_point_details=None, is_recursive=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if test_point_ids is not None:
            query_parameters['testPointIds'] = self._serialize.query('test_point_ids', test_point_ids, 'str')
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        if include_point_details is not None:
            query_parameters['includePointDetails'] = self._serialize.query('include_point_details', include_point_details, 'bool')
        if is_recursive is not None:
            query_parameters['isRecursive'] = self._serialize.query('is_recursive', is_recursive, 'bool')
        response = self._send(http_method='GET',
                              location_id='52df686e-bae4-4334-b0ee-b6cf4e6f6b73',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def update_test_points(self, test_point_update_params, project, plan_id, suite_id, include_point_details=None, return_identity_ref=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if include_point_details is not None:
            query_parameters['includePointDetails'] = self._serialize.query('include_point_details', include_point_details, 'bool')
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        content = self._serialize.body(test_point_update_params, '[TestPointUpdateParams]')
        response = self._send(http_method='PATCH',
                              location_id='52df686e-bae4-4334-b0ee-b6cf4e6f6b73',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def clone_test_suite(self, clone_request_body, project, deep_clone=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if deep_clone is not None:
            query_parameters['deepClone'] = self._serialize.query('deep_clone', deep_clone, 'bool')
        content = self._serialize.body(clone_request_body, 'CloneTestSuiteParams')
        response = self._send(http_method='POST',
                              location_id='181d4c97-0e98-4ee2-ad6a-4cada675e555',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('CloneTestSuiteOperationInformation', response)

    def get_suite_clone_information(self, project, clone_operation_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if clone_operation_id is not None:
            route_values['cloneOperationId'] = self._serialize.url('clone_operation_id', clone_operation_id, 'int')
        response = self._send(http_method='GET',
                              location_id='181d4c97-0e98-4ee2-ad6a-4cada675e555',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('CloneTestSuiteOperationInformation', response)

    def create_test_variable(self, test_variable_create_update_parameters, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_variable_create_update_parameters, 'TestVariableCreateUpdateParameters')
        response = self._send(http_method='POST',
                              location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestVariable', response)

    def delete_test_variable(self, project, test_variable_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_variable_id is not None:
            route_values['testVariableId'] = self._serialize.url('test_variable_id', test_variable_id, 'int')
        self._send(http_method='DELETE',
                   location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_test_variable_by_id(self, project, test_variable_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_variable_id is not None:
            route_values['testVariableId'] = self._serialize.url('test_variable_id', test_variable_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('TestVariable', response)

    def get_test_variables(self, project, continuation_token=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestVariable]', self._unwrap_collection(response))

    def update_test_variable(self, test_variable_create_update_parameters, project, test_variable_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_variable_id is not None:
            route_values['testVariableId'] = self._serialize.url('test_variable_id', test_variable_id, 'int')
        content = self._serialize.body(test_variable_create_update_parameters, 'TestVariableCreateUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestVariable', response)

