# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Dashboard(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'}
    }

    def __init__(self, _links=None, description=None, eTag=None, id=None, name=None, owner_id=None, position=None, refresh_interval=None, url=None, widgets=None):
        super(Dashboard, self).__init__()
        self._links = _links
        self.description = description
        self.eTag = eTag
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.position = position
        self.refresh_interval = refresh_interval
        self.url = url
        self.widgets = widgets


class DashboardGroup(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dashboard_entries': {'key': 'dashboardEntries', 'type': '[DashboardGroupEntry]'},
        'permission': {'key': 'permission', 'type': 'object'},
        'team_dashboard_permission': {'key': 'teamDashboardPermission', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, dashboard_entries=None, permission=None, team_dashboard_permission=None, url=None):
        super(DashboardGroup, self).__init__()
        self._links = _links
        self.dashboard_entries = dashboard_entries
        self.permission = permission
        self.team_dashboard_permission = team_dashboard_permission
        self.url = url


class DashboardGroupEntry(Dashboard):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links=None, description=None, eTag=None, id=None, name=None, owner_id=None, position=None, refresh_interval=None, url=None, widgets=None):
        super(DashboardGroupEntry, self).__init__(_links=_links, description=description, eTag=eTag, id=id, name=name, owner_id=owner_id, position=position, refresh_interval=refresh_interval, url=url, widgets=widgets)


class DashboardGroupEntryResponse(DashboardGroupEntry):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links=None, description=None, eTag=None, id=None, name=None, owner_id=None, position=None, refresh_interval=None, url=None, widgets=None):
        super(DashboardGroupEntryResponse, self).__init__(_links=_links, description=description, eTag=eTag, id=id, name=name, owner_id=owner_id, position=position, refresh_interval=refresh_interval, url=url, widgets=widgets)


class DashboardResponse(DashboardGroupEntry):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links=None, description=None, eTag=None, id=None, name=None, owner_id=None, position=None, refresh_interval=None, url=None, widgets=None):
        super(DashboardResponse, self).__init__(_links=_links, description=description, eTag=eTag, id=id, name=name, owner_id=owner_id, position=position, refresh_interval=refresh_interval, url=url, widgets=widgets)


class LightboxOptions(Model):

    _attribute_map = {
        'height': {'key': 'height', 'type': 'int'},
        'resizable': {'key': 'resizable', 'type': 'bool'},
        'width': {'key': 'width', 'type': 'int'}
    }

    def __init__(self, height=None, resizable=None, width=None):
        super(LightboxOptions, self).__init__()
        self.height = height
        self.resizable = resizable
        self.width = width


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class SemanticVersion(Model):

    _attribute_map = {
        'major': {'key': 'major', 'type': 'int'},
        'minor': {'key': 'minor', 'type': 'int'},
        'patch': {'key': 'patch', 'type': 'int'}
    }

    def __init__(self, major=None, minor=None, patch=None):
        super(SemanticVersion, self).__init__()
        self.major = major
        self.minor = minor
        self.patch = patch


