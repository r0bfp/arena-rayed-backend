class GameNotFound(Exception):
    def __init__(self, msg='Game not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
