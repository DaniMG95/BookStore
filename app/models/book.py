from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.crud_base import CrudBase
from app.db import Base, book_users


class Book(Base, CrudBase):
    __tablename__ = "books"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    category = Column(String(100))
    year = Column(Integer)
    price = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")
    owners = relationship("User", secondary=book_users, back_populates="books")
    shops = relationship("Stock", back_populates="book")
