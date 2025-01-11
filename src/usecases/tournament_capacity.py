
from typing import List
from sqlalchemy.orm import Session

from ..repositories.tournament_capacity import TournamentCapacityRepository
from ..schemas.tournament_capacity import TournamentCapacityOut



class TournamentCapacityUseCase:
    @staticmethod
    def list(db: Session) -> List[TournamentCapacityOut]:
        return TournamentCapacityRepository.find_all(db)

