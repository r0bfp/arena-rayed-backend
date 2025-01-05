
from typing import List
from sqlalchemy.orm import Session

from ..errors.user import UserNotFound
from ..repositories.user import UserRepository
from ..errors.participant import ParticipantAlreadyAdded, ParticipantNotFound
from ..schemas.participant import ParticipantIn, ParticipantOut
from ..models.participant import Participant
from ..errors.tournament import TournamentFull, TournamentNotFound, Unauthorized
from ..repositories.tournament import TournamentRepository
from ..repositories.participant import ParticipantRepository
from ..models.tournament import Tournament


class ParticipantUseCase:
    @staticmethod
    def create(db: Session, tournament_id: int, owner_id: int, participant: ParticipantIn) -> ParticipantOut:
        tournament = TournamentRepository.find_by_id(db, tournament_id)

        if not tournament:
            raise TournamentNotFound

        if tournament.owner_id != owner_id:
            raise Unauthorized

        if ParticipantRepository.exists_by_user_id_and_tournament_id(db, participant.user_id, tournament_id):
            raise ParticipantAlreadyAdded

        if not UserRepository.exists_by_id(db, participant.user_id):
            raise UserNotFound

        participant_amount = ParticipantRepository.count_by_tournament_id(db, tournament_id)

        if participant_amount >= tournament.capacity.capacity:
            raise TournamentFull

        return ParticipantRepository.create_by_tournament_id_and_user_id(db, tournament_id, participant.user_id)


    @staticmethod
    def delete(db: Session, tournament_id: int, owner_id: int, participant_id: int) -> None:
        tournament = TournamentRepository.find_by_id(db, tournament_id)

        if not tournament:
            raise TournamentNotFound
        
        if tournament.owner_id != owner_id:
            raise Unauthorized
        
        if not ParticipantRepository.exists_by_id(db, participant_id):
            raise ParticipantNotFound

        return ParticipantRepository.delete_by_id(db, participant_id)


    @staticmethod
    def join(db: Session, tournament_id: int, user_id: int) -> Participant:
        tournament = TournamentRepository.find_by_id(db, tournament_id)

        if not tournament:
            raise TournamentNotFound

        participant_amount = ParticipantRepository.count_by_tournament_id(db, tournament_id)

        if participant_amount >= tournament.capacity.capacity:
            raise TournamentFull
        
        if ParticipantRepository.exists_by_user_id_and_tournament_id(db, user_id, tournament_id):
            raise ParticipantAlreadyAdded

        return ParticipantRepository.create_by_tournament_id_and_user_id(db, tournament_id, user_id)


    @staticmethod
    def leave(db: Session, tournament_id: int, user_id: int) -> None:
        tournament = TournamentRepository.find_by_id(db, tournament_id)

        if not tournament:
            raise TournamentNotFound

        ParticipantRepository.delete_by_tournament_id_and_user_id(db, tournament_id, user_id)


    @staticmethod
    def list(db: Session, tournament_id: int) -> List[Tournament]:
        if not TournamentRepository.find_by_id(db, tournament_id):
            raise TournamentNotFound

        return ParticipantRepository.find_all_by_tournament_id(db, tournament_id)


