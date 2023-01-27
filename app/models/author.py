from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base
from app.models.crud_base import CrudBase


class Author(Base, CrudBase):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    books = relationship("Book", back_populates="author")
