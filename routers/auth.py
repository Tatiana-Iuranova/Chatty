from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import timedelta

from database import get_db
from models import User
from schemas import UserCreate, UserLogin, UserResponse
from security import get_password_hash, verify_password, create_access_token

router = APIRouter()

# Эндпоинт для регистрации пользователя
@router.post("/register", response_model=UserResponse)
async def register_user(user_create: UserCreate, db: AsyncSession = Depends(get_db)):
    # Проверяем, существует ли уже пользователь с таким email
    result = await db.execute(select(User).where(User.email == user_create.email))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")

    # Хешируем пароль
    hashed_password = get_password_hash(user_create.password)
    new_user = User(email=user_create.email, hashed_password=hashed_password, nickname=user_create.nickname)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

# Эндпоинт для авторизации
@router.post("/login", response_model=UserResponse)
async def login_user(user_login: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_login.email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Генерация JWT-токена
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
