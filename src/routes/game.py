
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from ..usecases.game import GameUseCase
from ..schemas.game import GameOut
from ..configs.database import get_db



router = APIRouter(prefix='/games', tags=["Games"])


@router.get('', response_model=List[GameOut])
def list(db: Session = Depends(get_db)) -> List[GameOut]:
    return GameUseCase.list(db)