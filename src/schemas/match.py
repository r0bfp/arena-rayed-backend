from operator import is_
from typing import List, Optional
from pydantic import BaseModel, BaseModel, model_validator

from .user import UserBase

from ..models.enums import MatchStatus, PlayerStatus



class User(BaseModel):
    id: int
    username: str


class Player(BaseModel):
    id: int
    user_id: int
    status: PlayerStatus
    username: str
    is_winner: bool

    @model_validator(mode='before')
    @classmethod
    def flat_player(cls, player: UserBase) -> str:
        player.username = player.user.username
        player.user_id = player.user.id

        return player


class MatchOut(BaseModel):
    id: int
    status: MatchStatus
    round_number: int
    contested: bool
    players: List[Player]
