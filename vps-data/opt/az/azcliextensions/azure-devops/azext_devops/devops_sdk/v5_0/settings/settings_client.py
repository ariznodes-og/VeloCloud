# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client


class SettingsClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(SettingsClient, self).__init__(base_url, creds)
        self._serialize = Serializer()
        self._deserialize = Deserializer()

    resource_area_identifier = None

    def get_entries(self, user_scope, key=None):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if key is not None:
            route_values['key'] = self._serialize.url('key', key, 'str')
        response = self._send(http_method='GET',
                              location_id='cd006711-163d-4cd4-a597-b05bad2556ff',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('{object}', self._unwrap_collection(response))

    def remove_entries(self, user_scope, key):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if key is not None:
            route_values['key'] = self._serialize.url('key', key, 'str')
        self._send(http_method='DELETE',
                   location_id='cd006711-163d-4cd4-a597-b05bad2556ff',
                   version='5.0-preview.1',
                   route_values=route_values)

    def set_entries(self, entries, user_scope):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        content = self._serialize.body(entries, '{object}')
        self._send(http_method='PATCH',
                   location_id='cd006711-163d-4cd4-a597-b05bad2556ff',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content)

    def get_entries_for_scope(self, user_scope, scope_name, scope_value, key=None):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if scope_name is not None:
            route_values['scopeName'] = self._serialize.url('scope_name', scope_name, 'str')
        if scope_value is not None:
            route_values['scopeValue'] = self._serialize.url('scope_value', scope_value, 'str')
        if key is not None:
            route_values['key'] = self._serialize.url('key', key, 'str')
        response = self._send(http_method='GET',
                              location_id='4cbaafaf-e8af-4570-98d1-79ee99c56327',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('{object}', self._unwrap_collection(response))

    def remove_entries_for_scope(self, user_scope, scope_name, scope_value, key):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if scope_name is not None:
            route_values['scopeName'] = self._serialize.url('scope_name', scope_name, 'str')
        if scope_value is not None:
            route_values['scopeValue'] = self._serialize.url('scope_value', scope_value, 'str')
        if key is not None:
            route_values['key'] = self._serialize.url('key', key, 'str')
        self._send(http_method='DELETE',
                   location_id='4cbaafaf-e8af-4570-98d1-79ee99c56327',
                   version='5.0-preview.1',
                   route_values=route_values)

    def set_entries_for_scope(self, entries, user_scope, scope_name, scope_value):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if scope_name is not None:
            route_values['scopeName'] = self._serialize.url('scope_name', scope_name, 'str')
        if scope_value is not None:
            route_values['scopeValue'] = self._serialize.url('scope_value', scope_value, 'str')
        content = self._serialize.body(entries, '{object}')
        self._send(http_method='PATCH',
                   location_id='4cbaafaf-e8af-4570-98d1-79ee99c56327',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content)

