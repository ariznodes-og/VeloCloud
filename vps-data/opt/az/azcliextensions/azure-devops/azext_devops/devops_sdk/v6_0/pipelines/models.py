# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Artifact(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, signed_content=None, url=None):
        super(Artifact, self).__init__()
        self.name = name
        self.signed_content = signed_content
        self.url = url


class BuildResourceParameters(Model):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(BuildResourceParameters, self).__init__()
        self.version = version


class ContainerResourceParameters(Model):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(ContainerResourceParameters, self).__init__()
        self.version = version


class CreatePipelineConfigurationParameters(Model):

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(CreatePipelineConfigurationParameters, self).__init__()
        self.type = type


class CreatePipelineParameters(Model):

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'CreatePipelineConfigurationParameters'},
        'folder': {'key': 'folder', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, configuration=None, folder=None, name=None):
        super(CreatePipelineParameters, self).__init__()
        self.configuration = configuration
        self.folder = folder
        self.name = name


class Log(Model):

    _attribute_map = {
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'line_count': {'key': 'lineCount', 'type': 'long'},
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, created_on=None, id=None, last_changed_on=None, line_count=None, signed_content=None, url=None):
        super(Log, self).__init__()
        self.created_on = created_on
        self.id = id
        self.last_changed_on = last_changed_on
        self.line_count = line_count
        self.signed_content = signed_content
        self.url = url


class LogCollection(Model):

    _attribute_map = {
        'logs': {'key': 'logs', 'type': '[Log]'},
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, logs=None, signed_content=None, url=None):
        super(LogCollection, self).__init__()
        self.logs = logs
        self.signed_content = signed_content
        self.url = url


class PackageResourceParameters(Model):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(PackageResourceParameters, self).__init__()
        self.version = version


class PipelineBase(Model):

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None):
        super(PipelineBase, self).__init__()
        self.folder = folder
        self.id = id
        self.name = name
        self.revision = revision


class PipelineConfiguration(Model):

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(PipelineConfiguration, self).__init__()
        self.type = type


class PipelineReference(PipelineBase):

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None, url=None):
        super(PipelineReference, self).__init__(folder=folder, id=id, name=name, revision=revision)
        self.url = url


class PipelineResourceParameters(Model):

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(PipelineResourceParameters, self).__init__()
        self.version = version


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class Repository(Model):

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(Repository, self).__init__()
        self.type = type


class RepositoryResource(Model):

    _attribute_map = {
        'ref_name': {'key': 'refName', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'Repository'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, ref_name=None, repository=None, version=None):
        super(RepositoryResource, self).__init__()
        self.ref_name = ref_name
        self.repository = repository
        self.version = version


class RepositoryResourceParameters(Model):

    _attribute_map = {
        'ref_name': {'key': 'refName', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'token_type': {'key': 'tokenType', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, ref_name=None, token=None, token_type=None, version=None):
        super(RepositoryResourceParameters, self).__init__()
        self.ref_name = ref_name
        self.token = token
        self.token_type = token_type
        self.version = version


class RunPipelineParameters(Model):

    _attribute_map = {
        'preview_run': {'key': 'previewRun', 'type': 'bool'},
        'resources': {'key': 'resources', 'type': 'RunResourcesParameters'},
        'stages_to_skip': {'key': 'stagesToSkip', 'type': '[str]'},
        'template_parameters': {'key': 'templateParameters', 'type': '{str}'},
        'variables': {'key': 'variables', 'type': '{Variable}'},
        'yaml_override': {'key': 'yamlOverride', 'type': 'str'}
    }

    def __init__(self, preview_run=None, resources=None, stages_to_skip=None, template_parameters=None, variables=None, yaml_override=None):
        super(RunPipelineParameters, self).__init__()
        self.preview_run = preview_run
        self.resources = resources
        self.stages_to_skip = stages_to_skip
        self.template_parameters = template_parameters
        self.variables = variables
        self.yaml_override = yaml_override


class RunReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(RunReference, self).__init__()
        self.id = id
        self.name = name


class RunResources(Model):

    _attribute_map = {
        'repositories': {'key': 'repositories', 'type': '{RepositoryResource}'}
    }

    def __init__(self, repositories=None):
        super(RunResources, self).__init__()
        self.repositories = repositories


class RunResourcesParameters(Model):

    _attribute_map = {
        'builds': {'key': 'builds', 'type': '{BuildResourceParameters}'},
        'containers': {'key': 'containers', 'type': '{ContainerResourceParameters}'},
        'packages': {'key': 'packages', 'type': '{PackageResourceParameters}'},
        'pipelines': {'key': 'pipelines', 'type': '{PipelineResourceParameters}'},
        'repositories': {'key': 'repositories', 'type': '{RepositoryResourceParameters}'}
    }

    def __init__(self, builds=None, containers=None, packages=None, pipelines=None, repositories=None):
        super(RunResourcesParameters, self).__init__()
        self.builds = builds
        self.containers = containers
        self.packages = packages
        self.pipelines = pipelines
        self.repositories = repositories


class SignalRConnection(Model):

    _attribute_map = {
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'}
    }

    def __init__(self, signed_content=None):
        super(SignalRConnection, self).__init__()
        self.signed_content = signed_content


class SignedUrl(Model):

    _attribute_map = {
        'signature_expires': {'key': 'signatureExpires', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, signature_expires=None, url=None):
        super(SignedUrl, self).__init__()
        self.signature_expires = signature_expires
        self.url = url


class Variable(Model):

    _attribute_map = {
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_secret=None, value=None):
        super(Variable, self).__init__()
        self.is_secret = is_secret
        self.value = value


class Pipeline(PipelineBase):

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'configuration': {'key': 'configuration', 'type': 'PipelineConfiguration'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None, _links=None, configuration=None, url=None):
        super(Pipeline, self).__init__(folder=folder, id=id, name=name, revision=revision)
        self._links = _links
        self.configuration = configuration
        self.url = url


class Run(RunReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'final_yaml': {'key': 'finalYaml', 'type': 'str'},
        'finished_date': {'key': 'finishedDate', 'type': 'iso-8601'},
        'pipeline': {'key': 'pipeline', 'type': 'PipelineReference'},
        'resources': {'key': 'resources', 'type': 'RunResources'},
        'result': {'key': 'result', 'type': 'object'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{Variable}'}
    }

    def __init__(self, id=None, name=None, _links=None, created_date=None, final_yaml=None, finished_date=None, pipeline=None, resources=None, result=None, state=None, url=None, variables=None):
        super(Run, self).__init__(id=id, name=name)
        self._links = _links
        self.created_date = created_date
        self.final_yaml = final_yaml
        self.finished_date = finished_date
        self.pipeline = pipeline
        self.resources = resources
        self.result = result
        self.state = state
        self.url = url
        self.variables = variables


__all__ = [
    'Artifact',
    'BuildResourceParameters',
    'ContainerResourceParameters',
    'CreatePipelineConfigurationParameters',
    'CreatePipelineParameters',
    'Log',
    'LogCollection',
    'PackageResourceParameters',
    'PipelineBase',
    'PipelineConfiguration',
    'PipelineReference',
    'PipelineResourceParameters',
    'ReferenceLinks',
    'Repository',
    'RepositoryResource',
    'RepositoryResourceParameters',
    'RunPipelineParameters',
    'RunReference',
    'RunResources',
    'RunResourcesParameters',
    'SignalRConnection',
    'SignedUrl',
    'Variable',
    'Pipeline',
    'Run',
]
