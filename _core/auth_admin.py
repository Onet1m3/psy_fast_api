from sqladmin.authentication import AuthenticationBackend
from fastapi.requests import Request
from .config import config
from db.database import get_db
from repositories.db_models.user_db import is_admin


class MyBackend(AuthenticationBackend):

    async def login(self, request: Request) -> bool:
        form = await request.form()
        if is_user_admin := is_admin(form):
            request.session.update({"token": "is_admin"})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        print(request.session)
        return "token" in request.session

SECRET_KEY = config("SECRET_KEY")
authentication_backend = MyBackend(secret_key=SECRET_KEY)