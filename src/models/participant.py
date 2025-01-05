from sqlalchemy import ForeignKey, types, Column
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from src.configs.database import Base


class Participant(Base):
    __tablename__ = 'users_tournaments'

    id            = Column(types.Integer, primary_key=True, index=True)
    user_id       = Column(types.Integer, ForeignKey('users.id'), nullable=False)
    tournament_id = Column(types.Integer, ForeignKey('tournaments.id'), nullable=False)
    added_at      = Column(types.DateTime, default=datetime.now(timezone.utc))

    user = relationship('User', back_populates='participate')
    tournament = relationship('Tournament', back_populates='participants')

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
