# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Issue(Model):

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'data': {'key': 'data', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, category=None, data=None, message=None, type=None):
        super(Issue, self).__init__()
        self.category = category
        self.data = data
        self.message = message
        self.type = type


class JobOption(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, data=None, id=None):
        super(JobOption, self).__init__()
        self.data = data
        self.id = id


class MaskHint(Model):

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, type=None, value=None):
        super(MaskHint, self).__init__()
        self.type = type
        self.value = value


class PlanEnvironment(Model):

    _attribute_map = {
        'mask': {'key': 'mask', 'type': '[MaskHint]'},
        'options': {'key': 'options', 'type': '{JobOption}'},
        'variables': {'key': 'variables', 'type': '{str}'}
    }

    def __init__(self, mask=None, options=None, variables=None):
        super(PlanEnvironment, self).__init__()
        self.mask = mask
        self.options = options
        self.variables = variables


class ProjectReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class TaskAgentJob(Model):

    _attribute_map = {
        'container': {'key': 'container', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'sidecar_containers': {'key': 'sidecarContainers', 'type': '{str}'},
        'steps': {'key': 'steps', 'type': '[TaskAgentJobStep]'},
        'variables': {'key': 'variables', 'type': '[TaskAgentJobVariable]'}
    }

    def __init__(self, container=None, id=None, name=None, sidecar_containers=None, steps=None, variables=None):
        super(TaskAgentJob, self).__init__()
        self.container = container
        self.id = id
        self.name = name
        self.sidecar_containers = sidecar_containers
        self.steps = steps
        self.variables = variables


class TaskAgentJobStep(Model):

    _attribute_map = {
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'env': {'key': 'env', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'task': {'key': 'task', 'type': 'TaskAgentJobTask'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, condition=None, continue_on_error=None, enabled=None, env=None, id=None, inputs=None, name=None, task=None, timeout_in_minutes=None, type=None):
        super(TaskAgentJobStep, self).__init__()
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.enabled = enabled
        self.env = env
        self.id = id
        self.inputs = inputs
        self.name = name
        self.task = task
        self.timeout_in_minutes = timeout_in_minutes
        self.type = type


class TaskAgentJobTask(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, version=None):
        super(TaskAgentJobTask, self).__init__()
        self.id = id
        self.name = name
        self.version = version


class TaskAgentJobVariable(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, secret=None, value=None):
        super(TaskAgentJobVariable, self).__init__()
        self.name = name
        self.secret = secret
        self.value = value


class TaskAttachment(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'str'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'record_id': {'key': 'recordId', 'type': 'str'},
        'timeline_id': {'key': 'timelineId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, _links=None, created_on=None, last_changed_by=None, last_changed_on=None, name=None, record_id=None, timeline_id=None, type=None):
        super(TaskAttachment, self).__init__()
        self._links = _links
        self.created_on = created_on
        self.last_changed_by = last_changed_by
        self.last_changed_on = last_changed_on
        self.name = name
        self.record_id = record_id
        self.timeline_id = timeline_id
        self.type = type


class TaskLogReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'location': {'key': 'location', 'type': 'str'}
    }

    def __init__(self, id=None, location=None):
        super(TaskLogReference, self).__init__()
        self.id = id
        self.location = location


class TaskOrchestrationItem(Model):

    _attribute_map = {
        'item_type': {'key': 'itemType', 'type': 'object'}
    }

    def __init__(self, item_type=None):
        super(TaskOrchestrationItem, self).__init__()
        self.item_type = item_type


class TaskOrchestrationOwner(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None):
        super(TaskOrchestrationOwner, self).__init__()
        self._links = _links
        self.id = id
        self.name = name


class TaskOrchestrationPlanGroupsQueueMetrics(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, count=None, status=None):
        super(TaskOrchestrationPlanGroupsQueueMetrics, self).__init__()
        self.count = count
        self.status = status


class TaskOrchestrationPlanReference(Model):

    _attribute_map = {
        'artifact_location': {'key': 'artifactLocation', 'type': 'str'},
        'artifact_uri': {'key': 'artifactUri', 'type': 'str'},
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, artifact_location=None, artifact_uri=None, definition=None, owner=None, plan_group=None, plan_id=None, plan_type=None, scope_identifier=None, version=None):
        super(TaskOrchestrationPlanReference, self).__init__()
        self.artifact_location = artifact_location
        self.artifact_uri = artifact_uri
        self.definition = definition
        self.owner = owner
        self.plan_group = plan_group
        self.plan_id = plan_id
        self.plan_type = plan_type
        self.scope_identifier = scope_identifier
        self.version = version


class TaskOrchestrationQueuedPlan(Model):

    _attribute_map = {
        'assign_time': {'key': 'assignTime', 'type': 'iso-8601'},
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'pool_id': {'key': 'poolId', 'type': 'int'},
        'queue_position': {'key': 'queuePosition', 'type': 'int'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'}
    }

    def __init__(self, assign_time=None, definition=None, owner=None, plan_group=None, plan_id=None, pool_id=None, queue_position=None, queue_time=None, scope_identifier=None):
        super(TaskOrchestrationQueuedPlan, self).__init__()
        self.assign_time = assign_time
        self.definition = definition
        self.owner = owner
        self.plan_group = plan_group
        self.plan_id = plan_id
        self.pool_id = pool_id
        self.queue_position = queue_position
        self.queue_time = queue_time
        self.scope_identifier = scope_identifier


class TaskOrchestrationQueuedPlanGroup(Model):

    _attribute_map = {
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plans': {'key': 'plans', 'type': '[TaskOrchestrationQueuedPlan]'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'queue_position': {'key': 'queuePosition', 'type': 'int'}
    }

    def __init__(self, definition=None, owner=None, plan_group=None, plans=None, project=None, queue_position=None):
        super(TaskOrchestrationQueuedPlanGroup, self).__init__()
        self.definition = definition
        self.owner = owner
        self.plan_group = plan_group
        self.plans = plans
        self.project = project
        self.queue_position = queue_position


class TaskReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, inputs=None, name=None, version=None):
        super(TaskReference, self).__init__()
        self.id = id
        self.inputs = inputs
        self.name = name
        self.version = version


class TimelineAttempt(Model):

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'record_id': {'key': 'recordId', 'type': 'str'},
        'timeline_id': {'key': 'timelineId', 'type': 'str'}
    }

    def __init__(self, attempt=None, identifier=None, record_id=None, timeline_id=None):
        super(TimelineAttempt, self).__init__()
        self.attempt = attempt
        self.identifier = identifier
        self.record_id = record_id
        self.timeline_id = timeline_id


class TimelineRecord(Model):

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'change_id': {'key': 'changeId', 'type': 'int'},
        'current_operation': {'key': 'currentOperation', 'type': 'str'},
        'details': {'key': 'details', 'type': 'TimelineReference'},
        'error_count': {'key': 'errorCount', 'type': 'int'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'location': {'key': 'location', 'type': 'str'},
        'log': {'key': 'log', 'type': 'TaskLogReference'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'previous_attempts': {'key': 'previousAttempts', 'type': '[TimelineAttempt]'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'object'},
        'task': {'key': 'task', 'type': 'TaskReference'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'},
        'warning_count': {'key': 'warningCount', 'type': 'int'},
        'worker_name': {'key': 'workerName', 'type': 'str'}
    }

    def __init__(self, attempt=None, change_id=None, current_operation=None, details=None, error_count=None, finish_time=None, id=None, identifier=None, issues=None, last_modified=None, location=None, log=None, name=None, order=None, parent_id=None, percent_complete=None, previous_attempts=None, ref_name=None, result=None, result_code=None, start_time=None, state=None, task=None, type=None, variables=None, warning_count=None, worker_name=None):
        super(TimelineRecord, self).__init__()
        self.attempt = attempt
        self.change_id = change_id
        self.current_operation = current_operation
        self.details = details
        self.error_count = error_count
        self.finish_time = finish_time
        self.id = id
        self.identifier = identifier
        self.issues = issues
        self.last_modified = last_modified
        self.location = location
        self.log = log
        self.name = name
        self.order = order
        self.parent_id = parent_id
        self.percent_complete = percent_complete
        self.previous_attempts = previous_attempts
        self.ref_name = ref_name
        self.result = result
        self.result_code = result_code
        self.start_time = start_time
        self.state = state
        self.task = task
        self.type = type
        self.variables = variables
        self.warning_count = warning_count
        self.worker_name = worker_name


class TimelineRecordFeedLinesWrapper(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'step_id': {'key': 'stepId', 'type': 'str'},
        'value': {'key': 'value', 'type': '[str]'}
    }

    def __init__(self, count=None, step_id=None, value=None):
        super(TimelineRecordFeedLinesWrapper, self).__init__()
        self.count = count
        self.step_id = step_id
        self.value = value


class TimelineReference(Model):

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'}
    }

    def __init__(self, change_id=None, id=None, location=None):
        super(TimelineReference, self).__init__()
        self.change_id = change_id
        self.id = id
        self.location = location


class VariableValue(Model):

    _attribute_map = {
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_secret=None, value=None):
        super(VariableValue, self).__init__()
        self.is_secret = is_secret
        self.value = value


class TaskLog(TaskLogReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'location': {'key': 'location', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'index_location': {'key': 'indexLocation', 'type': 'str'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'line_count': {'key': 'lineCount', 'type': 'long'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, id=None, location=None, created_on=None, index_location=None, last_changed_on=None, line_count=None, path=None):
        super(TaskLog, self).__init__(id=id, location=location)
        self.created_on = created_on
        self.index_location = index_location
        self.last_changed_on = last_changed_on
        self.line_count = line_count
        self.path = path


class TaskOrchestrationContainer(TaskOrchestrationItem):

    _attribute_map = {
        'item_type': {'key': 'itemType', 'type': 'object'},
        'children': {'key': 'children', 'type': '[TaskOrchestrationItem]'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'data': {'key': 'data', 'type': '{str}'},
        'max_concurrency': {'key': 'maxConcurrency', 'type': 'int'},
        'parallel': {'key': 'parallel', 'type': 'bool'},
        'rollback': {'key': 'rollback', 'type': 'TaskOrchestrationContainer'}
    }

    def __init__(self, item_type=None, children=None, continue_on_error=None, data=None, max_concurrency=None, parallel=None, rollback=None):
        super(TaskOrchestrationContainer, self).__init__(item_type=item_type)
        self.children = children
        self.continue_on_error = continue_on_error
        self.data = data
        self.max_concurrency = max_concurrency
        self.parallel = parallel
        self.rollback = rollback


class TaskOrchestrationPlan(TaskOrchestrationPlanReference):

    _attribute_map = {
        'artifact_location': {'key': 'artifactLocation', 'type': 'str'},
        'artifact_uri': {'key': 'artifactUri', 'type': 'str'},
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'},
        'environment': {'key': 'environment', 'type': 'PlanEnvironment'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'implementation': {'key': 'implementation', 'type': 'TaskOrchestrationContainer'},
        'initialization_log': {'key': 'initializationLog', 'type': 'TaskLogReference'},
        'requested_by_id': {'key': 'requestedById', 'type': 'str'},
        'requested_for_id': {'key': 'requestedForId', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'object'},
        'timeline': {'key': 'timeline', 'type': 'TimelineReference'}
    }

    def __init__(self, artifact_location=None, artifact_uri=None, definition=None, owner=None, plan_group=None, plan_id=None, plan_type=None, scope_identifier=None, version=None, environment=None, finish_time=None, implementation=None, initialization_log=None, requested_by_id=None, requested_for_id=None, result=None, result_code=None, start_time=None, state=None, timeline=None):
        super(TaskOrchestrationPlan, self).__init__(artifact_location=artifact_location, artifact_uri=artifact_uri, definition=definition, owner=owner, plan_group=plan_group, plan_id=plan_id, plan_type=plan_type, scope_identifier=scope_identifier, version=version)
        self.environment = environment
        self.finish_time = finish_time
        self.implementation = implementation
        self.initialization_log = initialization_log
        self.requested_by_id = requested_by_id
        self.requested_for_id = requested_for_id
        self.result = result
        self.result_code = result_code
        self.start_time = start_time
        self.state = state
        self.timeline = timeline


class Timeline(TimelineReference):

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'str'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'records': {'key': 'records', 'type': '[TimelineRecord]'}
    }

    def __init__(self, change_id=None, id=None, location=None, last_changed_by=None, last_changed_on=None, records=None):
        super(Timeline, self).__init__(change_id=change_id, id=id, location=location)
        self.last_changed_by = last_changed_by
        self.last_changed_on = last_changed_on
        self.records = records


__all__ = [
    'Issue',
    'JobOption',
    'MaskHint',
    'PlanEnvironment',
    'ProjectReference',
    'ReferenceLinks',
    'TaskAgentJob',
    'TaskAgentJobStep',
    'TaskAgentJobTask',
    'TaskAgentJobVariable',
    'TaskAttachment',
    'TaskLogReference',
    'TaskOrchestrationItem',
    'TaskOrchestrationOwner',
    'TaskOrchestrationPlanGroupsQueueMetrics',
    'TaskOrchestrationPlanReference',
    'TaskOrchestrationQueuedPlan',
    'TaskOrchestrationQueuedPlanGroup',
    'TaskReference',
    'TimelineAttempt',
    'TimelineRecord',
    'TimelineRecordFeedLinesWrapper',
    'TimelineReference',
    'VariableValue',
    'TaskLog',
    'TaskOrchestrationContainer',
    'TaskOrchestrationPlan',
    'Timeline',
]
