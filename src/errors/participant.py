class ParticipantNotFound(Exception):
    def __init__(self, msg='Participant not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class ParticipantAlreadyAdded(Exception):
    def __init__(self, msg='Participant already added', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)