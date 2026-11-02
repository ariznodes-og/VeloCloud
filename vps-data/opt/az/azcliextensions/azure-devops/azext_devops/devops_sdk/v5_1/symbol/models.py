# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class DebugEntryCreateBatch(Model):

    _attribute_map = {
        'create_behavior': {'key': 'createBehavior', 'type': 'object'},
        'debug_entries': {'key': 'debugEntries', 'type': '[DebugEntry]'}
    }

    def __init__(self, create_behavior=None, debug_entries=None):
        super(DebugEntryCreateBatch, self).__init__()
        self.create_behavior = create_behavior
        self.debug_entries = debug_entries


class JsonBlobBlockHash(Model):

    _attribute_map = {
        'hash_bytes': {'key': 'hashBytes', 'type': 'str'}
    }

    def __init__(self, hash_bytes=None):
        super(JsonBlobBlockHash, self).__init__()
        self.hash_bytes = hash_bytes


class JsonBlobIdentifier(Model):

    _attribute_map = {
        'identifier_value': {'key': 'identifierValue', 'type': 'str'}
    }

    def __init__(self, identifier_value=None):
        super(JsonBlobIdentifier, self).__init__()
        self.identifier_value = identifier_value


class JsonBlobIdentifierWithBlocks(Model):

    _attribute_map = {
        'block_hashes': {'key': 'blockHashes', 'type': '[JsonBlobBlockHash]'},
        'identifier_value': {'key': 'identifierValue', 'type': 'str'}
    }

    def __init__(self, block_hashes=None, identifier_value=None):
        super(JsonBlobIdentifierWithBlocks, self).__init__()
        self.block_hashes = block_hashes
        self.identifier_value = identifier_value


class ResourceBase(Model):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'storage_eTag': {'key': 'storageETag', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_date=None, id=None, storage_eTag=None, url=None):
        super(ResourceBase, self).__init__()
        self.created_by = created_by
        self.created_date = created_date
        self.id = id
        self.storage_eTag = storage_eTag
        self.url = url


class DebugEntry(ResourceBase):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'storage_eTag': {'key': 'storageETag', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'blob_details': {'key': 'blobDetails', 'type': 'JsonBlobIdentifierWithBlocks'},
        'blob_identifier': {'key': 'blobIdentifier', 'type': 'JsonBlobIdentifier'},
        'blob_uri': {'key': 'blobUri', 'type': 'str'},
        'client_key': {'key': 'clientKey', 'type': 'str'},
        'information_level': {'key': 'informationLevel', 'type': 'object'},
        'request_id': {'key': 'requestId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, created_by=None, created_date=None, id=None, storage_eTag=None, url=None, blob_details=None, blob_identifier=None, blob_uri=None, client_key=None, information_level=None, request_id=None, status=None):
        super(DebugEntry, self).__init__(created_by=created_by, created_date=created_date, id=id, storage_eTag=storage_eTag, url=url)
        self.blob_details = blob_details
        self.blob_identifier = blob_identifier
        self.blob_uri = blob_uri
        self.client_key = client_key
        self.information_level = information_level
        self.request_id = request_id
        self.status = status


class Request(ResourceBase):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'storage_eTag': {'key': 'storageETag', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'expiration_date': {'key': 'expirationDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, created_by=None, created_date=None, id=None, storage_eTag=None, url=None, description=None, expiration_date=None, name=None, status=None):
        super(Request, self).__init__(created_by=created_by, created_date=created_date, id=id, storage_eTag=storage_eTag, url=url)
        self.description = description
        self.expiration_date = expiration_date
        self.name = name
        self.status = status


__all__ = [
    'DebugEntryCreateBatch',
    'JsonBlobBlockHash',
    'JsonBlobIdentifier',
    'JsonBlobIdentifierWithBlocks',
    'ResourceBase',
    'DebugEntry',
    'Request',
]
