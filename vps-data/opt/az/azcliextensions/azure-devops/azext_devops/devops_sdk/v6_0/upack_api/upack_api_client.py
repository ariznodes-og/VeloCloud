# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class UPackApiClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(UPackApiClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'd397749b-f115-4027-b6dd-77a65dd10d21'

    def delete_package_version_from_recycle_bin(self, feed_id, package_name, package_version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        self._send(http_method='DELETE',
                   location_id='3ba455ae-31e6-409e-849f-56c66888d004',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_package_version_metadata_from_recycle_bin(self, feed_id, package_name, package_version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='GET',
                              location_id='3ba455ae-31e6-409e-849f-56c66888d004',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('UPackPackageVersionDeletionState', response)

    def restore_package_version_from_recycle_bin(self, package_version_details, feed_id, package_name, package_version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'UPackRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='3ba455ae-31e6-409e-849f-56c66888d004',
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version(self, feed_id, package_name, package_version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='DELETE',
                              location_id='72f61ca4-e07c-4eca-be75-6c0b2f3f4051',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def get_package_version(self, feed_id, package_name, package_version, project=None, show_deleted=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        query_parameters = {}
        if show_deleted is not None:
            query_parameters['showDeleted'] = self._serialize.query('show_deleted', show_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='72f61ca4-e07c-4eca-be75-6c0b2f3f4051',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def update_package_version(self, package_version_details, feed_id, package_name, package_version, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'PackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='72f61ca4-e07c-4eca-be75-6c0b2f3f4051',
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content)

