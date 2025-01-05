from pydantic import AliasPath, BaseModel, Field
from datetime import datetime


class User(BaseModel):
    username: str
    points: int


class ParticipantIn(BaseModel):
    user_id: int


class ParticipantOut(BaseModel):
    id: int
    user_participant: User = Field(validation_alias=AliasPath('user'))
    added_at: datetime

    class Config:
        from_attributes = True