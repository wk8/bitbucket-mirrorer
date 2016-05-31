from __future__ import absolute_import

from django.test import TestCase

from mock import patch, PropertyMock
import github

from app.models import RepoUser
from app.lib.user_backends.github import GithubUserBackend


class GithubUserBackendTests(TestCase):

    @property
    def backend(self):
        return GithubUserBackend(self.user)

    @property
    def user(self):
        return RepoUser(backend='Github',
                        name='wk8',
                        password='password')

    def test_url(self):
        self.assertEqual('https://github.com/wk8', self.backend.url())

    def test_are_creds_valid_with_valid_creds(self):
        with patch.object(github.Github, 'get_user') as patched_get_user:
            type(patched_get_user.return_value).login = PropertyMock(return_value='wk8')

            self.assertTrue(self.backend.are_creds_valid())

    def test_are_creds_valid_with_invalid_creds(self):
        with patch.object(github.Github, 'get_user') as patched_get_user:
            mocked_login = PropertyMock()
            mocked_login.side_effect = github.BadCredentialsException(401, 'dummy data')
            type(patched_get_user.return_value).login = mocked_login

            self.assertFalse(self.backend.are_creds_valid())
