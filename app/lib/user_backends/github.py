import base


class GithubUserBackend(base.UserBackend):

    def url(self):
        return 'https://github.com/%s' % (self.user.name, )

    def are_creds_valid(self):
        '''
        Should return true iff the credentials are valid
        '''
        raise NotImplementedError

    @classmethod
    def all_backends(cls):
        '''
        Returns a list of all available backends
        '''
        # TODO wkpo
        pass
