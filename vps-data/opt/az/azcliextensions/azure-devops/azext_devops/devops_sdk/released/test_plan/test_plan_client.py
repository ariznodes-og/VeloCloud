# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.test_plan import models


class TestPlanClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(TestPlanClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_suites_by_test_case_id(self, test_case_id):
        query_parameters = {}
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'int')
        response = self._send(http_method='GET',
                              location_id='a4080e84-f17b-4fad-84f1-7960b6525bf2',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TestSuite]', self._unwrap_collection(response))

