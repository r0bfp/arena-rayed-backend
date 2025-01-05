
from sqlalchemy.orm import Session

from .match import MatchUseCase

from ..models.enums import PlayerStatus
from ..errors.match import MatchNotFound
from ..repositories.match import MatchRepository
from ..errors.player import InvalidPlayerStatus, PlayerNotFound
from ..repositories.player import PlayerRepository


class PlayerUseCase:
    @staticmethod
    def set_winner(db: Session, match_id: int, user_id: int, winner_id: int) -> None:
        match = MatchRepository.find_by_id(db, match_id)

        if not match:
            raise MatchNotFound

        player = PlayerRepository.find_by_match_id_and_user_id(db, match_id, user_id)
        winner = PlayerRepository.find_by_match_id_and_user_id(db, match_id, winner_id)

        if not winner:
            raise PlayerNotFound('Winner are not a player of this match')

        if not player:
            raise PlayerNotFound('You are not a player of this match')

        if player.status != PlayerStatus.PLAYING:
            raise InvalidPlayerStatus('Player are not playing to define winner')

        player.winner_id = winner_id
        player.status = PlayerStatus.FINISHED

        PlayerRepository.create_or_update(db, player.as_dict())
        MatchUseCase.update_status_if_players_finished(db, match)


    @staticmethod
    def ready(db: Session, match_id: int, user_id: int) -> None:
        match = MatchRepository.find_by_id(db, match_id)

        if not match:
            raise MatchNotFound

        player = PlayerRepository.find_by_match_id_and_user_id(db, match_id, user_id)
        opponent = PlayerRepository.find_opponent(db, match_id, user_id)

        if not player:
            raise PlayerNotFound('You are not a player of this match')

        if player.status == PlayerStatus.READY:
            raise InvalidPlayerStatus('Player is already ready')

        player.status = PlayerStatus.READY

        PlayerRepository.create_or_update(db, player.as_dict())

        if opponent.status == PlayerStatus.READY:
            opponent.status = PlayerStatus.PLAYING
            player.status = PlayerStatus.PLAYING

            PlayerRepository.create_or_update(db, player.as_dict())
            PlayerRepository.create_or_update(db, opponent.as_dict())
        
        MatchUseCase.update_status_if_both_players_ready(db, match)
