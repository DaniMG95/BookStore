from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    category: str
    year: int
    price: int


class BookCreate(BookBase):
    author_id: int


class BookSchema(BookCreate):
    id: int

    class Config:
        orm_mode = True
