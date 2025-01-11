from pydantic import BaseModel, BaseModel


class GameOut(BaseModel):
    id: int
    name: str
