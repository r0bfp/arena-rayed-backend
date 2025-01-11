
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from ..errors.coins import CoinPackageNotFound

from ..utils.auth import Auth
from ..usecases.coin import CoinPackageUseCase
from ..schemas.coin import CoinsOut
from ..configs.database import get_db



router = APIRouter(prefix='/coins', tags=["Coins Packages"])


@router.get('/packages', response_model=List[CoinsOut])
def list(db: Session = Depends(get_db)) -> List[CoinsOut]:
    return CoinPackageUseCase.list(db)


@router.post('/packages/{package_id}/buy', response_model=CoinsOut, status_code=status.HTTP_201_CREATED)
def buy_coins(
    package_id: int, 
    user_id: int = Depends(Auth.is_authenticated),
    db: Session = Depends(get_db)
) -> CoinsOut:
    try:
        return CoinPackageUseCase.buy(db, user_id, package_id)
    except CoinPackageNotFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

