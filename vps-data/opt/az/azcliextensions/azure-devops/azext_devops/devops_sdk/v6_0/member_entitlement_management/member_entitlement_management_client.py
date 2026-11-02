# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class MemberEntitlementManagementClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(MemberEntitlementManagementClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '68ddce18-2501-45f1-a17b-7931a9922690'

    def add_group_entitlement(self, group_entitlement, rule_option=None):
        query_parameters = {}
        if rule_option is not None:
            query_parameters['ruleOption'] = self._serialize.query('rule_option', rule_option, 'str')
        content = self._serialize.body(group_entitlement, 'GroupEntitlement')
        response = self._send(http_method='POST',
                              location_id='2280bffa-58a2-49da-822e-0764a1bb44f7',
                              version='6.0-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GroupEntitlementOperationReference', response)

    def delete_group_entitlement(self, group_id, rule_option=None, remove_group_membership=None):
        route_values = {}
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        query_parameters = {}
        if rule_option is not None:
            query_parameters['ruleOption'] = self._serialize.query('rule_option', rule_option, 'str')
        if remove_group_membership is not None:
            query_parameters['removeGroupMembership'] = self._serialize.query('remove_group_membership', remove_group_membership, 'bool')
        response = self._send(http_method='DELETE',
                              location_id='2280bffa-58a2-49da-822e-0764a1bb44f7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GroupEntitlementOperationReference', response)

    def get_group_entitlement(self, group_id):
        route_values = {}
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        response = self._send(http_method='GET',
                              location_id='2280bffa-58a2-49da-822e-0764a1bb44f7',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GroupEntitlement', response)

    def update_group_entitlement(self, document, group_id, rule_option=None):
        route_values = {}
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        query_parameters = {}
        if rule_option is not None:
            query_parameters['ruleOption'] = self._serialize.query('rule_option', rule_option, 'str')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='2280bffa-58a2-49da-822e-0764a1bb44f7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('GroupEntitlementOperationReference', response)

    def get_group_entitlements(self):
        response = self._send(http_method='GET',
                              location_id='9bce1f43-2629-419f-8f6c-7503be58a4f3',
                              version='6.0-preview.1')
        return self._deserialize('[GroupEntitlement]', self._unwrap_collection(response))

    def add_member_to_group(self, group_id, member_id):
        route_values = {}
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if member_id is not None:
            route_values['memberId'] = self._serialize.url('member_id', member_id, 'str')
        self._send(http_method='PUT',
                   location_id='45a36e53-5286-4518-aa72-2d29f7acc5d8',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_group_members(self, group_id, max_results=None, paging_token=None):
        route_values = {}
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        query_parameters = {}
        if max_results is not None:
            query_parameters['maxResults'] = self._serialize.query('max_results', max_results, 'int')
        if paging_token is not None:
            query_parameters['pagingToken'] = self._serialize.query('paging_token', paging_token, 'str')
        response = self._send(http_method='GET',
                              location_id='45a36e53-5286-4518-aa72-2d29f7acc5d8',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PagedGraphMemberList', response)

    def remove_member_from_group(self, group_id, member_id):
        route_values = {}
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if member_id is not None:
            route_values['memberId'] = self._serialize.url('member_id', member_id, 'str')
        self._send(http_method='DELETE',
                   location_id='45a36e53-5286-4518-aa72-2d29f7acc5d8',
                   version='6.0-preview.1',
                   route_values=route_values)

    def add_user_entitlement(self, user_entitlement):
        content = self._serialize.body(user_entitlement, 'UserEntitlement')
        response = self._send(http_method='POST',
                              location_id='387f832c-dbf2-4643-88e9-c1aa94dbb737',
                              version='6.0-preview.3',
                              content=content)
        return self._deserialize('UserEntitlementsPostResponse', response)

    def search_user_entitlements(self, continuation_token=None, select=None, filter=None, order_by=None):
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if select is not None:
            query_parameters['select'] = self._serialize.query('select', select, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query('filter', filter, 'str')
        if order_by is not None:
            query_parameters['$orderBy'] = self._serialize.query('order_by', order_by, 'str')
        response = self._send(http_method='GET',
                              location_id='387f832c-dbf2-4643-88e9-c1aa94dbb737',
                              version='6.0-preview.3',
                              query_parameters=query_parameters)
        return self._deserialize('PagedGraphMemberList', response)

    def update_user_entitlements(self, document, do_not_send_invite_for_new_users=None):
        query_parameters = {}
        if do_not_send_invite_for_new_users is not None:
            query_parameters['doNotSendInviteForNewUsers'] = self._serialize.query('do_not_send_invite_for_new_users', do_not_send_invite_for_new_users, 'bool')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='387f832c-dbf2-4643-88e9-c1aa94dbb737',
                              version='6.0-preview.3',
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('UserEntitlementOperationReference', response)

    def delete_user_entitlement(self, user_id):
        route_values = {}
        if user_id is not None:
            route_values['userId'] = self._serialize.url('user_id', user_id, 'str')
        self._send(http_method='DELETE',
                   location_id='8480c6eb-ce60-47e9-88df-eca3c801638b',
                   version='6.0-preview.3',
                   route_values=route_values)

    def get_user_entitlement(self, user_id):
        route_values = {}
        if user_id is not None:
            route_values['userId'] = self._serialize.url('user_id', user_id, 'str')
        response = self._send(http_method='GET',
                              location_id='8480c6eb-ce60-47e9-88df-eca3c801638b',
                              version='6.0-preview.3',
                              route_values=route_values)
        return self._deserialize('UserEntitlement', response)

    def update_user_entitlement(self, document, user_id):
        route_values = {}
        if user_id is not None:
            route_values['userId'] = self._serialize.url('user_id', user_id, 'str')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='8480c6eb-ce60-47e9-88df-eca3c801638b',
                              version='6.0-preview.3',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('UserEntitlementsPatchResponse', response)

    def get_users_summary(self, select=None):
        query_parameters = {}
        if select is not None:
            query_parameters['select'] = self._serialize.query('select', select, 'str')
        response = self._send(http_method='GET',
                              location_id='5ae55b13-c9dd-49d1-957e-6e76c152e3d9',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('UsersSummary', response)

