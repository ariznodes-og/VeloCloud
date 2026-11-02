# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class FileContainer(Model):

    _attribute_map = {
        'artifact_uri': {'key': 'artifactUri', 'type': 'str'},
        'content_location': {'key': 'contentLocation', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'long'},
        'item_location': {'key': 'itemLocation', 'type': 'str'},
        'locator_path': {'key': 'locatorPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': 'object'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'security_token': {'key': 'securityToken', 'type': 'str'},
        'signing_key_id': {'key': 'signingKeyId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'}
    }

    def __init__(self, artifact_uri=None, content_location=None, created_by=None, date_created=None, description=None, id=None, item_location=None, locator_path=None, name=None, options=None, scope_identifier=None, security_token=None, signing_key_id=None, size=None):
        super(FileContainer, self).__init__()
        self.artifact_uri = artifact_uri
        self.content_location = content_location
        self.created_by = created_by
        self.date_created = date_created
        self.description = description
        self.id = id
        self.item_location = item_location
        self.locator_path = locator_path
        self.name = name
        self.options = options
        self.scope_identifier = scope_identifier
        self.security_token = security_token
        self.signing_key_id = signing_key_id
        self.size = size


class FileContainerItem(Model):

    _attribute_map = {
        'container_id': {'key': 'containerId', 'type': 'long'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'content_location': {'key': 'contentLocation', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'date_last_modified': {'key': 'dateLastModified', 'type': 'iso-8601'},
        'file_encoding': {'key': 'fileEncoding', 'type': 'int'},
        'file_hash': {'key': 'fileHash', 'type': 'str'},
        'file_id': {'key': 'fileId', 'type': 'int'},
        'file_length': {'key': 'fileLength', 'type': 'long'},
        'file_type': {'key': 'fileType', 'type': 'int'},
        'item_location': {'key': 'itemLocation', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'object'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'ticket': {'key': 'ticket', 'type': 'str'}
    }

    def __init__(self, container_id=None, content_id=None, content_location=None, created_by=None, date_created=None, date_last_modified=None, file_encoding=None, file_hash=None, file_id=None, file_length=None, file_type=None, item_location=None, item_type=None, last_modified_by=None, path=None, scope_identifier=None, status=None, ticket=None):
        super(FileContainerItem, self).__init__()
        self.container_id = container_id
        self.content_id = content_id
        self.content_location = content_location
        self.created_by = created_by
        self.date_created = date_created
        self.date_last_modified = date_last_modified
        self.file_encoding = file_encoding
        self.file_hash = file_hash
        self.file_id = file_id
        self.file_length = file_length
        self.file_type = file_type
        self.item_location = item_location
        self.item_type = item_type
        self.last_modified_by = last_modified_by
        self.path = path
        self.scope_identifier = scope_identifier
        self.status = status
        self.ticket = ticket


__all__ = [
    'FileContainer',
    'FileContainerItem',
]
