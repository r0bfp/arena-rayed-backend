
from typing import List
from sqlalchemy.orm import Session

from ..errors.coins import CoinPackageNotFound
from ..repositories.user import UserRepository
from ..repositories.coin import CoinPackageRepository
from ..models.coin_package import CoinPackage


class CoinPackageUseCase:
    @staticmethod
    def list(db: Session) -> List[CoinPackage]:
        return CoinPackageRepository.find_all(db)


    @staticmethod
    def buy(db: Session, user_id: int, package_id: int) -> CoinPackage:
        package = CoinPackageRepository.find_by_id(db, package_id)

        if not package:
            return CoinPackageNotFound

        user = UserRepository.find_by_id(db, user_id)

        user.coins += package.amount

        UserRepository.create_or_update(db, user.as_dict())

        return package
