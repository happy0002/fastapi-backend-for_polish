from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=50)
    uid: str = Field(..., min_length=3, max_length=20)
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    uid: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=6)
