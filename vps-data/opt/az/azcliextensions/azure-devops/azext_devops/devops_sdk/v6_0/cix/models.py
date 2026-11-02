# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigurationFile(Model):

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'is_base64_encoded': {'key': 'isBase64Encoded', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, content=None, is_base64_encoded=None, path=None):
        super(ConfigurationFile, self).__init__()
        self.content = content
        self.is_base64_encoded = is_base64_encoded
        self.path = path


class CreatedResources(Model):

    _attribute_map = {
        'resources': {'key': 'resources', 'type': '{object}'}
    }

    def __init__(self, resources=None):
        super(CreatedResources, self).__init__()
        self.resources = resources


class CreatePipelineConnectionInputs(Model):

    _attribute_map = {
        'project': {'key': 'project', 'type': 'TeamProject'},
        'provider_data': {'key': 'providerData', 'type': '{str}'},
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'redirect_url': {'key': 'redirectUrl', 'type': 'str'},
        'request_source': {'key': 'requestSource', 'type': 'str'}
    }

    def __init__(self, project=None, provider_data=None, provider_id=None, redirect_url=None, request_source=None):
        super(CreatePipelineConnectionInputs, self).__init__()
        self.project = project
        self.provider_data = provider_data
        self.provider_id = provider_id
        self.redirect_url = redirect_url
        self.request_source = request_source


class DetectedBuildFramework(Model):

    _attribute_map = {
        'build_targets': {'key': 'buildTargets', 'type': '[DetectedBuildTarget]'},
        'id': {'key': 'id', 'type': 'str'},
        'settings': {'key': 'settings', 'type': '{str}'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, build_targets=None, id=None, settings=None, version=None):
        super(DetectedBuildFramework, self).__init__()
        self.build_targets = build_targets
        self.id = id
        self.settings = settings
        self.version = version


class DetectedBuildTarget(Model):

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'settings': {'key': 'settings', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, path=None, settings=None, type=None):
        super(DetectedBuildTarget, self).__init__()
        self.path = path
        self.settings = settings
        self.type = type


class OperationReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None):
        super(OperationReference, self).__init__()
        self.id = id
        self.plugin_id = plugin_id
        self.status = status
        self.url = url


class OperationResultReference(Model):

    _attribute_map = {
        'result_url': {'key': 'resultUrl', 'type': 'str'}
    }

    def __init__(self, result_url=None):
        super(OperationResultReference, self).__init__()
        self.result_url = result_url


class PipelineConnection(Model):

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'redirect_url': {'key': 'redirectUrl', 'type': 'str'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'},
        'team_project_id': {'key': 'teamProjectId', 'type': 'str'}
    }

    def __init__(self, account_id=None, definition_id=None, redirect_url=None, service_endpoint_id=None, team_project_id=None):
        super(PipelineConnection, self).__init__()
        self.account_id = account_id
        self.definition_id = definition_id
        self.redirect_url = redirect_url
        self.service_endpoint_id = service_endpoint_id
        self.team_project_id = team_project_id


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ResourceCreationParameter(Model):

    _attribute_map = {
        'resource_to_create': {'key': 'resourceToCreate', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, resource_to_create=None, type=None):
        super(ResourceCreationParameter, self).__init__()
        self.resource_to_create = resource_to_create
        self.type = type


class TeamProjectReference(Model):

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.default_team_image_url = default_team_image_url
        self.description = description
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility


class Template(Model):

    _attribute_map = {
        'assets': {'key': 'assets', 'type': '[TemplateAsset]'},
        'category': {'key': 'category', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[TemplateDataSourceBinding]'},
        'description': {'key': 'description', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[TemplateParameterDefinition]'},
        'recommended_weight': {'key': 'recommendedWeight', 'type': 'int'}
    }

    def __init__(self, assets=None, category=None, content=None, data_source_bindings=None, description=None, icon_url=None, id=None, name=None, parameters=None, recommended_weight=None):
        super(Template, self).__init__()
        self.assets = assets
        self.category = category
        self.content = content
        self.data_source_bindings = data_source_bindings
        self.description = description
        self.icon_url = icon_url
        self.id = id
        self.name = name
        self.parameters = parameters
        self.recommended_weight = recommended_weight


class TemplateAsset(Model):

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'destination_path': {'key': 'destinationPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, content=None, description=None, destination_path=None, path=None, type=None):
        super(TemplateAsset, self).__init__()
        self.content = content
        self.description = description
        self.destination_path = destination_path
        self.path = path
        self.type = type


class TemplateDataSourceBinding(Model):

    _attribute_map = {
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_parameter_name': {'key': 'endpointParameterName', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, data_source_name=None, endpoint_parameter_name=None, parameters=None, result_template=None, target=None):
        super(TemplateDataSourceBinding, self).__init__()
        self.data_source_name = data_source_name
        self.endpoint_parameter_name = endpoint_parameter_name
        self.parameters = parameters
        self.result_template = result_template
        self.target = target


class TemplateParameterDefinition(Model):

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'possible_values': {'key': 'possibleValues', 'type': '[str]'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, default_value=None, display_name=None, name=None, possible_values=None, required=None, type=None):
        super(TemplateParameterDefinition, self).__init__()
        self.default_value = default_value
        self.display_name = display_name
        self.name = name
        self.possible_values = possible_values
        self.required = required
        self.type = type


class TemplateParameters(Model):

    _attribute_map = {
        'tokens': {'key': 'tokens', 'type': '{object}'}
    }

    def __init__(self, tokens=None):
        super(TemplateParameters, self).__init__()
        self.tokens = tokens


class WebApiTeamRef(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(WebApiTeamRef, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class Operation(OperationReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_message': {'key': 'detailedMessage', 'type': 'str'},
        'result_message': {'key': 'resultMessage', 'type': 'str'},
        'result_url': {'key': 'resultUrl', 'type': 'OperationResultReference'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, _links=None, detailed_message=None, result_message=None, result_url=None):
        super(Operation, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self._links = _links
        self.detailed_message = detailed_message
        self.result_message = result_message
        self.result_url = result_url


class TeamProject(TeamProjectReference):

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'capabilities': {'key': 'capabilities', 'type': '{{str}}'},
        'default_team': {'key': 'defaultTeam', 'type': 'WebApiTeamRef'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None, _links=None, capabilities=None, default_team=None):
        super(TeamProject, self).__init__(abbreviation=abbreviation, default_team_image_url=default_team_image_url, description=description, id=id, last_update_time=last_update_time, name=name, revision=revision, state=state, url=url, visibility=visibility)
        self._links = _links
        self.capabilities = capabilities
        self.default_team = default_team


__all__ = [
    'ConfigurationFile',
    'CreatedResources',
    'CreatePipelineConnectionInputs',
    'DetectedBuildFramework',
    'DetectedBuildTarget',
    'OperationReference',
    'OperationResultReference',
    'PipelineConnection',
    'ReferenceLinks',
    'ResourceCreationParameter',
    'TeamProjectReference',
    'Template',
    'TemplateAsset',
    'TemplateDataSourceBinding',
    'TemplateParameterDefinition',
    'TemplateParameters',
    'WebApiTeamRef',
    'Operation',
    'TeamProject',
]
