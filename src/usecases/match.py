
from sqlalchemy.orm import Session

from .tournament import TournamentUseCase

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
    def update_status_if_both_players_finished(db, match: Match) -> None:
        player_one = match.players[0]
        player_two = match.players[1]

        if player_one.status == PlayerStatus.FINISHED and player_two.status == PlayerStatus.FINISHED:
            match.contested = player_one.is_winner == player_two.is_winner

            if player_one.is_winner:
                match.winner_id = player_one.id
            else:
                match.winner_id = player_two.id

            match.status = MatchStatus.COMPLETED

            MatchRepository.create_or_update(db, match.as_dict())
            TournamentUseCase.generate_next_round_if_prev_finished(db, match.tournament_id)


    @staticmethod
    def update_status_if_both_players_ready(db, match: Match) -> None:
        if match.players[0].status == PlayerStatus.READY and match.players[1].status == PlayerStatus.READY:
            match.status = MatchStatus.ONGOING

            MatchRepository.create_or_update(db, match.as_dict())