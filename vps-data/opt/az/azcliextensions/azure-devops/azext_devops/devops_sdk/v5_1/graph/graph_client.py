# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class GraphClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(GraphClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'bb1e7ec9-e901-4b68-999a-de7012b920f8'

    def delete_avatar(self, subject_descriptor):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        self._send(http_method='DELETE',
                   location_id='801eaf9c-0585-4be8-9cdb-b0efa074de91',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_avatar(self, subject_descriptor, size=None, format=None):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        query_parameters = {}
        if size is not None:
            query_parameters['size'] = self._serialize.query('size', size, 'str')
        if format is not None:
            query_parameters['format'] = self._serialize.query('format', format, 'str')
        response = self._send(http_method='GET',
                              location_id='801eaf9c-0585-4be8-9cdb-b0efa074de91',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Avatar', response)

    def set_avatar(self, avatar, subject_descriptor):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        content = self._serialize.body(avatar, 'Avatar')
        self._send(http_method='PUT',
                   location_id='801eaf9c-0585-4be8-9cdb-b0efa074de91',
                   version='5.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_descriptor(self, storage_key):
        route_values = {}
        if storage_key is not None:
            route_values['storageKey'] = self._serialize.url('storage_key', storage_key, 'str')
        response = self._send(http_method='GET',
                              location_id='048aee0a-7072-4cde-ab73-7af77b1e0b4e',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('GraphDescriptorResult', response)

    def create_group(self, creation_context, scope_descriptor=None, group_descriptors=None):
        query_parameters = {}
        if scope_descriptor is not None:
            query_parameters['scopeDescriptor'] = self._serialize.query('scope_descriptor', scope_descriptor, 'str')
        if group_descriptors is not None:
            group_descriptors = ",".join(group_descriptors)
            query_parameters['groupDescriptors'] = self._serialize.query('group_descriptors', group_descriptors, 'str')
        content = self._serialize.body(creation_context, 'GraphGroupCreationContext')
        response = self._send(http_method='POST',
                              location_id='ebbe6af8-0b91-4c13-8cf1-777c14858188',
                              version='5.1-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GraphGroup', response)

    def delete_group(self, group_descriptor):
        route_values = {}
        if group_descriptor is not None:
            route_values['groupDescriptor'] = self._serialize.url('group_descriptor', group_descriptor, 'str')
        self._send(http_method='DELETE',
                   location_id='ebbe6af8-0b91-4c13-8cf1-777c14858188',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_group(self, group_descriptor):
        route_values = {}
        if group_descriptor is not None:
            route_values['groupDescriptor'] = self._serialize.url('group_descriptor', group_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='ebbe6af8-0b91-4c13-8cf1-777c14858188',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('GraphGroup', response)

    def list_groups(self, scope_descriptor=None, subject_types=None, continuation_token=None):
        query_parameters = {}
        if scope_descriptor is not None:
            query_parameters['scopeDescriptor'] = self._serialize.query('scope_descriptor', scope_descriptor, 'str')
        if subject_types is not None:
            subject_types = ",".join(subject_types)
            query_parameters['subjectTypes'] = self._serialize.query('subject_types', subject_types, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='ebbe6af8-0b91-4c13-8cf1-777c14858188',
                              version='5.1-preview.1',
                              query_parameters=query_parameters)
        response_object = models.PagedGraphGroups()
        response_object.graph_groups = self._deserialize('[GraphGroup]', self._unwrap_collection(response))
        response_object.continuation_token = response.headers.get('X-MS-ContinuationToken')
        return response_object

    def update_group(self, group_descriptor, patch_document):
        route_values = {}
        if group_descriptor is not None:
            route_values['groupDescriptor'] = self._serialize.url('group_descriptor', group_descriptor, 'str')
        content = self._serialize.body(patch_document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='ebbe6af8-0b91-4c13-8cf1-777c14858188',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('GraphGroup', response)

    def add_membership(self, subject_descriptor, container_descriptor):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        if container_descriptor is not None:
            route_values['containerDescriptor'] = self._serialize.url('container_descriptor', container_descriptor, 'str')
        response = self._send(http_method='PUT',
                              location_id='3fd2e6ca-fb30-443a-b579-95b19ed0934c',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('GraphMembership', response)

    def check_membership_existence(self, subject_descriptor, container_descriptor):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        if container_descriptor is not None:
            route_values['containerDescriptor'] = self._serialize.url('container_descriptor', container_descriptor, 'str')
        self._send(http_method='HEAD',
                   location_id='3fd2e6ca-fb30-443a-b579-95b19ed0934c',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_membership(self, subject_descriptor, container_descriptor):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        if container_descriptor is not None:
            route_values['containerDescriptor'] = self._serialize.url('container_descriptor', container_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='3fd2e6ca-fb30-443a-b579-95b19ed0934c',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('GraphMembership', response)

    def remove_membership(self, subject_descriptor, container_descriptor):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        if container_descriptor is not None:
            route_values['containerDescriptor'] = self._serialize.url('container_descriptor', container_descriptor, 'str')
        self._send(http_method='DELETE',
                   location_id='3fd2e6ca-fb30-443a-b579-95b19ed0934c',
                   version='5.1-preview.1',
                   route_values=route_values)

    def list_memberships(self, subject_descriptor, direction=None, depth=None):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        query_parameters = {}
        if direction is not None:
            query_parameters['direction'] = self._serialize.query('direction', direction, 'str')
        if depth is not None:
            query_parameters['depth'] = self._serialize.query('depth', depth, 'int')
        response = self._send(http_method='GET',
                              location_id='e34b6394-6b30-4435-94a9-409a5eef3e31',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GraphMembership]', self._unwrap_collection(response))

    def get_membership_state(self, subject_descriptor):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='1ffe5c94-1144-4191-907b-d0211cad36a8',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('GraphMembershipState', response)

    def get_provider_info(self, user_descriptor):
        route_values = {}
        if user_descriptor is not None:
            route_values['userDescriptor'] = self._serialize.url('user_descriptor', user_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='1e377995-6fa2-4588-bd64-930186abdcfa',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('GraphProviderInfo', response)

    def request_access(self, message):
        content = self._serialize.body(message, 'str')
        self._send(http_method='POST',
                   location_id='8d54bf92-8c99-47f2-9972-b21341f1722e',
                   version='5.1-preview.1',
                   content=content)

    def get_storage_key(self, subject_descriptor):
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='eb85f8cc-f0f6-4264-a5b1-ffe2e4d4801f',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('GraphStorageKeyResult', response)

    def lookup_subjects(self, subject_lookup):
        content = self._serialize.body(subject_lookup, 'GraphSubjectLookup')
        response = self._send(http_method='POST',
                              location_id='4dd4d168-11f2-48c4-83e8-756fa0de027c',
                              version='5.1-preview.1',
                              content=content)
        return self._deserialize('{GraphSubject}', self._unwrap_collection(response))

    def create_user(self, creation_context, group_descriptors=None):
        query_parameters = {}
        if group_descriptors is not None:
            group_descriptors = ",".join(group_descriptors)
            query_parameters['groupDescriptors'] = self._serialize.query('group_descriptors', group_descriptors, 'str')
        content = self._serialize.body(creation_context, 'GraphUserCreationContext')
        response = self._send(http_method='POST',
                              location_id='005e26ec-6b77-4e4f-a986-b3827bf241f5',
                              version='5.1-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GraphUser', response)

    def delete_user(self, user_descriptor):
        route_values = {}
        if user_descriptor is not None:
            route_values['userDescriptor'] = self._serialize.url('user_descriptor', user_descriptor, 'str')
        self._send(http_method='DELETE',
                   location_id='005e26ec-6b77-4e4f-a986-b3827bf241f5',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_user(self, user_descriptor):
        route_values = {}
        if user_descriptor is not None:
            route_values['userDescriptor'] = self._serialize.url('user_descriptor', user_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='005e26ec-6b77-4e4f-a986-b3827bf241f5',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('GraphUser', response)

    def list_users(self, subject_types=None, continuation_token=None):
        query_parameters = {}
        if subject_types is not None:
            subject_types = ",".join(subject_types)
            query_parameters['subjectTypes'] = self._serialize.query('subject_types', subject_types, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='005e26ec-6b77-4e4f-a986-b3827bf241f5',
                              version='5.1-preview.1',
                              query_parameters=query_parameters)
        response_object = models.PagedGraphUsers()
        response_object.graph_users = self._deserialize('[GraphUser]', self._unwrap_collection(response))
        response_object.continuation_token = response.headers.get('X-MS-ContinuationToken')
        return response_object

    def update_user(self, update_context, user_descriptor):
        route_values = {}
        if user_descriptor is not None:
            route_values['userDescriptor'] = self._serialize.url('user_descriptor', user_descriptor, 'str')
        content = self._serialize.body(update_context, 'GraphUserUpdateContext')
        response = self._send(http_method='PATCH',
                              location_id='005e26ec-6b77-4e4f-a986-b3827bf241f5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GraphUser', response)

