from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.crud_base import CrudBase

from app.db import Base


class Shop(Base, CrudBase):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    city = Column(String(100))
    books = relationship("Stock", back_populates="shop")
