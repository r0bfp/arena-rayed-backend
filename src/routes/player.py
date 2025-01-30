from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from ..schemas.player import PlayerOpponentOut
from ..configs.database import get_db
from ..utils.auth import Auth
from ..usecases.player import PlayerUseCase


router = APIRouter(prefix='/players')


@router.get('/me/opponents')
def me(
    db: Session = Depends(get_db), 
    user_id = Depends(Auth.is_authenticated)
) -> List[PlayerOpponentOut]:
    return PlayerUseCase.find_opponents(db, user_id)
