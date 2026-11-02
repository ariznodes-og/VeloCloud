# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildDefinitionReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(BuildDefinitionReference, self).__init__()
        self.id = id
        self.name = name


class CloneOperationCommonResponse(Model):

    _attribute_map = {
        'clone_statistics': {'key': 'cloneStatistics', 'type': 'CloneStatistics'},
        'completion_date': {'key': 'completionDate', 'type': 'iso-8601'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'links': {'key': 'links', 'type': 'ReferenceLinks'},
        'message': {'key': 'message', 'type': 'str'},
        'op_id': {'key': 'opId', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, clone_statistics=None, completion_date=None, creation_date=None, links=None, message=None, op_id=None, state=None):
        super(CloneOperationCommonResponse, self).__init__()
        self.clone_statistics = clone_statistics
        self.completion_date = completion_date
        self.creation_date = creation_date
        self.links = links
        self.message = message
        self.op_id = op_id
        self.state = state


class CloneOptions(Model):

    _attribute_map = {
        'clone_requirements': {'key': 'cloneRequirements', 'type': 'bool'},
        'copy_all_suites': {'key': 'copyAllSuites', 'type': 'bool'},
        'copy_ancestor_hierarchy': {'key': 'copyAncestorHierarchy', 'type': 'bool'},
        'destination_work_item_type': {'key': 'destinationWorkItemType', 'type': 'str'},
        'override_parameters': {'key': 'overrideParameters', 'type': '{str}'},
        'related_link_comment': {'key': 'relatedLinkComment', 'type': 'str'}
    }

    def __init__(self, clone_requirements=None, copy_all_suites=None, copy_ancestor_hierarchy=None, destination_work_item_type=None, override_parameters=None, related_link_comment=None):
        super(CloneOptions, self).__init__()
        self.clone_requirements = clone_requirements
        self.copy_all_suites = copy_all_suites
        self.copy_ancestor_hierarchy = copy_ancestor_hierarchy
        self.destination_work_item_type = destination_work_item_type
        self.override_parameters = override_parameters
        self.related_link_comment = related_link_comment


class CloneStatistics(Model):

    _attribute_map = {
        'cloned_requirements_count': {'key': 'clonedRequirementsCount', 'type': 'int'},
        'cloned_shared_steps_count': {'key': 'clonedSharedStepsCount', 'type': 'int'},
        'cloned_test_cases_count': {'key': 'clonedTestCasesCount', 'type': 'int'},
        'total_requirements_count': {'key': 'totalRequirementsCount', 'type': 'int'},
        'total_test_cases_count': {'key': 'totalTestCasesCount', 'type': 'int'}
    }

    def __init__(self, cloned_requirements_count=None, cloned_shared_steps_count=None, cloned_test_cases_count=None, total_requirements_count=None, total_test_cases_count=None):
        super(CloneStatistics, self).__init__()
        self.cloned_requirements_count = cloned_requirements_count
        self.cloned_shared_steps_count = cloned_shared_steps_count
        self.cloned_test_cases_count = cloned_test_cases_count
        self.total_requirements_count = total_requirements_count
        self.total_test_cases_count = total_test_cases_count


class CloneTestPlanOperationInformation(Model):

    _attribute_map = {
        'clone_operation_response': {'key': 'cloneOperationResponse', 'type': 'CloneOperationCommonResponse'},
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_test_plan': {'key': 'destinationTestPlan', 'type': 'TestPlan'},
        'source_test_plan': {'key': 'sourceTestPlan', 'type': 'SourceTestplanResponse'}
    }

    def __init__(self, clone_operation_response=None, clone_options=None, destination_test_plan=None, source_test_plan=None):
        super(CloneTestPlanOperationInformation, self).__init__()
        self.clone_operation_response = clone_operation_response
        self.clone_options = clone_options
        self.destination_test_plan = destination_test_plan
        self.source_test_plan = source_test_plan


class CloneTestPlanParams(Model):

    _attribute_map = {
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_test_plan': {'key': 'destinationTestPlan', 'type': 'DestinationTestPlanCloneParams'},
        'source_test_plan': {'key': 'sourceTestPlan', 'type': 'SourceTestPlanInfo'}
    }

    def __init__(self, clone_options=None, destination_test_plan=None, source_test_plan=None):
        super(CloneTestPlanParams, self).__init__()
        self.clone_options = clone_options
        self.destination_test_plan = destination_test_plan
        self.source_test_plan = source_test_plan


class CloneTestSuiteOperationInformation(Model):

    _attribute_map = {
        'cloned_test_suite': {'key': 'clonedTestSuite', 'type': 'TestSuiteReferenceWithProject'},
        'clone_operation_response': {'key': 'cloneOperationResponse', 'type': 'CloneOperationCommonResponse'},
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_test_suite': {'key': 'destinationTestSuite', 'type': 'TestSuiteReferenceWithProject'},
        'source_test_suite': {'key': 'sourceTestSuite', 'type': 'TestSuiteReferenceWithProject'}
    }

    def __init__(self, cloned_test_suite=None, clone_operation_response=None, clone_options=None, destination_test_suite=None, source_test_suite=None):
        super(CloneTestSuiteOperationInformation, self).__init__()
        self.cloned_test_suite = cloned_test_suite
        self.clone_operation_response = clone_operation_response
        self.clone_options = clone_options
        self.destination_test_suite = destination_test_suite
        self.source_test_suite = source_test_suite


class CloneTestSuiteParams(Model):

    _attribute_map = {
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_test_suite': {'key': 'destinationTestSuite', 'type': 'DestinationTestSuiteInfo'},
        'source_test_suite': {'key': 'sourceTestSuite', 'type': 'SourceTestSuiteInfo'}
    }

    def __init__(self, clone_options=None, destination_test_suite=None, source_test_suite=None):
        super(CloneTestSuiteParams, self).__init__()
        self.clone_options = clone_options
        self.destination_test_suite = destination_test_suite
        self.source_test_suite = source_test_suite


class Configuration(Model):

    _attribute_map = {
        'configuration_id': {'key': 'configurationId', 'type': 'int'}
    }

    def __init__(self, configuration_id=None):
        super(Configuration, self).__init__()
        self.configuration_id = configuration_id


class DestinationTestSuiteInfo(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'project': {'key': 'project', 'type': 'str'}
    }

    def __init__(self, id=None, project=None):
        super(DestinationTestSuiteInfo, self).__init__()
        self.id = id
        self.project = project


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


class LastResultDetails(Model):

    _attribute_map = {
        'date_completed': {'key': 'dateCompleted', 'type': 'iso-8601'},
        'duration': {'key': 'duration', 'type': 'long'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'}
    }

    def __init__(self, date_completed=None, duration=None, run_by=None):
        super(LastResultDetails, self).__init__()
        self.date_completed = date_completed
        self.duration = duration
        self.run_by = run_by


class NameValuePair(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(NameValuePair, self).__init__()
        self.name = name
        self.value = value


class PointAssignment(Configuration):

    _attribute_map = {
        'configuration_id': {'key': 'configurationId', 'type': 'int'},
        'configuration_name': {'key': 'configurationName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'}
    }

    def __init__(self, configuration_id=None, configuration_name=None, id=None, tester=None):
        super(PointAssignment, self).__init__(configuration_id=configuration_id)
        self.configuration_name = configuration_name
        self.id = id
        self.tester = tester


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ReleaseEnvironmentDefinitionReference(Model):

    _attribute_map = {
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'environment_definition_id': {'key': 'environmentDefinitionId', 'type': 'int'}
    }

    def __init__(self, definition_id=None, environment_definition_id=None):
        super(ReleaseEnvironmentDefinitionReference, self).__init__()
        self.definition_id = definition_id
        self.environment_definition_id = environment_definition_id


class Results(Model):

    _attribute_map = {
        'outcome': {'key': 'outcome', 'type': 'object'}
    }

    def __init__(self, outcome=None):
        super(Results, self).__init__()
        self.outcome = outcome


class SourceTestPlanInfo(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'suite_ids': {'key': 'suiteIds', 'type': '[int]'}
    }

    def __init__(self, id=None, suite_ids=None):
        super(SourceTestPlanInfo, self).__init__()
        self.id = id
        self.suite_ids = suite_ids


class SourceTestSuiteInfo(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(SourceTestSuiteInfo, self).__init__()
        self.id = id


class SuiteEntryUpdateParams(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'sequence_number': {'key': 'sequenceNumber', 'type': 'int'},
        'suite_entry_type': {'key': 'suiteEntryType', 'type': 'object'}
    }

    def __init__(self, id=None, sequence_number=None, suite_entry_type=None):
        super(SuiteEntryUpdateParams, self).__init__()
        self.id = id
        self.sequence_number = sequence_number
        self.suite_entry_type = suite_entry_type


class SuiteTestCaseCreateUpdateParameters(Model):

    _attribute_map = {
        'point_assignments': {'key': 'pointAssignments', 'type': '[Configuration]'},
        'work_item': {'key': 'workItem', 'type': 'WorkItem'}
    }

    def __init__(self, point_assignments=None, work_item=None):
        super(SuiteTestCaseCreateUpdateParameters, self).__init__()
        self.point_assignments = point_assignments
        self.work_item = work_item


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


class TestCase(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': 'ReferenceLinks'},
        'order': {'key': 'order', 'type': 'int'},
        'point_assignments': {'key': 'pointAssignments', 'type': '[PointAssignment]'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'test_plan': {'key': 'testPlan', 'type': 'TestPlanReference'},
        'test_suite': {'key': 'testSuite', 'type': 'TestSuiteReference'},
        'work_item': {'key': 'workItem', 'type': 'WorkItemDetails'}
    }

    def __init__(self, links=None, order=None, point_assignments=None, project=None, test_plan=None, test_suite=None, work_item=None):
        super(TestCase, self).__init__()
        self.links = links
        self.order = order
        self.point_assignments = point_assignments
        self.project = project
        self.test_plan = test_plan
        self.test_suite = test_suite
        self.work_item = work_item


class TestCaseReference(Model):

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'IdentityRef'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, id=None, name=None, state=None):
        super(TestCaseReference, self).__init__()
        self.assigned_to = assigned_to
        self.id = id
        self.name = name
        self.state = state


class TestConfigurationCreateUpdateParameters(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'state': {'key': 'state', 'type': 'object'},
        'values': {'key': 'values', 'type': '[NameValuePair]'}
    }

    def __init__(self, description=None, is_default=None, name=None, state=None, values=None):
        super(TestConfigurationCreateUpdateParameters, self).__init__()
        self.description = description
        self.is_default = is_default
        self.name = name
        self.state = state
        self.values = values


class TestConfigurationReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TestConfigurationReference, self).__init__()
        self.id = id
        self.name = name


class TestEnvironment(Model):

    _attribute_map = {
        'environment_id': {'key': 'environmentId', 'type': 'str'},
        'environment_name': {'key': 'environmentName', 'type': 'str'}
    }

    def __init__(self, environment_id=None, environment_name=None):
        super(TestEnvironment, self).__init__()
        self.environment_id = environment_id
        self.environment_name = environment_name


class TestOutcomeSettings(Model):

    _attribute_map = {
        'sync_outcome_across_suites': {'key': 'syncOutcomeAcrossSuites', 'type': 'bool'}
    }

    def __init__(self, sync_outcome_across_suites=None):
        super(TestOutcomeSettings, self).__init__()
        self.sync_outcome_across_suites = sync_outcome_across_suites


class TestPlanCreateParams(Model):

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build_definition': {'key': 'buildDefinition', 'type': 'BuildDefinitionReference'},
        'build_id': {'key': 'buildId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_outcome_settings': {'key': 'testOutcomeSettings', 'type': 'TestOutcomeSettings'}
    }

    def __init__(self, area_path=None, automated_test_environment=None, automated_test_settings=None, build_definition=None, build_id=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, test_outcome_settings=None):
        super(TestPlanCreateParams, self).__init__()
        self.area_path = area_path
        self.automated_test_environment = automated_test_environment
        self.automated_test_settings = automated_test_settings
        self.build_definition = build_definition
        self.build_id = build_id
        self.description = description
        self.end_date = end_date
        self.iteration = iteration
        self.manual_test_environment = manual_test_environment
        self.manual_test_settings = manual_test_settings
        self.name = name
        self.owner = owner
        self.release_environment_definition = release_environment_definition
        self.start_date = start_date
        self.state = state
        self.test_outcome_settings = test_outcome_settings


class TestPlanReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TestPlanReference, self).__init__()
        self.id = id
        self.name = name


class TestPlansHubRefreshData(Model):

    _attribute_map = {
        'is_advanced_extension_enabled': {'key': 'isAdvancedExtensionEnabled', 'type': 'bool'},
        'selected_suite_id': {'key': 'selectedSuiteId', 'type': 'int'},
        'selected_suite_name': {'key': 'selectedSuiteName', 'type': 'str'},
        'test_case_page_size': {'key': 'testCasePageSize', 'type': 'int'},
        'test_cases': {'key': 'testCases', 'type': '[TestCase]'},
        'test_cases_continuation_token': {'key': 'testCasesContinuationToken', 'type': 'str'},
        'test_plan': {'key': 'testPlan', 'type': 'TestPlanDetailedReference'},
        'test_point_page_size': {'key': 'testPointPageSize', 'type': 'int'},
        'test_points': {'key': 'testPoints', 'type': '[TestPoint]'},
        'test_points_continuation_token': {'key': 'testPointsContinuationToken', 'type': 'str'},
        'test_suites': {'key': 'testSuites', 'type': '[TestSuite]'},
        'test_suites_continuation_token': {'key': 'testSuitesContinuationToken', 'type': 'str'}
    }

    def __init__(self, is_advanced_extension_enabled=None, selected_suite_id=None, selected_suite_name=None, test_case_page_size=None, test_cases=None, test_cases_continuation_token=None, test_plan=None, test_point_page_size=None, test_points=None, test_points_continuation_token=None, test_suites=None, test_suites_continuation_token=None):
        super(TestPlansHubRefreshData, self).__init__()
        self.is_advanced_extension_enabled = is_advanced_extension_enabled
        self.selected_suite_id = selected_suite_id
        self.selected_suite_name = selected_suite_name
        self.test_case_page_size = test_case_page_size
        self.test_cases = test_cases
        self.test_cases_continuation_token = test_cases_continuation_token
        self.test_plan = test_plan
        self.test_point_page_size = test_point_page_size
        self.test_points = test_points
        self.test_points_continuation_token = test_points_continuation_token
        self.test_suites = test_suites
        self.test_suites_continuation_token = test_suites_continuation_token


class TestPlanUpdateParams(TestPlanCreateParams):

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build_definition': {'key': 'buildDefinition', 'type': 'BuildDefinitionReference'},
        'build_id': {'key': 'buildId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_outcome_settings': {'key': 'testOutcomeSettings', 'type': 'TestOutcomeSettings'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, area_path=None, automated_test_environment=None, automated_test_settings=None, build_definition=None, build_id=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, test_outcome_settings=None, revision=None):
        super(TestPlanUpdateParams, self).__init__(area_path=area_path, automated_test_environment=automated_test_environment, automated_test_settings=automated_test_settings, build_definition=build_definition, build_id=build_id, description=description, end_date=end_date, iteration=iteration, manual_test_environment=manual_test_environment, manual_test_settings=manual_test_settings, name=name, owner=owner, release_environment_definition=release_environment_definition, start_date=start_date, state=state, test_outcome_settings=test_outcome_settings)
        self.revision = revision


class TestPoint(Model):

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'TestConfigurationReference'},
        'id': {'key': 'id', 'type': 'int'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_automated': {'key': 'isAutomated', 'type': 'bool'},
        'last_reset_to_active': {'key': 'lastResetToActive', 'type': 'iso-8601'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'links': {'key': 'links', 'type': 'ReferenceLinks'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'results': {'key': 'results', 'type': 'TestPointResults'},
        'test_case_reference': {'key': 'testCaseReference', 'type': 'TestCaseReference'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'},
        'test_plan': {'key': 'testPlan', 'type': 'TestPlanReference'},
        'test_suite': {'key': 'testSuite', 'type': 'TestSuiteReference'}
    }

    def __init__(self, comment=None, configuration=None, id=None, is_active=None, is_automated=None, last_reset_to_active=None, last_updated_by=None, last_updated_date=None, links=None, project=None, results=None, test_case_reference=None, tester=None, test_plan=None, test_suite=None):
        super(TestPoint, self).__init__()
        self.comment = comment
        self.configuration = configuration
        self.id = id
        self.is_active = is_active
        self.is_automated = is_automated
        self.last_reset_to_active = last_reset_to_active
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.links = links
        self.project = project
        self.results = results
        self.test_case_reference = test_case_reference
        self.tester = tester
        self.test_plan = test_plan
        self.test_suite = test_suite


class TestPointCount(Model):

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'test_plan_id': {'key': 'testPlanId', 'type': 'int'},
        'test_suite_id': {'key': 'testSuiteId', 'type': 'int'}
    }

    def __init__(self, count=None, test_plan_id=None, test_suite_id=None):
        super(TestPointCount, self).__init__()
        self.count = count
        self.test_plan_id = test_plan_id
        self.test_suite_id = test_suite_id


class TestPointResults(Model):

    _attribute_map = {
        'failure_type': {'key': 'failureType', 'type': 'object'},
        'last_resolution_state': {'key': 'lastResolutionState', 'type': 'object'},
        'last_result_details': {'key': 'lastResultDetails', 'type': 'LastResultDetails'},
        'last_result_id': {'key': 'lastResultId', 'type': 'int'},
        'last_result_state': {'key': 'lastResultState', 'type': 'object'},
        'last_run_build_number': {'key': 'lastRunBuildNumber', 'type': 'str'},
        'last_test_run_id': {'key': 'lastTestRunId', 'type': 'int'},
        'outcome': {'key': 'outcome', 'type': 'object'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, failure_type=None, last_resolution_state=None, last_result_details=None, last_result_id=None, last_result_state=None, last_run_build_number=None, last_test_run_id=None, outcome=None, state=None):
        super(TestPointResults, self).__init__()
        self.failure_type = failure_type
        self.last_resolution_state = last_resolution_state
        self.last_result_details = last_result_details
        self.last_result_id = last_result_id
        self.last_result_state = last_result_state
        self.last_run_build_number = last_run_build_number
        self.last_test_run_id = last_test_run_id
        self.outcome = outcome
        self.state = state


class TestPointUpdateParams(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'results': {'key': 'results', 'type': 'Results'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'}
    }

    def __init__(self, id=None, is_active=None, results=None, tester=None):
        super(TestPointUpdateParams, self).__init__()
        self.id = id
        self.is_active = is_active
        self.results = results
        self.tester = tester


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


class TestSuiteCreateUpdateCommonParams(Model):

    _attribute_map = {
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[TestConfigurationReference]'},
        'default_testers': {'key': 'defaultTesters', 'type': '[IdentityRef]'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_suite': {'key': 'parentSuite', 'type': 'TestSuiteReference'},
        'query_string': {'key': 'queryString', 'type': 'str'}
    }

    def __init__(self, default_configurations=None, default_testers=None, inherit_default_configurations=None, name=None, parent_suite=None, query_string=None):
        super(TestSuiteCreateUpdateCommonParams, self).__init__()
        self.default_configurations = default_configurations
        self.default_testers = default_testers
        self.inherit_default_configurations = inherit_default_configurations
        self.name = name
        self.parent_suite = parent_suite
        self.query_string = query_string


class TestSuiteReference(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TestSuiteReference, self).__init__()
        self.id = id
        self.name = name


class TestSuiteReferenceWithProject(TestSuiteReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, id=None, name=None, project=None):
        super(TestSuiteReferenceWithProject, self).__init__(id=id, name=name)
        self.project = project


class TestSuiteUpdateParams(TestSuiteCreateUpdateCommonParams):

    _attribute_map = {
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[TestConfigurationReference]'},
        'default_testers': {'key': 'defaultTesters', 'type': '[IdentityRef]'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_suite': {'key': 'parentSuite', 'type': 'TestSuiteReference'},
        'query_string': {'key': 'queryString', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, default_configurations=None, default_testers=None, inherit_default_configurations=None, name=None, parent_suite=None, query_string=None, revision=None):
        super(TestSuiteUpdateParams, self).__init__(default_configurations=default_configurations, default_testers=default_testers, inherit_default_configurations=inherit_default_configurations, name=name, parent_suite=parent_suite, query_string=query_string)
        self.revision = revision


class TestVariableCreateUpdateParameters(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'}
    }

    def __init__(self, description=None, name=None, values=None):
        super(TestVariableCreateUpdateParameters, self).__init__()
        self.description = description
        self.name = name
        self.values = values


class WorkItem(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(WorkItem, self).__init__()
        self.id = id


class WorkItemDetails(Model):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'work_item_fields': {'key': 'workItemFields', 'type': '[object]'}
    }

    def __init__(self, id=None, name=None, work_item_fields=None):
        super(WorkItemDetails, self).__init__()
        self.id = id
        self.name = name
        self.work_item_fields = work_item_fields


class DestinationTestPlanCloneParams(TestPlanCreateParams):

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build_definition': {'key': 'buildDefinition', 'type': 'BuildDefinitionReference'},
        'build_id': {'key': 'buildId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_outcome_settings': {'key': 'testOutcomeSettings', 'type': 'TestOutcomeSettings'},
        'project': {'key': 'project', 'type': 'str'}
    }

    def __init__(self, area_path=None, automated_test_environment=None, automated_test_settings=None, build_definition=None, build_id=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, test_outcome_settings=None, project=None):
        super(DestinationTestPlanCloneParams, self).__init__(area_path=area_path, automated_test_environment=automated_test_environment, automated_test_settings=automated_test_settings, build_definition=build_definition, build_id=build_id, description=description, end_date=end_date, iteration=iteration, manual_test_environment=manual_test_environment, manual_test_settings=manual_test_settings, name=name, owner=owner, release_environment_definition=release_environment_definition, start_date=start_date, state=state, test_outcome_settings=test_outcome_settings)
        self.project = project


class SourceTestplanResponse(TestPlanReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'suite_ids': {'key': 'suiteIds', 'type': '[int]'}
    }

    def __init__(self, id=None, name=None, project=None, suite_ids=None):
        super(SourceTestplanResponse, self).__init__(id=id, name=name)
        self.project = project
        self.suite_ids = suite_ids


class SuiteEntry(SuiteEntryUpdateParams):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'sequence_number': {'key': 'sequenceNumber', 'type': 'int'},
        'suite_entry_type': {'key': 'suiteEntryType', 'type': 'object'},
        'suite_id': {'key': 'suiteId', 'type': 'int'}
    }

    def __init__(self, id=None, sequence_number=None, suite_entry_type=None, suite_id=None):
        super(SuiteEntry, self).__init__(id=id, sequence_number=sequence_number, suite_entry_type=suite_entry_type)
        self.suite_id = suite_id


class TestConfiguration(TestConfigurationCreateUpdateParameters):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'state': {'key': 'state', 'type': 'object'},
        'values': {'key': 'values', 'type': '[NameValuePair]'},
        'id': {'key': 'id', 'type': 'int'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, description=None, is_default=None, name=None, state=None, values=None, id=None, project=None):
        super(TestConfiguration, self).__init__(description=description, is_default=is_default, name=name, state=state, values=values)
        self.id = id
        self.project = project


class TestPlan(TestPlanUpdateParams):

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build_definition': {'key': 'buildDefinition', 'type': 'BuildDefinitionReference'},
        'build_id': {'key': 'buildId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_outcome_settings': {'key': 'testOutcomeSettings', 'type': 'TestOutcomeSettings'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'previous_build_id': {'key': 'previousBuildId', 'type': 'int'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'root_suite': {'key': 'rootSuite', 'type': 'TestSuiteReference'},
        'updated_by': {'key': 'updatedBy', 'type': 'IdentityRef'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, area_path=None, automated_test_environment=None, automated_test_settings=None, build_definition=None, build_id=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, test_outcome_settings=None, revision=None, _links=None, id=None, previous_build_id=None, project=None, root_suite=None, updated_by=None, updated_date=None):
        super(TestPlan, self).__init__(area_path=area_path, automated_test_environment=automated_test_environment, automated_test_settings=automated_test_settings, build_definition=build_definition, build_id=build_id, description=description, end_date=end_date, iteration=iteration, manual_test_environment=manual_test_environment, manual_test_settings=manual_test_settings, name=name, owner=owner, release_environment_definition=release_environment_definition, start_date=start_date, state=state, test_outcome_settings=test_outcome_settings, revision=revision)
        self._links = _links
        self.id = id
        self.previous_build_id = previous_build_id
        self.project = project
        self.root_suite = root_suite
        self.updated_by = updated_by
        self.updated_date = updated_date


class TestPlanDetailedReference(TestPlanReference):

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'root_suite_id': {'key': 'rootSuiteId', 'type': 'int'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'}
    }

    def __init__(self, id=None, name=None, area_path=None, end_date=None, iteration=None, root_suite_id=None, start_date=None):
        super(TestPlanDetailedReference, self).__init__(id=id, name=name)
        self.area_path = area_path
        self.end_date = end_date
        self.iteration = iteration
        self.root_suite_id = root_suite_id
        self.start_date = start_date


class TestSuiteCreateParams(TestSuiteCreateUpdateCommonParams):

    _attribute_map = {
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[TestConfigurationReference]'},
        'default_testers': {'key': 'defaultTesters', 'type': '[IdentityRef]'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_suite': {'key': 'parentSuite', 'type': 'TestSuiteReference'},
        'query_string': {'key': 'queryString', 'type': 'str'},
        'requirement_id': {'key': 'requirementId', 'type': 'int'},
        'suite_type': {'key': 'suiteType', 'type': 'object'}
    }

    def __init__(self, default_configurations=None, default_testers=None, inherit_default_configurations=None, name=None, parent_suite=None, query_string=None, requirement_id=None, suite_type=None):
        super(TestSuiteCreateParams, self).__init__(default_configurations=default_configurations, default_testers=default_testers, inherit_default_configurations=inherit_default_configurations, name=name, parent_suite=parent_suite, query_string=query_string)
        self.requirement_id = requirement_id
        self.suite_type = suite_type


class TestVariable(TestVariableCreateUpdateParameters):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
        'id': {'key': 'id', 'type': 'int'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, description=None, name=None, values=None, id=None, project=None):
        super(TestVariable, self).__init__(description=description, name=name, values=values)
        self.id = id
        self.project = project


class TestSuite(TestSuiteCreateParams):

    _attribute_map = {
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[TestConfigurationReference]'},
        'default_testers': {'key': 'defaultTesters', 'type': '[IdentityRef]'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_suite': {'key': 'parentSuite', 'type': 'TestSuiteReference'},
        'query_string': {'key': 'queryString', 'type': 'str'},
        'requirement_id': {'key': 'requirementId', 'type': 'int'},
        'suite_type': {'key': 'suiteType', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'children': {'key': 'children', 'type': '[TestSuite]'},
        'has_children': {'key': 'hasChildren', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'last_error': {'key': 'lastError', 'type': 'str'},
        'last_populated_date': {'key': 'lastPopulatedDate', 'type': 'iso-8601'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'plan': {'key': 'plan', 'type': 'TestPlanReference'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, default_configurations=None, default_testers=None, inherit_default_configurations=None, name=None, parent_suite=None, query_string=None, requirement_id=None, suite_type=None, _links=None, children=None, has_children=None, id=None, last_error=None, last_populated_date=None, last_updated_by=None, last_updated_date=None, plan=None, project=None, revision=None):
        super(TestSuite, self).__init__(default_configurations=default_configurations, default_testers=default_testers, inherit_default_configurations=inherit_default_configurations, name=name, parent_suite=parent_suite, query_string=query_string, requirement_id=requirement_id, suite_type=suite_type)
        self._links = _links
        self.children = children
        self.has_children = has_children
        self.id = id
        self.last_error = last_error
        self.last_populated_date = last_populated_date
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.plan = plan
        self.project = project
        self.revision = revision


__all__ = [
    'BuildDefinitionReference',
    'CloneOperationCommonResponse',
    'CloneOptions',
    'CloneStatistics',
    'CloneTestPlanOperationInformation',
    'CloneTestPlanParams',
    'CloneTestSuiteOperationInformation',
    'CloneTestSuiteParams',
    'Configuration',
    'DestinationTestSuiteInfo',
    'GraphSubjectBase',
    'IdentityRef',
    'LastResultDetails',
    'NameValuePair',
    'PointAssignment',
    'ReferenceLinks',
    'ReleaseEnvironmentDefinitionReference',
    'Results',
    'SourceTestPlanInfo',
    'SourceTestSuiteInfo',
    'SuiteEntryUpdateParams',
    'SuiteTestCaseCreateUpdateParameters',
    'TeamProjectReference',
    'TestCase',
    'TestCaseReference',
    'TestConfigurationCreateUpdateParameters',
    'TestConfigurationReference',
    'TestEnvironment',
    'TestOutcomeSettings',
    'TestPlanCreateParams',
    'TestPlanReference',
    'TestPlansHubRefreshData',
    'TestPlanUpdateParams',
    'TestPoint',
    'TestPointCount',
    'TestPointResults',
    'TestPointUpdateParams',
    'TestSettings',
    'TestSuiteCreateUpdateCommonParams',
    'TestSuiteReference',
    'TestSuiteReferenceWithProject',
    'TestSuiteUpdateParams',
    'TestVariableCreateUpdateParameters',
    'WorkItem',
    'WorkItemDetails',
    'DestinationTestPlanCloneParams',
    'SourceTestplanResponse',
    'SuiteEntry',
    'TestConfiguration',
    'TestPlan',
    'TestPlanDetailedReference',
    'TestSuiteCreateParams',
    'TestVariable',
    'TestSuite',
]
