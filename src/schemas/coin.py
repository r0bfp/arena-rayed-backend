from typing import List, Optional
from pydantic import BaseModel, BaseModel


class CoinsOut(BaseModel):
    id: int
    amount: int
    price: float
