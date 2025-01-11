class CoinPackageNotFound(Exception):
    def __init__(self, msg='Coin package not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
