# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AggregatedDataForResultTrend(Model):

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'object'},
        'results_by_outcome': {'key': 'resultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'run_summary_by_state': {'key': 'runSummaryByState', 'type': '{AggregatedRunsByState}'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'},
        'total_tests': {'key': 'totalTests', 'type': 'int'}
    }

    def __init__(self, duration=None, results_by_outcome=None, run_summary_by_state=None, test_results_context=None, total_tests=None):
        super(AggregatedDataForResultTrend, self).__init__()
        self.duration = duration
        self.results_by_outcome = results_by_outcome
        self.run_summary_by_state = run_summary_by_state
        self.test_results_context = test_results_context
        self.total_tests = total_tests


class AggregatedResultDetailsByOutcome(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'duration': {'key': 'duration', 'type': 'object'},
        'outcome': {'key': 'outcome', 'type': 'object'},
        'rerun_result_count': {'key': 'rerunResultCount', 'type': 'int'}
    }

    def __init__(self, count=None, duration=None, outcome=None, rerun_result_count=None):
        super(AggregatedResultDetailsByOutcome, self).__init__()
        self.count = count
        self.duration = duration
        self.outcome = outcome
        self.rerun_result_count = rerun_result_count


class AggregatedResultsAnalysis(Model):

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'object'},
        'not_reported_results_by_outcome': {'key': 'notReportedResultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'previous_context': {'key': 'previousContext', 'type': 'TestResultsContext'},
        'results_by_outcome': {'key': 'resultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'results_difference': {'key': 'resultsDifference', 'type': 'AggregatedResultsDifference'},
        'run_summary_by_outcome': {'key': 'runSummaryByOutcome', 'type': '{AggregatedRunsByOutcome}'},
        'run_summary_by_state': {'key': 'runSummaryByState', 'type': '{AggregatedRunsByState}'},
        'total_tests': {'key': 'totalTests', 'type': 'int'}
    }

    def __init__(self, duration=None, not_reported_results_by_outcome=None, previous_context=None, results_by_outcome=None, results_difference=None, run_summary_by_outcome=None, run_summary_by_state=None, total_tests=None):
        super(AggregatedResultsAnalysis, self).__init__()
        self.duration = duration
        self.not_reported_results_by_outcome = not_reported_results_by_outcome
        self.previous_context = previous_context
        self.results_by_outcome = results_by_outcome
        self.results_difference = results_difference
        self.run_summary_by_outcome = run_summary_by_outcome
        self.run_summary_by_state = run_summary_by_state
        self.total_tests = total_tests


class AggregatedResultsByOutcome(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'duration': {'key': 'duration', 'type': 'object'},
        'group_by_field': {'key': 'groupByField', 'type': 'str'},
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'outcome': {'key': 'outcome', 'type': 'object'},
        'rerun_result_count': {'key': 'rerunResultCount', 'type': 'int'}
    }

    def __init__(self, count=None, duration=None, group_by_field=None, group_by_value=None, outcome=None, rerun_result_count=None):
        super(AggregatedResultsByOutcome, self).__init__()
        self.count = count
        self.duration = duration
        self.group_by_field = group_by_field
        self.group_by_value = group_by_value
        self.outcome = outcome
        self.rerun_result_count = rerun_result_count


class AggregatedResultsDifference(Model):

    _attribute_map = {
        'increase_in_duration': {'key': 'increaseInDuration', 'type': 'object'},
        'increase_in_failures': {'key': 'increaseInFailures', 'type': 'int'},
        'increase_in_non_impacted_tests': {'key': 'increaseInNonImpactedTests', 'type': 'int'},
        'increase_in_other_tests': {'key': 'increaseInOtherTests', 'type': 'int'},
        'increase_in_passed_tests': {'key': 'increaseInPassedTests', 'type': 'int'},
        'increase_in_total_tests': {'key': 'increaseInTotalTests', 'type': 'int'}
    }

    def __init__(self, increase_in_duration=None, increase_in_failures=None, increase_in_non_impacted_tests=None, increase_in_other_tests=None, increase_in_passed_tests=None, increase_in_total_tests=None):
        super(AggregatedResultsDifference, self).__init__()
        self.increase_in_duration = increase_in_duration
        self.increase_in_failures = increase_in_failures
        self.increase_in_non_impacted_tests = increase_in_non_impacted_tests
        self.increase_in_other_tests = increase_in_other_tests
        self.increase_in_passed_tests = increase_in_passed_tests
        self.increase_in_total_tests = increase_in_total_tests


class AggregatedRunsByOutcome(Model):

    _attribute_map = {
        'outcome': {'key': 'outcome', 'type': 'object'},
        'runs_count': {'key': 'runsCount', 'type': 'int'}
    }

    def __init__(self, outcome=None, runs_count=None):
        super(AggregatedRunsByOutcome, self).__init__()
        self.outcome = outcome
        self.runs_count = runs_count


class AggregatedRunsByState(Model):

    _attribute_map = {
        'results_by_outcome': {'key': 'resultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'runs_count': {'key': 'runsCount', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, results_by_outcome=None, runs_count=None, state=None):
        super(AggregatedRunsByState, self).__init__()
        self.results_by_outcome = results_by_outcome
        self.runs_count = runs_count
        self.state = state


class BuildConfiguration(Model):

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'build_definition_id': {'key': 'buildDefinitionId', 'type': 'int'},
        'build_system': {'key': 'buildSystem', 'type': 'str'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'flavor': {'key': 'flavor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'number': {'key': 'number', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'repository_guid': {'key': 'repositoryGuid', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'int'},
        'repository_type': {'key': 'repositoryType', 'type': 'str'},
        'source_version': {'key': 'sourceVersion', 'type': 'str'},
        'target_branch_name': {'key': 'targetBranchName', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, branch_name=None, build_definition_id=None, build_system=None, creation_date=None, flavor=None, id=None, number=None, platform=None, project=None, repository_guid=None, repository_id=None, repository_type=None, source_version=None, target_branch_name=None, uri=None):
        super(BuildConfiguration, self).__init__()
        self.branch_name = branch_name
        self.build_definition_id = build_definition_id
        self.build_system = build_system
        self.creation_date = creation_date
        self.flavor = flavor
        self.id = id
        self.number = number
        self.platform = platform
        self.project = project
        self.repository_guid = repository_guid
        self.repository_id = repository_id
        self.repository_type = repository_type
        self.source_version = source_version
        self.target_branch_name = target_branch_name
        self.uri = uri


class BuildCoverage(Model):

    _attribute_map = {
        'code_coverage_file_url': {'key': 'codeCoverageFileUrl', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'BuildConfiguration'},
        'last_error': {'key': 'lastError', 'type': 'str'},
        'modules': {'key': 'modules', 'type': '[ModuleCoverage]'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, code_coverage_file_url=None, configuration=None, last_error=None, modules=None, state=None):
        super(BuildCoverage, self).__init__()
        self.code_coverage_file_url = code_coverage_file_url
        self.configuration = configuration
        self.last_error = last_error
        self.modules = modules
        self.state = state


class BuildReference(Model):

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'build_system': {'key': 'buildSystem', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'int'},
        'number': {'key': 'number', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, branch_name=None, build_system=None, definition_id=None, id=None, number=None, repository_id=None, uri=None):
        super(BuildReference, self).__init__()
        self.branch_name = branch_name
        self.build_system = build_system
        self.definition_id = definition_id
        self.id = id
        self.number = number
        self.repository_id = repository_id
        self.uri = uri


class CodeCoverageData(Model):

    _attribute_map = {
        'build_flavor': {'key': 'buildFlavor', 'type': 'str'},
        'build_platform': {'key': 'buildPlatform', 'type': 'str'},
        'coverage_stats': {'key': 'coverageStats', 'type': '[CodeCoverageStatistics]'}
    }

    def __init__(self, build_flavor=None, build_platform=None, coverage_stats=None):
        super(CodeCoverageData, self).__init__()
        self.build_flavor = build_flavor
        self.build_platform = build_platform
        self.coverage_stats = coverage_stats


class CodeCoverageStatistics(Model):

    _attribute_map = {
        'covered': {'key': 'covered', 'type': 'int'},
        'delta': {'key': 'delta', 'type': 'float'},
        'is_delta_available': {'key': 'isDeltaAvailable', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'}
    }

    def __init__(self, covered=None, delta=None, is_delta_available=None, label=None, position=None, total=None):
        super(CodeCoverageStatistics, self).__init__()
        self.covered = covered
        self.delta = delta
        self.is_delta_available = is_delta_available
        self.label = label
        self.position = position
        self.total = total


class CodeCoverageSummary(Model):

    _attribute_map = {
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'coverage_data': {'key': 'coverageData', 'type': '[CodeCoverageData]'},
        'delta_build': {'key': 'deltaBuild', 'type': 'ShallowReference'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, build=None, coverage_data=None, delta_build=None, status=None):
        super(CodeCoverageSummary, self).__init__()
        self.build = build
        self.coverage_data = coverage_data
        self.delta_build = delta_build
        self.status = status


class CoverageStatistics(Model):

    _attribute_map = {
        'blocks_covered': {'key': 'blocksCovered', 'type': 'int'},
        'blocks_not_covered': {'key': 'blocksNotCovered', 'type': 'int'},
        'lines_covered': {'key': 'linesCovered', 'type': 'int'},
        'lines_not_covered': {'key': 'linesNotCovered', 'type': 'int'},
        'lines_partially_covered': {'key': 'linesPartiallyCovered', 'type': 'int'}
    }

    def __init__(self, blocks_covered=None, blocks_not_covered=None, lines_covered=None, lines_not_covered=None, lines_partially_covered=None):
        super(CoverageStatistics, self).__init__()
        self.blocks_covered = blocks_covered
        self.blocks_not_covered = blocks_not_covered
        self.lines_covered = lines_covered
        self.lines_not_covered = lines_not_covered
        self.lines_partially_covered = lines_partially_covered


class CustomTestField(Model):

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, field_name=None, value=None):
        super(CustomTestField, self).__init__()
        self.field_name = field_name
        self.value = value


class DtlEnvironmentDetails(Model):

    _attribute_map = {
        'csm_content': {'key': 'csmContent', 'type': 'str'},
        'csm_parameters': {'key': 'csmParameters', 'type': 'str'},
        'subscription_name': {'key': 'subscriptionName', 'type': 'str'}
    }

    def __init__(self, csm_content=None, csm_parameters=None, subscription_name=None):
        super(DtlEnvironmentDetails, self).__init__()
        self.csm_content = csm_content
        self.csm_parameters = csm_parameters
        self.subscription_name = subscription_name


class FailingSince(Model):

    _attribute_map = {
        'build': {'key': 'build', 'type': 'BuildReference'},
        'date': {'key': 'date', 'type': 'iso-8601'},
        'release': {'key': 'release', 'type': 'ReleaseReference'}
    }

    def __init__(self, build=None, date=None, release=None):
        super(FailingSince, self).__init__()
        self.build = build
        self.date = date
        self.release = release


class FieldDetailsForTestResults(Model):

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'groups_for_field': {'key': 'groupsForField', 'type': '[object]'}
    }

    def __init__(self, field_name=None, groups_for_field=None):
        super(FieldDetailsForTestResults, self).__init__()
        self.field_name = field_name
        self.groups_for_field = groups_for_field


class FileCoverageRequest(Model):

    _attribute_map = {
        'file_path': {'key': 'filePath', 'type': 'str'},
        'pull_request_base_iteration_id': {'key': 'pullRequestBaseIterationId', 'type': 'int'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'},
        'pull_request_iteration_id': {'key': 'pullRequestIterationId', 'type': 'int'},
        'repo_id': {'key': 'repoId', 'type': 'str'}
    }

    def __init__(self, file_path=None, pull_request_base_iteration_id=None, pull_request_id=None, pull_request_iteration_id=None, repo_id=None):
        super(FileCoverageRequest, self).__init__()
        self.file_path = file_path
        self.pull_request_base_iteration_id = pull_request_base_iteration_id
        self.pull_request_id = pull_request_id
        self.pull_request_iteration_id = pull_request_iteration_id
        self.repo_id = repo_id


class FlakyDetection(Model):

    _attribute_map = {
        'flaky_detection_pipelines': {'key': 'flakyDetectionPipelines', 'type': 'FlakyDetectionPipelines'},
        'flaky_detection_type': {'key': 'flakyDetectionType', 'type': 'object'}
    }

    def __init__(self, flaky_detection_pipelines=None, flaky_detection_type=None):
        super(FlakyDetection, self).__init__()
        self.flaky_detection_pipelines = flaky_detection_pipelines
        self.flaky_detection_type = flaky_detection_type


class FlakyDetectionPipelines(Model):

    _attribute_map = {
        'allowed_pipelines': {'key': 'allowedPipelines', 'type': '[int]'},
        'is_all_pipelines_allowed': {'key': 'isAllPipelinesAllowed', 'type': 'bool'}
    }

    def __init__(self, allowed_pipelines=None, is_all_pipelines_allowed=None):
        super(FlakyDetectionPipelines, self).__init__()
        self.allowed_pipelines = allowed_pipelines
        self.is_all_pipelines_allowed = is_all_pipelines_allowed


class FlakySettings(Model):

    _attribute_map = {
        'flaky_detection': {'key': 'flakyDetection', 'type': 'FlakyDetection'},
        'flaky_in_summary_report': {'key': 'flakyInSummaryReport', 'type': 'bool'},
        'is_flaky_bug_created': {'key': 'isFlakyBugCreated', 'type': 'bool'},
        'manual_mark_unmark_flaky': {'key': 'manualMarkUnmarkFlaky', 'type': 'bool'}
    }

    def __init__(self, flaky_detection=None, flaky_in_summary_report=None, is_flaky_bug_created=None, manual_mark_unmark_flaky=None):
        super(FlakySettings, self).__init__()
        self.flaky_detection = flaky_detection
        self.flaky_in_summary_report = flaky_in_summary_report
        self.is_flaky_bug_created = is_flaky_bug_created
        self.manual_mark_unmark_flaky = manual_mark_unmark_flaky


class FunctionCoverage(Model):

    _attribute_map = {
        'class_': {'key': 'class', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'source_file': {'key': 'sourceFile', 'type': 'str'},
        'statistics': {'key': 'statistics', 'type': 'CoverageStatistics'}
    }

    def __init__(self, class_=None, name=None, namespace=None, source_file=None, statistics=None):
        super(FunctionCoverage, self).__init__()
        self.class_ = class_
        self.name = name
        self.namespace = namespace
        self.source_file = source_file
        self.statistics = statistics


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


class JobReference(Model):

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'job_name': {'key': 'jobName', 'type': 'str'}
    }

    def __init__(self, attempt=None, job_name=None):
        super(JobReference, self).__init__()
        self.attempt = attempt
        self.job_name = job_name


class ModuleCoverage(Model):

    _attribute_map = {
        'block_count': {'key': 'blockCount', 'type': 'int'},
        'block_data': {'key': 'blockData', 'type': 'str'},
        'file_url': {'key': 'fileUrl', 'type': 'str'},
        'functions': {'key': 'functions', 'type': '[FunctionCoverage]'},
        'name': {'key': 'name', 'type': 'str'},
        'signature': {'key': 'signature', 'type': 'str'},
        'signature_age': {'key': 'signatureAge', 'type': 'int'},
        'statistics': {'key': 'statistics', 'type': 'CoverageStatistics'}
    }

    def __init__(self, block_count=None, block_data=None, file_url=None, functions=None, name=None, signature=None, signature_age=None, statistics=None):
        super(ModuleCoverage, self).__init__()
        self.block_count = block_count
        self.block_data = block_data
        self.file_url = file_url
        self.functions = functions
        self.name = name
        self.signature = signature
        self.signature_age = signature_age
        self.statistics = statistics


class NewTestResultLoggingSettings(Model):

    _attribute_map = {
        'log_new_tests': {'key': 'logNewTests', 'type': 'bool'}
    }

    def __init__(self, log_new_tests=None):
        super(NewTestResultLoggingSettings, self).__init__()
        self.log_new_tests = log_new_tests


class PhaseReference(Model):

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'phase_name': {'key': 'phaseName', 'type': 'str'}
    }

    def __init__(self, attempt=None, phase_name=None):
        super(PhaseReference, self).__init__()
        self.attempt = attempt
        self.phase_name = phase_name


class PipelineReference(Model):

    _attribute_map = {
        'job_reference': {'key': 'jobReference', 'type': 'JobReference'},
        'phase_reference': {'key': 'phaseReference', 'type': 'PhaseReference'},
        'pipeline_id': {'key': 'pipelineId', 'type': 'int'},
        'stage_reference': {'key': 'stageReference', 'type': 'StageReference'}
    }

    def __init__(self, job_reference=None, phase_reference=None, pipeline_id=None, stage_reference=None):
        super(PipelineReference, self).__init__()
        self.job_reference = job_reference
        self.phase_reference = phase_reference
        self.pipeline_id = pipeline_id
        self.stage_reference = stage_reference


class PipelineTestMetrics(Model):

    _attribute_map = {
        'current_context': {'key': 'currentContext', 'type': 'PipelineReference'},
        'results_analysis': {'key': 'resultsAnalysis', 'type': 'ResultsAnalysis'},
        'result_summary': {'key': 'resultSummary', 'type': 'ResultSummary'},
        'run_summary': {'key': 'runSummary', 'type': 'RunSummary'},
        'summary_at_child': {'key': 'summaryAtChild', 'type': '[PipelineTestMetrics]'}
    }

    def __init__(self, current_context=None, results_analysis=None, result_summary=None, run_summary=None, summary_at_child=None):
        super(PipelineTestMetrics, self).__init__()
        self.current_context = current_context
        self.results_analysis = results_analysis
        self.result_summary = result_summary
        self.run_summary = run_summary
        self.summary_at_child = summary_at_child


class QueryModel(Model):

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'}
    }

    def __init__(self, query=None):
        super(QueryModel, self).__init__()
        self.query = query


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ReleaseReference(Model):

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'environment_creation_date': {'key': 'environmentCreationDate', 'type': 'iso-8601'},
        'environment_definition_id': {'key': 'environmentDefinitionId', 'type': 'int'},
        'environment_definition_name': {'key': 'environmentDefinitionName', 'type': 'str'},
        'environment_id': {'key': 'environmentId', 'type': 'int'},
        'environment_name': {'key': 'environmentName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, attempt=None, creation_date=None, definition_id=None, environment_creation_date=None, environment_definition_id=None, environment_definition_name=None, environment_id=None, environment_name=None, id=None, name=None):
        super(ReleaseReference, self).__init__()
        self.attempt = attempt
        self.creation_date = creation_date
        self.definition_id = definition_id
        self.environment_creation_date = environment_creation_date
        self.environment_definition_id = environment_definition_id
        self.environment_definition_name = environment_definition_name
        self.environment_id = environment_id
        self.environment_name = environment_name
        self.id = id
        self.name = name


class ResultsAnalysis(Model):

    _attribute_map = {
        'previous_context': {'key': 'previousContext', 'type': 'PipelineReference'},
        'results_difference': {'key': 'resultsDifference', 'type': 'AggregatedResultsDifference'},
        'test_failures_analysis': {'key': 'testFailuresAnalysis', 'type': 'TestResultFailuresAnalysis'}
    }

    def __init__(self, previous_context=None, results_difference=None, test_failures_analysis=None):
        super(ResultsAnalysis, self).__init__()
        self.previous_context = previous_context
        self.results_difference = results_difference
        self.test_failures_analysis = test_failures_analysis


class ResultsFilter(Model):

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'branch': {'key': 'branch', 'type': 'str'},
        'executed_in': {'key': 'executedIn', 'type': 'object'},
        'group_by': {'key': 'groupBy', 'type': 'str'},
        'max_complete_date': {'key': 'maxCompleteDate', 'type': 'iso-8601'},
        'results_count': {'key': 'resultsCount', 'type': 'int'},
        'test_case_id': {'key': 'testCaseId', 'type': 'int'},
        'test_case_reference_ids': {'key': 'testCaseReferenceIds', 'type': '[int]'},
        'test_plan_id': {'key': 'testPlanId', 'type': 'int'},
        'test_point_ids': {'key': 'testPointIds', 'type': '[int]'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'},
        'trend_days': {'key': 'trendDays', 'type': 'int'}
    }

    def __init__(self, automated_test_name=None, branch=None, executed_in=None, group_by=None, max_complete_date=None, results_count=None, test_case_id=None, test_case_reference_ids=None, test_plan_id=None, test_point_ids=None, test_results_context=None, trend_days=None):
        super(ResultsFilter, self).__init__()
        self.automated_test_name = automated_test_name
        self.branch = branch
        self.executed_in = executed_in
        self.group_by = group_by
        self.max_complete_date = max_complete_date
        self.results_count = results_count
        self.test_case_id = test_case_id
        self.test_case_reference_ids = test_case_reference_ids
        self.test_plan_id = test_plan_id
        self.test_point_ids = test_point_ids
        self.test_results_context = test_results_context
        self.trend_days = trend_days


class ResultsSummaryByOutcome(Model):

    _attribute_map = {
        'aggregated_result_details_by_outcome': {'key': 'aggregatedResultDetailsByOutcome', 'type': '{AggregatedResultDetailsByOutcome}'},
        'duration': {'key': 'duration', 'type': 'object'},
        'not_reported_test_count': {'key': 'notReportedTestCount', 'type': 'int'},
        'total_test_count': {'key': 'totalTestCount', 'type': 'int'}
    }

    def __init__(self, aggregated_result_details_by_outcome=None, duration=None, not_reported_test_count=None, total_test_count=None):
        super(ResultsSummaryByOutcome, self).__init__()
        self.aggregated_result_details_by_outcome = aggregated_result_details_by_outcome
        self.duration = duration
        self.not_reported_test_count = not_reported_test_count
        self.total_test_count = total_test_count


class ResultSummary(Model):

    _attribute_map = {
        'result_summary_by_run_state': {'key': 'resultSummaryByRunState', 'type': '{ResultsSummaryByOutcome}'}
    }

    def __init__(self, result_summary_by_run_state=None):
        super(ResultSummary, self).__init__()
        self.result_summary_by_run_state = result_summary_by_run_state


class RunCreateModel(Model):

    _attribute_map = {
        'automated': {'key': 'automated', 'type': 'bool'},
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_drop_location': {'key': 'buildDropLocation', 'type': 'str'},
        'build_flavor': {'key': 'buildFlavor', 'type': 'str'},
        'build_platform': {'key': 'buildPlatform', 'type': 'str'},
        'build_reference': {'key': 'buildReference', 'type': 'BuildConfiguration'},
        'comment': {'key': 'comment', 'type': 'str'},
        'complete_date': {'key': 'completeDate', 'type': 'str'},
        'configuration_ids': {'key': 'configurationIds', 'type': '[int]'},
        'controller': {'key': 'controller', 'type': 'str'},
        'custom_test_fields': {'key': 'customTestFields', 'type': '[CustomTestField]'},
        'dtl_aut_environment': {'key': 'dtlAutEnvironment', 'type': 'ShallowReference'},
        'dtl_test_environment': {'key': 'dtlTestEnvironment', 'type': 'ShallowReference'},
        'due_date': {'key': 'dueDate', 'type': 'str'},
        'environment_details': {'key': 'environmentDetails', 'type': 'DtlEnvironmentDetails'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'RunFilter'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'pipeline_reference': {'key': 'pipelineReference', 'type': 'PipelineReference'},
        'plan': {'key': 'plan', 'type': 'ShallowReference'},
        'point_ids': {'key': 'pointIds', 'type': '[int]'},
        'release_environment_uri': {'key': 'releaseEnvironmentUri', 'type': 'str'},
        'release_reference': {'key': 'releaseReference', 'type': 'ReleaseReference'},
        'release_uri': {'key': 'releaseUri', 'type': 'str'},
        'run_summary': {'key': 'runSummary', 'type': '[RunSummaryModel]'},
        'run_timeout': {'key': 'runTimeout', 'type': 'object'},
        'source_workflow': {'key': 'sourceWorkflow', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[TestTag]'},
        'test_configurations_mapping': {'key': 'testConfigurationsMapping', 'type': 'str'},
        'test_environment_id': {'key': 'testEnvironmentId', 'type': 'str'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, automated=None, build=None, build_drop_location=None, build_flavor=None, build_platform=None, build_reference=None, comment=None, complete_date=None, configuration_ids=None, controller=None, custom_test_fields=None, dtl_aut_environment=None, dtl_test_environment=None, due_date=None, environment_details=None, error_message=None, filter=None, iteration=None, name=None, owner=None, pipeline_reference=None, plan=None, point_ids=None, release_environment_uri=None, release_reference=None, release_uri=None, run_summary=None, run_timeout=None, source_workflow=None, start_date=None, state=None, tags=None, test_configurations_mapping=None, test_environment_id=None, test_settings=None, type=None):
        super(RunCreateModel, self).__init__()
        self.automated = automated
        self.build = build
        self.build_drop_location = build_drop_location
        self.build_flavor = build_flavor
        self.build_platform = build_platform
        self.build_reference = build_reference
        self.comment = comment
        self.complete_date = complete_date
        self.configuration_ids = configuration_ids
        self.controller = controller
        self.custom_test_fields = custom_test_fields
        self.dtl_aut_environment = dtl_aut_environment
        self.dtl_test_environment = dtl_test_environment
        self.due_date = due_date
        self.environment_details = environment_details
        self.error_message = error_message
        self.filter = filter
        self.iteration = iteration
        self.name = name
        self.owner = owner
        self.pipeline_reference = pipeline_reference
        self.plan = plan
        self.point_ids = point_ids
        self.release_environment_uri = release_environment_uri
        self.release_reference = release_reference
        self.release_uri = release_uri
        self.run_summary = run_summary
        self.run_timeout = run_timeout
        self.source_workflow = source_workflow
        self.start_date = start_date
        self.state = state
        self.tags = tags
        self.test_configurations_mapping = test_configurations_mapping
        self.test_environment_id = test_environment_id
        self.test_settings = test_settings
        self.type = type


class RunFilter(Model):

    _attribute_map = {
        'source_filter': {'key': 'sourceFilter', 'type': 'str'},
        'test_case_filter': {'key': 'testCaseFilter', 'type': 'str'}
    }

    def __init__(self, source_filter=None, test_case_filter=None):
        super(RunFilter, self).__init__()
        self.source_filter = source_filter
        self.test_case_filter = test_case_filter


class RunStatistic(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'resolution_state': {'key': 'resolutionState', 'type': 'TestResolutionState'},
        'result_metadata': {'key': 'resultMetadata', 'type': 'object'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, count=None, outcome=None, resolution_state=None, result_metadata=None, state=None):
        super(RunStatistic, self).__init__()
        self.count = count
        self.outcome = outcome
        self.resolution_state = resolution_state
        self.result_metadata = result_metadata
        self.state = state


class RunSummary(Model):

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'object'},
        'no_config_runs_count': {'key': 'noConfigRunsCount', 'type': 'int'},
        'run_summary_by_outcome': {'key': 'runSummaryByOutcome', 'type': '{int}'},
        'run_summary_by_state': {'key': 'runSummaryByState', 'type': '{int}'},
        'total_runs_count': {'key': 'totalRunsCount', 'type': 'int'}
    }

    def __init__(self, duration=None, no_config_runs_count=None, run_summary_by_outcome=None, run_summary_by_state=None, total_runs_count=None):
        super(RunSummary, self).__init__()
        self.duration = duration
        self.no_config_runs_count = no_config_runs_count
        self.run_summary_by_outcome = run_summary_by_outcome
        self.run_summary_by_state = run_summary_by_state
        self.total_runs_count = total_runs_count


class RunSummaryModel(Model):

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'long'},
        'result_count': {'key': 'resultCount', 'type': 'int'},
        'test_outcome': {'key': 'testOutcome', 'type': 'object'}
    }

    def __init__(self, duration=None, result_count=None, test_outcome=None):
        super(RunSummaryModel, self).__init__()
        self.duration = duration
        self.result_count = result_count
        self.test_outcome = test_outcome


class RunUpdateModel(Model):

    _attribute_map = {
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_drop_location': {'key': 'buildDropLocation', 'type': 'str'},
        'build_flavor': {'key': 'buildFlavor', 'type': 'str'},
        'build_platform': {'key': 'buildPlatform', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'str'},
        'controller': {'key': 'controller', 'type': 'str'},
        'delete_in_progress_results': {'key': 'deleteInProgressResults', 'type': 'bool'},
        'dtl_aut_environment': {'key': 'dtlAutEnvironment', 'type': 'ShallowReference'},
        'dtl_environment': {'key': 'dtlEnvironment', 'type': 'ShallowReference'},
        'dtl_environment_details': {'key': 'dtlEnvironmentDetails', 'type': 'DtlEnvironmentDetails'},
        'due_date': {'key': 'dueDate', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'log_entries': {'key': 'logEntries', 'type': '[TestMessageLogDetails]'},
        'name': {'key': 'name', 'type': 'str'},
        'release_environment_uri': {'key': 'releaseEnvironmentUri', 'type': 'str'},
        'release_uri': {'key': 'releaseUri', 'type': 'str'},
        'run_summary': {'key': 'runSummary', 'type': '[RunSummaryModel]'},
        'source_workflow': {'key': 'sourceWorkflow', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'substate': {'key': 'substate', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[TestTag]'},
        'test_environment_id': {'key': 'testEnvironmentId', 'type': 'str'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'}
    }

    def __init__(self, build=None, build_drop_location=None, build_flavor=None, build_platform=None, comment=None, completed_date=None, controller=None, delete_in_progress_results=None, dtl_aut_environment=None, dtl_environment=None, dtl_environment_details=None, due_date=None, error_message=None, iteration=None, log_entries=None, name=None, release_environment_uri=None, release_uri=None, run_summary=None, source_workflow=None, started_date=None, state=None, substate=None, tags=None, test_environment_id=None, test_settings=None):
        super(RunUpdateModel, self).__init__()
        self.build = build
        self.build_drop_location = build_drop_location
        self.build_flavor = build_flavor
        self.build_platform = build_platform
        self.comment = comment
        self.completed_date = completed_date
        self.controller = controller
        self.delete_in_progress_results = delete_in_progress_results
        self.dtl_aut_environment = dtl_aut_environment
        self.dtl_environment = dtl_environment
        self.dtl_environment_details = dtl_environment_details
        self.due_date = due_date
        self.error_message = error_message
        self.iteration = iteration
        self.log_entries = log_entries
        self.name = name
        self.release_environment_uri = release_environment_uri
        self.release_uri = release_uri
        self.run_summary = run_summary
        self.source_workflow = source_workflow
        self.started_date = started_date
        self.state = state
        self.substate = substate
        self.tags = tags
        self.test_environment_id = test_environment_id
        self.test_settings = test_settings


class ShallowReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(ShallowReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class ShallowTestCaseResult(Model):

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'automated_test_storage': {'key': 'automatedTestStorage', 'type': 'str'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'id': {'key': 'id', 'type': 'int'},
        'is_re_run': {'key': 'isReRun', 'type': 'bool'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'ref_id': {'key': 'refId', 'type': 'int'},
        'run_id': {'key': 'runId', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'test_case_title': {'key': 'testCaseTitle', 'type': 'str'}
    }

    def __init__(self, automated_test_name=None, automated_test_storage=None, duration_in_ms=None, id=None, is_re_run=None, outcome=None, owner=None, priority=None, ref_id=None, run_id=None, tags=None, test_case_title=None):
        super(ShallowTestCaseResult, self).__init__()
        self.automated_test_name = automated_test_name
        self.automated_test_storage = automated_test_storage
        self.duration_in_ms = duration_in_ms
        self.id = id
        self.is_re_run = is_re_run
        self.outcome = outcome
        self.owner = owner
        self.priority = priority
        self.ref_id = ref_id
        self.run_id = run_id
        self.tags = tags
        self.test_case_title = test_case_title


class SharedStepModel(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, id=None, revision=None):
        super(SharedStepModel, self).__init__()
        self.id = id
        self.revision = revision


class StageReference(Model):

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'stage_name': {'key': 'stageName', 'type': 'str'}
    }

    def __init__(self, attempt=None, stage_name=None):
        super(StageReference, self).__init__()
        self.attempt = attempt
        self.stage_name = stage_name


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


class TestAttachment(Model):

    _attribute_map = {
        'attachment_type': {'key': 'attachmentType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, attachment_type=None, comment=None, created_date=None, file_name=None, id=None, size=None, url=None):
        super(TestAttachment, self).__init__()
        self.attachment_type = attachment_type
        self.comment = comment
        self.created_date = created_date
        self.file_name = file_name
        self.id = id
        self.size = size
        self.url = url


class TestAttachmentReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(TestAttachmentReference, self).__init__()
        self.id = id
        self.url = url


class TestAttachmentRequestModel(Model):

    _attribute_map = {
        'attachment_type': {'key': 'attachmentType', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'stream': {'key': 'stream', 'type': 'str'}
    }

    def __init__(self, attachment_type=None, comment=None, file_name=None, stream=None):
        super(TestAttachmentRequestModel, self).__init__()
        self.attachment_type = attachment_type
        self.comment = comment
        self.file_name = file_name
        self.stream = stream


class TestCaseResult(Model):

    _attribute_map = {
        'afn_strip_id': {'key': 'afnStripId', 'type': 'int'},
        'area': {'key': 'area', 'type': 'ShallowReference'},
        'associated_bugs': {'key': 'associatedBugs', 'type': '[ShallowReference]'},
        'automated_test_id': {'key': 'automatedTestId', 'type': 'str'},
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'automated_test_storage': {'key': 'automatedTestStorage', 'type': 'str'},
        'automated_test_type': {'key': 'automatedTestType', 'type': 'str'},
        'automated_test_type_id': {'key': 'automatedTestTypeId', 'type': 'str'},
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_reference': {'key': 'buildReference', 'type': 'BuildReference'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'computer_name': {'key': 'computerName', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'ShallowReference'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'custom_fields': {'key': 'customFields', 'type': '[CustomTestField]'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'failing_since': {'key': 'failingSince', 'type': 'FailingSince'},
        'failure_type': {'key': 'failureType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'iteration_details': {'key': 'iterationDetails', 'type': '[TestIterationDetailsModel]'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'priority': {'key': 'priority', 'type': 'int'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'release': {'key': 'release', 'type': 'ShallowReference'},
        'release_reference': {'key': 'releaseReference', 'type': 'ReleaseReference'},
        'reset_count': {'key': 'resetCount', 'type': 'int'},
        'resolution_state': {'key': 'resolutionState', 'type': 'str'},
        'resolution_state_id': {'key': 'resolutionStateId', 'type': 'int'},
        'result_group_type': {'key': 'resultGroupType', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'sub_results': {'key': 'subResults', 'type': '[TestSubResult]'},
        'test_case': {'key': 'testCase', 'type': 'ShallowReference'},
        'test_case_reference_id': {'key': 'testCaseReferenceId', 'type': 'int'},
        'test_case_revision': {'key': 'testCaseRevision', 'type': 'int'},
        'test_case_title': {'key': 'testCaseTitle', 'type': 'str'},
        'test_plan': {'key': 'testPlan', 'type': 'ShallowReference'},
        'test_point': {'key': 'testPoint', 'type': 'ShallowReference'},
        'test_run': {'key': 'testRun', 'type': 'ShallowReference'},
        'test_suite': {'key': 'testSuite', 'type': 'ShallowReference'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, afn_strip_id=None, area=None, associated_bugs=None, automated_test_id=None, automated_test_name=None, automated_test_storage=None, automated_test_type=None, automated_test_type_id=None, build=None, build_reference=None, comment=None, completed_date=None, computer_name=None, configuration=None, created_date=None, custom_fields=None, duration_in_ms=None, error_message=None, failing_since=None, failure_type=None, id=None, iteration_details=None, last_updated_by=None, last_updated_date=None, outcome=None, owner=None, priority=None, project=None, release=None, release_reference=None, reset_count=None, resolution_state=None, resolution_state_id=None, result_group_type=None, revision=None, run_by=None, stack_trace=None, started_date=None, state=None, sub_results=None, test_case=None, test_case_reference_id=None, test_case_revision=None, test_case_title=None, test_plan=None, test_point=None, test_run=None, test_suite=None, url=None):
        super(TestCaseResult, self).__init__()
        self.afn_strip_id = afn_strip_id
        self.area = area
        self.associated_bugs = associated_bugs
        self.automated_test_id = automated_test_id
        self.automated_test_name = automated_test_name
        self.automated_test_storage = automated_test_storage
        self.automated_test_type = automated_test_type
        self.automated_test_type_id = automated_test_type_id
        self.build = build
        self.build_reference = build_reference
        self.comment = comment
        self.completed_date = completed_date
        self.computer_name = computer_name
        self.configuration = configuration
        self.created_date = created_date
        self.custom_fields = custom_fields
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.failing_since = failing_since
        self.failure_type = failure_type
        self.id = id
        self.iteration_details = iteration_details
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.outcome = outcome
        self.owner = owner
        self.priority = priority
        self.project = project
        self.release = release
        self.release_reference = release_reference
        self.reset_count = reset_count
        self.resolution_state = resolution_state
        self.resolution_state_id = resolution_state_id
        self.result_group_type = result_group_type
        self.revision = revision
        self.run_by = run_by
        self.stack_trace = stack_trace
        self.started_date = started_date
        self.state = state
        self.sub_results = sub_results
        self.test_case = test_case
        self.test_case_reference_id = test_case_reference_id
        self.test_case_revision = test_case_revision
        self.test_case_title = test_case_title
        self.test_plan = test_plan
        self.test_point = test_point
        self.test_run = test_run
        self.test_suite = test_suite
        self.url = url


class TestCaseResultAttachmentModel(Model):

    _attribute_map = {
        'action_path': {'key': 'actionPath', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, action_path=None, id=None, iteration_id=None, name=None, size=None, url=None):
        super(TestCaseResultAttachmentModel, self).__init__()
        self.action_path = action_path
        self.id = id
        self.iteration_id = iteration_id
        self.name = name
        self.size = size
        self.url = url


class TestCaseResultIdentifier(Model):

    _attribute_map = {
        'test_result_id': {'key': 'testResultId', 'type': 'int'},
        'test_run_id': {'key': 'testRunId', 'type': 'int'}
    }

    def __init__(self, test_result_id=None, test_run_id=None):
        super(TestCaseResultIdentifier, self).__init__()
        self.test_result_id = test_result_id
        self.test_run_id = test_run_id


class TestEnvironment(Model):

    _attribute_map = {
        'environment_id': {'key': 'environmentId', 'type': 'str'},
        'environment_name': {'key': 'environmentName', 'type': 'str'}
    }

    def __init__(self, environment_id=None, environment_name=None):
        super(TestEnvironment, self).__init__()
        self.environment_id = environment_id
        self.environment_name = environment_name


class TestFailureDetails(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'test_results': {'key': 'testResults', 'type': '[TestCaseResultIdentifier]'}
    }

    def __init__(self, count=None, test_results=None):
        super(TestFailureDetails, self).__init__()
        self.count = count
        self.test_results = test_results


class TestFailuresAnalysis(Model):

    _attribute_map = {
        'existing_failures': {'key': 'existingFailures', 'type': 'TestFailureDetails'},
        'fixed_tests': {'key': 'fixedTests', 'type': 'TestFailureDetails'},
        'new_failures': {'key': 'newFailures', 'type': 'TestFailureDetails'},
        'previous_context': {'key': 'previousContext', 'type': 'TestResultsContext'}
    }

    def __init__(self, existing_failures=None, fixed_tests=None, new_failures=None, previous_context=None):
        super(TestFailuresAnalysis, self).__init__()
        self.existing_failures = existing_failures
        self.fixed_tests = fixed_tests
        self.new_failures = new_failures
        self.previous_context = previous_context


class TestFlakyIdentifier(Model):

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'is_flaky': {'key': 'isFlaky', 'type': 'bool'}
    }

    def __init__(self, branch_name=None, is_flaky=None):
        super(TestFlakyIdentifier, self).__init__()
        self.branch_name = branch_name
        self.is_flaky = is_flaky


class TestHistoryQuery(Model):

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'branch': {'key': 'branch', 'type': 'str'},
        'build_definition_id': {'key': 'buildDefinitionId', 'type': 'int'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'group_by': {'key': 'groupBy', 'type': 'object'},
        'max_complete_date': {'key': 'maxCompleteDate', 'type': 'iso-8601'},
        'release_env_definition_id': {'key': 'releaseEnvDefinitionId', 'type': 'int'},
        'results_for_group': {'key': 'resultsForGroup', 'type': '[TestResultHistoryForGroup]'},
        'test_case_id': {'key': 'testCaseId', 'type': 'int'},
        'trend_days': {'key': 'trendDays', 'type': 'int'}
    }

    def __init__(self, automated_test_name=None, branch=None, build_definition_id=None, continuation_token=None, group_by=None, max_complete_date=None, release_env_definition_id=None, results_for_group=None, test_case_id=None, trend_days=None):
        super(TestHistoryQuery, self).__init__()
        self.automated_test_name = automated_test_name
        self.branch = branch
        self.build_definition_id = build_definition_id
        self.continuation_token = continuation_token
        self.group_by = group_by
        self.max_complete_date = max_complete_date
        self.release_env_definition_id = release_env_definition_id
        self.results_for_group = results_for_group
        self.test_case_id = test_case_id
        self.trend_days = trend_days


class TestIterationDetailsModel(Model):

    _attribute_map = {
        'action_results': {'key': 'actionResults', 'type': '[TestActionResultModel]'},
        'attachments': {'key': 'attachments', 'type': '[TestCaseResultAttachmentModel]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[TestResultParameterModel]'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, action_results=None, attachments=None, comment=None, completed_date=None, duration_in_ms=None, error_message=None, id=None, outcome=None, parameters=None, started_date=None, url=None):
        super(TestIterationDetailsModel, self).__init__()
        self.action_results = action_results
        self.attachments = attachments
        self.comment = comment
        self.completed_date = completed_date
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.id = id
        self.outcome = outcome
        self.parameters = parameters
        self.started_date = started_date
        self.url = url


class TestLog(Model):

    _attribute_map = {
        'log_reference': {'key': 'logReference', 'type': 'TestLogReference'},
        'meta_data': {'key': 'metaData', 'type': '{str}'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'size': {'key': 'size', 'type': 'long'}
    }

    def __init__(self, log_reference=None, meta_data=None, modified_on=None, size=None):
        super(TestLog, self).__init__()
        self.log_reference = log_reference
        self.meta_data = meta_data
        self.modified_on = modified_on
        self.size = size


class TestLogReference(Model):

    _attribute_map = {
        'build_id': {'key': 'buildId', 'type': 'int'},
        'file_path': {'key': 'filePath', 'type': 'str'},
        'release_env_id': {'key': 'releaseEnvId', 'type': 'int'},
        'release_id': {'key': 'releaseId', 'type': 'int'},
        'result_id': {'key': 'resultId', 'type': 'int'},
        'run_id': {'key': 'runId', 'type': 'int'},
        'scope': {'key': 'scope', 'type': 'object'},
        'sub_result_id': {'key': 'subResultId', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, build_id=None, file_path=None, release_env_id=None, release_id=None, result_id=None, run_id=None, scope=None, sub_result_id=None, type=None):
        super(TestLogReference, self).__init__()
        self.build_id = build_id
        self.file_path = file_path
        self.release_env_id = release_env_id
        self.release_id = release_id
        self.result_id = result_id
        self.run_id = run_id
        self.scope = scope
        self.sub_result_id = sub_result_id
        self.type = type


class TestLogStoreEndpointDetails(Model):

    _attribute_map = {
        'endpoint_sASUri': {'key': 'endpointSASUri', 'type': 'str'},
        'endpoint_type': {'key': 'endpointType', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, endpoint_sASUri=None, endpoint_type=None, status=None):
        super(TestLogStoreEndpointDetails, self).__init__()
        self.endpoint_sASUri = endpoint_sASUri
        self.endpoint_type = endpoint_type
        self.status = status


class TestMessageLogDetails(Model):

    _attribute_map = {
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'entry_id': {'key': 'entryId', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, date_created=None, entry_id=None, message=None):
        super(TestMessageLogDetails, self).__init__()
        self.date_created = date_created
        self.entry_id = entry_id
        self.message = message


class TestMethod(Model):

    _attribute_map = {
        'container': {'key': 'container', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, container=None, name=None):
        super(TestMethod, self).__init__()
        self.container = container
        self.name = name


class TestOperationReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, status=None, url=None):
        super(TestOperationReference, self).__init__()
        self.id = id
        self.status = status
        self.url = url


class TestResolutionState(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'}
    }

    def __init__(self, id=None, name=None, project=None):
        super(TestResolutionState, self).__init__()
        self.id = id
        self.name = name
        self.project = project


class TestResultDocument(Model):

    _attribute_map = {
        'operation_reference': {'key': 'operationReference', 'type': 'TestOperationReference'},
        'payload': {'key': 'payload', 'type': 'TestResultPayload'}
    }

    def __init__(self, operation_reference=None, payload=None):
        super(TestResultDocument, self).__init__()
        self.operation_reference = operation_reference
        self.payload = payload


class TestResultFailuresAnalysis(Model):

    _attribute_map = {
        'existing_failures': {'key': 'existingFailures', 'type': 'TestFailureDetails'},
        'fixed_tests': {'key': 'fixedTests', 'type': 'TestFailureDetails'},
        'new_failures': {'key': 'newFailures', 'type': 'TestFailureDetails'}
    }

    def __init__(self, existing_failures=None, fixed_tests=None, new_failures=None):
        super(TestResultFailuresAnalysis, self).__init__()
        self.existing_failures = existing_failures
        self.fixed_tests = fixed_tests
        self.new_failures = new_failures


class TestResultHistory(Model):

    _attribute_map = {
        'group_by_field': {'key': 'groupByField', 'type': 'str'},
        'results_for_group': {'key': 'resultsForGroup', 'type': '[TestResultHistoryDetailsForGroup]'}
    }

    def __init__(self, group_by_field=None, results_for_group=None):
        super(TestResultHistory, self).__init__()
        self.group_by_field = group_by_field
        self.results_for_group = results_for_group


class TestResultHistoryDetailsForGroup(Model):

    _attribute_map = {
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'latest_result': {'key': 'latestResult', 'type': 'TestCaseResult'}
    }

    def __init__(self, group_by_value=None, latest_result=None):
        super(TestResultHistoryDetailsForGroup, self).__init__()
        self.group_by_value = group_by_value
        self.latest_result = latest_result


class TestResultHistoryForGroup(Model):

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'group_by_value': {'key': 'groupByValue', 'type': 'str'},
        'results': {'key': 'results', 'type': '[TestCaseResult]'}
    }

    def __init__(self, display_name=None, group_by_value=None, results=None):
        super(TestResultHistoryForGroup, self).__init__()
        self.display_name = display_name
        self.group_by_value = group_by_value
        self.results = results


class TestResultMetaData(Model):

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'automated_test_storage': {'key': 'automatedTestStorage', 'type': 'str'},
        'flaky_identifiers': {'key': 'flakyIdentifiers', 'type': '[TestFlakyIdentifier]'},
        'owner': {'key': 'owner', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'test_case_reference_id': {'key': 'testCaseReferenceId', 'type': 'int'},
        'test_case_title': {'key': 'testCaseTitle', 'type': 'str'}
    }

    def __init__(self, automated_test_name=None, automated_test_storage=None, flaky_identifiers=None, owner=None, priority=None, test_case_reference_id=None, test_case_title=None):
        super(TestResultMetaData, self).__init__()
        self.automated_test_name = automated_test_name
        self.automated_test_storage = automated_test_storage
        self.flaky_identifiers = flaky_identifiers
        self.owner = owner
        self.priority = priority
        self.test_case_reference_id = test_case_reference_id
        self.test_case_title = test_case_title


class TestResultMetaDataUpdateInput(Model):

    _attribute_map = {
        'flaky_identifiers': {'key': 'flakyIdentifiers', 'type': '[TestFlakyIdentifier]'}
    }

    def __init__(self, flaky_identifiers=None):
        super(TestResultMetaDataUpdateInput, self).__init__()
        self.flaky_identifiers = flaky_identifiers


class TestResultModelBase(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'}
    }

    def __init__(self, comment=None, completed_date=None, duration_in_ms=None, error_message=None, outcome=None, started_date=None):
        super(TestResultModelBase, self).__init__()
        self.comment = comment
        self.completed_date = completed_date
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.outcome = outcome
        self.started_date = started_date


class TestResultParameterModel(Model):

    _attribute_map = {
        'action_path': {'key': 'actionPath', 'type': 'str'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'parameter_name': {'key': 'parameterName', 'type': 'str'},
        'step_identifier': {'key': 'stepIdentifier', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, action_path=None, iteration_id=None, parameter_name=None, step_identifier=None, url=None, value=None):
        super(TestResultParameterModel, self).__init__()
        self.action_path = action_path
        self.iteration_id = iteration_id
        self.parameter_name = parameter_name
        self.step_identifier = step_identifier
        self.url = url
        self.value = value


class TestResultPayload(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'stream': {'key': 'stream', 'type': 'str'}
    }

    def __init__(self, comment=None, name=None, stream=None):
        super(TestResultPayload, self).__init__()
        self.comment = comment
        self.name = name
        self.stream = stream


class TestResultsContext(Model):

    _attribute_map = {
        'build': {'key': 'build', 'type': 'BuildReference'},
        'context_type': {'key': 'contextType', 'type': 'object'},
        'pipeline_reference': {'key': 'pipelineReference', 'type': 'PipelineReference'},
        'release': {'key': 'release', 'type': 'ReleaseReference'}
    }

    def __init__(self, build=None, context_type=None, pipeline_reference=None, release=None):
        super(TestResultsContext, self).__init__()
        self.build = build
        self.context_type = context_type
        self.pipeline_reference = pipeline_reference
        self.release = release


class TestResultsDetails(Model):

    _attribute_map = {
        'group_by_field': {'key': 'groupByField', 'type': 'str'},
        'results_for_group': {'key': 'resultsForGroup', 'type': '[TestResultsDetailsForGroup]'}
    }

    def __init__(self, group_by_field=None, results_for_group=None):
        super(TestResultsDetails, self).__init__()
        self.group_by_field = group_by_field
        self.results_for_group = results_for_group


class TestResultsDetailsForGroup(Model):

    _attribute_map = {
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'results': {'key': 'results', 'type': '[TestCaseResult]'},
        'results_count_by_outcome': {'key': 'resultsCountByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, group_by_value=None, results=None, results_count_by_outcome=None, tags=None):
        super(TestResultsDetailsForGroup, self).__init__()
        self.group_by_value = group_by_value
        self.results = results
        self.results_count_by_outcome = results_count_by_outcome
        self.tags = tags


class TestResultsQuery(Model):

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '[str]'},
        'results': {'key': 'results', 'type': '[TestCaseResult]'},
        'results_filter': {'key': 'resultsFilter', 'type': 'ResultsFilter'}
    }

    def __init__(self, fields=None, results=None, results_filter=None):
        super(TestResultsQuery, self).__init__()
        self.fields = fields
        self.results = results
        self.results_filter = results_filter


class TestResultsSettings(Model):

    _attribute_map = {
        'flaky_settings': {'key': 'flakySettings', 'type': 'FlakySettings'},
        'new_test_result_logging_settings': {'key': 'newTestResultLoggingSettings', 'type': 'NewTestResultLoggingSettings'}
    }

    def __init__(self, flaky_settings=None, new_test_result_logging_settings=None):
        super(TestResultsSettings, self).__init__()
        self.flaky_settings = flaky_settings
        self.new_test_result_logging_settings = new_test_result_logging_settings


class TestResultSummary(Model):

    _attribute_map = {
        'aggregated_results_analysis': {'key': 'aggregatedResultsAnalysis', 'type': 'AggregatedResultsAnalysis'},
        'no_config_runs_count': {'key': 'noConfigRunsCount', 'type': 'int'},
        'team_project': {'key': 'teamProject', 'type': 'TeamProjectReference'},
        'test_failures': {'key': 'testFailures', 'type': 'TestFailuresAnalysis'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'},
        'total_runs_count': {'key': 'totalRunsCount', 'type': 'int'}
    }

    def __init__(self, aggregated_results_analysis=None, no_config_runs_count=None, team_project=None, test_failures=None, test_results_context=None, total_runs_count=None):
        super(TestResultSummary, self).__init__()
        self.aggregated_results_analysis = aggregated_results_analysis
        self.no_config_runs_count = no_config_runs_count
        self.team_project = team_project
        self.test_failures = test_failures
        self.test_results_context = test_results_context
        self.total_runs_count = total_runs_count


class TestResultsUpdateSettings(Model):

    _attribute_map = {
        'flaky_settings': {'key': 'flakySettings', 'type': 'FlakySettings'},
        'new_test_result_logging_settings': {'key': 'newTestResultLoggingSettings', 'type': 'NewTestResultLoggingSettings'}
    }

    def __init__(self, flaky_settings=None, new_test_result_logging_settings=None):
        super(TestResultsUpdateSettings, self).__init__()
        self.flaky_settings = flaky_settings
        self.new_test_result_logging_settings = new_test_result_logging_settings


class TestResultTrendFilter(Model):

    _attribute_map = {
        'branch_names': {'key': 'branchNames', 'type': '[str]'},
        'build_count': {'key': 'buildCount', 'type': 'int'},
        'definition_ids': {'key': 'definitionIds', 'type': '[int]'},
        'env_definition_ids': {'key': 'envDefinitionIds', 'type': '[int]'},
        'max_complete_date': {'key': 'maxCompleteDate', 'type': 'iso-8601'},
        'publish_context': {'key': 'publishContext', 'type': 'str'},
        'test_run_titles': {'key': 'testRunTitles', 'type': '[str]'},
        'trend_days': {'key': 'trendDays', 'type': 'int'}
    }

    def __init__(self, branch_names=None, build_count=None, definition_ids=None, env_definition_ids=None, max_complete_date=None, publish_context=None, test_run_titles=None, trend_days=None):
        super(TestResultTrendFilter, self).__init__()
        self.branch_names = branch_names
        self.build_count = build_count
        self.definition_ids = definition_ids
        self.env_definition_ids = env_definition_ids
        self.max_complete_date = max_complete_date
        self.publish_context = publish_context
        self.test_run_titles = test_run_titles
        self.trend_days = trend_days


class TestRun(Model):

    _attribute_map = {
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_configuration': {'key': 'buildConfiguration', 'type': 'BuildConfiguration'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'controller': {'key': 'controller', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'custom_fields': {'key': 'customFields', 'type': '[CustomTestField]'},
        'drop_location': {'key': 'dropLocation', 'type': 'str'},
        'dtl_aut_environment': {'key': 'dtlAutEnvironment', 'type': 'ShallowReference'},
        'dtl_environment': {'key': 'dtlEnvironment', 'type': 'ShallowReference'},
        'dtl_environment_creation_details': {'key': 'dtlEnvironmentCreationDetails', 'type': 'DtlEnvironmentDetails'},
        'due_date': {'key': 'dueDate', 'type': 'iso-8601'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'RunFilter'},
        'id': {'key': 'id', 'type': 'int'},
        'incomplete_tests': {'key': 'incompleteTests', 'type': 'int'},
        'is_automated': {'key': 'isAutomated', 'type': 'bool'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'not_applicable_tests': {'key': 'notApplicableTests', 'type': 'int'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'passed_tests': {'key': 'passedTests', 'type': 'int'},
        'phase': {'key': 'phase', 'type': 'str'},
        'pipeline_reference': {'key': 'pipelineReference', 'type': 'PipelineReference'},
        'plan': {'key': 'plan', 'type': 'ShallowReference'},
        'post_process_state': {'key': 'postProcessState', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'release': {'key': 'release', 'type': 'ReleaseReference'},
        'release_environment_uri': {'key': 'releaseEnvironmentUri', 'type': 'str'},
        'release_uri': {'key': 'releaseUri', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'run_statistics': {'key': 'runStatistics', 'type': '[RunStatistic]'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'substate': {'key': 'substate', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[TestTag]'},
        'test_environment': {'key': 'testEnvironment', 'type': 'TestEnvironment'},
        'test_message_log_id': {'key': 'testMessageLogId', 'type': 'int'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'},
        'total_tests': {'key': 'totalTests', 'type': 'int'},
        'unanalyzed_tests': {'key': 'unanalyzedTests', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'web_access_url': {'key': 'webAccessUrl', 'type': 'str'}
    }

    def __init__(self, build=None, build_configuration=None, comment=None, completed_date=None, controller=None, created_date=None, custom_fields=None, drop_location=None, dtl_aut_environment=None, dtl_environment=None, dtl_environment_creation_details=None, due_date=None, error_message=None, filter=None, id=None, incomplete_tests=None, is_automated=None, iteration=None, last_updated_by=None, last_updated_date=None, name=None, not_applicable_tests=None, owner=None, passed_tests=None, phase=None, pipeline_reference=None, plan=None, post_process_state=None, project=None, release=None, release_environment_uri=None, release_uri=None, revision=None, run_statistics=None, started_date=None, state=None, substate=None, tags=None, test_environment=None, test_message_log_id=None, test_settings=None, total_tests=None, unanalyzed_tests=None, url=None, web_access_url=None):
        super(TestRun, self).__init__()
        self.build = build
        self.build_configuration = build_configuration
        self.comment = comment
        self.completed_date = completed_date
        self.controller = controller
        self.created_date = created_date
        self.custom_fields = custom_fields
        self.drop_location = drop_location
        self.dtl_aut_environment = dtl_aut_environment
        self.dtl_environment = dtl_environment
        self.dtl_environment_creation_details = dtl_environment_creation_details
        self.due_date = due_date
        self.error_message = error_message
        self.filter = filter
        self.id = id
        self.incomplete_tests = incomplete_tests
        self.is_automated = is_automated
        self.iteration = iteration
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.name = name
        self.not_applicable_tests = not_applicable_tests
        self.owner = owner
        self.passed_tests = passed_tests
        self.phase = phase
        self.pipeline_reference = pipeline_reference
        self.plan = plan
        self.post_process_state = post_process_state
        self.project = project
        self.release = release
        self.release_environment_uri = release_environment_uri
        self.release_uri = release_uri
        self.revision = revision
        self.run_statistics = run_statistics
        self.started_date = started_date
        self.state = state
        self.substate = substate
        self.tags = tags
        self.test_environment = test_environment
        self.test_message_log_id = test_message_log_id
        self.test_settings = test_settings
        self.total_tests = total_tests
        self.unanalyzed_tests = unanalyzed_tests
        self.url = url
        self.web_access_url = web_access_url


class TestRunCoverage(Model):

    _attribute_map = {
        'last_error': {'key': 'lastError', 'type': 'str'},
        'modules': {'key': 'modules', 'type': '[ModuleCoverage]'},
        'state': {'key': 'state', 'type': 'str'},
        'test_run': {'key': 'testRun', 'type': 'ShallowReference'}
    }

    def __init__(self, last_error=None, modules=None, state=None, test_run=None):
        super(TestRunCoverage, self).__init__()
        self.last_error = last_error
        self.modules = modules
        self.state = state
        self.test_run = test_run


class TestRunStatistic(Model):

    _attribute_map = {
        'run': {'key': 'run', 'type': 'ShallowReference'},
        'run_statistics': {'key': 'runStatistics', 'type': '[RunStatistic]'}
    }

    def __init__(self, run=None, run_statistics=None):
        super(TestRunStatistic, self).__init__()
        self.run = run
        self.run_statistics = run_statistics


class TestSettings(Model):

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_public': {'key': 'isPublic', 'type': 'bool'},
        'machine_roles': {'key': 'machineRoles', 'type': 'str'},
        'test_settings_content': {'key': 'testSettingsContent', 'type': 'str'},
        'test_settings_id': {'key': 'testSettingsId', 'type': 'int'},
        'test_settings_name': {'key': 'testSettingsName', 'type': 'str'}
    }

    def __init__(self, area_path=None, description=None, is_public=None, machine_roles=None, test_settings_content=None, test_settings_id=None, test_settings_name=None):
        super(TestSettings, self).__init__()
        self.area_path = area_path
        self.description = description
        self.is_public = is_public
        self.machine_roles = machine_roles
        self.test_settings_content = test_settings_content
        self.test_settings_id = test_settings_id
        self.test_settings_name = test_settings_name


class TestSubResult(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'computer_name': {'key': 'computerName', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'ShallowReference'},
        'custom_fields': {'key': 'customFields', 'type': '[CustomTestField]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'long'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'result_group_type': {'key': 'resultGroupType', 'type': 'object'},
        'sequence_id': {'key': 'sequenceId', 'type': 'int'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'sub_results': {'key': 'subResults', 'type': '[TestSubResult]'},
        'test_result': {'key': 'testResult', 'type': 'TestCaseResultIdentifier'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, comment=None, completed_date=None, computer_name=None, configuration=None, custom_fields=None, display_name=None, duration_in_ms=None, error_message=None, id=None, last_updated_date=None, outcome=None, parent_id=None, result_group_type=None, sequence_id=None, stack_trace=None, started_date=None, sub_results=None, test_result=None, url=None):
        super(TestSubResult, self).__init__()
        self.comment = comment
        self.completed_date = completed_date
        self.computer_name = computer_name
        self.configuration = configuration
        self.custom_fields = custom_fields
        self.display_name = display_name
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.id = id
        self.last_updated_date = last_updated_date
        self.outcome = outcome
        self.parent_id = parent_id
        self.result_group_type = result_group_type
        self.sequence_id = sequence_id
        self.stack_trace = stack_trace
        self.started_date = started_date
        self.sub_results = sub_results
        self.test_result = test_result
        self.url = url


class TestSummaryForWorkItem(Model):

    _attribute_map = {
        'summary': {'key': 'summary', 'type': 'AggregatedDataForResultTrend'},
        'work_item': {'key': 'workItem', 'type': 'WorkItemReference'}
    }

    def __init__(self, summary=None, work_item=None):
        super(TestSummaryForWorkItem, self).__init__()
        self.summary = summary
        self.work_item = work_item


class TestTag(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(TestTag, self).__init__()
        self.name = name


class TestTagSummary(Model):

    _attribute_map = {
        'tags_group_by_test_artifact': {'key': 'tagsGroupByTestArtifact', 'type': '{[TestTag]}'}
    }

    def __init__(self, tags_group_by_test_artifact=None):
        super(TestTagSummary, self).__init__()
        self.tags_group_by_test_artifact = tags_group_by_test_artifact


class TestTagsUpdateModel(Model):

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '[{ key: OperationType; value: [TestTag] }]'}
    }

    def __init__(self, tags=None):
        super(TestTagsUpdateModel, self).__init__()
        self.tags = tags


class TestToWorkItemLinks(Model):

    _attribute_map = {
        'test': {'key': 'test', 'type': 'TestMethod'},
        'work_items': {'key': 'workItems', 'type': '[WorkItemReference]'}
    }

    def __init__(self, test=None, work_items=None):
        super(TestToWorkItemLinks, self).__init__()
        self.test = test
        self.work_items = work_items


class WorkItemReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, type=None, url=None, web_url=None):
        super(WorkItemReference, self).__init__()
        self.id = id
        self.name = name
        self.type = type
        self.url = url
        self.web_url = web_url


class WorkItemToTestLinks(Model):

    _attribute_map = {
        'executed_in': {'key': 'executedIn', 'type': 'object'},
        'tests': {'key': 'tests', 'type': '[TestMethod]'},
        'work_item': {'key': 'workItem', 'type': 'WorkItemReference'}
    }

    def __init__(self, executed_in=None, tests=None, work_item=None):
        super(WorkItemToTestLinks, self).__init__()
        self.executed_in = executed_in
        self.tests = tests
        self.work_item = work_item


class TestActionResultModel(TestResultModelBase):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'action_path': {'key': 'actionPath', 'type': 'str'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'shared_step_model': {'key': 'sharedStepModel', 'type': 'SharedStepModel'},
        'step_identifier': {'key': 'stepIdentifier', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, comment=None, completed_date=None, duration_in_ms=None, error_message=None, outcome=None, started_date=None, action_path=None, iteration_id=None, shared_step_model=None, step_identifier=None, url=None):
        super(TestActionResultModel, self).__init__(comment=comment, completed_date=completed_date, duration_in_ms=duration_in_ms, error_message=error_message, outcome=outcome, started_date=started_date)
        self.action_path = action_path
        self.iteration_id = iteration_id
        self.shared_step_model = shared_step_model
        self.step_identifier = step_identifier
        self.url = url


__all__ = [
    'AggregatedDataForResultTrend',
    'AggregatedResultDetailsByOutcome',
    'AggregatedResultsAnalysis',
    'AggregatedResultsByOutcome',
    'AggregatedResultsDifference',
    'AggregatedRunsByOutcome',
    'AggregatedRunsByState',
    'BuildConfiguration',
    'BuildCoverage',
    'BuildReference',
    'CodeCoverageData',
    'CodeCoverageStatistics',
    'CodeCoverageSummary',
    'CoverageStatistics',
    'CustomTestField',
    'DtlEnvironmentDetails',
    'FailingSince',
    'FieldDetailsForTestResults',
    'FileCoverageRequest',
    'FlakyDetection',
    'FlakyDetectionPipelines',
    'FlakySettings',
    'FunctionCoverage',
    'GraphSubjectBase',
    'IdentityRef',
    'JobReference',
    'ModuleCoverage',
    'NewTestResultLoggingSettings',
    'PhaseReference',
    'PipelineReference',
    'PipelineTestMetrics',
    'QueryModel',
    'ReferenceLinks',
    'ReleaseReference',
    'ResultsAnalysis',
    'ResultsFilter',
    'ResultsSummaryByOutcome',
    'ResultSummary',
    'RunCreateModel',
    'RunFilter',
    'RunStatistic',
    'RunSummary',
    'RunSummaryModel',
    'RunUpdateModel',
    'ShallowReference',
    'ShallowTestCaseResult',
    'SharedStepModel',
    'StageReference',
    'TeamProjectReference',
    'TestAttachment',
    'TestAttachmentReference',
    'TestAttachmentRequestModel',
    'TestCaseResult',
    'TestCaseResultAttachmentModel',
    'TestCaseResultIdentifier',
    'TestEnvironment',
    'TestFailureDetails',
    'TestFailuresAnalysis',
    'TestFlakyIdentifier',
    'TestHistoryQuery',
    'TestIterationDetailsModel',
    'TestLog',
    'TestLogReference',
    'TestLogStoreEndpointDetails',
    'TestMessageLogDetails',
    'TestMethod',
    'TestOperationReference',
    'TestResolutionState',
    'TestResultDocument',
    'TestResultFailuresAnalysis',
    'TestResultHistory',
    'TestResultHistoryDetailsForGroup',
    'TestResultHistoryForGroup',
    'TestResultMetaData',
    'TestResultMetaDataUpdateInput',
    'TestResultModelBase',
    'TestResultParameterModel',
    'TestResultPayload',
    'TestResultsContext',
    'TestResultsDetails',
    'TestResultsDetailsForGroup',
    'TestResultsQuery',
    'TestResultsSettings',
    'TestResultSummary',
    'TestResultsUpdateSettings',
    'TestResultTrendFilter',
    'TestRun',
    'TestRunCoverage',
    'TestRunStatistic',
    'TestSettings',
    'TestSubResult',
    'TestSummaryForWorkItem',
    'TestTag',
    'TestTagSummary',
    'TestTagsUpdateModel',
    'TestToWorkItemLinks',
    'WorkItemReference',
    'WorkItemToTestLinks',
    'TestActionResultModel',
]
