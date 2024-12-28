class DuplicatedUsername(Exception):
    def __init__(self, msg='Username already exists', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DuplicatedEmail(Exception):
    def __init__(self, msg='Email already exists', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UserNotFound(Exception):
    def __init__(self, msg='User not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)