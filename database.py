from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from config import settings

# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/books_db"
# engine = create_engine(DATABASE_URL)

engine = create_async_engine(settings.async_database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Создаём зависимость для работы с БД в FastAPI
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
