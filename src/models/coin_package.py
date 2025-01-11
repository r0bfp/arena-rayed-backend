from sqlalchemy import types, Column
from src.configs.database import Base


class CoinPackage(Base):
    __tablename__ = 'coins_packages'

    id     = Column(types.Integer, primary_key=True, index=True)
    amount = Column(types.Float, nullable=False)
    price  = Column(types.Float, nullable=False)


    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
