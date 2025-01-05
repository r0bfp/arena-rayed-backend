from typing import List
from sqlalchemy.orm import Session

from ..models.tournament import Tournament


class TournamentRepository:
    @staticmethod
    def update_status(db: Session, tournament_id: int, status: str) -> Tournament:
        tournament = Tournament(id=tournament_id, status=status)

        db.merge(tournament)
        db.commit()

        return tournament


    @staticmethod
    def find_all(db: Session) -> List[Tournament]:
        return db.query(Tournament).all()


    @staticmethod
    def find_by_id(db: Session, id: int) -> Tournament:
        return db.query(Tournament).filter(Tournament.id == id).first()


    @staticmethod
    def exists_by_name(db: Session, name: str) -> Tournament:
        return db.query(Tournament).filter(Tournament.name == name).first() is not None


    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        tournament = db.query(Tournament).filter(Tournament.id == id).first()

        db.delete(tournament)
        db.commit()


    @staticmethod
    def create_or_update(db: Session, tournament: dict) -> Tournament:
        tournament = Tournament(**tournament)

        if tournament.id:
            db.merge(tournament)
        else:
            db.add(tournament)

        db.commit()

        return tournament