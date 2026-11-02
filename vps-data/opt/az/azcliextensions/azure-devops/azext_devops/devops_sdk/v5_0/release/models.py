# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AgentArtifactDefinition(Model):

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'artifact_type': {'key': 'artifactType', 'type': 'object'},
        'details': {'key': 'details', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, alias=None, artifact_type=None, details=None, name=None, version=None):
        super(AgentArtifactDefinition, self).__init__()
        self.alias = alias
        self.artifact_type = artifact_type
        self.details = details
        self.name = name
        self.version = version


class ApprovalOptions(Model):

    _attribute_map = {
        'auto_triggered_and_previous_environment_approved_can_be_skipped': {'key': 'autoTriggeredAndPreviousEnvironmentApprovedCanBeSkipped', 'type': 'bool'},
        'enforce_identity_revalidation': {'key': 'enforceIdentityRevalidation', 'type': 'bool'},
        'execution_order': {'key': 'executionOrder', 'type': 'object'},
        'release_creator_can_be_approver': {'key': 'releaseCreatorCanBeApprover', 'type': 'bool'},
        'required_approver_count': {'key': 'requiredApproverCount', 'type': 'int'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, auto_triggered_and_previous_environment_approved_can_be_skipped=None, enforce_identity_revalidation=None, execution_order=None, release_creator_can_be_approver=None, required_approver_count=None, timeout_in_minutes=None):
        super(ApprovalOptions, self).__init__()
        self.auto_triggered_and_previous_environment_approved_can_be_skipped = auto_triggered_and_previous_environment_approved_can_be_skipped
        self.enforce_identity_revalidation = enforce_identity_revalidation
        self.execution_order = execution_order
        self.release_creator_can_be_approver = release_creator_can_be_approver
        self.required_approver_count = required_approver_count
        self.timeout_in_minutes = timeout_in_minutes


class Artifact(Model):

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'definition_reference': {'key': 'definitionReference', 'type': '{ArtifactSourceReference}'},
        'is_primary': {'key': 'isPrimary', 'type': 'bool'},
        'is_retained': {'key': 'isRetained', 'type': 'bool'},
        'source_id': {'key': 'sourceId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, alias=None, definition_reference=None, is_primary=None, is_retained=None, source_id=None, type=None):
        super(Artifact, self).__init__()
        self.alias = alias
        self.definition_reference = definition_reference
        self.is_primary = is_primary
        self.is_retained = is_retained
        self.source_id = source_id
        self.type = type


class ArtifactMetadata(Model):

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'instance_reference': {'key': 'instanceReference', 'type': 'BuildVersion'}
    }

    def __init__(self, alias=None, instance_reference=None):
        super(ArtifactMetadata, self).__init__()
        self.alias = alias
        self.instance_reference = instance_reference


class ArtifactSourceReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ArtifactSourceReference, self).__init__()
        self.id = id
        self.name = name


class ArtifactTriggerConfiguration(Model):

    _attribute_map = {
        'is_trigger_supported': {'key': 'isTriggerSupported', 'type': 'bool'},
        'is_trigger_supported_only_in_hosted': {'key': 'isTriggerSupportedOnlyInHosted', 'type': 'bool'},
        'is_webhook_supported_at_server_level': {'key': 'isWebhookSupportedAtServerLevel', 'type': 'bool'},
        'payload_hash_header_name': {'key': 'payloadHashHeaderName', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '{str}'},
        'webhook_payload_mapping': {'key': 'webhookPayloadMapping', 'type': '{str}'}
    }

    def __init__(self, is_trigger_supported=None, is_trigger_supported_only_in_hosted=None, is_webhook_supported_at_server_level=None, payload_hash_header_name=None, resources=None, webhook_payload_mapping=None):
        super(ArtifactTriggerConfiguration, self).__init__()
        self.is_trigger_supported = is_trigger_supported
        self.is_trigger_supported_only_in_hosted = is_trigger_supported_only_in_hosted
        self.is_webhook_supported_at_server_level = is_webhook_supported_at_server_level
        self.payload_hash_header_name = payload_hash_header_name
        self.resources = resources
        self.webhook_payload_mapping = webhook_payload_mapping


