from fastapi import APIRouter, Depends
from app.schemas.book import BookSchema, BookCreate
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.book import Book
from app.models.author import Author
from app.models.shop import Shop
from app.models.stock import Stock


router = APIRouter(
    prefix="/book",
    tags=["book"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{book_id}", response_model=BookSchema)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = await Book.get_id(db=db, id=book_id)
    return db_book


@router.post("/", response_model=BookSchema)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = await Book.create(db=db, **book.dict())
    return db_book


@router.get("/", response_model=list[BookSchema])
async def get_books(author: str = None, city: str = None, db: Session = Depends(get_db)):
    query = db.query(Book).join(Stock, Shop, Author)
    if author:
        query = query.filter(Author.name == author)
    if city:
        query = query.filter(Shop.city == city)
    books = query.all()
    return books


@router.delete("/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    await Book.remove_id(db=db, id=book_id)
    return {"details": "Book deleted"}


@router.patch("/{book_id}", response_model=BookSchema)
async def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    await Book.update_id(db=db, id=book_id, data_change=book.dict())
    return await Book.get_id(db=db, id=book_id)
