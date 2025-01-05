from sqlalchemy import types, Column
from sqlalchemy.orm import relationship
from src.configs.database import Base

class TournamentCapacity(Base):
    __tablename__ = "tournament_capacities"

    id       = Column(types.Integer, primary_key=True, index=True)
    capacity = Column(types.Integer, nullable=False)
    price    = Column(types.Integer, nullable=False)

    tournament = relationship("Tournament", back_populates="capacity")

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
