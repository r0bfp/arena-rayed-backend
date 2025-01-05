from sqlalchemy import types, Column
from src.configs.database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Game(Base):
    __tablename__ = "games"

    id         = Column(types.Integer, primary_key=True, index=True)
    name       = Column(types.String(200), nullable=False)
    created_at = Column(types.DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(types.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    tournament = relationship('Tournament', back_populates='game')

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
