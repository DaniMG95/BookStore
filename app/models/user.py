from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, Session
from app.models.crud_base import CrudBase
from app.models.book import Book

from app.db import Base, book_users


class User(Base, CrudBase):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=False)

    books = relationship("Book", secondary=book_users, back_populates="owners")

    @classmethod
    async def insert_book(cls, db: Session, user_id: int, book_id: int):
        user = await cls.get_id(id=user_id, db=db)
        book = await Book.get_id(id=book_id, db=db)
        user.books.append(book)
        db.add(user)
        db.commit()

    async def activate_user(self, db: Session):
        await User.update_id(id=self.id, db=db, data_change={"is_active": True})

    @classmethod
    async def get_user_by_email(cls, email: str, db: Session):
        return db.query(cls).filter(cls.email == email).first()
