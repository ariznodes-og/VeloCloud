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


class NuGetPackagesBatchRequest(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': 'BatchOperationData'},
        'operation': {'key': 'operation', 'type': 'object'},
        'packages': {'key': 'packages', 'type': '[MinimalPackageDetails]'}
    }

    def __init__(self, data=None, operation=None, packages=None):
        super(NuGetPackagesBatchRequest, self).__init__()
        self.data = data
        self.operation = operation
        self.packages = packages


class NuGetPackageVersionDeletionState(Model):

    _attribute_map = {
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, deleted_date=None, name=None, version=None):
        super(NuGetPackageVersionDeletionState, self).__init__()
        self.deleted_date = deleted_date
        self.name = name
        self.version = version


class NuGetRecycleBinPackageVersionDetails(Model):

    _attribute_map = {
        'deleted': {'key': 'deleted', 'type': 'bool'}
    }

    def __init__(self, deleted=None):
        super(NuGetRecycleBinPackageVersionDetails, self).__init__()
        self.deleted = deleted


class Package(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'permanently_deleted_date': {'key': 'permanentlyDeletedDate', 'type': 'iso-8601'},
        'source_chain': {'key': 'sourceChain', 'type': '[UpstreamSourceInfo]'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, _links=None, deleted_date=None, id=None, name=None, permanently_deleted_date=None, source_chain=None, version=None):
        super(Package, self).__init__()
        self._links = _links
        self.deleted_date = deleted_date
        self.id = id
        self.name = name
        self.permanently_deleted_date = permanently_deleted_date
        self.source_chain = source_chain
        self.version = version


class PackageVersionDetails(Model):

    _attribute_map = {
        'listed': {'key': 'listed', 'type': 'bool'},
        'views': {'key': 'views', 'type': 'JsonPatchOperation'}
    }

    def __init__(self, listed=None, views=None):
        super(PackageVersionDetails, self).__init__()
        self.listed = listed
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
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'source_type': {'key': 'sourceType', 'type': 'object'}
    }

    def __init__(self, id=None, location=None, name=None, source_type=None):
        super(UpstreamSourceInfo, self).__init__()
        self.id = id
        self.location = location
        self.name = name
        self.source_type = source_type


class BatchListData(BatchOperationData):

    _attribute_map = {
        'listed': {'key': 'listed', 'type': 'bool'}
    }

    def __init__(self, listed=None):
        super(BatchListData, self).__init__()
        self.listed = listed


__all__ = [
    'BatchOperationData',
    'JsonPatchOperation',
    'MinimalPackageDetails',
    'NuGetPackagesBatchRequest',
    'NuGetPackageVersionDeletionState',
    'NuGetRecycleBinPackageVersionDetails',
    'Package',
    'PackageVersionDetails',
    'ReferenceLinks',
    'UpstreamSourceInfo',
    'BatchListData',
]
