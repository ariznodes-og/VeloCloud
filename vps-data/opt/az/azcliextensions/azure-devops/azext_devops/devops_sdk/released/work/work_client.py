# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.work import models


class WorkClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(WorkClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '1d4f49f9-02b9-4e26-b826-2cdb6195f2a9'

    def get_backlog_configurations(self, team_context):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        response = self._send(http_method='GET',
                              location_id='7799f497-3cb5-4f16-ad4f-5cd06012db64',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('BacklogConfiguration', response)

    def get_column_suggested_values(self, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='eb7ec5a3-1ba3-4fd1-b834-49a5a387e57d',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BoardSuggestedValue]', self._unwrap_collection(response))

    def get_row_suggested_values(self, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='bb494cc6-a0f5-4c6c-8dca-ea6912e79eb9',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BoardSuggestedValue]', self._unwrap_collection(response))

    def get_board(self, team_context, id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        response = self._send(http_method='GET',
                              location_id='23ad19fc-3b8e-4877-8462-b3f92bc06b40',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('Board', response)

    def get_boards(self, team_context):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        response = self._send(http_method='GET',
                              location_id='23ad19fc-3b8e-4877-8462-b3f92bc06b40',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BoardReference]', self._unwrap_collection(response))

    def set_board_options(self, options, team_context, id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        content = self._serialize.body(options, '{str}')
        response = self._send(http_method='PUT',
                              location_id='23ad19fc-3b8e-4877-8462-b3f92bc06b40',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('{str}', self._unwrap_collection(response))

    def get_capacities_with_identity_ref(self, team_context, iteration_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'str')
        response = self._send(http_method='GET',
                              location_id='74412d15-8c1a-4352-a48d-ef1ed5587d57',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[TeamMemberCapacityIdentityRef]', self._unwrap_collection(response))

    def get_capacity_with_identity_ref(self, team_context, iteration_id, team_member_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'str')
        if team_member_id is not None:
            route_values['teamMemberId'] = self._serialize.url('team_member_id', team_member_id, 'str')
        response = self._send(http_method='GET',
                              location_id='74412d15-8c1a-4352-a48d-ef1ed5587d57',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TeamMemberCapacityIdentityRef', response)

    def replace_capacities_with_identity_ref(self, capacities, team_context, iteration_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'str')
        content = self._serialize.body(capacities, '[TeamMemberCapacityIdentityRef]')
        response = self._send(http_method='PUT',
                              location_id='74412d15-8c1a-4352-a48d-ef1ed5587d57',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TeamMemberCapacityIdentityRef]', self._unwrap_collection(response))

    def update_capacity_with_identity_ref(self, patch, team_context, iteration_id, team_member_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'str')
        if team_member_id is not None:
            route_values['teamMemberId'] = self._serialize.url('team_member_id', team_member_id, 'str')
        content = self._serialize.body(patch, 'CapacityPatch')
        response = self._send(http_method='PATCH',
                              location_id='74412d15-8c1a-4352-a48d-ef1ed5587d57',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TeamMemberCapacityIdentityRef', response)

    def get_board_card_rule_settings(self, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        response = self._send(http_method='GET',
                              location_id='b044a3d9-02ea-49c7-91a1-b730949cc896',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('BoardCardRuleSettings', response)

    def update_board_card_rule_settings(self, board_card_rule_settings, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        content = self._serialize.body(board_card_rule_settings, 'BoardCardRuleSettings')
        response = self._send(http_method='PATCH',
                              location_id='b044a3d9-02ea-49c7-91a1-b730949cc896',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BoardCardRuleSettings', response)

    def get_board_card_settings(self, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        response = self._send(http_method='GET',
                              location_id='07c3b467-bc60-4f05-8e34-599ce288fafc',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('BoardCardSettings', response)

    def update_board_card_settings(self, board_card_settings_to_save, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        content = self._serialize.body(board_card_settings_to_save, 'BoardCardSettings')
        response = self._send(http_method='PUT',
                              location_id='07c3b467-bc60-4f05-8e34-599ce288fafc',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BoardCardSettings', response)

    def get_board_chart(self, team_context, board, name):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='45fe888c-239e-49fd-958c-df1a1ab21d97',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('BoardChart', response)

    def get_board_charts(self, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        response = self._send(http_method='GET',
                              location_id='45fe888c-239e-49fd-958c-df1a1ab21d97',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BoardChartReference]', self._unwrap_collection(response))

    def update_board_chart(self, chart, team_context, board, name):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        content = self._serialize.body(chart, 'BoardChart')
        response = self._send(http_method='PATCH',
                              location_id='45fe888c-239e-49fd-958c-df1a1ab21d97',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BoardChart', response)

    def get_board_columns(self, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        response = self._send(http_method='GET',
                              location_id='c555d7ff-84e1-47df-9923-a3fe0cd8751b',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BoardColumn]', self._unwrap_collection(response))

    def update_board_columns(self, board_columns, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        content = self._serialize.body(board_columns, '[BoardColumn]')
        response = self._send(http_method='PUT',
                              location_id='c555d7ff-84e1-47df-9923-a3fe0cd8751b',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[BoardColumn]', self._unwrap_collection(response))

    def get_delivery_timeline_data(self, project, id, revision=None, start_date=None, end_date=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        if start_date is not None:
            query_parameters['startDate'] = self._serialize.query('start_date', start_date, 'iso-8601')
        if end_date is not None:
            query_parameters['endDate'] = self._serialize.query('end_date', end_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='bdd0834e-101f-49f0-a6ae-509f384a12b4',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeliveryViewData', response)

    def delete_team_iteration(self, team_context, id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        self._send(http_method='DELETE',
                   location_id='c9175577-28a1-4b06-9197-8636af9f64ad',
                   version='5.1',
                   route_values=route_values)

    def get_team_iteration(self, team_context, id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        response = self._send(http_method='GET',
                              location_id='c9175577-28a1-4b06-9197-8636af9f64ad',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TeamSettingsIteration', response)

    def get_team_iterations(self, team_context, timeframe=None):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        query_parameters = {}
        if timeframe is not None:
            query_parameters['$timeframe'] = self._serialize.query('timeframe', timeframe, 'str')
        response = self._send(http_method='GET',
                              location_id='c9175577-28a1-4b06-9197-8636af9f64ad',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TeamSettingsIteration]', self._unwrap_collection(response))

    def post_team_iteration(self, iteration, team_context):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(iteration, 'TeamSettingsIteration')
        response = self._send(http_method='POST',
                              location_id='c9175577-28a1-4b06-9197-8636af9f64ad',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TeamSettingsIteration', response)

    def create_plan(self, posted_plan, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(posted_plan, 'CreatePlan')
        response = self._send(http_method='POST',
                              location_id='0b42cb47-cd73-4810-ac90-19c9ba147453',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Plan', response)

    def delete_plan(self, project, id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        self._send(http_method='DELETE',
                   location_id='0b42cb47-cd73-4810-ac90-19c9ba147453',
                   version='5.1',
                   route_values=route_values)

    def get_plan(self, project, id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        response = self._send(http_method='GET',
                              location_id='0b42cb47-cd73-4810-ac90-19c9ba147453',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('Plan', response)

    def get_plans(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='0b42cb47-cd73-4810-ac90-19c9ba147453',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[Plan]', self._unwrap_collection(response))

    def update_plan(self, updated_plan, project, id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        content = self._serialize.body(updated_plan, 'UpdatePlan')
        response = self._send(http_method='PUT',
                              location_id='0b42cb47-cd73-4810-ac90-19c9ba147453',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Plan', response)

    def get_board_rows(self, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        response = self._send(http_method='GET',
                              location_id='0863355d-aefd-4d63-8669-984c9b7b0e78',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[BoardRow]', self._unwrap_collection(response))

    def update_board_rows(self, board_rows, team_context, board):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if board is not None:
            route_values['board'] = self._serialize.url('board', board, 'str')
        content = self._serialize.body(board_rows, '[BoardRow]')
        response = self._send(http_method='PUT',
                              location_id='0863355d-aefd-4d63-8669-984c9b7b0e78',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[BoardRow]', self._unwrap_collection(response))

    def get_team_days_off(self, team_context, iteration_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'str')
        response = self._send(http_method='GET',
                              location_id='2d4faa2e-9150-4cbf-a47a-932b1b4a0773',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TeamSettingsDaysOff', response)

    def update_team_days_off(self, days_off_patch, team_context, iteration_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'str')
        content = self._serialize.body(days_off_patch, 'TeamSettingsDaysOffPatch')
        response = self._send(http_method='PATCH',
                              location_id='2d4faa2e-9150-4cbf-a47a-932b1b4a0773',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TeamSettingsDaysOff', response)

    def get_team_field_values(self, team_context):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        response = self._send(http_method='GET',
                              location_id='07ced576-58ed-49e6-9c1e-5cb53ab8bf2a',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TeamFieldValues', response)

    def update_team_field_values(self, patch, team_context):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(patch, 'TeamFieldValuesPatch')
        response = self._send(http_method='PATCH',
                              location_id='07ced576-58ed-49e6-9c1e-5cb53ab8bf2a',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TeamFieldValues', response)

    def get_team_settings(self, team_context):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        response = self._send(http_method='GET',
                              location_id='c3c1012b-bea7-49d7-b45e-1664e566f84c',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TeamSetting', response)

    def update_team_settings(self, team_settings_patch, team_context):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(team_settings_patch, 'TeamSettingsPatch')
        response = self._send(http_method='PATCH',
                              location_id='c3c1012b-bea7-49d7-b45e-1664e566f84c',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TeamSetting', response)

