from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db import Base
from app.models.crud_base import CrudBase


class Stock(Base, CrudBase):
    __tablename__ = "stock"

    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    shop_id = Column(Integer, ForeignKey("shops.id"), primary_key=True)
    amount = Column(Integer)

    book = relationship("Book", back_populates="shops")
    shop = relationship("Shop", back_populates="books")
