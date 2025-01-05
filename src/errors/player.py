class PlayerNotFound(Exception):
    def __init__(self, msg='Player not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class InvalidPlayerStatus(Exception):
    def __init__(self, msg='Invalid player status', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)