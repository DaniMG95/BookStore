from fastapi import FastAPI
from app.routers import book, user, author, token, shop
from app.db import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

# dasdsaasd
for router in [author, book, shop, user, token]:
    app.include_router(router.router)
