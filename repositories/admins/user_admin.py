from sqladmin import ModelView
from db.models import DbUser, DbPostCategory, DbPost


class UserAdmin(ModelView, model=DbUser):
    column_list = [DbUser.id, DbUser.username]

class PostAdmin(ModelView, model=DbPost):
    column_list = [DbPost.id, DbPost.title]
    

class PostCategoryAdmin(ModelView, model=DbPostCategory):
    column_list = [DbPostCategory.id, DbPostCategory.section]
    column_details_exclude_list  = [DbPostCategory.category]
