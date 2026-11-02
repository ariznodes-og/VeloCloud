# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GraphSubjectBase(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class IdentityRef(GraphSubjectBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


class PolicyConfigurationRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, type=None, url=None):
        super(PolicyConfigurationRef, self).__init__()
        self.id = id
        self.type = type
        self.url = url


class PolicyEvaluationRecord(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'configuration': {'key': 'configuration', 'type': 'PolicyConfiguration'},
        'context': {'key': 'context', 'type': 'object'},
        'evaluation_id': {'key': 'evaluationId', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, _links=None, artifact_id=None, completed_date=None, configuration=None, context=None, evaluation_id=None, started_date=None, status=None):
        super(PolicyEvaluationRecord, self).__init__()
        self._links = _links
        self.artifact_id = artifact_id
        self.completed_date = completed_date
        self.configuration = configuration
        self.context = context
        self.evaluation_id = evaluation_id
        self.started_date = started_date
        self.status = status


class PolicyTypeRef(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, url=None):
        super(PolicyTypeRef, self).__init__()
        self.display_name = display_name
        self.id = id
        self.url = url


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class VersionedPolicyConfigurationRef(PolicyConfigurationRef):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, id=None, type=None, url=None, revision=None):
        super(VersionedPolicyConfigurationRef, self).__init__(id=id, type=type, url=url)
        self.revision = revision


class PolicyConfiguration(VersionedPolicyConfigurationRef):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'is_blocking': {'key': 'isBlocking', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_enterprise_managed': {'key': 'isEnterpriseManaged', 'type': 'bool'},
        'settings': {'key': 'settings', 'type': 'object'}
    }

    def __init__(self, id=None, type=None, url=None, revision=None, _links=None, created_by=None, created_date=None, is_blocking=None, is_deleted=None, is_enabled=None, is_enterprise_managed=None, settings=None):
        super(PolicyConfiguration, self).__init__(id=id, type=type, url=url, revision=revision)
        self._links = _links
        self.created_by = created_by
        self.created_date = created_date
        self.is_blocking = is_blocking
        self.is_deleted = is_deleted
        self.is_enabled = is_enabled
        self.is_enterprise_managed = is_enterprise_managed
        self.settings = settings


class PolicyType(PolicyTypeRef):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, url=None, _links=None, description=None):
        super(PolicyType, self).__init__(display_name=display_name, id=id, url=url)
        self._links = _links
        self.description = description


__all__ = [
    'GraphSubjectBase',
    'IdentityRef',
    'PolicyConfigurationRef',
    'PolicyEvaluationRecord',
    'PolicyTypeRef',
    'ReferenceLinks',
    'VersionedPolicyConfigurationRef',
    'PolicyConfiguration',
    'PolicyType',
]