class ArtifactTypeDefinition(Model):

    _attribute_map = {
        'artifact_trigger_configuration': {'key': 'artifactTriggerConfiguration', 'type': 'ArtifactTriggerConfiguration'},
        'artifact_type': {'key': 'artifactType', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'endpoint_type_id': {'key': 'endpointTypeId', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'unique_source_identifier': {'key': 'uniqueSourceIdentifier', 'type': 'str'}
    }

    def __init__(self, artifact_trigger_configuration=None, artifact_type=None, display_name=None, endpoint_type_id=None, input_descriptors=None, name=None, unique_source_identifier=None):
        super(ArtifactTypeDefinition, self).__init__()
        self.artifact_trigger_configuration = artifact_trigger_configuration
        self.artifact_type = artifact_type
        self.display_name = display_name
        self.endpoint_type_id = endpoint_type_id
        self.input_descriptors = input_descriptors
        self.name = name
        self.unique_source_identifier = unique_source_identifier


class ArtifactVersion(Model):

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'default_version': {'key': 'defaultVersion', 'type': 'BuildVersion'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'source_id': {'key': 'sourceId', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[BuildVersion]'}
    }

    def __init__(self, alias=None, default_version=None, error_message=None, source_id=None, versions=None):
        super(ArtifactVersion, self).__init__()
        self.alias = alias
        self.default_version = default_version
        self.error_message = error_message
        self.source_id = source_id
        self.versions = versions


class ArtifactVersionQueryResult(Model):

    _attribute_map = {
        'artifact_versions': {'key': 'artifactVersions', 'type': '[ArtifactVersion]'}
    }

    def __init__(self, artifact_versions=None):
        super(ArtifactVersionQueryResult, self).__init__()
        self.artifact_versions = artifact_versions


class AuthorizationHeader(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(AuthorizationHeader, self).__init__()
        self.name = name
        self.value = value


class AutoTriggerIssue(Model):

    _attribute_map = {
        'issue': {'key': 'issue', 'type': 'Issue'},
        'issue_source': {'key': 'issueSource', 'type': 'object'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'release_definition_reference': {'key': 'releaseDefinitionReference', 'type': 'ReleaseDefinitionShallowReference'},
        'release_trigger_type': {'key': 'releaseTriggerType', 'type': 'object'}
    }

    def __init__(self, issue=None, issue_source=None, project=None, release_definition_reference=None, release_trigger_type=None):
        super(AutoTriggerIssue, self).__init__()
        self.issue = issue
        self.issue_source = issue_source
        self.project = project
        self.release_definition_reference = release_definition_reference
        self.release_trigger_type = release_trigger_type


class BuildVersion(Model):

    _attribute_map = {
        'commit_message': {'key': 'commitMessage', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'str'},
        'definition_name': {'key': 'definitionName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_multi_definition_type': {'key': 'isMultiDefinitionType', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'source_branch': {'key': 'sourceBranch', 'type': 'str'},
        'source_pull_request_version': {'key': 'sourcePullRequestVersion', 'type': 'SourcePullRequestVersion'},
        'source_repository_id': {'key': 'sourceRepositoryId', 'type': 'str'},
        'source_repository_type': {'key': 'sourceRepositoryType', 'type': 'str'},
        'source_version': {'key': 'sourceVersion', 'type': 'str'}
    }

    def __init__(self, commit_message=None, definition_id=None, definition_name=None, id=None, is_multi_definition_type=None, name=None, source_branch=None, source_pull_request_version=None, source_repository_id=None, source_repository_type=None, source_version=None):
        super(BuildVersion, self).__init__()
        self.commit_message = commit_message
        self.definition_id = definition_id
        self.definition_name = definition_name
        self.id = id
        self.is_multi_definition_type = is_multi_definition_type
        self.name = name
        self.source_branch = source_branch
        self.source_pull_request_version = source_pull_request_version
        self.source_repository_id = source_repository_id
        self.source_repository_type = source_repository_type
        self.source_version = source_version


class Change(Model):

    _attribute_map = {
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'display_uri': {'key': 'displayUri', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'pushed_by': {'key': 'pushedBy', 'type': 'IdentityRef'},
        'pusher': {'key': 'pusher', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'}
    }

    def __init__(self, author=None, change_type=None, display_uri=None, id=None, location=None, message=None, pushed_by=None, pusher=None, timestamp=None):
        super(Change, self).__init__()
        self.author = author
        self.change_type = change_type
        self.display_uri = display_uri
        self.id = id
        self.location = location
        self.message = message
        self.pushed_by = pushed_by
        self.pusher = pusher
        self.timestamp = timestamp


class Condition(Model):

    _attribute_map = {
        'condition_type': {'key': 'conditionType', 'type': 'object'},
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, condition_type=None, name=None, value=None):
        super(Condition, self).__init__()
        self.condition_type = condition_type
        self.name = name
        self.value = value


class ConfigurationVariableValue(Model):

    _attribute_map = {
        'allow_override': {'key': 'allowOverride', 'type': 'bool'},
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, allow_override=None, is_secret=None, value=None):
        super(ConfigurationVariableValue, self).__init__()
        self.allow_override = allow_override
        self.is_secret = is_secret
        self.value = value


class DataSourceBindingBase(Model):

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target


class DefinitionEnvironmentReference(Model):

    _attribute_map = {
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'definition_environment_name': {'key': 'definitionEnvironmentName', 'type': 'str'},
        'release_definition_id': {'key': 'releaseDefinitionId', 'type': 'int'},
        'release_definition_name': {'key': 'releaseDefinitionName', 'type': 'str'}
    }

    def __init__(self, definition_environment_id=None, definition_environment_name=None, release_definition_id=None, release_definition_name=None):
        super(DefinitionEnvironmentReference, self).__init__()
        self.definition_environment_id = definition_environment_id
        self.definition_environment_name = definition_environment_name
        self.release_definition_id = release_definition_id
        self.release_definition_name = release_definition_name


class Deployment(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'attempt': {'key': 'attempt', 'type': 'int'},
        'completed_on': {'key': 'completedOn', 'type': 'iso-8601'},
        'conditions': {'key': 'conditions', 'type': '[Condition]'},
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'deployment_status': {'key': 'deploymentStatus', 'type': 'object'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': '[ReleaseApproval]'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': '[ReleaseApproval]'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'},
        'queued_on': {'key': 'queuedOn', 'type': 'iso-8601'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release': {'key': 'release', 'type': 'ReleaseReference'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_environment': {'key': 'releaseEnvironment', 'type': 'ReleaseEnvironmentShallowReference'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'requested_for': {'key': 'requestedFor', 'type': 'IdentityRef'},
        'scheduled_deployment_time': {'key': 'scheduledDeploymentTime', 'type': 'iso-8601'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'}
    }

    def __init__(self, _links=None, attempt=None, completed_on=None, conditions=None, definition_environment_id=None, deployment_status=None, id=None, last_modified_by=None, last_modified_on=None, operation_status=None, post_deploy_approvals=None, pre_deploy_approvals=None, project_reference=None, queued_on=None, reason=None, release=None, release_definition=None, release_environment=None, requested_by=None, requested_for=None, scheduled_deployment_time=None, started_on=None):
        super(Deployment, self).__init__()
        self._links = _links
        self.attempt = attempt
        self.completed_on = completed_on
        self.conditions = conditions
        self.definition_environment_id = definition_environment_id
        self.deployment_status = deployment_status
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.operation_status = operation_status
        self.post_deploy_approvals = post_deploy_approvals
        self.pre_deploy_approvals = pre_deploy_approvals
        self.project_reference = project_reference
        self.queued_on = queued_on
        self.reason = reason
        self.release = release
        self.release_definition = release_definition
        self.release_environment = release_environment
        self.requested_by = requested_by
        self.requested_for = requested_for
        self.scheduled_deployment_time = scheduled_deployment_time
        self.started_on = started_on


class DeploymentAttempt(Model):

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'deployment_id': {'key': 'deploymentId', 'type': 'int'},
        'error_log': {'key': 'errorLog', 'type': 'str'},
        'has_started': {'key': 'hasStarted', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'job': {'key': 'job', 'type': 'ReleaseTask'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'post_deployment_gates': {'key': 'postDeploymentGates', 'type': 'ReleaseGates'},
        'pre_deployment_gates': {'key': 'preDeploymentGates', 'type': 'ReleaseGates'},
        'queued_on': {'key': 'queuedOn', 'type': 'iso-8601'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release_deploy_phases': {'key': 'releaseDeployPhases', 'type': '[ReleaseDeployPhase]'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'requested_for': {'key': 'requestedFor', 'type': 'IdentityRef'},
        'run_plan_id': {'key': 'runPlanId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'tasks': {'key': 'tasks', 'type': '[ReleaseTask]'}
    }

    def __init__(self, attempt=None, deployment_id=None, error_log=None, has_started=None, id=None, issues=None, job=None, last_modified_by=None, last_modified_on=None, operation_status=None, post_deployment_gates=None, pre_deployment_gates=None, queued_on=None, reason=None, release_deploy_phases=None, requested_by=None, requested_for=None, run_plan_id=None, status=None, tasks=None):
        super(DeploymentAttempt, self).__init__()
        self.attempt = attempt
        self.deployment_id = deployment_id
        self.error_log = error_log
        self.has_started = has_started
        self.id = id
        self.issues = issues
        self.job = job
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.operation_status = operation_status
        self.post_deployment_gates = post_deployment_gates
        self.pre_deployment_gates = pre_deployment_gates
        self.queued_on = queued_on
        self.reason = reason
        self.release_deploy_phases = release_deploy_phases
        self.requested_by = requested_by
        self.requested_for = requested_for
        self.run_plan_id = run_plan_id
        self.status = status
        self.tasks = tasks


class DeploymentJob(Model):

    _attribute_map = {
        'job': {'key': 'job', 'type': 'ReleaseTask'},
        'tasks': {'key': 'tasks', 'type': '[ReleaseTask]'}
    }

    def __init__(self, job=None, tasks=None):
        super(DeploymentJob, self).__init__()
        self.job = job
        self.tasks = tasks


class DeploymentQueryParameters(Model):

    _attribute_map = {
        'artifact_source_id': {'key': 'artifactSourceId', 'type': 'str'},
        'artifact_type_id': {'key': 'artifactTypeId', 'type': 'str'},
        'artifact_versions': {'key': 'artifactVersions', 'type': '[str]'},
        'deployments_per_environment': {'key': 'deploymentsPerEnvironment', 'type': 'int'},
        'deployment_status': {'key': 'deploymentStatus', 'type': 'object'},
        'environments': {'key': 'environments', 'type': '[DefinitionEnvironmentReference]'},
        'expands': {'key': 'expands', 'type': 'object'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'latest_deployments_only': {'key': 'latestDeploymentsOnly', 'type': 'bool'},
        'max_deployments_per_environment': {'key': 'maxDeploymentsPerEnvironment', 'type': 'int'},
        'max_modified_time': {'key': 'maxModifiedTime', 'type': 'iso-8601'},
        'min_modified_time': {'key': 'minModifiedTime', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'query_order': {'key': 'queryOrder', 'type': 'object'},
        'query_type': {'key': 'queryType', 'type': 'object'},
        'source_branch': {'key': 'sourceBranch', 'type': 'str'}
    }

    def __init__(self, artifact_source_id=None, artifact_type_id=None, artifact_versions=None, deployments_per_environment=None, deployment_status=None, environments=None, expands=None, is_deleted=None, latest_deployments_only=None, max_deployments_per_environment=None, max_modified_time=None, min_modified_time=None, operation_status=None, query_order=None, query_type=None, source_branch=None):
        super(DeploymentQueryParameters, self).__init__()
        self.artifact_source_id = artifact_source_id
        self.artifact_type_id = artifact_type_id
        self.artifact_versions = artifact_versions
        self.deployments_per_environment = deployments_per_environment
        self.deployment_status = deployment_status
        self.environments = environments
        self.expands = expands
        self.is_deleted = is_deleted
        self.latest_deployments_only = latest_deployments_only
        self.max_deployments_per_environment = max_deployments_per_environment
        self.max_modified_time = max_modified_time
        self.min_modified_time = min_modified_time
        self.operation_status = operation_status
        self.query_order = query_order
        self.query_type = query_type
        self.source_branch = source_branch


class EmailRecipients(Model):

    _attribute_map = {
        'email_addresses': {'key': 'emailAddresses', 'type': '[str]'},
        'tfs_ids': {'key': 'tfsIds', 'type': '[str]'}
    }

    def __init__(self, email_addresses=None, tfs_ids=None):
        super(EmailRecipients, self).__init__()
        self.email_addresses = email_addresses
        self.tfs_ids = tfs_ids


class EnvironmentExecutionPolicy(Model):

    _attribute_map = {
        'concurrency_count': {'key': 'concurrencyCount', 'type': 'int'},
        'queue_depth_count': {'key': 'queueDepthCount', 'type': 'int'}
    }

    def __init__(self, concurrency_count=None, queue_depth_count=None):
        super(EnvironmentExecutionPolicy, self).__init__()
        self.concurrency_count = concurrency_count
        self.queue_depth_count = queue_depth_count


class EnvironmentOptions(Model):

    _attribute_map = {
        'auto_link_work_items': {'key': 'autoLinkWorkItems', 'type': 'bool'},
        'badge_enabled': {'key': 'badgeEnabled', 'type': 'bool'},
        'email_notification_type': {'key': 'emailNotificationType', 'type': 'str'},
        'email_recipients': {'key': 'emailRecipients', 'type': 'str'},
        'enable_access_token': {'key': 'enableAccessToken', 'type': 'bool'},
        'publish_deployment_status': {'key': 'publishDeploymentStatus', 'type': 'bool'},
        'pull_request_deployment_enabled': {'key': 'pullRequestDeploymentEnabled', 'type': 'bool'},
        'skip_artifacts_download': {'key': 'skipArtifactsDownload', 'type': 'bool'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, auto_link_work_items=None, badge_enabled=None, email_notification_type=None, email_recipients=None, enable_access_token=None, publish_deployment_status=None, pull_request_deployment_enabled=None, skip_artifacts_download=None, timeout_in_minutes=None):
        super(EnvironmentOptions, self).__init__()
        self.auto_link_work_items = auto_link_work_items
        self.badge_enabled = badge_enabled
        self.email_notification_type = email_notification_type
        self.email_recipients = email_recipients
        self.enable_access_token = enable_access_token
        self.publish_deployment_status = publish_deployment_status
        self.pull_request_deployment_enabled = pull_request_deployment_enabled
        self.skip_artifacts_download = skip_artifacts_download
        self.timeout_in_minutes = timeout_in_minutes


class EnvironmentRetentionPolicy(Model):

    _attribute_map = {
        'days_to_keep': {'key': 'daysToKeep', 'type': 'int'},
        'releases_to_keep': {'key': 'releasesToKeep', 'type': 'int'},
        'retain_build': {'key': 'retainBuild', 'type': 'bool'}
    }

    def __init__(self, days_to_keep=None, releases_to_keep=None, retain_build=None):
        super(EnvironmentRetentionPolicy, self).__init__()
        self.days_to_keep = days_to_keep
        self.releases_to_keep = releases_to_keep
        self.retain_build = retain_build


class EnvironmentTrigger(Model):

    _attribute_map = {
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'release_definition_id': {'key': 'releaseDefinitionId', 'type': 'int'},
        'trigger_content': {'key': 'triggerContent', 'type': 'str'},
        'trigger_type': {'key': 'triggerType', 'type': 'object'}
    }

    def __init__(self, definition_environment_id=None, release_definition_id=None, trigger_content=None, trigger_type=None):
        super(EnvironmentTrigger, self).__init__()
        self.definition_environment_id = definition_environment_id
        self.release_definition_id = release_definition_id
        self.trigger_content = trigger_content
        self.trigger_type = trigger_type


class FavoriteItem(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, data=None, id=None, name=None, type=None):
        super(FavoriteItem, self).__init__()
        self.data = data
        self.id = id
        self.name = name
        self.type = type


class Folder(Model):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'IdentityRef'},
        'last_changed_date': {'key': 'lastChangedDate', 'type': 'iso-8601'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, last_changed_by=None, last_changed_date=None, path=None):
        super(Folder, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.last_changed_by = last_changed_by
        self.last_changed_date = last_changed_date
        self.path = path


class GateUpdateMetadata(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'gates_to_ignore': {'key': 'gatesToIgnore', 'type': '[str]'}
    }

    def __init__(self, comment=None, gates_to_ignore=None):
        super(GateUpdateMetadata, self).__init__()
        self.comment = comment
        self.gates_to_ignore = gates_to_ignore


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


class IgnoredGate(Model):

    _attribute_map = {
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, last_modified_on=None, name=None):
        super(IgnoredGate, self).__init__()
        self.last_modified_on = last_modified_on
        self.name = name


class InputDescriptor(Model):

    _attribute_map = {
        'dependency_input_ids': {'key': 'dependencyInputIds', 'type': '[str]'},
        'description': {'key': 'description', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'has_dynamic_value_information': {'key': 'hasDynamicValueInformation', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'input_mode': {'key': 'inputMode', 'type': 'object'},
        'is_confidential': {'key': 'isConfidential', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'use_in_default_description': {'key': 'useInDefaultDescription', 'type': 'bool'},
        'validation': {'key': 'validation', 'type': 'InputValidation'},
        'value_hint': {'key': 'valueHint', 'type': 'str'},
        'values': {'key': 'values', 'type': 'InputValues'}
    }

    def __init__(self, dependency_input_ids=None, description=None, group_name=None, has_dynamic_value_information=None, id=None, input_mode=None, is_confidential=None, name=None, properties=None, type=None, use_in_default_description=None, validation=None, value_hint=None, values=None):
        super(InputDescriptor, self).__init__()
        self.dependency_input_ids = dependency_input_ids
        self.description = description
        self.group_name = group_name
        self.has_dynamic_value_information = has_dynamic_value_information
        self.id = id
        self.input_mode = input_mode
        self.is_confidential = is_confidential
        self.name = name
        self.properties = properties
        self.type = type
        self.use_in_default_description = use_in_default_description
        self.validation = validation
        self.value_hint = value_hint
        self.values = values


class InputValidation(Model):

    _attribute_map = {
        'data_type': {'key': 'dataType', 'type': 'object'},
        'is_required': {'key': 'isRequired', 'type': 'bool'},
        'max_length': {'key': 'maxLength', 'type': 'int'},
        'max_value': {'key': 'maxValue', 'type': 'decimal'},
        'min_length': {'key': 'minLength', 'type': 'int'},
        'min_value': {'key': 'minValue', 'type': 'decimal'},
        'pattern': {'key': 'pattern', 'type': 'str'},
        'pattern_mismatch_error_message': {'key': 'patternMismatchErrorMessage', 'type': 'str'}
    }

    def __init__(self, data_type=None, is_required=None, max_length=None, max_value=None, min_length=None, min_value=None, pattern=None, pattern_mismatch_error_message=None):
        super(InputValidation, self).__init__()
        self.data_type = data_type
        self.is_required = is_required
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.pattern = pattern
        self.pattern_mismatch_error_message = pattern_mismatch_error_message


class InputValue(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': '{object}'},
        'display_value': {'key': 'displayValue', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, data=None, display_value=None, value=None):
        super(InputValue, self).__init__()
        self.data = data
        self.display_value = display_value
        self.value = value


class InputValues(Model):

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'error': {'key': 'error', 'type': 'InputValuesError'},
        'input_id': {'key': 'inputId', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'is_limited_to_possible_values': {'key': 'isLimitedToPossibleValues', 'type': 'bool'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'possible_values': {'key': 'possibleValues', 'type': '[InputValue]'}
    }

    def __init__(self, default_value=None, error=None, input_id=None, is_disabled=None, is_limited_to_possible_values=None, is_read_only=None, possible_values=None):
        super(InputValues, self).__init__()
        self.default_value = default_value
        self.error = error
        self.input_id = input_id
        self.is_disabled = is_disabled
        self.is_limited_to_possible_values = is_limited_to_possible_values
        self.is_read_only = is_read_only
        self.possible_values = possible_values


class InputValuesError(Model):

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, message=None):
        super(InputValuesError, self).__init__()
        self.message = message


class InputValuesQuery(Model):

    _attribute_map = {
        'current_values': {'key': 'currentValues', 'type': '{str}'},
        'input_values': {'key': 'inputValues', 'type': '[InputValues]'},
        'resource': {'key': 'resource', 'type': 'object'}
    }

    def __init__(self, current_values=None, input_values=None, resource=None):
        super(InputValuesQuery, self).__init__()
        self.current_values = current_values
        self.input_values = input_values
        self.resource = resource


class Issue(Model):

    _attribute_map = {
        'data': {'key': 'data', 'type': '{str}'},
        'issue_type': {'key': 'issueType', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, data=None, issue_type=None, message=None):
        super(Issue, self).__init__()
        self.data = data
        self.issue_type = issue_type
        self.message = message


class MailMessage(Model):

    _attribute_map = {
        'body': {'key': 'body', 'type': 'str'},
        'cc': {'key': 'cc', 'type': 'EmailRecipients'},
        'in_reply_to': {'key': 'inReplyTo', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'reply_by': {'key': 'replyBy', 'type': 'iso-8601'},
        'reply_to': {'key': 'replyTo', 'type': 'EmailRecipients'},
        'sections': {'key': 'sections', 'type': '[object]'},
        'sender_type': {'key': 'senderType', 'type': 'object'},
        'subject': {'key': 'subject', 'type': 'str'},
        'to': {'key': 'to', 'type': 'EmailRecipients'}
    }

    def __init__(self, body=None, cc=None, in_reply_to=None, message_id=None, reply_by=None, reply_to=None, sections=None, sender_type=None, subject=None, to=None):
        super(MailMessage, self).__init__()
        self.body = body
        self.cc = cc
        self.in_reply_to = in_reply_to
        self.message_id = message_id
        self.reply_by = reply_by
        self.reply_to = reply_to
        self.sections = sections
        self.sender_type = sender_type
        self.subject = subject
        self.to = to


class ManualIntervention(Model):

    _attribute_map = {
        'approver': {'key': 'approver', 'type': 'IdentityRef'},
        'comments': {'key': 'comments', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'instructions': {'key': 'instructions', 'type': 'str'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'release': {'key': 'release', 'type': 'ReleaseShallowReference'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_environment': {'key': 'releaseEnvironment', 'type': 'ReleaseEnvironmentShallowReference'},
        'status': {'key': 'status', 'type': 'object'},
        'task_instance_id': {'key': 'taskInstanceId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, approver=None, comments=None, created_on=None, id=None, instructions=None, modified_on=None, name=None, release=None, release_definition=None, release_environment=None, status=None, task_instance_id=None, url=None):
        super(ManualIntervention, self).__init__()
        self.approver = approver
        self.comments = comments
        self.created_on = created_on
        self.id = id
        self.instructions = instructions
        self.modified_on = modified_on
        self.name = name
        self.release = release
        self.release_definition = release_definition
        self.release_environment = release_environment
        self.status = status
        self.task_instance_id = task_instance_id
        self.url = url


class ManualInterventionUpdateMetadata(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, comment=None, status=None):
        super(ManualInterventionUpdateMetadata, self).__init__()
        self.comment = comment
        self.status = status


class Metric(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'int'}
    }

    def __init__(self, name=None, value=None):
        super(Metric, self).__init__()
        self.name = name
        self.value = value


class PipelineProcess(Model):

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(PipelineProcess, self).__init__()
        self.type = type


class ProcessParameters(Model):

    _attribute_map = {
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBindingBase]'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinitionBase]'},
        'source_definitions': {'key': 'sourceDefinitions', 'type': '[TaskSourceDefinitionBase]'}
    }

    def __init__(self, data_source_bindings=None, inputs=None, source_definitions=None):
        super(ProcessParameters, self).__init__()
        self.data_source_bindings = data_source_bindings
        self.inputs = inputs
        self.source_definitions = source_definitions


class ProjectReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name


class QueuedReleaseData(Model):

    _attribute_map = {
        'project_id': {'key': 'projectId', 'type': 'str'},
        'queue_position': {'key': 'queuePosition', 'type': 'int'},
        'release_id': {'key': 'releaseId', 'type': 'int'}
    }

    def __init__(self, project_id=None, queue_position=None, release_id=None):
        super(QueuedReleaseData, self).__init__()
        self.project_id = project_id
        self.queue_position = queue_position
        self.release_id = release_id


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class Release(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifacts': {'key': 'artifacts', 'type': '[Artifact]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'definition_snapshot_revision': {'key': 'definitionSnapshotRevision', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'environments': {'key': 'environments', 'type': '[ReleaseEnvironment]'},
        'id': {'key': 'id', 'type': 'int'},
        'keep_forever': {'key': 'keepForever', 'type': 'bool'},
        'logs_container_url': {'key': 'logsContainerUrl', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'pool_name': {'key': 'poolName', 'type': 'str'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'},
        'properties': {'key': 'properties', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_name_format': {'key': 'releaseNameFormat', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggering_artifact_alias': {'key': 'triggeringArtifactAlias', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'variable_groups': {'key': 'variableGroups', 'type': '[VariableGroup]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, _links=None, artifacts=None, comment=None, created_by=None, created_on=None, definition_snapshot_revision=None, description=None, environments=None, id=None, keep_forever=None, logs_container_url=None, modified_by=None, modified_on=None, name=None, pool_name=None, project_reference=None, properties=None, reason=None, release_definition=None, release_name_format=None, status=None, tags=None, triggering_artifact_alias=None, url=None, variable_groups=None, variables=None):
        super(Release, self).__init__()
        self._links = _links
        self.artifacts = artifacts
        self.comment = comment
        self.created_by = created_by
        self.created_on = created_on
        self.definition_snapshot_revision = definition_snapshot_revision
        self.description = description
        self.environments = environments
        self.id = id
        self.keep_forever = keep_forever
        self.logs_container_url = logs_container_url
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.pool_name = pool_name
        self.project_reference = project_reference
        self.properties = properties
        self.reason = reason
        self.release_definition = release_definition
        self.release_name_format = release_name_format
        self.status = status
        self.tags = tags
        self.triggering_artifact_alias = triggering_artifact_alias
        self.url = url
        self.variable_groups = variable_groups
        self.variables = variables


class ReleaseApproval(Model):

    _attribute_map = {
        'approval_type': {'key': 'approvalType', 'type': 'object'},
        'approved_by': {'key': 'approvedBy', 'type': 'IdentityRef'},
        'approver': {'key': 'approver', 'type': 'IdentityRef'},
        'attempt': {'key': 'attempt', 'type': 'int'},
        'comments': {'key': 'comments', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'history': {'key': 'history', 'type': '[ReleaseApprovalHistory]'},
        'id': {'key': 'id', 'type': 'int'},
        'is_automated': {'key': 'isAutomated', 'type': 'bool'},
        'is_notification_on': {'key': 'isNotificationOn', 'type': 'bool'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'rank': {'key': 'rank', 'type': 'int'},
        'release': {'key': 'release', 'type': 'ReleaseShallowReference'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_environment': {'key': 'releaseEnvironment', 'type': 'ReleaseEnvironmentShallowReference'},
        'revision': {'key': 'revision', 'type': 'int'},
        'status': {'key': 'status', 'type': 'object'},
        'trial_number': {'key': 'trialNumber', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, approval_type=None, approved_by=None, approver=None, attempt=None, comments=None, created_on=None, history=None, id=None, is_automated=None, is_notification_on=None, modified_on=None, rank=None, release=None, release_definition=None, release_environment=None, revision=None, status=None, trial_number=None, url=None):
        super(ReleaseApproval, self).__init__()
        self.approval_type = approval_type
        self.approved_by = approved_by
        self.approver = approver
        self.attempt = attempt
        self.comments = comments
        self.created_on = created_on
        self.history = history
        self.id = id
        self.is_automated = is_automated
        self.is_notification_on = is_notification_on
        self.modified_on = modified_on
        self.rank = rank
        self.release = release
        self.release_definition = release_definition
        self.release_environment = release_environment
        self.revision = revision
        self.status = status
        self.trial_number = trial_number
        self.url = url


class ReleaseApprovalHistory(Model):

    _attribute_map = {
        'approver': {'key': 'approver', 'type': 'IdentityRef'},
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'comments': {'key': 'comments', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, approver=None, changed_by=None, comments=None, created_on=None, modified_on=None, revision=None):
        super(ReleaseApprovalHistory, self).__init__()
        self.approver = approver
        self.changed_by = changed_by
        self.comments = comments
        self.created_on = created_on
        self.modified_on = modified_on
        self.revision = revision


class ReleaseCondition(Condition):

    _attribute_map = {
        'condition_type': {'key': 'conditionType', 'type': 'object'},
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'result': {'key': 'result', 'type': 'bool'}
    }

    def __init__(self, condition_type=None, name=None, value=None, result=None):
        super(ReleaseCondition, self).__init__(condition_type=condition_type, name=name, value=value)
        self.result = result


class ReleaseDefinitionApprovals(Model):

    _attribute_map = {
        'approval_options': {'key': 'approvalOptions', 'type': 'ApprovalOptions'},
        'approvals': {'key': 'approvals', 'type': '[ReleaseDefinitionApprovalStep]'}
    }

    def __init__(self, approval_options=None, approvals=None):
        super(ReleaseDefinitionApprovals, self).__init__()
        self.approval_options = approval_options
        self.approvals = approvals


class ReleaseDefinitionEnvironment(Model):

    _attribute_map = {
        'badge_url': {'key': 'badgeUrl', 'type': 'str'},
        'conditions': {'key': 'conditions', 'type': '[Condition]'},
        'current_release': {'key': 'currentRelease', 'type': 'ReleaseShallowReference'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deploy_phases': {'key': 'deployPhases', 'type': '[object]'},
        'deploy_step': {'key': 'deployStep', 'type': 'ReleaseDefinitionDeployStep'},
        'environment_options': {'key': 'environmentOptions', 'type': 'EnvironmentOptions'},
        'environment_triggers': {'key': 'environmentTriggers', 'type': '[EnvironmentTrigger]'},
        'execution_policy': {'key': 'executionPolicy', 'type': 'EnvironmentExecutionPolicy'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': 'ReleaseDefinitionApprovals'},
        'post_deployment_gates': {'key': 'postDeploymentGates', 'type': 'ReleaseDefinitionGatesStep'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': 'ReleaseDefinitionApprovals'},
        'pre_deployment_gates': {'key': 'preDeploymentGates', 'type': 'ReleaseDefinitionGatesStep'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'properties': {'key': 'properties', 'type': 'object'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'rank': {'key': 'rank', 'type': 'int'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'EnvironmentRetentionPolicy'},
        'run_options': {'key': 'runOptions', 'type': '{str}'},
        'schedules': {'key': 'schedules', 'type': '[ReleaseSchedule]'},
        'variable_groups': {'key': 'variableGroups', 'type': '[int]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, badge_url=None, conditions=None, current_release=None, demands=None, deploy_phases=None, deploy_step=None, environment_options=None, environment_triggers=None, execution_policy=None, id=None, name=None, owner=None, post_deploy_approvals=None, post_deployment_gates=None, pre_deploy_approvals=None, pre_deployment_gates=None, process_parameters=None, properties=None, queue_id=None, rank=None, retention_policy=None, run_options=None, schedules=None, variable_groups=None, variables=None):
        super(ReleaseDefinitionEnvironment, self).__init__()
        self.badge_url = badge_url
        self.conditions = conditions
        self.current_release = current_release
        self.demands = demands
        self.deploy_phases = deploy_phases
        self.deploy_step = deploy_step
        self.environment_options = environment_options
        self.environment_triggers = environment_triggers
        self.execution_policy = execution_policy
        self.id = id
        self.name = name
        self.owner = owner
        self.post_deploy_approvals = post_deploy_approvals
        self.post_deployment_gates = post_deployment_gates
        self.pre_deploy_approvals = pre_deploy_approvals
        self.pre_deployment_gates = pre_deployment_gates
        self.process_parameters = process_parameters
        self.properties = properties
        self.queue_id = queue_id
        self.rank = rank
        self.retention_policy = retention_policy
        self.run_options = run_options
        self.schedules = schedules
        self.variable_groups = variable_groups
        self.variables = variables


class ReleaseDefinitionEnvironmentStep(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(ReleaseDefinitionEnvironmentStep, self).__init__()
        self.id = id


class ReleaseDefinitionEnvironmentSummary(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'last_releases': {'key': 'lastReleases', 'type': '[ReleaseShallowReference]'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, last_releases=None, name=None):
        super(ReleaseDefinitionEnvironmentSummary, self).__init__()
        self.id = id
        self.last_releases = last_releases
        self.name = name


class ReleaseDefinitionEnvironmentTemplate(Model):

    _attribute_map = {
        'can_delete': {'key': 'canDelete', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'environment': {'key': 'environment', 'type': 'ReleaseDefinitionEnvironment'},
        'icon_task_id': {'key': 'iconTaskId', 'type': 'str'},
        'icon_uri': {'key': 'iconUri', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, can_delete=None, category=None, description=None, environment=None, icon_task_id=None, icon_uri=None, id=None, is_deleted=None, name=None):
        super(ReleaseDefinitionEnvironmentTemplate, self).__init__()
        self.can_delete = can_delete
        self.category = category
        self.description = description
        self.environment = environment
        self.icon_task_id = icon_task_id
        self.icon_uri = icon_uri
        self.id = id
        self.is_deleted = is_deleted
        self.name = name


class ReleaseDefinitionGate(Model):

    _attribute_map = {
        'tasks': {'key': 'tasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, tasks=None):
        super(ReleaseDefinitionGate, self).__init__()
        self.tasks = tasks


class ReleaseDefinitionGatesOptions(Model):

    _attribute_map = {
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'minimum_success_duration': {'key': 'minimumSuccessDuration', 'type': 'int'},
        'sampling_interval': {'key': 'samplingInterval', 'type': 'int'},
        'stabilization_time': {'key': 'stabilizationTime', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'}
    }

    def __init__(self, is_enabled=None, minimum_success_duration=None, sampling_interval=None, stabilization_time=None, timeout=None):
        super(ReleaseDefinitionGatesOptions, self).__init__()
        self.is_enabled = is_enabled
        self.minimum_success_duration = minimum_success_duration
        self.sampling_interval = sampling_interval
        self.stabilization_time = stabilization_time
        self.timeout = timeout


class ReleaseDefinitionGatesStep(Model):

    _attribute_map = {
        'gates': {'key': 'gates', 'type': '[ReleaseDefinitionGate]'},
        'gates_options': {'key': 'gatesOptions', 'type': 'ReleaseDefinitionGatesOptions'},
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, gates=None, gates_options=None, id=None):
        super(ReleaseDefinitionGatesStep, self).__init__()
        self.gates = gates
        self.gates_options = gates_options
        self.id = id


class ReleaseDefinitionRevision(Model):

    _attribute_map = {
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'definition_url': {'key': 'definitionUrl', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, api_version=None, changed_by=None, changed_date=None, change_type=None, comment=None, definition_id=None, definition_url=None, revision=None):
        super(ReleaseDefinitionRevision, self).__init__()
        self.api_version = api_version
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.change_type = change_type
        self.comment = comment
        self.definition_id = definition_id
        self.definition_url = definition_url
        self.revision = revision


class ReleaseDefinitionShallowReference(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, path=None, project_reference=None, url=None):
        super(ReleaseDefinitionShallowReference, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.path = path
        self.project_reference = project_reference
        self.url = url


class ReleaseDefinitionSummary(Model):

    _attribute_map = {
        'environments': {'key': 'environments', 'type': '[ReleaseDefinitionEnvironmentSummary]'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'releases': {'key': 'releases', 'type': '[Release]'}
    }

    def __init__(self, environments=None, release_definition=None, releases=None):
        super(ReleaseDefinitionSummary, self).__init__()
        self.environments = environments
        self.release_definition = release_definition
        self.releases = releases


class ReleaseDefinitionUndeleteParameter(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'}
    }

    def __init__(self, comment=None):
        super(ReleaseDefinitionUndeleteParameter, self).__init__()
        self.comment = comment


class ReleaseDeployPhase(Model):

    _attribute_map = {
        'deployment_jobs': {'key': 'deploymentJobs', 'type': '[DeploymentJob]'},
        'error_log': {'key': 'errorLog', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'manual_interventions': {'key': 'manualInterventions', 'type': '[ManualIntervention]'},
        'name': {'key': 'name', 'type': 'str'},
        'phase_id': {'key': 'phaseId', 'type': 'str'},
        'phase_type': {'key': 'phaseType', 'type': 'object'},
        'rank': {'key': 'rank', 'type': 'int'},
        'run_plan_id': {'key': 'runPlanId', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, deployment_jobs=None, error_log=None, id=None, manual_interventions=None, name=None, phase_id=None, phase_type=None, rank=None, run_plan_id=None, started_on=None, status=None):
        super(ReleaseDeployPhase, self).__init__()
        self.deployment_jobs = deployment_jobs
        self.error_log = error_log
        self.id = id
        self.manual_interventions = manual_interventions
        self.name = name
        self.phase_id = phase_id
        self.phase_type = phase_type
        self.rank = rank
        self.run_plan_id = run_plan_id
        self.started_on = started_on
        self.status = status


class ReleaseEnvironment(Model):

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[ReleaseCondition]'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deploy_phases_snapshot': {'key': 'deployPhasesSnapshot', 'type': '[object]'},
        'deploy_steps': {'key': 'deploySteps', 'type': '[DeploymentAttempt]'},
        'environment_options': {'key': 'environmentOptions', 'type': 'EnvironmentOptions'},
        'id': {'key': 'id', 'type': 'int'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'next_scheduled_utc_time': {'key': 'nextScheduledUtcTime', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'post_approvals_snapshot': {'key': 'postApprovalsSnapshot', 'type': 'ReleaseDefinitionApprovals'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': '[ReleaseApproval]'},
        'post_deployment_gates_snapshot': {'key': 'postDeploymentGatesSnapshot', 'type': 'ReleaseDefinitionGatesStep'},
        'pre_approvals_snapshot': {'key': 'preApprovalsSnapshot', 'type': 'ReleaseDefinitionApprovals'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': '[ReleaseApproval]'},
        'pre_deployment_gates_snapshot': {'key': 'preDeploymentGatesSnapshot', 'type': 'ReleaseDefinitionGatesStep'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'rank': {'key': 'rank', 'type': 'int'},
        'release': {'key': 'release', 'type': 'ReleaseShallowReference'},
        'release_created_by': {'key': 'releaseCreatedBy', 'type': 'IdentityRef'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_description': {'key': 'releaseDescription', 'type': 'str'},
        'release_id': {'key': 'releaseId', 'type': 'int'},
        'scheduled_deployment_time': {'key': 'scheduledDeploymentTime', 'type': 'iso-8601'},
        'schedules': {'key': 'schedules', 'type': '[ReleaseSchedule]'},
        'status': {'key': 'status', 'type': 'object'},
        'time_to_deploy': {'key': 'timeToDeploy', 'type': 'float'},
        'trigger_reason': {'key': 'triggerReason', 'type': 'str'},
        'variable_groups': {'key': 'variableGroups', 'type': '[VariableGroup]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'},
        'workflow_tasks': {'key': 'workflowTasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, conditions=None, created_on=None, definition_environment_id=None, demands=None, deploy_phases_snapshot=None, deploy_steps=None, environment_options=None, id=None, modified_on=None, name=None, next_scheduled_utc_time=None, owner=None, post_approvals_snapshot=None, post_deploy_approvals=None, post_deployment_gates_snapshot=None, pre_approvals_snapshot=None, pre_deploy_approvals=None, pre_deployment_gates_snapshot=None, process_parameters=None, queue_id=None, rank=None, release=None, release_created_by=None, release_definition=None, release_description=None, release_id=None, scheduled_deployment_time=None, schedules=None, status=None, time_to_deploy=None, trigger_reason=None, variable_groups=None, variables=None, workflow_tasks=None):
        super(ReleaseEnvironment, self).__init__()
        self.conditions = conditions
        self.created_on = created_on
        self.definition_environment_id = definition_environment_id
        self.demands = demands
        self.deploy_phases_snapshot = deploy_phases_snapshot
        self.deploy_steps = deploy_steps
        self.environment_options = environment_options
        self.id = id
        self.modified_on = modified_on
        self.name = name
        self.next_scheduled_utc_time = next_scheduled_utc_time
        self.owner = owner
        self.post_approvals_snapshot = post_approvals_snapshot
        self.post_deploy_approvals = post_deploy_approvals
        self.post_deployment_gates_snapshot = post_deployment_gates_snapshot
        self.pre_approvals_snapshot = pre_approvals_snapshot
        self.pre_deploy_approvals = pre_deploy_approvals
        self.pre_deployment_gates_snapshot = pre_deployment_gates_snapshot
        self.process_parameters = process_parameters
        self.queue_id = queue_id
        self.rank = rank
        self.release = release
        self.release_created_by = release_created_by
        self.release_definition = release_definition
        self.release_description = release_description
        self.release_id = release_id
        self.scheduled_deployment_time = scheduled_deployment_time
        self.schedules = schedules
        self.status = status
        self.time_to_deploy = time_to_deploy
        self.trigger_reason = trigger_reason
        self.variable_groups = variable_groups
        self.variables = variables
        self.workflow_tasks = workflow_tasks


class ReleaseEnvironmentShallowReference(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, url=None):
        super(ReleaseEnvironmentShallowReference, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.url = url


class ReleaseEnvironmentUpdateMetadata(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'scheduled_deployment_time': {'key': 'scheduledDeploymentTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, comment=None, scheduled_deployment_time=None, status=None, variables=None):
        super(ReleaseEnvironmentUpdateMetadata, self).__init__()
        self.comment = comment
        self.scheduled_deployment_time = scheduled_deployment_time
        self.status = status
        self.variables = variables


class ReleaseGates(Model):

    _attribute_map = {
        'deployment_jobs': {'key': 'deploymentJobs', 'type': '[DeploymentJob]'},
        'id': {'key': 'id', 'type': 'int'},
        'ignored_gates': {'key': 'ignoredGates', 'type': '[IgnoredGate]'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'run_plan_id': {'key': 'runPlanId', 'type': 'str'},
        'stabilization_completed_on': {'key': 'stabilizationCompletedOn', 'type': 'iso-8601'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'succeeding_since': {'key': 'succeedingSince', 'type': 'iso-8601'}
    }

    def __init__(self, deployment_jobs=None, id=None, ignored_gates=None, last_modified_on=None, run_plan_id=None, stabilization_completed_on=None, started_on=None, status=None, succeeding_since=None):
        super(ReleaseGates, self).__init__()
        self.deployment_jobs = deployment_jobs
        self.id = id
        self.ignored_gates = ignored_gates
        self.last_modified_on = last_modified_on
        self.run_plan_id = run_plan_id
        self.stabilization_completed_on = stabilization_completed_on
        self.started_on = started_on
        self.status = status
        self.succeeding_since = succeeding_since


class ReleaseReference(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifacts': {'key': 'artifacts', 'type': '[Artifact]'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'name': {'key': 'name', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'url': {'key': 'url', 'type': 'str'},
        'web_access_uri': {'key': 'webAccessUri', 'type': 'str'}
    }

    def __init__(self, _links=None, artifacts=None, created_by=None, created_on=None, description=None, id=None, modified_by=None, name=None, reason=None, release_definition=None, url=None, web_access_uri=None):
        super(ReleaseReference, self).__init__()
        self._links = _links
        self.artifacts = artifacts
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
        self.modified_by = modified_by
        self.name = name
        self.reason = reason
        self.release_definition = release_definition
        self.url = url
        self.web_access_uri = web_access_uri


class ReleaseRevision(Model):

    _attribute_map = {
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'change_details': {'key': 'changeDetails', 'type': 'str'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'definition_snapshot_revision': {'key': 'definitionSnapshotRevision', 'type': 'int'},
        'release_id': {'key': 'releaseId', 'type': 'int'}
    }

    def __init__(self, changed_by=None, changed_date=None, change_details=None, change_type=None, comment=None, definition_snapshot_revision=None, release_id=None):
        super(ReleaseRevision, self).__init__()
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.change_details = change_details
        self.change_type = change_type
        self.comment = comment
        self.definition_snapshot_revision = definition_snapshot_revision
        self.release_id = release_id


class ReleaseSchedule(Model):

    _attribute_map = {
        'days_to_release': {'key': 'daysToRelease', 'type': 'object'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'start_hours': {'key': 'startHours', 'type': 'int'},
        'start_minutes': {'key': 'startMinutes', 'type': 'int'},
        'time_zone_id': {'key': 'timeZoneId', 'type': 'str'}
    }

    def __init__(self, days_to_release=None, job_id=None, start_hours=None, start_minutes=None, time_zone_id=None):
        super(ReleaseSchedule, self).__init__()
        self.days_to_release = days_to_release
        self.job_id = job_id
        self.start_hours = start_hours
        self.start_minutes = start_minutes
        self.time_zone_id = time_zone_id


class ReleaseSettings(Model):

    _attribute_map = {
        'retention_settings': {'key': 'retentionSettings', 'type': 'RetentionSettings'}
    }

    def __init__(self, retention_settings=None):
        super(ReleaseSettings, self).__init__()
        self.retention_settings = retention_settings


class ReleaseShallowReference(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, url=None):
        super(ReleaseShallowReference, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.url = url


class ReleaseStartEnvironmentMetadata(Model):

    _attribute_map = {
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, definition_environment_id=None, variables=None):
        super(ReleaseStartEnvironmentMetadata, self).__init__()
        self.definition_environment_id = definition_environment_id
        self.variables = variables


class ReleaseStartMetadata(Model):

    _attribute_map = {
        'artifacts': {'key': 'artifacts', 'type': '[ArtifactMetadata]'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'environments_metadata': {'key': 'environmentsMetadata', 'type': '[ReleaseStartEnvironmentMetadata]'},
        'is_draft': {'key': 'isDraft', 'type': 'bool'},
        'manual_environments': {'key': 'manualEnvironments', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'object'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, artifacts=None, definition_id=None, description=None, environments_metadata=None, is_draft=None, manual_environments=None, properties=None, reason=None, variables=None):
        super(ReleaseStartMetadata, self).__init__()
        self.artifacts = artifacts
        self.definition_id = definition_id
        self.description = description
        self.environments_metadata = environments_metadata
        self.is_draft = is_draft
        self.manual_environments = manual_environments
        self.properties = properties
        self.reason = reason
        self.variables = variables


class ReleaseTask(Model):

    _attribute_map = {
        'agent_name': {'key': 'agentName', 'type': 'str'},
        'date_ended': {'key': 'dateEnded', 'type': 'iso-8601'},
        'date_started': {'key': 'dateStarted', 'type': 'iso-8601'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'line_count': {'key': 'lineCount', 'type': 'long'},
        'log_url': {'key': 'logUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'rank': {'key': 'rank', 'type': 'int'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'task': {'key': 'task', 'type': 'WorkflowTaskReference'},
        'timeline_record_id': {'key': 'timelineRecordId', 'type': 'str'}
    }

    def __init__(self, agent_name=None, date_ended=None, date_started=None, finish_time=None, id=None, issues=None, line_count=None, log_url=None, name=None, percent_complete=None, rank=None, result_code=None, start_time=None, status=None, task=None, timeline_record_id=None):
        super(ReleaseTask, self).__init__()
        self.agent_name = agent_name
        self.date_ended = date_ended
        self.date_started = date_started
        self.finish_time = finish_time
        self.id = id
        self.issues = issues
        self.line_count = line_count
        self.log_url = log_url
        self.name = name
        self.percent_complete = percent_complete
        self.rank = rank
        self.result_code = result_code
        self.start_time = start_time
        self.status = status
        self.task = task
        self.timeline_record_id = timeline_record_id


class ReleaseTaskAttachment(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'record_id': {'key': 'recordId', 'type': 'str'},
        'timeline_id': {'key': 'timelineId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, _links=None, created_on=None, modified_by=None, modified_on=None, name=None, record_id=None, timeline_id=None, type=None):
        super(ReleaseTaskAttachment, self).__init__()
        self._links = _links
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.record_id = record_id
        self.timeline_id = timeline_id
        self.type = type


class ReleaseUpdateMetadata(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'keep_forever': {'key': 'keepForever', 'type': 'bool'},
        'manual_environments': {'key': 'manualEnvironments', 'type': '[str]'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, comment=None, keep_forever=None, manual_environments=None, status=None):
        super(ReleaseUpdateMetadata, self).__init__()
        self.comment = comment
        self.keep_forever = keep_forever
        self.manual_environments = manual_environments
        self.status = status


class ReleaseWorkItemRef(Model):

    _attribute_map = {
        'assignee': {'key': 'assignee', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, assignee=None, id=None, state=None, title=None, type=None, url=None):
        super(ReleaseWorkItemRef, self).__init__()
        self.assignee = assignee
        self.id = id
        self.state = state
        self.title = title
        self.type = type
        self.url = url


class RetentionPolicy(Model):

    _attribute_map = {
        'days_to_keep': {'key': 'daysToKeep', 'type': 'int'}
    }

    def __init__(self, days_to_keep=None):
        super(RetentionPolicy, self).__init__()
        self.days_to_keep = days_to_keep


class RetentionSettings(Model):

    _attribute_map = {
        'days_to_keep_deleted_releases': {'key': 'daysToKeepDeletedReleases', 'type': 'int'},
        'default_environment_retention_policy': {'key': 'defaultEnvironmentRetentionPolicy', 'type': 'EnvironmentRetentionPolicy'},
        'maximum_environment_retention_policy': {'key': 'maximumEnvironmentRetentionPolicy', 'type': 'EnvironmentRetentionPolicy'}
    }

    def __init__(self, days_to_keep_deleted_releases=None, default_environment_retention_policy=None, maximum_environment_retention_policy=None):
        super(RetentionSettings, self).__init__()
        self.days_to_keep_deleted_releases = days_to_keep_deleted_releases
        self.default_environment_retention_policy = default_environment_retention_policy
        self.maximum_environment_retention_policy = maximum_environment_retention_policy


class SourcePullRequestVersion(Model):

    _attribute_map = {
        'pull_request_id': {'key': 'pullRequestId', 'type': 'str'},
        'pull_request_merged_at': {'key': 'pullRequestMergedAt', 'type': 'iso-8601'},
        'source_branch_commit_id': {'key': 'sourceBranchCommitId', 'type': 'str'}
    }

    def __init__(self, pull_request_id=None, pull_request_merged_at=None, source_branch_commit_id=None):
        super(SourcePullRequestVersion, self).__init__()
        self.pull_request_id = pull_request_id
        self.pull_request_merged_at = pull_request_merged_at
        self.source_branch_commit_id = source_branch_commit_id


class SummaryMailSection(Model):

    _attribute_map = {
        'html_content': {'key': 'htmlContent', 'type': 'str'},
        'rank': {'key': 'rank', 'type': 'int'},
        'section_type': {'key': 'sectionType', 'type': 'object'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, html_content=None, rank=None, section_type=None, title=None):
        super(SummaryMailSection, self).__init__()
        self.html_content = html_content
        self.rank = rank
        self.section_type = section_type
        self.title = title


class TaskInputDefinitionBase(Model):

    _attribute_map = {
        'aliases': {'key': 'aliases', 'type': '[str]'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'validation': {'key': 'validation', 'type': 'TaskInputValidation'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, aliases=None, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinitionBase, self).__init__()
        self.aliases = aliases
        self.default_value = default_value
        self.group_name = group_name
        self.help_mark_down = help_mark_down
        self.label = label
        self.name = name
        self.options = options
        self.properties = properties
        self.required = required
        self.type = type
        self.validation = validation
        self.visible_rule = visible_rule


class TaskInputValidation(Model):

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, expression=None, message=None):
        super(TaskInputValidation, self).__init__()
        self.expression = expression
        self.message = message


class TaskSourceDefinitionBase(Model):

    _attribute_map = {
        'auth_key': {'key': 'authKey', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, auth_key=None, endpoint=None, key_selector=None, selector=None, target=None):
        super(TaskSourceDefinitionBase, self).__init__()
        self.auth_key = auth_key
        self.endpoint = endpoint
        self.key_selector = key_selector
        self.selector = selector
        self.target = target


class VariableGroup(Model):

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_shared': {'key': 'isShared', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'provider_data': {'key': 'providerData', 'type': 'VariableGroupProviderData'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, id=None, is_shared=None, modified_by=None, modified_on=None, name=None, provider_data=None, type=None, variables=None):
        super(VariableGroup, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
        self.is_shared = is_shared
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.provider_data = provider_data
        self.type = type
        self.variables = variables


class VariableGroupProviderData(Model):

    _attribute_map = {
    }

    def __init__(self):
        super(VariableGroupProviderData, self).__init__()


class VariableValue(Model):

    _attribute_map = {
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_secret=None, value=None):
        super(VariableValue, self).__init__()
        self.is_secret = is_secret
        self.value = value


class WorkflowTask(Model):

    _attribute_map = {
        'always_run': {'key': 'alwaysRun', 'type': 'bool'},
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'environment': {'key': 'environment', 'type': '{str}'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'override_inputs': {'key': 'overrideInputs', 'type': '{str}'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'task_id': {'key': 'taskId', 'type': 'str'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, always_run=None, condition=None, continue_on_error=None, definition_type=None, enabled=None, environment=None, inputs=None, name=None, override_inputs=None, ref_name=None, task_id=None, timeout_in_minutes=None, version=None):
        super(WorkflowTask, self).__init__()
        self.always_run = always_run
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.definition_type = definition_type
        self.enabled = enabled
        self.environment = environment
        self.inputs = inputs
        self.name = name
        self.override_inputs = override_inputs
        self.ref_name = ref_name
        self.task_id = task_id
        self.timeout_in_minutes = timeout_in_minutes
        self.version = version


class WorkflowTaskReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, version=None):
        super(WorkflowTaskReference, self).__init__()
        self.id = id
        self.name = name
        self.version = version


class ReleaseDefinition(ReleaseDefinitionShallowReference):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'},
        'url': {'key': 'url', 'type': 'str'},
        'artifacts': {'key': 'artifacts', 'type': '[Artifact]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'environments': {'key': 'environments', 'type': '[ReleaseDefinitionEnvironment]'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_release': {'key': 'lastRelease', 'type': 'ReleaseReference'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'pipeline_process': {'key': 'pipelineProcess', 'type': 'PipelineProcess'},
        'properties': {'key': 'properties', 'type': 'object'},
        'release_name_format': {'key': 'releaseNameFormat', 'type': 'str'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
        'revision': {'key': 'revision', 'type': 'int'},
        'source': {'key': 'source', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggers': {'key': 'triggers', 'type': '[object]'},
        'variable_groups': {'key': 'variableGroups', 'type': '[int]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, _links=None, id=None, name=None, path=None, project_reference=None, url=None, artifacts=None, comment=None, created_by=None, created_on=None, description=None, environments=None, is_deleted=None, last_release=None, modified_by=None, modified_on=None, pipeline_process=None, properties=None, release_name_format=None, retention_policy=None, revision=None, source=None, tags=None, triggers=None, variable_groups=None, variables=None):
        super(ReleaseDefinition, self).__init__(_links=_links, id=id, name=name, path=path, project_reference=project_reference, url=url)
        self.artifacts = artifacts
        self.comment = comment
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.environments = environments
        self.is_deleted = is_deleted
        self.last_release = last_release
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.pipeline_process = pipeline_process
        self.properties = properties
        self.release_name_format = release_name_format
        self.retention_policy = retention_policy
        self.revision = revision
        self.source = source
        self.tags = tags
        self.triggers = triggers
        self.variable_groups = variable_groups
        self.variables = variables


class ReleaseDefinitionApprovalStep(ReleaseDefinitionEnvironmentStep):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'approver': {'key': 'approver', 'type': 'IdentityRef'},
        'is_automated': {'key': 'isAutomated', 'type': 'bool'},
        'is_notification_on': {'key': 'isNotificationOn', 'type': 'bool'},
        'rank': {'key': 'rank', 'type': 'int'}
    }

    def __init__(self, id=None, approver=None, is_automated=None, is_notification_on=None, rank=None):
        super(ReleaseDefinitionApprovalStep, self).__init__(id=id)
        self.approver = approver
        self.is_automated = is_automated
        self.is_notification_on = is_notification_on
        self.rank = rank


class ReleaseDefinitionDeployStep(ReleaseDefinitionEnvironmentStep):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'tasks': {'key': 'tasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, id=None, tasks=None):
        super(ReleaseDefinitionDeployStep, self).__init__(id=id)
        self.tasks = tasks


__all__ = [
    'AgentArtifactDefinition',
    'ApprovalOptions',
    'Artifact',
    'ArtifactMetadata',
    'ArtifactSourceReference',
    'ArtifactTriggerConfiguration',
    'ArtifactTypeDefinition',
    'ArtifactVersion',
    'ArtifactVersionQueryResult',
    'AuthorizationHeader',
    'AutoTriggerIssue',
    'BuildVersion',
    'Change',
    'Condition',
    'ConfigurationVariableValue',
    'DataSourceBindingBase',
    'DefinitionEnvironmentReference',
    'Deployment',
    'DeploymentAttempt',
    'DeploymentJob',
    'DeploymentQueryParameters',
    'EmailRecipients',
    'EnvironmentExecutionPolicy',
    'EnvironmentOptions',
    'EnvironmentRetentionPolicy',
    'EnvironmentTrigger',
    'FavoriteItem',
    'Folder',
    'GateUpdateMetadata',
    'GraphSubjectBase',
    'IdentityRef',
    'IgnoredGate',
    'InputDescriptor',
    'InputValidation',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'InputValuesQuery',
    'Issue',
    'MailMessage',
    'ManualIntervention',
    'ManualInterventionUpdateMetadata',
    'Metric',
    'PipelineProcess',
    'ProcessParameters',
    'ProjectReference',
    'QueuedReleaseData',
    'ReferenceLinks',
    'Release',
    'ReleaseApproval',
    'ReleaseApprovalHistory',
    'ReleaseCondition',
    'ReleaseDefinitionApprovals',
    'ReleaseDefinitionEnvironment',
    'ReleaseDefinitionEnvironmentStep',
    'ReleaseDefinitionEnvironmentSummary',
    'ReleaseDefinitionEnvironmentTemplate',
    'ReleaseDefinitionGate',
    'ReleaseDefinitionGatesOptions',
    'ReleaseDefinitionGatesStep',
    'ReleaseDefinitionRevision',
    'ReleaseDefinitionShallowReference',
    'ReleaseDefinitionSummary',
    'ReleaseDefinitionUndeleteParameter',
    'ReleaseDeployPhase',
    'ReleaseEnvironment',
    'ReleaseEnvironmentShallowReference',
    'ReleaseEnvironmentUpdateMetadata',
    'ReleaseGates',
    'ReleaseReference',
    'ReleaseRevision',
    'ReleaseSchedule',
    'ReleaseSettings',
    'ReleaseShallowReference',
    'ReleaseStartEnvironmentMetadata',
    'ReleaseStartMetadata',
    'ReleaseTask',
    'ReleaseTaskAttachment',
    'ReleaseUpdateMetadata',
    'ReleaseWorkItemRef',
    'RetentionPolicy',
    'RetentionSettings',
    'SourcePullRequestVersion',
    'SummaryMailSection',
    'TaskInputDefinitionBase',
    'TaskInputValidation',
    'TaskSourceDefinitionBase',
    'VariableGroup',
    'VariableGroupProviderData',
    'VariableValue',
    'WorkflowTask',
    'WorkflowTaskReference',
    'ReleaseDefinition',
    'ReleaseDefinitionApprovalStep',
    'ReleaseDefinitionDeployStep',
]
