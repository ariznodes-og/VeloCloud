# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class MavenClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(MavenClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '6f7f8c07-ff36-473c-bcf3-bd6cc9b6c066'

    def download_package(self, feed_id, group_id, artifact_id, version, file_name, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if file_name is not None:
            route_values['fileName'] = self._serialize.url('file_name', file_name, 'str')
        response = self._send(http_method='GET',
                              location_id='c338d4b5-d30a-47e2-95b7-f157ef558833',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('object', response)

    def delete_package_version_from_recycle_bin(self, feed, group_id, artifact_id, version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        self._send(http_method='DELETE',
                   location_id='f67e10eb-1254-4953-add7-d49b83a16c9f',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_package_version_metadata_from_recycle_bin(self, feed, group_id, artifact_id, version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='f67e10eb-1254-4953-add7-d49b83a16c9f',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('MavenPackageVersionDeletionState', response)

    def restore_package_version_from_recycle_bin(self, package_version_details, feed, group_id, artifact_id, version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        content = self._serialize.body(package_version_details, 'MavenRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='f67e10eb-1254-4953-add7-d49b83a16c9f',
                   version='5.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_package_version(self, feed, group_id, artifact_id, version, project=None, show_deleted=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        query_parameters = {}
        if show_deleted is not None:
            query_parameters['showDeleted'] = self._serialize.query('show_deleted', show_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='180ed967-377a-4112-986b-607adb14ded4',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def package_delete(self, feed, group_id, artifact_id, version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        self._send(http_method='DELETE',
                   location_id='180ed967-377a-4112-986b-607adb14ded4',
                   version='5.1-preview.1',
                   route_values=route_values)

