# --------------------------------------------------------------------------------------------


class ClientFactoryV6_0(object):

    def __init__(self, connection):
        self._connection = connection

    def get_accounts_client(self):
        return self._connection.get_client('azure.devops.v6_0.accounts.accounts_client.AccountsClient')

    def get_audit_client(self):
        return self._connection.get_client('azure.devops.v6_0.audit.audit_client.AuditClient')

    def get_build_client(self):
        return self._connection.get_client('azure.devops.v6_0.build.build_client.BuildClient')

    def get_cix_client(self):
        return self._connection.get_client('azure.devops.v6_0.cix.cix_client.CixClient')

    def get_client_trace_client(self):
        return self._connection.get_client('azure.devops.v6_0.client_trace.client_trace_client.ClientTraceClient')

    def get_cloud_load_test_client(self):
        return self._connection.get_client('azure.devops.v6_0.cloud_load_test.cloud_load_test_client.CloudLoadTestClient')

    def get_contributions_client(self):
        return self._connection.get_client('azure.devops.v6_0.contributions.contributions_client.ContributionsClient')

    def get_core_client(self):
        return self._connection.get_client('azure.devops.v6_0.core.core_client.CoreClient')

    def get_customer_intelligence_client(self):
        return self._connection.get_client('azure.devops.v6_0.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient')

    def get_dashboard_client(self):
        return self._connection.get_client('azure.devops.v6_0.dashboard.dashboard_client.DashboardClient')

    def get_extension_management_client(self):
        return self._connection.get_client('azure.devops.v6_0.extension_management.extension_management_client.ExtensionManagementClient')

    def get_feature_availability_client(self):
        return self._connection.get_client('azure.devops.v6_0.feature_availability.feature_availability_client.FeatureAvailabilityClient')

    def get_feature_management_client(self):
        return self._connection.get_client('azure.devops.v6_0.feature_management.feature_management_client.FeatureManagementClient')

    def get_feed_client(self):
        return self._connection.get_client('azure.devops.v6_0.feed.feed_client.FeedClient')

    def get_file_container_client(self):
        return self._connection.get_client('azure.devops.v6_0.file_container.file_container_client.FileContainerClient')

    def get_gallery_client(self):
        return self._connection.get_client('azure.devops.v6_0.gallery.gallery_client.GalleryClient')

    def get_git_client(self):
        return self._connection.get_client('azure.devops.v6_0.git.git_client.GitClient')

    def get_graph_client(self):
        return self._connection.get_client('azure.devops.v6_0.graph.graph_client.GraphClient')

    def get_identity_client(self):
        return self._connection.get_client('azure.devops.v6_0.identity.identity_client.IdentityClient')

    def get_location_client(self):
        return self._connection.get_client('azure.devops.v6_0.location.location_client.LocationClient')

    def get_maven_client(self):
        return self._connection.get_client('azure.devops.v6_0.maven.maven_client.MavenClient')

    def get_member_entitlement_management_client(self):
        return self._connection.get_client('azure.devops.v6_0.member_entitlement_management.member_entitlement_management_client.MemberEntitlementManagementClient')

    def get_notification_client(self):
        return self._connection.get_client('azure.devops.v6_0.notification.notification_client.NotificationClient')

    def get_npm_client(self):
        return self._connection.get_client('azure.devops.v6_0.npm.npm_client.NpmClient')

    def get_nuget_client(self):
        return self._connection.get_client('azure.devops.v6_0.nuget.nuget_client.NuGetClient')

    def get_operations_client(self):
        return self._connection.get_client('azure.devops.v6_0.operations.operations_client.OperationsClient')

    def get_pipeline_permissions_client(self):
        return self._connection.get_client('azure.devops.v6_0.pipeline_permissions.pipeline_permissions_client.PipelinePermissionsClient')

    def get_pipelines_client(self):
        return self._connection.get_client('azure.devops.v6_0.pipelines.pipelines_client.PipelinesClient')

    def get_pipelines_checks_client(self):
        return self._connection.get_client('azure.devops.v6_0.pipelines_checks.pipelines_checks_client.PipelinesChecksClient')

    def get_policy_client(self):
        return self._connection.get_client('azure.devops.v6_0.policy.policy_client.PolicyClient')

    def get_profile_client(self):
        return self._connection.get_client('azure.devops.v6_0.profile.profile_client.ProfileClient')

    def get_profile_regions_client(self):
        return self._connection.get_client('azure.devops.v6_0.profile_regions.profile_regions_client.ProfileRegionsClient')

    def get_project_analysis_client(self):
        return self._connection.get_client('azure.devops.v6_0.project_analysis.project_analysis_client.ProjectAnalysisClient')

    def get_provenance_client(self):
        return self._connection.get_client('azure.devops.v6_0.provenance.provenance_client.ProvenanceClient')

    def get_py_pi_api_client(self):
        return self._connection.get_client('azure.devops.v6_0.py_pi_api.py_pi_api_client.PyPiApiClient')

    def get_release_client(self):
        return self._connection.get_client('azure.devops.v6_0.release.release_client.ReleaseClient')

    def get_search_client(self):
        return self._connection.get_client('azure.devops.v6_0.search.search_client.SearchClient')

    def get_security_client(self):
        return self._connection.get_client('azure.devops.v6_0.security.security_client.SecurityClient')

    def get_service_endpoint_client(self):
        return self._connection.get_client('azure.devops.v6_0.service_endpoint.service_endpoint_client.ServiceEndpointClient')

    def get_service_hooks_client(self):
        return self._connection.get_client('azure.devops.v6_0.service_hooks.service_hooks_client.ServiceHooksClient')

    def get_settings_client(self):
        return self._connection.get_client('azure.devops.v6_0.settings.settings_client.SettingsClient')

    def get_symbol_client(self):
        return self._connection.get_client('azure.devops.v6_0.symbol.symbol_client.SymbolClient')

    def get_task_client(self):
        return self._connection.get_client('azure.devops.v6_0.task.task_client.TaskClient')

    def get_task_agent_client(self):
        return self._connection.get_client('azure.devops.v6_0.task_agent.task_agent_client.TaskAgentClient')

    def get_test_client(self):
        return self._connection.get_client('azure.devops.v6_0.test.test_client.TestClient')

    def get_test_plan_client(self):
        return self._connection.get_client('azure.devops.v6_0.test_plan.test_plan_client.TestPlanClient')

    def get_test_results_client(self):
        return self._connection.get_client('azure.devops.v6_0.test_results.test_results_client.TestResultsClient')

    def get_tfvc_client(self):
        return self._connection.get_client('azure.devops.v6_0.tfvc.tfvc_client.TfvcClient')

    def get_token_admin_client(self):
        return self._connection.get_client('azure.devops.v6_0.token_admin.token_admin_client.TokenAdminClient')

    def get_upack_api_client(self):
        return self._connection.get_client('azure.devops.v6_0.upack_api.upack_api_client.UPackApiClient')

    def get_upack_packaging_client(self):
        return self._connection.get_client('azure.devops.v6_0.upack_packaging.upack_packaging_client.UPackPackagingClient')

    def get_wiki_client(self):
        return self._connection.get_client('azure.devops.v6_0.wiki.wiki_client.WikiClient')

    def get_work_client(self):
        return self._connection.get_client('azure.devops.v6_0.work.work_client.WorkClient')

    def get_work_item_tracking_client(self):
        return self._connection.get_client('azure.devops.v6_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

    def get_work_item_tracking_process_client(self):
        return self._connection.get_client('azure.devops.v6_0.work_item_tracking_process.work_item_tracking_process_client.WorkItemTrackingProcessClient')

    def get_work_item_tracking_process_template_client(self):
        return self._connection.get_client('azure.devops.v6_0.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient')

