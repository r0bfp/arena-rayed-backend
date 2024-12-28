from sqlalchemy import types, Column
from src.configs.database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"

    id: int              = Column(types.Integer, primary_key=True, index=True)
    username: str        = Column(types.String(100), nullable=False)
    password: str        = Column(types.String(200), nullable=False)
    email: str           = Column(types.String(200), nullable=False)
    coins: int           = Column(types.Integer, nullable=False)
    points: int          = Column(types.Integer, nullable=False)
    created_at: datetime = Column(types.DateTime, default=datetime.now(timezone.utc))
    updated_at: datetime = Column(types.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))


    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
