# --------------------------------------------------------------------------------------------


class ClientFactory(object):

    def __init__(self, connection):
        self._connection = connection

    def get_accounts_client(self):
        return self._connection.get_client('azure.devops.released.accounts.accounts_client.AccountsClient')

    def get_build_client(self):
        return self._connection.get_client('azure.devops.released.build.build_client.BuildClient')

    def get_cloud_load_test_client(self):
        return self._connection.get_client('azure.devops.released.cloud_load_test.cloud_load_test_client.CloudLoadTestClient')

    def get_core_client(self):
        return self._connection.get_client('azure.devops.released.core.core_client.CoreClient')

    def get_git_client(self):
        return self._connection.get_client('azure.devops.released.git.git_client.GitClient')

    def get_identity_client(self):
        return self._connection.get_client('azure.devops.released.identity.identity_client.IdentityClient')

    def get_notification_client(self):
        return self._connection.get_client('azure.devops.released.notification.notification_client.NotificationClient')

    def get_operations_client(self):
        return self._connection.get_client('azure.devops.released.operations.operations_client.OperationsClient')

    def get_policy_client(self):
        return self._connection.get_client('azure.devops.released.policy.policy_client.PolicyClient')

    def get_profile_client(self):
        return self._connection.get_client('azure.devops.released.profile.profile_client.ProfileClient')

    def get_release_client(self):
        return self._connection.get_client('azure.devops.released.release.release_client.ReleaseClient')

    def get_security_client(self):
        return self._connection.get_client('azure.devops.released.security.security_client.SecurityClient')

    def get_service_hooks_client(self):
        return self._connection.get_client('azure.devops.released.service_hooks.service_hooks_client.ServiceHooksClient')

    def get_task_client(self):
        return self._connection.get_client('azure.devops.released.task.task_client.TaskClient')

    def get_task_agent_client(self):
        return self._connection.get_client('azure.devops.released.task_agent.task_agent_client.TaskAgentClient')

    def get_test_client(self):
        return self._connection.get_client('azure.devops.released.test.test_client.TestClient')

    def get_test_plan_client(self):
        return self._connection.get_client('azure.devops.released.test_plan.test_plan_client.TestPlanClient')

    def get_test_results_client(self):
        return self._connection.get_client('azure.devops.released.test_results.test_results_client.TestResultsClient')

    def get_tfvc_client(self):
        return self._connection.get_client('azure.devops.released.tfvc.tfvc_client.TfvcClient')

    def get_wiki_client(self):
        return self._connection.get_client('azure.devops.released.wiki.wiki_client.WikiClient')

    def get_work_client(self):
        return self._connection.get_client('azure.devops.released.work.work_client.WorkClient')

    def get_work_item_tracking_client(self):
        return self._connection.get_client('azure.devops.released.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

