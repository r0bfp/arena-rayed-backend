from enum import Enum


class TournamentStatus(str, Enum):
    PENDING = 'pending'
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'


class PlayerStatus(str, Enum):
    PENDING = 'pending'
    READY = 'ready'
    PLAYING = 'playing'
    FINISHED = 'finished'
    CANCELLED = 'cancelled'


class MatchStatus(str, Enum):
    PENDING = 'pending'
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'