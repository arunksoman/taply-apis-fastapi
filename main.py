from fastapi import FastAPI
from app.user import login
from app.admin import admin
from app import config
from functools import lru_cache
import os
from app.config import get_config

settings = get_config(os.getenv("ENV") or "test")
print(os.getenv("ENV"), settings)
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
print(SQLALCHEMY_DATABASE_URL)

app = FastAPI()
app.include_router(login.router)
app.include_router(admin.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# uvicorn main:app --reload