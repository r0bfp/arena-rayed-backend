from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from ..schemas.match import MatchOut
from src.errors.tournament_capacity import CapacityNotFound
from src.errors.game import GameNotFound
from src.errors.tournament import InvalidTournamentDuration, InvalidTournamentStatus, NotEnoughCoins, TournamentAlreadyExists, TournamentCapacityNotReached, TournamentNotFound, Unauthorized
from src.schemas.tournament import TournamentIn, TournamentOut
from src.configs.database import get_db
from src.utils.auth import Auth
from src.usecases.tournament import TournamentUseCase


router = APIRouter(prefix='/tournaments', tags=["Tournaments"])


@router.get('', response_model=List[TournamentOut])
def list(db: Session = Depends(get_db)) -> List[TournamentOut]:
    return TournamentUseCase.list(db)


@router.post('', response_model=TournamentOut, status_code=status.HTTP_201_CREATED)
def create(
    request: TournamentIn, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> TournamentOut:
    try: 
        return TournamentUseCase.create(db, request, user_id)
    except TournamentAlreadyExists as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    except InvalidTournamentDuration as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    except GameNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except CapacityNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except NotEnoughCoins as err:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=str(err))


@router.delete('/{tournament_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(
    tournament_id: int,
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> None:
    try: 
        return TournamentUseCase.delete(db, tournament_id, user_id)
    except TournamentNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except Unauthorized as err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(err))


@router.post('/{tournament_id}/start', status_code=status.HTTP_200_OK)
def start(
    tournament_id: int,
    db: Session = Depends(get_db), 
    user_id: int = Depends(Auth.is_authenticated)
) -> None:
    try: 
        return TournamentUseCase.start(db, tournament_id, user_id)
    except TournamentNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    except Unauthorized as err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(err))
    except InvalidTournamentStatus as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    except TournamentCapacityNotReached as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


@router.get('/{tournament_id}/matches', response_model=List[MatchOut])
def list_matches(tournament_id: int, db: Session = Depends(get_db)) -> List[MatchOut]:
    return TournamentUseCase.list_all_matches_by_tournament(db, tournament_id)


# @router.put('/{tournament_id}/generate-next-round')
# def list_matches(tournament_id: int, db: Session = Depends(get_db)):
#     TournamentUseCase.generate_next_round_if_prev_finished(db, tournament_id)
#     return 'OK'