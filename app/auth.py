from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from app.models import User
from app.schemas import UserCreate, UserLogin
from app.crud import create_user, get_user_by_uid, verify_password
from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def signup(user: UserCreate, db: Session):
    existing_user = db.query(User).filter((User.uid == user.uid) | (User.phone == user.phone)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with UID or Phone already exists")

    return create_user(db, user)

def login(user: UserLogin, db: Session):
    existing_user = get_user_by_uid(db, user.uid)
    if not existing_user or not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Invalid UID or password")
    
    return {"message": "Login successful", "user_id": existing_user.id}
