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


class Package(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'permanently_deleted_date': {'key': 'permanentlyDeletedDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, _links=None, deleted_date=None, id=None, name=None, permanently_deleted_date=None, version=None):
        super(Package, self).__init__()
        self._links = _links
        self.deleted_date = deleted_date
        self.id = id
        self.name = name
        self.permanently_deleted_date = permanently_deleted_date
        self.version = version


class PackageVersionDetails(Model):

    _attribute_map = {
        'views': {'key': 'views', 'type': 'JsonPatchOperation'}
    }

    def __init__(self, views=None):
        super(PackageVersionDetails, self).__init__()
        self.views = views


class PyPiPackagesBatchRequest(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': 'BatchOperationData'},
        'operation': {'key': 'operation', 'type': 'object'},
        'packages': {'key': 'packages', 'type': '[MinimalPackageDetails]'}
    }

    def __init__(self, data=None, operation=None, packages=None):
        super(PyPiPackagesBatchRequest, self).__init__()
        self.data = data
        self.operation = operation
        self.packages = packages


class PyPiPackageVersionDeletionState(Model):

    _attribute_map = {
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, deleted_date=None, name=None, version=None):
        super(PyPiPackageVersionDeletionState, self).__init__()
        self.deleted_date = deleted_date
        self.name = name
        self.version = version


class PyPiRecycleBinPackageVersionDetails(Model):

    _attribute_map = {
        'deleted': {'key': 'deleted', 'type': 'bool'}
    }

    def __init__(self, deleted=None):
        super(PyPiRecycleBinPackageVersionDetails, self).__init__()
        self.deleted = deleted


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


__all__ = [
    'BatchOperationData',
    'JsonPatchOperation',
    'MinimalPackageDetails',
    'Package',
    'PackageVersionDetails',
    'PyPiPackagesBatchRequest',
    'PyPiPackageVersionDeletionState',
    'PyPiRecycleBinPackageVersionDetails',
    'ReferenceLinks',
]
