from fastapi import APIRouter, Depends, Security
from app.auth import get_current_active_user, get_password_hash
from app.schemas.user import UserCreate, UserSchema
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{user_id}", response_model=UserSchema)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await User.get_id(db=db, id=user_id)
    return db_user


@router.get("/auth/me", response_model=UserSchema)
async def get_user_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/", response_model=UserSchema)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user.password = get_password_hash(user.password)
    db_user = await User.create(db=db, **user.dict())
    return db_user


@router.get("/", response_model=list[UserSchema])
async def get_all_users(db: Session = Depends(get_db)):
    users = await User.get_all(db=db)
    return users


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    await User.remove_id(db=db, id=user_id)
    return {"details": "User deleted"}


@router.post("/{book_id}", response_model=UserSchema)
async def buy_book(
    book_id: int, db: Session = Depends(get_db), current_user: User = Security(get_current_active_user, scopes=["buy"])
):
    await User.insert_book(db=db, user_id=current_user.id, book_id=book_id)
    db_user = await User.get_id(db=db, id=current_user.id)
    return db_user


@router.put("/activate/{user_id}", response_model=UserSchema)
async def activate_user(user_id, db: Session = Depends(get_db)):
    user = await User.get_id(id=user_id, db=db)
    await user.activate_user(db=db)
    return await User.get_id(id=user_id, db=db)
