# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class UPackLimitedPackageMetadata(Model):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(UPackLimitedPackageMetadata, self).__init__()
        self.version = version


class UPackLimitedPackageMetadataListResponse(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'value': {'key': 'value', 'type': '[UPackLimitedPackageMetadata]'}
    }

    def __init__(self, count=None, value=None):
        super(UPackLimitedPackageMetadataListResponse, self).__init__()
        self.count = count
        self.value = value


class UPackPackageMetadata(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'super_root_id': {'key': 'superRootId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, description=None, manifest_id=None, super_root_id=None, version=None):
        super(UPackPackageMetadata, self).__init__()
        self.description = description
        self.manifest_id = manifest_id
        self.super_root_id = super_root_id
        self.version = version


class UPackPackagePushMetadata(UPackPackageMetadata):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'super_root_id': {'key': 'superRootId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'proof_nodes': {'key': 'proofNodes', 'type': '[str]'}
    }

    def __init__(self, description=None, manifest_id=None, super_root_id=None, version=None, proof_nodes=None):
        super(UPackPackagePushMetadata, self).__init__(description=description, manifest_id=manifest_id, super_root_id=super_root_id, version=version)
        self.proof_nodes = proof_nodes


class UPackPackageVersionDeletionState(Model):

    _attribute_map = {
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, deleted_date=None, name=None, version=None):
        super(UPackPackageVersionDeletionState, self).__init__()
        self.deleted_date = deleted_date
        self.name = name
        self.version = version


__all__ = [
    'UPackLimitedPackageMetadata',
    'UPackLimitedPackageMetadataListResponse',
    'UPackPackageMetadata',
    'UPackPackagePushMetadata',
    'UPackPackageVersionDeletionState',
]
