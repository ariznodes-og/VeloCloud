# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Activity(Model):

    _attribute_map = {
        'capacity_per_day': {'key': 'capacityPerDay', 'type': 'float'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, capacity_per_day=None, name=None):
        super(Activity, self).__init__()
        self.capacity_per_day = capacity_per_day
        self.name = name


class BacklogColumn(Model):

    _attribute_map = {
        'column_field_reference': {'key': 'columnFieldReference', 'type': 'WorkItemFieldReference'},
        'width': {'key': 'width', 'type': 'int'}
    }

    def __init__(self, column_field_reference=None, width=None):
        super(BacklogColumn, self).__init__()
        self.column_field_reference = column_field_reference
        self.width = width


class BacklogConfiguration(Model):

    _attribute_map = {
        'backlog_fields': {'key': 'backlogFields', 'type': 'BacklogFields'},
        'bugs_behavior': {'key': 'bugsBehavior', 'type': 'object'},
        'hidden_backlogs': {'key': 'hiddenBacklogs', 'type': '[str]'},
        'is_bugs_behavior_configured': {'key': 'isBugsBehaviorConfigured', 'type': 'bool'},
        'portfolio_backlogs': {'key': 'portfolioBacklogs', 'type': '[BacklogLevelConfiguration]'},
        'requirement_backlog': {'key': 'requirementBacklog', 'type': 'BacklogLevelConfiguration'},
        'task_backlog': {'key': 'taskBacklog', 'type': 'BacklogLevelConfiguration'},
        'url': {'key': 'url', 'type': 'str'},
        'work_item_type_mapped_states': {'key': 'workItemTypeMappedStates', 'type': '[WorkItemTypeStateInfo]'}
    }

    def __init__(self, backlog_fields=None, bugs_behavior=None, hidden_backlogs=None, is_bugs_behavior_configured=None, portfolio_backlogs=None, requirement_backlog=None, task_backlog=None, url=None, work_item_type_mapped_states=None):
        super(BacklogConfiguration, self).__init__()
        self.backlog_fields = backlog_fields
        self.bugs_behavior = bugs_behavior
        self.hidden_backlogs = hidden_backlogs
        self.is_bugs_behavior_configured = is_bugs_behavior_configured
        self.portfolio_backlogs = portfolio_backlogs
        self.requirement_backlog = requirement_backlog
        self.task_backlog = task_backlog
        self.url = url
        self.work_item_type_mapped_states = work_item_type_mapped_states


class BacklogFields(Model):

    _attribute_map = {
        'type_fields': {'key': 'typeFields', 'type': '{str}'}
    }

    def __init__(self, type_fields=None):
        super(BacklogFields, self).__init__()
        self.type_fields = type_fields


class BacklogLevel(Model):

    _attribute_map = {
        'category_reference_name': {'key': 'categoryReferenceName', 'type': 'str'},
        'plural_name': {'key': 'pluralName', 'type': 'str'},
        'work_item_states': {'key': 'workItemStates', 'type': '[str]'},
        'work_item_types': {'key': 'workItemTypes', 'type': '[str]'}
    }

    def __init__(self, category_reference_name=None, plural_name=None, work_item_states=None, work_item_types=None):
        super(BacklogLevel, self).__init__()
        self.category_reference_name = category_reference_name
        self.plural_name = plural_name
        self.work_item_states = work_item_states
        self.work_item_types = work_item_types


class BacklogLevelConfiguration(Model):

    _attribute_map = {
        'add_panel_fields': {'key': 'addPanelFields', 'type': '[WorkItemFieldReference]'},
        'color': {'key': 'color', 'type': 'str'},
        'column_fields': {'key': 'columnFields', 'type': '[BacklogColumn]'},
        'default_work_item_type': {'key': 'defaultWorkItemType', 'type': 'WorkItemTypeReference'},
        'id': {'key': 'id', 'type': 'str'},
        'is_hidden': {'key': 'isHidden', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'rank': {'key': 'rank', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'work_item_count_limit': {'key': 'workItemCountLimit', 'type': 'int'},
        'work_item_types': {'key': 'workItemTypes', 'type': '[WorkItemTypeReference]'}
    }

    def __init__(self, add_panel_fields=None, color=None, column_fields=None, default_work_item_type=None, id=None, is_hidden=None, name=None, rank=None, type=None, work_item_count_limit=None, work_item_types=None):
        super(BacklogLevelConfiguration, self).__init__()
        self.add_panel_fields = add_panel_fields
        self.color = color
        self.column_fields = column_fields
        self.default_work_item_type = default_work_item_type
        self.id = id
        self.is_hidden = is_hidden
        self.name = name
        self.rank = rank
        self.type = type
        self.work_item_count_limit = work_item_count_limit
        self.work_item_types = work_item_types


class BacklogLevelWorkItems(Model):

    _attribute_map = {
        'work_items': {'key': 'workItems', 'type': '[WorkItemLink]'}
    }

    def __init__(self, work_items=None):
        super(BacklogLevelWorkItems, self).__init__()
        self.work_items = work_items


class BoardBadge(Model):

    _attribute_map = {
        'board_id': {'key': 'boardId', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'}
    }

    def __init__(self, board_id=None, image_url=None):
        super(BoardBadge, self).__init__()
        self.board_id = board_id
        self.image_url = image_url


class BoardCardRuleSettings(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'rules': {'key': 'rules', 'type': '{[Rule]}'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, rules=None, url=None):
        super(BoardCardRuleSettings, self).__init__()
        self._links = _links
        self.rules = rules
        self.url = url


class BoardCardSettings(Model):

    _attribute_map = {
        'cards': {'key': 'cards', 'type': '{[FieldSetting]}'}
    }

    def __init__(self, cards=None):
        super(BoardCardSettings, self).__init__()
        self.cards = cards


class BoardChartReference(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, url=None):
        super(BoardChartReference, self).__init__()
        self.name = name
        self.url = url


class BoardColumn(Model):

    _attribute_map = {
        'column_type': {'key': 'columnType', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_split': {'key': 'isSplit', 'type': 'bool'},
        'item_limit': {'key': 'itemLimit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'state_mappings': {'key': 'stateMappings', 'type': '{str}'}
    }

    def __init__(self, column_type=None, description=None, id=None, is_split=None, item_limit=None, name=None, state_mappings=None):
        super(BoardColumn, self).__init__()
        self.column_type = column_type
        self.description = description
        self.id = id
        self.is_split = is_split
        self.item_limit = item_limit
        self.name = name
        self.state_mappings = state_mappings


class BoardFields(Model):

    _attribute_map = {
        'column_field': {'key': 'columnField', 'type': 'FieldReference'},
        'done_field': {'key': 'doneField', 'type': 'FieldReference'},
        'row_field': {'key': 'rowField', 'type': 'FieldReference'}
    }

    def __init__(self, column_field=None, done_field=None, row_field=None):
        super(BoardFields, self).__init__()
        self.column_field = column_field
        self.done_field = done_field
        self.row_field = row_field


class BoardReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(BoardReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class BoardRow(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(BoardRow, self).__init__()
        self.id = id
        self.name = name


class BoardSuggestedValue(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(BoardSuggestedValue, self).__init__()
        self.name = name


class BoardUserSettings(Model):

    _attribute_map = {
        'auto_refresh_state': {'key': 'autoRefreshState', 'type': 'bool'}
    }

    def __init__(self, auto_refresh_state=None):
        super(BoardUserSettings, self).__init__()
        self.auto_refresh_state = auto_refresh_state


class CapacityPatch(Model):

    _attribute_map = {
        'activities': {'key': 'activities', 'type': '[Activity]'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'}
    }

    def __init__(self, activities=None, days_off=None):
        super(CapacityPatch, self).__init__()
        self.activities = activities
        self.days_off = days_off


class CategoryConfiguration(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'work_item_types': {'key': 'workItemTypes', 'type': '[WorkItemTypeReference]'}
    }

    def __init__(self, name=None, reference_name=None, work_item_types=None):
        super(CategoryConfiguration, self).__init__()
        self.name = name
        self.reference_name = reference_name
        self.work_item_types = work_item_types


class CreatePlan(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, name=None, properties=None, type=None):
        super(CreatePlan, self).__init__()
        self.description = description
        self.name = name
        self.properties = properties
        self.type = type


class DateRange(Model):

    _attribute_map = {
        'end': {'key': 'end', 'type': 'iso-8601'},
        'start': {'key': 'start', 'type': 'iso-8601'}
    }

    def __init__(self, end=None, start=None):
        super(DateRange, self).__init__()
        self.end = end
        self.start = start


class FieldReference(Model):

    _attribute_map = {
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, reference_name=None, url=None):
        super(FieldReference, self).__init__()
        self.reference_name = reference_name
        self.url = url


class FilterClause(Model):

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'index': {'key': 'index', 'type': 'int'},
        'logical_operator': {'key': 'logicalOperator', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, field_name=None, index=None, logical_operator=None, operator=None, value=None):
        super(FilterClause, self).__init__()
        self.field_name = field_name
        self.index = index
        self.logical_operator = logical_operator
        self.operator = operator
        self.value = value


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


class ITaskboardColumnMapping(Model):

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, state=None, work_item_type=None):
        super(ITaskboardColumnMapping, self).__init__()
        self.state = state
        self.work_item_type = work_item_type


class Link(Model):

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'rel': {'key': 'rel', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, attributes=None, rel=None, url=None):
        super(Link, self).__init__()
        self.attributes = attributes
        self.rel = rel
        self.url = url


class Member(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, image_url=None, unique_name=None, url=None):
        super(Member, self).__init__()
        self.display_name = display_name
        self.id = id
        self.image_url = image_url
        self.unique_name = unique_name
        self.url = url


class ParentChildWIMap(Model):

    _attribute_map = {
        'child_work_item_ids': {'key': 'childWorkItemIds', 'type': '[int]'},
        'id': {'key': 'id', 'type': 'int'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, child_work_item_ids=None, id=None, title=None):
        super(ParentChildWIMap, self).__init__()
        self.child_work_item_ids = child_work_item_ids
        self.id = id
        self.title = title


class Plan(Model):

    _attribute_map = {
        'created_by_identity': {'key': 'createdByIdentity', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'modified_by_identity': {'key': 'modifiedByIdentity', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'user_permissions': {'key': 'userPermissions', 'type': 'object'}
    }

    def __init__(self, created_by_identity=None, created_date=None, description=None, id=None, modified_by_identity=None, modified_date=None, name=None, properties=None, revision=None, type=None, url=None, user_permissions=None):
        super(Plan, self).__init__()
        self.created_by_identity = created_by_identity
        self.created_date = created_date
        self.description = description
        self.id = id
        self.modified_by_identity = modified_by_identity
        self.modified_date = modified_date
        self.name = name
        self.properties = properties
        self.revision = revision
        self.type = type
        self.url = url
        self.user_permissions = user_permissions


class PlanViewData(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, id=None, revision=None):
        super(PlanViewData, self).__init__()
        self.id = id
        self.revision = revision


class PredefinedQuery(Model):

    _attribute_map = {
        'has_more': {'key': 'hasMore', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'results': {'key': 'results', 'type': '[WorkItem]'},
        'url': {'key': 'url', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'}
    }

    def __init__(self, has_more=None, id=None, name=None, results=None, url=None, web_url=None):
        super(PredefinedQuery, self).__init__()
        self.has_more = has_more
        self.id = id
        self.name = name
        self.results = results
        self.url = url
        self.web_url = web_url


class ProcessConfiguration(Model):

    _attribute_map = {
        'bug_work_items': {'key': 'bugWorkItems', 'type': 'CategoryConfiguration'},
        'portfolio_backlogs': {'key': 'portfolioBacklogs', 'type': '[CategoryConfiguration]'},
        'requirement_backlog': {'key': 'requirementBacklog', 'type': 'CategoryConfiguration'},
        'task_backlog': {'key': 'taskBacklog', 'type': 'CategoryConfiguration'},
        'type_fields': {'key': 'typeFields', 'type': '{WorkItemFieldReference}'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, bug_work_items=None, portfolio_backlogs=None, requirement_backlog=None, task_backlog=None, type_fields=None, url=None):
        super(ProcessConfiguration, self).__init__()
        self.bug_work_items = bug_work_items
        self.portfolio_backlogs = portfolio_backlogs
        self.requirement_backlog = requirement_backlog
        self.task_backlog = task_backlog
        self.type_fields = type_fields
        self.url = url


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ReorderOperation(Model):

    _attribute_map = {
        'ids': {'key': 'ids', 'type': '[int]'},
        'iteration_path': {'key': 'iterationPath', 'type': 'str'},
        'next_id': {'key': 'nextId', 'type': 'int'},
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'previous_id': {'key': 'previousId', 'type': 'int'}
    }

    def __init__(self, ids=None, iteration_path=None, next_id=None, parent_id=None, previous_id=None):
        super(ReorderOperation, self).__init__()
        self.ids = ids
        self.iteration_path = iteration_path
        self.next_id = next_id
        self.parent_id = parent_id
        self.previous_id = previous_id


class ReorderResult(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'order': {'key': 'order', 'type': 'float'}
    }

    def __init__(self, id=None, order=None):
        super(ReorderResult, self).__init__()
        self.id = id
        self.order = order


class Rule(Model):

    _attribute_map = {
        'clauses': {'key': 'clauses', 'type': '[FilterClause]'},
        'filter': {'key': 'filter', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'settings': {'key': 'settings', 'type': '{str}'}
    }

    def __init__(self, clauses=None, filter=None, is_enabled=None, name=None, settings=None):
        super(Rule, self).__init__()
        self.clauses = clauses
        self.filter = filter
        self.is_enabled = is_enabled
        self.name = name
        self.settings = settings


class TaskboardColumn(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'mappings': {'key': 'mappings', 'type': '[ITaskboardColumnMapping]'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'}
    }

    def __init__(self, id=None, mappings=None, name=None, order=None):
        super(TaskboardColumn, self).__init__()
        self.id = id
        self.mappings = mappings
        self.name = name
        self.order = order


class TaskboardColumnMapping(Model):

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, state=None, work_item_type=None):
        super(TaskboardColumnMapping, self).__init__()
        self.state = state
        self.work_item_type = work_item_type


class TaskboardColumns(Model):

    _attribute_map = {
        'columns': {'key': 'columns', 'type': '[TaskboardColumn]'},
        'is_customized': {'key': 'isCustomized', 'type': 'bool'},
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'validation_messsage': {'key': 'validationMesssage', 'type': 'str'}
    }

    def __init__(self, columns=None, is_customized=None, is_valid=None, validation_messsage=None):
        super(TaskboardColumns, self).__init__()
        self.columns = columns
        self.is_customized = is_customized
        self.is_valid = is_valid
        self.validation_messsage = validation_messsage


class TaskboardWorkItemColumn(Model):

    _attribute_map = {
        'column': {'key': 'column', 'type': 'str'},
        'column_id': {'key': 'columnId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'work_item_id': {'key': 'workItemId', 'type': 'int'}
    }

    def __init__(self, column=None, column_id=None, state=None, work_item_id=None):
        super(TaskboardWorkItemColumn, self).__init__()
        self.column = column
        self.column_id = column_id
        self.state = state
        self.work_item_id = work_item_id


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


class TeamFieldValue(Model):

    _attribute_map = {
        'include_children': {'key': 'includeChildren', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, include_children=None, value=None):
        super(TeamFieldValue, self).__init__()
        self.include_children = include_children
        self.value = value


class TeamFieldValuesPatch(Model):

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'values': {'key': 'values', 'type': '[TeamFieldValue]'}
    }

    def __init__(self, default_value=None, values=None):
        super(TeamFieldValuesPatch, self).__init__()
        self.default_value = default_value
        self.values = values


class TeamIterationAttributes(Model):

    _attribute_map = {
        'finish_date': {'key': 'finishDate', 'type': 'iso-8601'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'time_frame': {'key': 'timeFrame', 'type': 'object'}
    }

    def __init__(self, finish_date=None, start_date=None, time_frame=None):
        super(TeamIterationAttributes, self).__init__()
        self.finish_date = finish_date
        self.start_date = start_date
        self.time_frame = time_frame


class TeamSettingsDataContractBase(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, url=None):
        super(TeamSettingsDataContractBase, self).__init__()
        self._links = _links
        self.url = url


class TeamSettingsDaysOff(TeamSettingsDataContractBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'}
    }

    def __init__(self, _links=None, url=None, days_off=None):
        super(TeamSettingsDaysOff, self).__init__(_links=_links, url=url)
        self.days_off = days_off


class TeamSettingsDaysOffPatch(Model):

    _attribute_map = {
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'}
    }

    def __init__(self, days_off=None):
        super(TeamSettingsDaysOffPatch, self).__init__()
        self.days_off = days_off


class TeamSettingsIteration(TeamSettingsDataContractBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'TeamIterationAttributes'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, _links=None, url=None, attributes=None, id=None, name=None, path=None):
        super(TeamSettingsIteration, self).__init__(_links=_links, url=url)
        self.attributes = attributes
        self.id = id
        self.name = name
        self.path = path


class TeamSettingsPatch(Model):

    _attribute_map = {
        'backlog_iteration': {'key': 'backlogIteration', 'type': 'str'},
        'backlog_visibilities': {'key': 'backlogVisibilities', 'type': '{bool}'},
        'bugs_behavior': {'key': 'bugsBehavior', 'type': 'object'},
        'default_iteration': {'key': 'defaultIteration', 'type': 'str'},
        'default_iteration_macro': {'key': 'defaultIterationMacro', 'type': 'str'},
        'working_days': {'key': 'workingDays', 'type': '[object]'}
    }

    def __init__(self, backlog_iteration=None, backlog_visibilities=None, bugs_behavior=None, default_iteration=None, default_iteration_macro=None, working_days=None):
        super(TeamSettingsPatch, self).__init__()
        self.backlog_iteration = backlog_iteration
        self.backlog_visibilities = backlog_visibilities
        self.bugs_behavior = bugs_behavior
        self.default_iteration = default_iteration
        self.default_iteration_macro = default_iteration_macro
        self.working_days = working_days


class TimelineCriteriaStatus(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, message=None, type=None):
        super(TimelineCriteriaStatus, self).__init__()
        self.message = message
        self.type = type


class TimelineIterationStatus(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, message=None, type=None):
        super(TimelineIterationStatus, self).__init__()
        self.message = message
        self.type = type


class TimelineTeamData(Model):

    _attribute_map = {
        'backlog': {'key': 'backlog', 'type': 'BacklogLevel'},
        'field_reference_names': {'key': 'fieldReferenceNames', 'type': '[str]'},
        'id': {'key': 'id', 'type': 'str'},
        'is_expanded': {'key': 'isExpanded', 'type': 'bool'},
        'iterations': {'key': 'iterations', 'type': '[TimelineTeamIteration]'},
        'name': {'key': 'name', 'type': 'str'},
        'order_by_field': {'key': 'orderByField', 'type': 'str'},
        'partially_paged_field_reference_names': {'key': 'partiallyPagedFieldReferenceNames', 'type': '[str]'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'TimelineTeamStatus'},
        'team_field_default_value': {'key': 'teamFieldDefaultValue', 'type': 'str'},
        'team_field_name': {'key': 'teamFieldName', 'type': 'str'},
        'team_field_values': {'key': 'teamFieldValues', 'type': '[TeamFieldValue]'},
        'work_item_type_colors': {'key': 'workItemTypeColors', 'type': '[WorkItemColor]'}
    }

    def __init__(self, backlog=None, field_reference_names=None, id=None, is_expanded=None, iterations=None, name=None, order_by_field=None, partially_paged_field_reference_names=None, project_id=None, status=None, team_field_default_value=None, team_field_name=None, team_field_values=None, work_item_type_colors=None):
        super(TimelineTeamData, self).__init__()
        self.backlog = backlog
        self.field_reference_names = field_reference_names
        self.id = id
        self.is_expanded = is_expanded
        self.iterations = iterations
        self.name = name
        self.order_by_field = order_by_field
        self.partially_paged_field_reference_names = partially_paged_field_reference_names
        self.project_id = project_id
        self.status = status
        self.team_field_default_value = team_field_default_value
        self.team_field_name = team_field_name
        self.team_field_values = team_field_values
        self.work_item_type_colors = work_item_type_colors


class TimelineTeamIteration(Model):

    _attribute_map = {
        'css_node_id': {'key': 'cssNodeId', 'type': 'str'},
        'finish_date': {'key': 'finishDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'partially_paged_work_items': {'key': 'partiallyPagedWorkItems', 'type': '[[object]]'},
        'path': {'key': 'path', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'TimelineIterationStatus'},
        'work_items': {'key': 'workItems', 'type': '[[object]]'}
    }

    def __init__(self, css_node_id=None, finish_date=None, name=None, partially_paged_work_items=None, path=None, start_date=None, status=None, work_items=None):
        super(TimelineTeamIteration, self).__init__()
        self.css_node_id = css_node_id
        self.finish_date = finish_date
        self.name = name
        self.partially_paged_work_items = partially_paged_work_items
        self.path = path
        self.start_date = start_date
        self.status = status
        self.work_items = work_items


class TimelineTeamStatus(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, message=None, type=None):
        super(TimelineTeamStatus, self).__init__()
        self.message = message
        self.type = type


class UpdatePlan(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, name=None, properties=None, revision=None, type=None):
        super(UpdatePlan, self).__init__()
        self.description = description
        self.name = name
        self.properties = properties
        self.revision = revision
        self.type = type


class UpdateTaskboardColumn(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'mappings': {'key': 'mappings', 'type': '[TaskboardColumnMapping]'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'}
    }

    def __init__(self, id=None, mappings=None, name=None, order=None):
        super(UpdateTaskboardColumn, self).__init__()
        self.id = id
        self.mappings = mappings
        self.name = name
        self.order = order


class UpdateTaskboardWorkItemColumn(Model):

    _attribute_map = {
        'new_column': {'key': 'newColumn', 'type': 'str'}
    }

    def __init__(self, new_column=None):
        super(UpdateTaskboardWorkItemColumn, self).__init__()
        self.new_column = new_column


class WorkItemColor(Model):

    _attribute_map = {
        'icon': {'key': 'icon', 'type': 'str'},
        'primary_color': {'key': 'primaryColor', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, icon=None, primary_color=None, work_item_type_name=None):
        super(WorkItemColor, self).__init__()
        self.icon = icon
        self.primary_color = primary_color
        self.work_item_type_name = work_item_type_name


class WorkItemFieldReference(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None, url=None):
        super(WorkItemFieldReference, self).__init__()
        self.name = name
        self.reference_name = reference_name
        self.url = url


class WorkItemLink(Model):

    _attribute_map = {
        'rel': {'key': 'rel', 'type': 'str'},
        'source': {'key': 'source', 'type': 'WorkItemReference'},
        'target': {'key': 'target', 'type': 'WorkItemReference'}
    }

    def __init__(self, rel=None, source=None, target=None):
        super(WorkItemLink, self).__init__()
        self.rel = rel
        self.source = source
        self.target = target


class WorkItemReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WorkItemReference, self).__init__()
        self.id = id
        self.url = url


class WorkItemRelation(Link):

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'rel': {'key': 'rel', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, attributes=None, rel=None, url=None):
        super(WorkItemRelation, self).__init__(attributes=attributes, rel=rel, url=url)


class WorkItemTrackingResourceReference(Model):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, url=None):
        super(WorkItemTrackingResourceReference, self).__init__()
        self.url = url


class WorkItemTypeReference(WorkItemTrackingResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, url=None, name=None):
        super(WorkItemTypeReference, self).__init__(url=url)
        self.name = name


class WorkItemTypeStateInfo(Model):

    _attribute_map = {
        'states': {'key': 'states', 'type': '{str}'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, states=None, work_item_type_name=None):
        super(WorkItemTypeStateInfo, self).__init__()
        self.states = states
        self.work_item_type_name = work_item_type_name


class Board(BoardReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allowed_mappings': {'key': 'allowedMappings', 'type': '{{[str]}}'},
        'can_edit': {'key': 'canEdit', 'type': 'bool'},
        'columns': {'key': 'columns', 'type': '[BoardColumn]'},
        'fields': {'key': 'fields', 'type': 'BoardFields'},
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'revision': {'key': 'revision', 'type': 'int'},
        'rows': {'key': 'rows', 'type': '[BoardRow]'}
    }

    def __init__(self, id=None, name=None, url=None, _links=None, allowed_mappings=None, can_edit=None, columns=None, fields=None, is_valid=None, revision=None, rows=None):
        super(Board, self).__init__(id=id, name=name, url=url)
        self._links = _links
        self.allowed_mappings = allowed_mappings
        self.can_edit = can_edit
        self.columns = columns
        self.fields = fields
        self.is_valid = is_valid
        self.revision = revision
        self.rows = rows


class BoardChart(BoardChartReference):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'settings': {'key': 'settings', 'type': '{object}'}
    }

    def __init__(self, name=None, url=None, _links=None, settings=None):
        super(BoardChart, self).__init__(name=name, url=url)
        self._links = _links
        self.settings = settings


class CapacityContractBase(TeamSettingsDataContractBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'activities': {'key': 'activities', 'type': '[Activity]'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'}
    }

    def __init__(self, _links=None, url=None, activities=None, days_off=None):
        super(CapacityContractBase, self).__init__(_links=_links, url=url)
        self.activities = activities
        self.days_off = days_off


class DeliveryViewData(PlanViewData):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'child_id_to_parent_id_map': {'key': 'childIdToParentIdMap', 'type': '{int}'},
        'criteria_status': {'key': 'criteriaStatus', 'type': 'TimelineCriteriaStatus'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'max_expanded_teams': {'key': 'maxExpandedTeams', 'type': 'int'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'teams': {'key': 'teams', 'type': '[TimelineTeamData]'}
    }

    def __init__(self, id=None, revision=None, child_id_to_parent_id_map=None, criteria_status=None, end_date=None, max_expanded_teams=None, start_date=None, teams=None):
        super(DeliveryViewData, self).__init__(id=id, revision=revision)
        self.child_id_to_parent_id_map = child_id_to_parent_id_map
        self.criteria_status = criteria_status
        self.end_date = end_date
        self.max_expanded_teams = max_expanded_teams
        self.start_date = start_date
        self.teams = teams


class IterationWorkItems(TeamSettingsDataContractBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'work_item_relations': {'key': 'workItemRelations', 'type': '[WorkItemLink]'}
    }

    def __init__(self, _links=None, url=None, work_item_relations=None):
        super(IterationWorkItems, self).__init__(_links=_links, url=url)
        self.work_item_relations = work_item_relations


class TeamFieldValues(TeamSettingsDataContractBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'field': {'key': 'field', 'type': 'FieldReference'},
        'values': {'key': 'values', 'type': '[TeamFieldValue]'}
    }

    def __init__(self, _links=None, url=None, default_value=None, field=None, values=None):
        super(TeamFieldValues, self).__init__(_links=_links, url=url)
        self.default_value = default_value
        self.field = field
        self.values = values


class TeamMemberCapacity(CapacityContractBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'activities': {'key': 'activities', 'type': '[Activity]'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'},
        'team_member': {'key': 'teamMember', 'type': 'Member'}
    }

    def __init__(self, _links=None, url=None, activities=None, days_off=None, team_member=None):
        super(TeamMemberCapacity, self).__init__(_links=_links, url=url, activities=activities, days_off=days_off)
        self.team_member = team_member


class TeamMemberCapacityIdentityRef(CapacityContractBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'activities': {'key': 'activities', 'type': '[Activity]'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'},
        'team_member': {'key': 'teamMember', 'type': 'IdentityRef'}
    }

    def __init__(self, _links=None, url=None, activities=None, days_off=None, team_member=None):
        super(TeamMemberCapacityIdentityRef, self).__init__(_links=_links, url=url, activities=activities, days_off=days_off)
        self.team_member = team_member


class TeamSetting(TeamSettingsDataContractBase):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'backlog_iteration': {'key': 'backlogIteration', 'type': 'TeamSettingsIteration'},
        'backlog_visibilities': {'key': 'backlogVisibilities', 'type': '{bool}'},
        'bugs_behavior': {'key': 'bugsBehavior', 'type': 'object'},
        'default_iteration': {'key': 'defaultIteration', 'type': 'TeamSettingsIteration'},
        'default_iteration_macro': {'key': 'defaultIterationMacro', 'type': 'str'},
        'working_days': {'key': 'workingDays', 'type': '[object]'}
    }

    def __init__(self, _links=None, url=None, backlog_iteration=None, backlog_visibilities=None, bugs_behavior=None, default_iteration=None, default_iteration_macro=None, working_days=None):
        super(TeamSetting, self).__init__(_links=_links, url=url)
        self.backlog_iteration = backlog_iteration
        self.backlog_visibilities = backlog_visibilities
        self.bugs_behavior = bugs_behavior
        self.default_iteration = default_iteration
        self.default_iteration_macro = default_iteration_macro
        self.working_days = working_days


class WorkItemCommentVersionRef(WorkItemTrackingResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'created_in_revision': {'key': 'createdInRevision', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, url=None, comment_id=None, created_in_revision=None, is_deleted=None, text=None, version=None):
        super(WorkItemCommentVersionRef, self).__init__(url=url)
        self.comment_id = comment_id
        self.created_in_revision = created_in_revision
        self.is_deleted = is_deleted
        self.text = text
        self.version = version


class WorkItemTrackingResource(WorkItemTrackingResourceReference):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'}
    }

    def __init__(self, url=None, _links=None):
        super(WorkItemTrackingResource, self).__init__(url=url)
        self._links = _links


class WorkItem(WorkItemTrackingResource):

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_version_ref': {'key': 'commentVersionRef', 'type': 'WorkItemCommentVersionRef'},
        'fields': {'key': 'fields', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'relations': {'key': 'relations', 'type': '[WorkItemRelation]'},
        'rev': {'key': 'rev', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comment_version_ref=None, fields=None, id=None, relations=None, rev=None):
        super(WorkItem, self).__init__(url=url, _links=_links)
        self.comment_version_ref = comment_version_ref
        self.fields = fields
        self.id = id
        self.relations = relations
        self.rev = rev


__all__ = [
    'Activity',
    'BacklogColumn',
    'BacklogConfiguration',
    'BacklogFields',
    'BacklogLevel',
    'BacklogLevelConfiguration',
    'BacklogLevelWorkItems',
    'BoardBadge',
    'BoardCardRuleSettings',
    'BoardCardSettings',
    'BoardChartReference',
    'BoardColumn',
    'BoardFields',
    'BoardReference',
    'BoardRow',
    'BoardSuggestedValue',
    'BoardUserSettings',
    'CapacityPatch',
    'CategoryConfiguration',
    'CreatePlan',
    'DateRange',
    'FieldReference',
    'FilterClause',
    'GraphSubjectBase',
    'IdentityRef',
    'ITaskboardColumnMapping',
    'Link',
    'Member',
    'ParentChildWIMap',
    'Plan',
    'PlanViewData',
    'PredefinedQuery',
    'ProcessConfiguration',
    'ReferenceLinks',
    'ReorderOperation',
    'ReorderResult',
    'Rule',
    'TaskboardColumn',
    'TaskboardColumnMapping',
    'TaskboardColumns',
    'TaskboardWorkItemColumn',
    'TeamContext',
    'TeamFieldValue',
    'TeamFieldValuesPatch',
    'TeamIterationAttributes',
    'TeamSettingsDataContractBase',
    'TeamSettingsDaysOff',
    'TeamSettingsDaysOffPatch',
    'TeamSettingsIteration',
    'TeamSettingsPatch',
    'TimelineCriteriaStatus',
    'TimelineIterationStatus',
    'TimelineTeamData',
    'TimelineTeamIteration',
    'TimelineTeamStatus',
    'UpdatePlan',
    'UpdateTaskboardColumn',
    'UpdateTaskboardWorkItemColumn',
    'WorkItemColor',
    'WorkItemFieldReference',
    'WorkItemLink',
    'WorkItemReference',
    'WorkItemRelation',
    'WorkItemTrackingResourceReference',
    'WorkItemTypeReference',
    'WorkItemTypeStateInfo',
    'Board',
    'BoardChart',
    'CapacityContractBase',
    'DeliveryViewData',
    'IterationWorkItems',
    'TeamFieldValues',
    'TeamMemberCapacity',
    'TeamMemberCapacityIdentityRef',
    'TeamSetting',
    'WorkItemCommentVersionRef',
    'WorkItemTrackingResource',
    'WorkItem',
]
