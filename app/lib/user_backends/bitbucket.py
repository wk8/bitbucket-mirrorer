from __future__ import absolute_import

from pybitbucket import bitbucket as pybb_bitbucket
from pybitbucket import auth as pybb_auth
from pybitbucket import user as pybb_user

import requests

from .base import UserBackend


class BitbucketUserBackend(UserBackend):

    def url(self):
        return 'https://bitbucket.org/%s' % (self.user.name, )

    def are_creds_valid(self):
        try:
            self._bitbucket_user()
            return True
        except requests.HTTPError:
            return False

    def _bitbucket_user(self):
        pybb_user.User.find_current_user(self._client())

    def _client(self):
        return pybb_bitbucket.Client(self._authenticator())

    def _authenticator(self):
        # the 3rd argument is the user's email, and is not needed
        return pybb_auth.BasicAuthenticator(self.user.name, self.user.password, None)
