
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from ..errors.player import InvalidPlayerStatus, PlayerNotFound
from src.configs.database import get_db
from ..usecases.player import PlayerUseCase
from ..utils.auth import Auth

from ..usecases.match import MatchUseCase
from ..schemas.match import MatchOut
from ..errors.match import MatchNotFound


router = APIRouter(prefix='/matches')


@router.get('/{match_id}', response_model=MatchOut)
def get_one(match_id: int, db: Session = Depends(get_db)) -> MatchOut:
    try:
        return MatchUseCase.get_one(db, match_id)
    except MatchNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.put('/{match_id}/players/ready')
def player_ready(
    match_id: int, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> None:
    try:
        return PlayerUseCase.ready(db, match_id, user_id)
    except InvalidPlayerStatus as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))
    except PlayerNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except MatchNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.put('/{match_id}/players/winner/{winner_id}')
def player_winner(
    match_id: int, 
    winner_id: int, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> None:
    try:
        return PlayerUseCase.set_winner(db, match_id, user_id, winner_id)
    except InvalidPlayerStatus as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    except PlayerNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except MatchNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))