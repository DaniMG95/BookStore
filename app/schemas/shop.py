from pydantic import BaseModel
from app.schemas.book import BookSchema


class StockSchema(BaseModel):
    amount: int
    book: BookSchema

    class Config:
        orm_mode = True


class ShopBase(BaseModel):
    name: str
    city: str


class ShopCreate(ShopBase):
    pass


class ShopSchema(ShopBase):
    id: int
    books: list[StockSchema] = []

    class Config:
        orm_mode = True


class StockCreate(BaseModel):
    book_id: int
    amount: int
