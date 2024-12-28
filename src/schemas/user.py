from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    coins: int
    points: int


class UserIn(UserBase):
    coins: int = 0
    points: int = 0
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True