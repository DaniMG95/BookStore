from fastapi import APIRouter, Depends
from app.schemas.author import AuthorCreate, AuthorSchema
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.author import Author


router = APIRouter(
    prefix="/author",
    tags=["author"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{author_id}", response_model=AuthorSchema)
async def get_author(author_id: int, db: Session = Depends(get_db)):
    db_author = await Author.get_id(db=db, id=author_id)
    return db_author


@router.post("/", response_model=AuthorSchema)
async def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = await Author.create(db=db, **author.dict())
    return db_author


@router.get("/", response_model=list[AuthorSchema])
async def get_all_authors(db: Session = Depends(get_db)):
    authors = await Author.get_all(db=db)
    return authors


@router.delete("/{author_id}")
async def get_author(author_id: int, db: Session = Depends(get_db)):
    await Author.remove_id(db=db, id=author_id)
    return {"details": "Author deleted"}
