class MatchNotFound(Exception):
    def __init__(self, msg='Match not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
