# Chatty
 Социальная сеть «Chatty» — учебная платформа, предназначенная для обмена контентом между  пользователями, общения и получения персонализированных рекомендаций. Платформа позволяет  пользователям создавать собственные посты, делиться изображениями, ставить лайки и  комментировать публикации других участников.


1. Create virtual environment "python -m venv .venv"
2. load virtual environment ".venv\Scripts\activate"
3. load necessary libraries "pip install -r requirements.txt"
4. Apply 'alembic revision --autogenerate -m "12e256d50854добавилтаблицу_users_and_post.py"'
5.   Apply migration "alembic upgrade head" 
6.  Start the server "uvicorn main:app --reload"