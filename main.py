from fastapi import FastAPI
from config import settings
from auth import router as auth_router

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# Подключаем маршруты для авторизации

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to Chatty API"}

@app.get("/")
def read_root():
    return {"app_name": settings.APP_NAME, "debug": settings.DEBUG}