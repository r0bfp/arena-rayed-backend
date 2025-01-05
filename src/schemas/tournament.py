from typing import List, Optional
from pydantic import AliasPath, BaseModel, Field
from datetime import datetime



class TournamentIn(BaseModel):
    name: str
    description: str
    starts_in: datetime
    ends_in: datetime
    game_id: int
    capacity_id: int


class User(BaseModel):
    username: str


class Capacity(BaseModel):
    id: int
    max: int = Field(validation_alias=AliasPath('capacity'))


class Game(BaseModel):
    id: int
    name: str


class TournamentOut(BaseModel):
    id: int
    name: str
    description: str
    starts_in: datetime
    ends_in: datetime
    status: str
    owner: User
    game: Game
    capacity: Capacity

    class Config:
        from_attributes = True