class TeamContext(Model):

    _attribute_map = {
        'project': {'key': 'project', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'team': {'key': 'team', 'type': 'str'},
        'team_id': {'key': 'teamId', 'type': 'str'}
    }

    def __init__(self, project=None, project_id=None, team=None, team_id=None):
        super(TeamContext, self).__init__()
        self.project = project
        self.project_id = project_id
        self.team = team
        self.team_id = team_id


class Widget(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'are_settings_blocked_for_user': {'key': 'areSettingsBlockedForUser', 'type': 'bool'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'dashboard': {'key': 'dashboard', 'type': 'Dashboard'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'position': {'key': 'position', 'type': 'WidgetPosition'},
        'settings': {'key': 'settings', 'type': 'str'},
        'settings_version': {'key': 'settingsVersion', 'type': 'SemanticVersion'},
        'size': {'key': 'size', 'type': 'WidgetSize'},
        'type_id': {'key': 'typeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, allowed_sizes=None, are_settings_blocked_for_user=None, artifact_id=None, configuration_contribution_id=None, configuration_contribution_relative_id=None, content_uri=None, contribution_id=None, dashboard=None, eTag=None, id=None, is_enabled=None, is_name_configurable=None, lightbox_options=None, loading_image_url=None, name=None, position=None, settings=None, settings_version=None, size=None, type_id=None, url=None):
        super(Widget, self).__init__()
        self._links = _links
        self.allowed_sizes = allowed_sizes
        self.are_settings_blocked_for_user = are_settings_blocked_for_user
        self.artifact_id = artifact_id
        self.configuration_contribution_id = configuration_contribution_id
        self.configuration_contribution_relative_id = configuration_contribution_relative_id
        self.content_uri = content_uri
        self.contribution_id = contribution_id
        self.dashboard = dashboard
        self.eTag = eTag
        self.id = id
        self.is_enabled = is_enabled
        self.is_name_configurable = is_name_configurable
        self.lightbox_options = lightbox_options
        self.loading_image_url = loading_image_url
        self.name = name
        self.position = position
        self.settings = settings
        self.settings_version = settings_version
        self.size = size
        self.type_id = type_id
        self.url = url


class WidgetMetadata(Model):

    _attribute_map = {
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'analytics_service_required': {'key': 'analyticsServiceRequired', 'type': 'bool'},
        'catalog_icon_url': {'key': 'catalogIconUrl', 'type': 'str'},
        'catalog_info_url': {'key': 'catalogInfoUrl', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'configuration_required': {'key': 'configurationRequired', 'type': 'bool'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'default_settings': {'key': 'defaultSettings', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'is_visible_from_catalog': {'key': 'isVisibleFromCatalog', 'type': 'bool'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[object]'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'type_id': {'key': 'typeId', 'type': 'str'}
    }

    def __init__(self, allowed_sizes=None, analytics_service_required=None, catalog_icon_url=None, catalog_info_url=None, configuration_contribution_id=None, configuration_contribution_relative_id=None, configuration_required=None, content_uri=None, contribution_id=None, default_settings=None, description=None, is_enabled=None, is_name_configurable=None, is_visible_from_catalog=None, lightbox_options=None, loading_image_url=None, name=None, publisher_name=None, supported_scopes=None, targets=None, type_id=None):
        super(WidgetMetadata, self).__init__()
        self.allowed_sizes = allowed_sizes
        self.analytics_service_required = analytics_service_required
        self.catalog_icon_url = catalog_icon_url
        self.catalog_info_url = catalog_info_url
        self.configuration_contribution_id = configuration_contribution_id
        self.configuration_contribution_relative_id = configuration_contribution_relative_id
        self.configuration_required = configuration_required
        self.content_uri = content_uri
        self.contribution_id = contribution_id
        self.default_settings = default_settings
        self.description = description
        self.is_enabled = is_enabled
        self.is_name_configurable = is_name_configurable
        self.is_visible_from_catalog = is_visible_from_catalog
        self.lightbox_options = lightbox_options
        self.loading_image_url = loading_image_url
        self.name = name
        self.publisher_name = publisher_name
        self.supported_scopes = supported_scopes
        self.targets = targets
        self.type_id = type_id


class WidgetMetadataResponse(Model):

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'widget_metadata': {'key': 'widgetMetadata', 'type': 'WidgetMetadata'}
    }

    def __init__(self, uri=None, widget_metadata=None):
        super(WidgetMetadataResponse, self).__init__()
        self.uri = uri
        self.widget_metadata = widget_metadata


class WidgetPosition(Model):

    _attribute_map = {
        'column': {'key': 'column', 'type': 'int'},
        'row': {'key': 'row', 'type': 'int'}
    }

    def __init__(self, column=None, row=None):
        super(WidgetPosition, self).__init__()
        self.column = column
        self.row = row


class WidgetResponse(Widget):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'are_settings_blocked_for_user': {'key': 'areSettingsBlockedForUser', 'type': 'bool'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'dashboard': {'key': 'dashboard', 'type': 'Dashboard'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'position': {'key': 'position', 'type': 'WidgetPosition'},
        'settings': {'key': 'settings', 'type': 'str'},
        'settings_version': {'key': 'settingsVersion', 'type': 'SemanticVersion'},
        'size': {'key': 'size', 'type': 'WidgetSize'},
        'type_id': {'key': 'typeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, _links=None, allowed_sizes=None, are_settings_blocked_for_user=None, artifact_id=None, configuration_contribution_id=None, configuration_contribution_relative_id=None, content_uri=None, contribution_id=None, dashboard=None, eTag=None, id=None, is_enabled=None, is_name_configurable=None, lightbox_options=None, loading_image_url=None, name=None, position=None, settings=None, settings_version=None, size=None, type_id=None, url=None):
        super(WidgetResponse, self).__init__(_links=_links, allowed_sizes=allowed_sizes, are_settings_blocked_for_user=are_settings_blocked_for_user, artifact_id=artifact_id, configuration_contribution_id=configuration_contribution_id, configuration_contribution_relative_id=configuration_contribution_relative_id, content_uri=content_uri, contribution_id=contribution_id, dashboard=dashboard, eTag=eTag, id=id, is_enabled=is_enabled, is_name_configurable=is_name_configurable, lightbox_options=lightbox_options, loading_image_url=loading_image_url, name=name, position=position, settings=settings, settings_version=settings_version, size=size, type_id=type_id, url=url)


class WidgetSize(Model):

    _attribute_map = {
        'column_span': {'key': 'columnSpan', 'type': 'int'},
        'row_span': {'key': 'rowSpan', 'type': 'int'}
    }

    def __init__(self, column_span=None, row_span=None):
        super(WidgetSize, self).__init__()
        self.column_span = column_span
        self.row_span = row_span


class WidgetsVersionedList(Model):

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'}
    }

    def __init__(self, eTag=None, widgets=None):
        super(WidgetsVersionedList, self).__init__()
        self.eTag = eTag
        self.widgets = widgets


class WidgetTypesResponse(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'uri': {'key': 'uri', 'type': 'str'},
        'widget_types': {'key': 'widgetTypes', 'type': '[WidgetMetadata]'}
    }

    def __init__(self, _links=None, uri=None, widget_types=None):
        super(WidgetTypesResponse, self).__init__()
        self._links = _links
        self.uri = uri
        self.widget_types = widget_types


__all__ = [
    'Dashboard',
    'DashboardGroup',
    'DashboardGroupEntry',
    'DashboardGroupEntryResponse',
    'DashboardResponse',
    'LightboxOptions',
    'ReferenceLinks',
    'SemanticVersion',
    'TeamContext',
    'Widget',
    'WidgetMetadata',
    'WidgetMetadataResponse',
    'WidgetPosition',
    'WidgetResponse',
    'WidgetSize',
    'WidgetsVersionedList',
    'WidgetTypesResponse',
]
