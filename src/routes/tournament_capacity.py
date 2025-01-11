
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from ..usecases.tournament_capacity import TournamentCapacityUseCase
from ..schemas.tournament_capacity import TournamentCapacityOut
from ..configs.database import get_db



router = APIRouter(prefix='/tournament_capacities', tags=["Tournament Capacities"])


@router.get('', response_model=List[TournamentCapacityOut])
def list(db: Session = Depends(get_db)) -> List[TournamentCapacityOut]:
    return TournamentCapacityUseCase.list(db)