from typing import List
from sqlalchemy.orm import Session

from ..models.coin_package import CoinPackage


class CoinPackageRepository:
    @staticmethod
    def find_all(db: Session) -> List[CoinPackage]:
        return db.query(CoinPackage).all()


    @staticmethod
    def find_by_id(db: Session, id: int) -> CoinPackage:
        return db.query(CoinPackage).filter(CoinPackage.id == id).first()