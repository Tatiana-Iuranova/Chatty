from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

#Users
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    nickname: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    nickname: str

    class Config:
        from_attributes = True