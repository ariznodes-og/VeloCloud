# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class CloudLoadTestClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(CloudLoadTestClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '7ae6d0a6-cda5-44cf-a261-28c392bed25c'

    def create_agent_group(self, group):
        content = self._serialize.body(group, 'AgentGroup')
        response = self._send(http_method='POST',
                              location_id='ab8d91c1-12d9-4ec5-874d-1ddb23e17720',
                              version='5.1',
                              content=content)
        return self._deserialize('AgentGroup', response)

    def get_agent_groups(self, agent_group_id=None, machine_setup_input=None, machine_access_data=None, outgoing_request_urls=None, agent_group_name=None):
        route_values = {}
        if agent_group_id is not None:
            route_values['agentGroupId'] = self._serialize.url('agent_group_id', agent_group_id, 'str')
        query_parameters = {}
        if machine_setup_input is not None:
            query_parameters['machineSetupInput'] = self._serialize.query('machine_setup_input', machine_setup_input, 'bool')
        if machine_access_data is not None:
            query_parameters['machineAccessData'] = self._serialize.query('machine_access_data', machine_access_data, 'bool')
        if outgoing_request_urls is not None:
            query_parameters['outgoingRequestUrls'] = self._serialize.query('outgoing_request_urls', outgoing_request_urls, 'bool')
        if agent_group_name is not None:
            query_parameters['agentGroupName'] = self._serialize.query('agent_group_name', agent_group_name, 'str')
        response = self._send(http_method='GET',
                              location_id='ab8d91c1-12d9-4ec5-874d-1ddb23e17720',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def delete_static_agent(self, agent_group_id, agent_name):
        route_values = {}
        if agent_group_id is not None:
            route_values['agentGroupId'] = self._serialize.url('agent_group_id', agent_group_id, 'str')
        query_parameters = {}
        if agent_name is not None:
            query_parameters['agentName'] = self._serialize.query('agent_name', agent_name, 'str')
        response = self._send(http_method='DELETE',
                              location_id='87e4b63d-7142-4b50-801e-72ba9ff8ee9b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('str', response)

    def get_static_agents(self, agent_group_id, agent_name=None):
        route_values = {}
        if agent_group_id is not None:
            route_values['agentGroupId'] = self._serialize.url('agent_group_id', agent_group_id, 'str')
        query_parameters = {}
        if agent_name is not None:
            query_parameters['agentName'] = self._serialize.query('agent_name', agent_name, 'str')
        response = self._send(http_method='GET',
                              location_id='87e4b63d-7142-4b50-801e-72ba9ff8ee9b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_application(self, application_id):
        route_values = {}
        if application_id is not None:
            route_values['applicationId'] = self._serialize.url('application_id', application_id, 'str')
        response = self._send(http_method='GET',
                              location_id='2c986dce-8e8d-4142-b541-d016d5aff764',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('Application', response)

    def get_applications(self, type=None):
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='2c986dce-8e8d-4142-b541-d016d5aff764',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[Application]', self._unwrap_collection(response))

    def get_counters(self, test_run_id, group_names, include_summary=None):
        route_values = {}
        if test_run_id is not None:
            route_values['testRunId'] = self._serialize.url('test_run_id', test_run_id, 'str')
        query_parameters = {}
        if group_names is not None:
            query_parameters['groupNames'] = self._serialize.query('group_names', group_names, 'str')
        if include_summary is not None:
            query_parameters['includeSummary'] = self._serialize.query('include_summary', include_summary, 'bool')
        response = self._send(http_method='GET',
                              location_id='29265ea4-b5a5-4b2e-b054-47f5f6f00183',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRunCounterInstance]', self._unwrap_collection(response))

    def get_application_counters(self, application_id=None, plugintype=None):
        query_parameters = {}
        if application_id is not None:
            query_parameters['applicationId'] = self._serialize.query('application_id', application_id, 'str')
        if plugintype is not None:
            query_parameters['plugintype'] = self._serialize.query('plugintype', plugintype, 'str')
        response = self._send(http_method='GET',
                              location_id='c1275ce9-6d26-4bc6-926b-b846502e812d',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[ApplicationCounters]', self._unwrap_collection(response))

    def get_counter_samples(self, counter_sample_query_details, test_run_id):
        route_values = {}
        if test_run_id is not None:
            route_values['testRunId'] = self._serialize.url('test_run_id', test_run_id, 'str')
        content = self._serialize.body(counter_sample_query_details, 'VssJsonCollectionWrapper')
        response = self._send(http_method='POST',
                              location_id='bad18480-7193-4518-992a-37289c5bb92d',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CounterSamplesResult', response)

    def get_load_test_run_errors(self, test_run_id, type=None, sub_type=None, detailed=None):
        route_values = {}
        if test_run_id is not None:
            route_values['testRunId'] = self._serialize.url('test_run_id', test_run_id, 'str')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if sub_type is not None:
            query_parameters['subType'] = self._serialize.query('sub_type', sub_type, 'str')
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query('detailed', detailed, 'bool')
        response = self._send(http_method='GET',
                              location_id='b52025a7-3fb4-4283-8825-7079e75bd402',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('LoadTestErrors', response)

    def get_test_run_messages(self, test_run_id):
        route_values = {}
        if test_run_id is not None:
            route_values['testRunId'] = self._serialize.url('test_run_id', test_run_id, 'str')
        response = self._send(http_method='GET',
                              location_id='2e7ba122-f522-4205-845b-2d270e59850a',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[TestRunMessage]', self._unwrap_collection(response))

    def get_plugin(self, type):
        route_values = {}
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='7dcb0bb2-42d5-4729-9958-c0401d5e7693',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('ApplicationType', response)

    def get_plugins(self):
        response = self._send(http_method='GET',
                              location_id='7dcb0bb2-42d5-4729-9958-c0401d5e7693',
                              version='5.1')
        return self._deserialize('[ApplicationType]', self._unwrap_collection(response))

    def get_load_test_result(self, test_run_id):
        route_values = {}
        if test_run_id is not None:
            route_values['testRunId'] = self._serialize.url('test_run_id', test_run_id, 'str')
        response = self._send(http_method='GET',
                              location_id='5ed69bd8-4557-4cec-9b75-1ad67d0c257b',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TestResults', response)

    def create_test_definition(self, test_definition):
        content = self._serialize.body(test_definition, 'TestDefinition')
        response = self._send(http_method='POST',
                              location_id='a8f9b135-f604-41ea-9d74-d9a5fd32fcd8',
                              version='5.1',
                              content=content)
        return self._deserialize('TestDefinition', response)

    def get_test_definition(self, test_definition_id):
        route_values = {}
        if test_definition_id is not None:
            route_values['testDefinitionId'] = self._serialize.url('test_definition_id', test_definition_id, 'str')
        response = self._send(http_method='GET',
                              location_id='a8f9b135-f604-41ea-9d74-d9a5fd32fcd8',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TestDefinition', response)

    def get_test_definitions(self, from_date=None, to_date=None, top=None):
        query_parameters = {}
        if from_date is not None:
            query_parameters['fromDate'] = self._serialize.query('from_date', from_date, 'str')
        if to_date is not None:
            query_parameters['toDate'] = self._serialize.query('to_date', to_date, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='a8f9b135-f604-41ea-9d74-d9a5fd32fcd8',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TestDefinitionBasic]', self._unwrap_collection(response))

    def update_test_definition(self, test_definition):
        content = self._serialize.body(test_definition, 'TestDefinition')
        response = self._send(http_method='PUT',
                              location_id='a8f9b135-f604-41ea-9d74-d9a5fd32fcd8',
                              version='5.1',
                              content=content)
        return self._deserialize('TestDefinition', response)

    def create_test_drop(self, web_test_drop):
        content = self._serialize.body(web_test_drop, 'TestDrop')
        response = self._send(http_method='POST',
                              location_id='d89d0e08-505c-4357-96f6-9729311ce8ad',
                              version='5.1',
                              content=content)
        return self._deserialize('TestDrop', response)

    def get_test_drop(self, test_drop_id):
        route_values = {}
        if test_drop_id is not None:
            route_values['testDropId'] = self._serialize.url('test_drop_id', test_drop_id, 'str')
        response = self._send(http_method='GET',
                              location_id='d89d0e08-505c-4357-96f6-9729311ce8ad',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TestDrop', response)

    def create_test_run(self, web_test_run):
        content = self._serialize.body(web_test_run, 'TestRun')
        response = self._send(http_method='POST',
                              location_id='b41a84ff-ff03-4ac1-b76e-e7ea25c92aba',
                              version='5.1',
                              content=content)
        return self._deserialize('TestRun', response)

    def get_test_run(self, test_run_id):
        route_values = {}
        if test_run_id is not None:
            route_values['testRunId'] = self._serialize.url('test_run_id', test_run_id, 'str')
        response = self._send(http_method='GET',
                              location_id='b41a84ff-ff03-4ac1-b76e-e7ea25c92aba',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TestRun', response)

    def get_test_runs(self, name=None, requested_by=None, status=None, run_type=None, from_date=None, to_date=None, detailed=None, top=None, runsourceidentifier=None, retention_state=None):
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if requested_by is not None:
            query_parameters['requestedBy'] = self._serialize.query('requested_by', requested_by, 'str')
        if status is not None:
            query_parameters['status'] = self._serialize.query('status', status, 'str')
        if run_type is not None:
            query_parameters['runType'] = self._serialize.query('run_type', run_type, 'str')
        if from_date is not None:
            query_parameters['fromDate'] = self._serialize.query('from_date', from_date, 'str')
        if to_date is not None:
            query_parameters['toDate'] = self._serialize.query('to_date', to_date, 'str')
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query('detailed', detailed, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if runsourceidentifier is not None:
            query_parameters['runsourceidentifier'] = self._serialize.query('runsourceidentifier', runsourceidentifier, 'str')
        if retention_state is not None:
            query_parameters['retentionState'] = self._serialize.query('retention_state', retention_state, 'str')
        response = self._send(http_method='GET',
                              location_id='b41a84ff-ff03-4ac1-b76e-e7ea25c92aba',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def update_test_run(self, web_test_run, test_run_id):
        route_values = {}
        if test_run_id is not None:
            route_values['testRunId'] = self._serialize.url('test_run_id', test_run_id, 'str')
        content = self._serialize.body(web_test_run, 'TestRun')
        self._send(http_method='PATCH',
                   location_id='b41a84ff-ff03-4ac1-b76e-e7ea25c92aba',
                   version='5.1',
                   route_values=route_values,
                   content=content)

