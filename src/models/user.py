from sqlalchemy import types, Column
from src.configs.database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id                    = Column(types.Integer, primary_key=True, index=True)
    username              = Column(types.String(100), nullable=False)
    password              = Column(types.String(200), nullable=False)
    email                 = Column(types.String(200), nullable=False)
    coins                 = Column(types.Integer, nullable=False)
    points                = Column(types.Integer, nullable=False)
    created_at            = Column(types.DateTime, default=datetime.now(timezone.utc))
    updated_at            = Column(types.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    tournament            = relationship('Tournament', back_populates='owner')
    participate           = relationship('Participant', back_populates='user')
    playing               = relationship('Player', foreign_keys='Player.user_id', back_populates='user')

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}