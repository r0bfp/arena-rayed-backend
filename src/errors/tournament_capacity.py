class CapacityNotFound(Exception):
    def __init__(self, msg='Capacity not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
