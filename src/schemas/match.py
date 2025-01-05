from typing import List, Optional
from pydantic import BaseModel, BaseModel

from ..models.enums import MatchStatus, PlayerStatus



class User(BaseModel):
    id: int
    username: str


class Player(BaseModel):
    id: int
    winner: Optional[User] = None
    status: PlayerStatus
    user: User



class MatchOut(BaseModel):
    id: int
    status: MatchStatus
    round_number: int
    contested: bool
    winner: Optional[User] = None
    players: List[Player]
