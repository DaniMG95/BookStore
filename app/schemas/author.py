from pydantic import BaseModel
from app.schemas.book import BookSchema


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorSchema(AuthorBase):
    id: str
    books: list[BookSchema] = []

    class Config:
        orm_mode = True


