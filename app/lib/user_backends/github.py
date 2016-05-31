from __future__ import absolute_import

import github

from .base import UserBackend


class GithubUserBackend(UserBackend):

    def url(self):
        return 'https://github.com/%s' % (self.user.name, )

    def are_creds_valid(self):
        try:
            self._github_user().login
            return True
        except github.BadCredentialsException:
            return False

    def _github_user(self):
        return self._client().get_user()

    def _client(self):
        return github.Github(self.user.name, self.user.password)
