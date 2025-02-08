from sqlalchemy.orm import Session
from app.models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user_data):
    new_user = User(
        full_name=user_data.full_name,
        uid=user_data.uid,
        phone=user_data.phone,
        password=hash_password(user_data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_uid(db: Session, uid: str):
    return db.query(User).filter(User.uid == uid).first()
