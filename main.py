from fastapi import FastAPI
from sqladmin import Admin
from db import models
from db.database import engine
from repositories.admins.user_admin import UserAdmin
from routers import user

app = FastAPI()

app.include_router(user.router)

models.Base.metadata.create_all(engine)



admin = Admin(app, engine, base_url='/admin')

admin.add_view(UserAdmin)