
from typing import List
from sqlalchemy.orm import Session

from ..schemas.game import GameOut

from ..repositories.game import GameRepository


class GameUseCase:
    @staticmethod
    def list(db: Session) -> List[GameOut]:
        return GameRepository.find_all(db)

