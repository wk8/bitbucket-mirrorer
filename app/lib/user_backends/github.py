from __future__ import absolute_import

import github

from .base import UserBackend


class GithubUserBackend(UserBackend):

    def url(self):
        return 'https://github.com/%s' % (self.user.name, )

    def are_creds_valid(self):
        client = github.Github(self.user.name, self.user.password)
        try:
            client.get_user().login
            return True
        except github.BadCredentialsException:
            return False
