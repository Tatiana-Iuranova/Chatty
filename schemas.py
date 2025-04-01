from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

#Users
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True

#Posts


# Base.metadata.create_all(bind=engine)


class PostCreate(BaseModel):
    title: str
    content: str


class PostResponse(PostCreate):
    id: int
    author_id: int

    class Config:
        from_attributes = True