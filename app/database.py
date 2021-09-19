from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from .config import get_config

settings = get_config(os.getenv("ENV") or "test")
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Generator function for dependency injection to fetch a new sesesion on a new request
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()