from fastapi import FastAPI
from sqladmin import Admin
from db import models
from db.database import engine
from _core.auth_admin import authentication_backend
from repositories.admins.user_admin import UserAdmin
from _core import authentication
from routers import user

app = FastAPI(title="Persefona API")

app.include_router(user.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(engine)





admin = Admin(app, engine, base_url='/admin', authentication_backend=authentication_backend, templates_dir="static/templates/admin")
admin.add_view(UserAdmin)