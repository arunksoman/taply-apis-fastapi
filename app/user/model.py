from app.database import Base
from sqlalchemy import Integer, Column, String

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(35), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    phone_no = Column(String(20), unique=True, nullable=True)
    passwd = Column(String(200), nullable=False)
    