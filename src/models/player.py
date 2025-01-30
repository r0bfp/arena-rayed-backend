from sqlalchemy import ForeignKey, types, Column, Enum
from sqlalchemy.orm import relationship
from .enums import PlayerStatus
from src.configs.database import Base


class Player(Base):
    __tablename__ = 'players'

    id        = Column(types.Integer, primary_key=True, index=True)
    match_id  = Column(types.Integer, ForeignKey('matches.id'), nullable=False)
    user_id   = Column(types.Integer, ForeignKey('users.id'), nullable=False)
    is_winner = Column(types.Boolean, nullable=False, default=False)
    status    = Column(Enum(PlayerStatus), nullable=False)

    user      = relationship('User', foreign_keys=[user_id])
    match     = relationship('Match', back_populates='players')


    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}