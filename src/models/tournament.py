from sqlalchemy import ForeignKey, types, Column, Enum
from sqlalchemy.orm import relationship
from .enums import TournamentStatus
from src.configs.database import Base
from datetime import datetime, timezone

class Tournament(Base):
    __tablename__ = 'tournaments'

    id             = Column(types.Integer, primary_key=True, index=True)
    name           = Column(types.String(length=50), nullable=False)
    description    = Column(types.String(length=250))
    starts_in      = Column(types.DateTime, nullable=False)
    ends_in        = Column(types.DateTime, nullable=False)
    status         = Column(Enum(TournamentStatus), default=TournamentStatus.PENDING)
    capacity_id    = Column(types.Integer, ForeignKey('tournament_capacities.id'), nullable=False)
    game_id        = Column(types.Integer, ForeignKey('games.id'), nullable=False)
    owner_id       = Column(types.Integer, ForeignKey('users.id'), nullable=False)
    created_at     = Column(types.DateTime, default=datetime.now(timezone.utc))
    updated_at     = Column(types.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    owner          = relationship('User', back_populates='tournament')
    game           = relationship('Game', back_populates='tournament')
    capacity       = relationship('TournamentCapacity', back_populates='tournament')
    matches        = relationship('Match', back_populates='tournament', cascade='all, delete-orphan')
    participants   = relationship('Participant', back_populates='tournament', cascade='all, delete-orphan')

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
