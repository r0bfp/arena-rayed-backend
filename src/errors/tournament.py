class InvalidTournamentDuration(Exception):
    def __init__(self, msg='Invalid tournament duration', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class TournamentAlreadyExists(Exception):
    def __init__(self, msg='Tournament already exists', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class NotEnoughCoins(Exception):
    def __init__(self, msg='Not enough coins', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class TournamentNotFound(Exception):
    def __init__(self, msg='Tournament not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class Unauthorized(Exception):
    def __init__(self, msg='Unauthorized', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class InvalidTournamentStatus(Exception):
    def __init__(self, msg='Invalid tournament status', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class TournamentCapacityNotReached(Exception):
    def __init__(self, msg='Tournament capacity not reached', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class TournamentFull(Exception):
    def __init__(self, msg='Tournament full', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


