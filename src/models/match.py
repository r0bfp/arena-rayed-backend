from sqlalchemy import Enum, ForeignKey, types, Column
from sqlalchemy.orm import relationship
from .enums import MatchStatus
from src.configs.database import Base


class Match(Base):
    __tablename__ = 'matches'

    id            = Column(types.Integer, primary_key=True, index=True)
    round_number  = Column(types.Integer, nullable=False)
    tournament_id = Column(types.Integer, ForeignKey('tournaments.id'), nullable=False)
    status        = Column(Enum(MatchStatus), nullable=False)
    contested     = Column(types.Boolean, nullable=False, default=False)

    tournament = relationship('Tournament', back_populates='matches')
    players    = relationship('Player', back_populates='match', cascade='all, delete-orphan')


    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}