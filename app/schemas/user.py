from pydantic import BaseModel
from app.schemas.book import BookSchema


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str
    is_active: bool = False


class UserSchema(UserBase):
    id: int
    is_active: bool
    books: list[BookSchema] = []

    class Config:
        orm_mode = True