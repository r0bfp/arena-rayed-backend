from pydantic import BaseModel, BaseModel


class TournamentCapacityOut(BaseModel):
    id: int
    capacity: int
    price: int
