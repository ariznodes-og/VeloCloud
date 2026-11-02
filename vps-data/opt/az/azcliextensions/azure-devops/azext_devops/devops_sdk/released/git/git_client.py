
from .git_client_base import GitClientBase


class GitClient(GitClientBase):

    def __init__(self, base_url=None, creds=None):
        super(GitClient, self).__init__(base_url, creds)
