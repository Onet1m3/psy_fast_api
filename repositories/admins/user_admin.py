from sqladmin import ModelView
from db.models import DbUser


class UserAdmin(ModelView, model=DbUser):
    column_list = [DbUser.id, DbUser.username]
