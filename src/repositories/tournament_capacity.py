from typing import List
from sqlalchemy.orm import Session

from ..models.tournament_capacity import TournamentCapacity


class TournamentCapacityRepository:
    @staticmethod
    def find_all(db: Session) -> List[TournamentCapacity]:
        return db.query(TournamentCapacity).all()

    @staticmethod
    def find_by_id(db: Session, id: int) -> TournamentCapacity:
        return db.query(TournamentCapacity).filter(TournamentCapacity.id == id).first()