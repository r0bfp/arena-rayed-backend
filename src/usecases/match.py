
from sqlalchemy.orm import Session

from ..models.enums import MatchStatus, PlayerStatus
from ..models.match import Match
from ..errors.match import MatchNotFound
from ..repositories.match import MatchRepository


class MatchUseCase:
    @staticmethod
    def get_one(db: Session, match_id: int) -> Match:
        match = MatchRepository.find_by_id(db, match_id)

        if not match:
            raise MatchNotFound

        return match


    @staticmethod
    def update_status_if_players_finished(db, match) -> None:
        player_one = match.players[0]
        player_two = match.players[1]

        if player_one.status == PlayerStatus.FINISHED and player_two.status == PlayerStatus.FINISHED:
            if player_one.winner_id != player_two.winner_id:
                match.contested = True
            else:
                match.winner_id = player_one.winner_id

            match.status = MatchStatus.COMPLETED

            MatchRepository.create_or_update(db, match.as_dict())


    @staticmethod
    def update_status_if_both_players_ready(db, match) -> None:
        if match.players[0].status == PlayerStatus.READY and match.players[1].status == PlayerStatus.READY:
            match.status = MatchStatus.ONGOING

            MatchRepository.create_or_update(db, match.as_dict())