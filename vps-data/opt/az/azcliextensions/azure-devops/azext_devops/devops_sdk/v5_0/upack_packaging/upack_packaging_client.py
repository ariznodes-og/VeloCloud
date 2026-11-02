# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class UPackPackagingClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(UPackPackagingClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'd397749b-f115-4027-b6dd-77a65dd10d21'

    def add_package(self, metadata, feed_id, package_name, package_version):
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(metadata, 'UPackPackagePushMetadata')
        self._send(http_method='PUT',
                   location_id='4cdb2ced-0758-4651-8032-010f070dd7e5',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content)

    def get_package_metadata(self, feed_id, package_name, package_version, intent=None):
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        query_parameters = {}
        if intent is not None:
            query_parameters['intent'] = self._serialize.query('intent', intent, 'str')
        response = self._send(http_method='GET',
                              location_id='4cdb2ced-0758-4651-8032-010f070dd7e5',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('UPackPackageMetadata', response)

    def get_package_versions_metadata(self, feed_id, package_name):
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        response = self._send(http_method='GET',
                              location_id='4cdb2ced-0758-4651-8032-010f070dd7e5',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('UPackLimitedPackageMetadataListResponse', response)

