from django.test import TestCase

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
