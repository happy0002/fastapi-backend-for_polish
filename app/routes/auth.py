from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserLogin
from app.auth import signup, login, get_db

router = APIRouter()

@router.post("/auth/signup")
def signup_route(user: UserCreate, db: Session = Depends(get_db)):
    return signup(user, db)

@router.post("/auth/login")
def login_route(user: UserLogin, db: Session = Depends(get_db)):
    return login(user, db)
