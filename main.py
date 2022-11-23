from fastapi import FastAPI
from sqladmin import Admin
from db import models
from db.database import engine
from _core.admin import UserAdmin

app = FastAPI()

models.Base.metadata.create_all(engine)

from db.models import DbUser



admin = Admin(app, engine, base_url='/admin')

admin.add_view(UserAdmin)