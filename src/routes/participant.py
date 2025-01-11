from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from ..errors.user import UserNotFound

from ..usecases.participant import ParticipantUseCase

from ..errors.participant import ParticipantAlreadyAdded, ParticipantNotFound
from src.errors.tournament import TournamentFull, TournamentNotFound, Unauthorized
from src.schemas.participant import ParticipantIn, ParticipantOut
from src.usecases.participant import ParticipantUseCase
from src.configs.database import get_db
from src.utils.auth import Auth


router = APIRouter(prefix='/tournaments', tags=["Tournaments"])


@router.post('/{tournament_id}/participants', response_model=ParticipantOut, status_code=status.HTTP_201_CREATED)
def create(
    tournament_id: int, 
    request: ParticipantIn, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> ParticipantOut:
    try: 
        return ParticipantUseCase.create(db, tournament_id, user_id, request)
    except TournamentNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except ParticipantAlreadyAdded as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))
    except UserNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except Unauthorized as err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(err))
    except TournamentFull as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))


@router.delete('/{tournament_id}/participants/{participant_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(
    tournament_id: int, 
    participant_id: int, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> None:
    try: 
        return ParticipantUseCase.delete(db, tournament_id, user_id, participant_id)
    except TournamentNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except ParticipantNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except Unauthorized as err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(err))


@router.post('/{tournament_id}/join', response_model=ParticipantOut, status_code=status.HTTP_201_CREATED)
def join(
    tournament_id: int, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> ParticipantOut:
    try:
        return ParticipantUseCase.join(db, tournament_id, user_id)
    except TournamentNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except ParticipantAlreadyAdded as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    except TournamentFull as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))


@router.delete('/{tournament_id}/leave', status_code=status.HTTP_204_NO_CONTENT)
def leave(
    tournament_id: int, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> None:
    try:
        ParticipantUseCase.leave(db, tournament_id, user_id)
    except TournamentNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.get('/{tournament_id}/participants', response_model=List[ParticipantOut])
def list(
    tournament_id: int,
    db: Session = Depends(get_db), 
) -> ParticipantOut:
    try:
        return ParticipantUseCase.list(db, tournament_id)
    except TournamentNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
