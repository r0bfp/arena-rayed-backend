from sqlalchemy.orm import Session

from src.models.participant import Participant


class ParticipantRepository:
    @staticmethod
    def create_by_tournament_id_and_user_id(db: Session, tournament_id: int, user_id: int) -> Participant:
        participant = Participant(tournament_id=tournament_id, user_id=user_id)

        db.add(participant)
        db.commit()

        return participant


    @staticmethod
    def delete_by_tournament_id_and_user_id(db: Session, tournament_id: int, participant_id: int) -> None:
        participant = db.query(Participant).filter(
            Participant.tournament_id == tournament_id,
            Participant.user_id == participant_id
        ).first()

        db.delete(participant)
        db.commit()


    @staticmethod
    def find_all_by_tournament_id(db: Session, tournament_id: int) -> list[Participant]:
        return db.query(Participant).filter(Participant.tournament_id == tournament_id).all()


    @staticmethod
    def exists_by_id(db: Session, participant_id: int) -> bool:
        return db.query(Participant).filter(Participant.id == participant_id).first() is not None
    

    @staticmethod
    def delete_by_id(db: Session, participant_id: int) -> bool:
        participant = db.query(Participant).filter(Participant.id == participant_id).first()

        db.delete(participant)
        db.commit()


    @staticmethod
    def exists_by_user_id_and_tournament_id(db: Session, user_id: int, tournament_id: int) -> bool:
        return db.query(Participant).filter(
            Participant.tournament_id == tournament_id,
            Participant.user_id == user_id
        ).first() is not None


    @staticmethod
    def count_by_tournament_id(db: Session, tournament_id: int) -> int:
        return db.query(Participant).filter(Participant.tournament_id == tournament_id).count()
    
