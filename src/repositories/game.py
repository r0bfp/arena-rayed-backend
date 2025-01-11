from typing import List
from sqlalchemy.orm import Session

from ..models.game import Game


class GameRepository:
    @staticmethod
    def find_all(db: Session) -> List[Game]:
        return db.query(Game).all()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Game).filter(Game.id == id).first() is not None