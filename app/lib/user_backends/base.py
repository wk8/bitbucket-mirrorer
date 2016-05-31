class UserBackend(object):
    '''
    A base backend for all users
    '''

    def __init__(self, user):
        self._user = user

    def url(self):
        '''
        Should return a URL to the user's profile
        '''
        raise NotImplementedError

    def are_creds_valid(self):
        '''
        Should return true iff the credentials are valid
        '''
        raise NotImplementedError

    @property
    def user(self):
        return self._user

    @classmethod
    def all_backends(cls):
        '''
        Returns a list of all available backends
        '''
        # TODO wkpo
        pass
