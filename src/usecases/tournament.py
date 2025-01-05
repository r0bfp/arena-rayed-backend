
from datetime import datetime
from random import shuffle
from typing import List
from sqlalchemy.orm import Session

from ..repositories.player import PlayerRepository
from ..repositories.match import MatchRepository
from ..repositories.participant import ParticipantRepository
from ..models.enums import MatchStatus, PlayerStatus, TournamentStatus
from ..schemas.tournament import TournamentIn
from ..errors.tournament_capacity import CapacityNotFound
from ..errors.tournament import InvalidTournamentDuration, InvalidTournamentStatus, NotEnoughCoins, TournamentAlreadyExists, TournamentCapacityNotReached, TournamentNotFound, Unauthorized
from ..errors.game import GameNotFound
from ..repositories.tournament import TournamentRepository
from ..repositories.tournament_capacity import TournamentCapacityRepository
from ..repositories.game import GameRepository
from ..repositories.user import UserRepository
from ..models.tournament import Tournament


class TournamentUseCase:
    @staticmethod
    def create(db: Session, new_tournament: TournamentIn, user_id: int) -> Tournament:
        if new_tournament.starts_in < datetime.now() or new_tournament.ends_in < datetime.now():
            raise InvalidTournamentDuration

        if new_tournament.starts_in > new_tournament.ends_in:
            raise InvalidTournamentDuration

        if TournamentRepository.exists_by_name(db, new_tournament.name):
            raise TournamentAlreadyExists

        if not GameRepository.exists_by_id(db, new_tournament.game_id):
            raise GameNotFound

        capacity = TournamentCapacityRepository.find_by_id(db, new_tournament.capacity_id)

        if not capacity:
            raise CapacityNotFound

        user = UserRepository.find_by_id(db, user_id)

        if user.coins < capacity.price:
            raise NotEnoughCoins

        user.coins -= capacity.price

        UserRepository.create_or_update(db, user.as_dict())

        return TournamentRepository.create_or_update(db, {
            **new_tournament.model_dump(),
            'owner_id': user_id,
        })


    @staticmethod
    def list(db: Session) -> List[Tournament]:
        return TournamentRepository.find_all(db)


    @staticmethod
    def delete(db: Session, tournament_id: int, owner_id: int) -> None:
        tournament = TournamentRepository.find_by_id(db, tournament_id)
        
        if not tournament:
            raise TournamentNotFound

        if tournament.owner_id != owner_id:
            raise Unauthorized

        TournamentRepository.delete_by_id(db, tournament_id)


    @staticmethod
    def start(db: Session, tournament_id: int, owner_id: int) -> None:
        tournament = TournamentRepository.find_by_id(db, tournament_id)
        
        if not tournament:
            raise TournamentNotFound("Tournament not found.")

        if tournament.owner_id != owner_id:
            raise Unauthorized("User is not authorized to start this tournament.")

        if tournament.status != TournamentStatus.PENDING:
            raise InvalidTournamentStatus("Tournament status must be PENDING to start.")

        players_count = ParticipantRepository.count_by_tournament_id(db, tournament_id)

        if players_count < tournament.capacity.capacity:
            raise TournamentCapacityNotReached("Minimum tournament capacity not reached.")

        TournamentRepository.update_status(db, tournament_id, TournamentStatus.ONGOING)

        players = ParticipantRepository.find_all_by_tournament_id(db, tournament_id)
        shuffle(players)

        players_pairs = [players[i:i + 2] for i in range(0, len(players), 2)]

        for pair in players_pairs:
            player_one = pair[0].user_id
            player_two = pair[1].user_id

            match = MatchRepository.create_or_update(db, {
                'round_number': 1,
                'tournament_id': tournament_id,
                'status': MatchStatus.ONGOING
            })

            PlayerRepository.create_or_update(db, {
                'match_id': match.id,
                'user_id': player_one,
                'status': PlayerStatus.PENDING
            })
            PlayerRepository.create_or_update(db, {
                'match_id': match.id,
                'user_id': player_two,
                'status': PlayerStatus.PENDING
            })


    @staticmethod
    def list_all_matches_by_tournament(db: Session, tournament_id: int) -> None:
        return MatchRepository.find_all_by_tournament_id(db, tournament_id)