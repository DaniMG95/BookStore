from sqlalchemy import create_engine, Table, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.const import HOST_DB, USER_DB, PASSWORD_DB

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://%s:%s@%s/db" % (USER_DB, PASSWORD_DB, HOST_DB)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

book_users = Table(
    "book_users",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
