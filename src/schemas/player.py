from pydantic import BaseModel, model_validator

from ..models.player import Player
from ..models.enums import PlayerStatus




class PlayerOpponentOut(BaseModel):
    id: int
    status: PlayerStatus
    username: str
    tournament: str
    round_number: int

    @model_validator(mode='before')
    @classmethod
    def flat_player(cls, player: Player) -> str:
        player.username = player.user.username
        player.tournament = player.match.tournament.name
        player.round_number = player.match.round_number

        return player
    
class PlayerIn(BaseModel):
    is_winner: bool
