from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    uid = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
