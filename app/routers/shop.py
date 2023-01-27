from fastapi import APIRouter, Depends
from app.schemas.shop import ShopSchema, ShopCreate, StockCreate
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.shop import Shop
from app.models.book import Book
from app.models.stock import Stock
from app.models.author import Author


router = APIRouter(
    prefix="/shop",
    tags=["shop"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{shop_id}", response_model=ShopSchema)
async def get_shop(shop_id: int, db: Session = Depends(get_db)):
    db_shop = await Shop.get_id(db=db, id=shop_id)
    return db_shop


@router.post("/", response_model=ShopSchema)
async def create_shop(shop: ShopCreate, db: Session = Depends(get_db)):
    db_shop = await Shop.create(db=db, **shop.dict())
    return db_shop


@router.get("/", response_model=list[ShopSchema])
async def get_shops(title: str = None, author: str = None, db: Session = Depends(get_db)):
    query = db.query(Shop).join(Stock, Book, Author)
    if title:
        query = query.filter(Book.name == title)
    if author:
        query = query.filter(Author.name == author)
    shops = query.all()
    return shops


@router.delete("/{shop_id}")
async def get_shop(shop_id: int, db: Session = Depends(get_db)):
    await Shop.remove_id(db=db, id=shop_id)
    return {"details": "Shop deleted"}


@router.post("/{shop_id}")
async def create_stock(shop_id: int, stock: StockCreate, db: Session = Depends(get_db)):
    shop = await Shop.get_id(db=db, id=shop_id)
    book = await Book.get_id(db=db, id=stock.book_id)
    await Stock.create(db=db, shop=shop, book=book, amount=stock.amount)
    return {"details": "stock created"}
