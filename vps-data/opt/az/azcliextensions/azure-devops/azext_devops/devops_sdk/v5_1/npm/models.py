# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BatchOperationData(Model):

    _attribute_map = {
    }

    def __init__(self):
        super(BatchOperationData, self).__init__()


class JsonPatchOperation(Model):

    _attribute_map = {
        'from_': {'key': 'from', 'type': 'str'},
        'op': {'key': 'op', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, from_=None, op=None, path=None, value=None):
        super(JsonPatchOperation, self).__init__()
        self.from_ = from_
        self.op = op
        self.path = path
        self.value = value


class MinimalPackageDetails(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, version=None):
        super(MinimalPackageDetails, self).__init__()
        self.id = id
        self.version = version


class NpmPackagesBatchRequest(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': 'BatchOperationData'},
        'operation': {'key': 'operation', 'type': 'object'},
        'packages': {'key': 'packages', 'type': '[MinimalPackageDetails]'}
    }

    def __init__(self, data=None, operation=None, packages=None):
        super(NpmPackagesBatchRequest, self).__init__()
        self.data = data
        self.operation = operation
        self.packages = packages


class NpmPackageVersionDeletionState(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'unpublished_date': {'key': 'unpublishedDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, name=None, unpublished_date=None, version=None):
        super(NpmPackageVersionDeletionState, self).__init__()
        self.name = name
        self.unpublished_date = unpublished_date
        self.version = version


class NpmRecycleBinPackageVersionDetails(Model):

    _attribute_map = {
        'deleted': {'key': 'deleted', 'type': 'bool'}
    }

    def __init__(self, deleted=None):
        super(NpmRecycleBinPackageVersionDetails, self).__init__()
        self.deleted = deleted


class Package(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'deprecate_message': {'key': 'deprecateMessage', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'permanently_deleted_date': {'key': 'permanentlyDeletedDate', 'type': 'iso-8601'},
        'source_chain': {'key': 'sourceChain', 'type': '[UpstreamSourceInfo]'},
        'unpublished_date': {'key': 'unpublishedDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, _links=None, deprecate_message=None, id=None, name=None, permanently_deleted_date=None, source_chain=None, unpublished_date=None, version=None):
        super(Package, self).__init__()
        self._links = _links
        self.deprecate_message = deprecate_message
        self.id = id
        self.name = name
        self.permanently_deleted_date = permanently_deleted_date
        self.source_chain = source_chain
        self.unpublished_date = unpublished_date
        self.version = version


class PackageVersionDetails(Model):

    _attribute_map = {
        'deprecate_message': {'key': 'deprecateMessage', 'type': 'str'},
        'views': {'key': 'views', 'type': 'JsonPatchOperation'}
    }

    def __init__(self, deprecate_message=None, views=None):
        super(PackageVersionDetails, self).__init__()
        self.deprecate_message = deprecate_message
        self.views = views


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class UpstreamSourceInfo(Model):

    _attribute_map = {
        'display_location': {'key': 'displayLocation', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'source_type': {'key': 'sourceType', 'type': 'object'}
    }

    def __init__(self, display_location=None, id=None, location=None, name=None, source_type=None):
        super(UpstreamSourceInfo, self).__init__()
        self.display_location = display_location
        self.id = id
        self.location = location
        self.name = name
        self.source_type = source_type


class BatchDeprecateData(BatchOperationData):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, message=None):
        super(BatchDeprecateData, self).__init__()
        self.message = message


__all__ = [
    'BatchOperationData',
    'JsonPatchOperation',
    'MinimalPackageDetails',
    'NpmPackagesBatchRequest',
    'NpmPackageVersionDeletionState',
    'NpmRecycleBinPackageVersionDetails',
    'Package',
    'PackageVersionDetails',
    'ReferenceLinks',
    'UpstreamSourceInfo',
    'BatchDeprecateData',
]
