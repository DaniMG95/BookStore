from fastapi import FastAPI
from app.routers import book, user, author, token, shop
from app.db import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

for router in [author, book, shop, user, token]:
    app.include_router(router.router)

saddsa = 34342
sad = 44
