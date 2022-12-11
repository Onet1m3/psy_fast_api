from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin
from db.database import engine
from _core.auth_admin import authentication_backend
from repositories.admins.user_admin import UserAdmin
from repositories.admins.post_admin import PostAdmin, PostCategoryAdmin
from _core import authentication
from routers import user, post

app = FastAPI(title="Persefona API")

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(post.router)

# models.Base.metadata.create_all(engine)





admin = Admin(app, engine, base_url='/admin', authentication_backend=authentication_backend, templates_dir="static/templates/admin")
admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
admin.add_view(PostCategoryAdmin)

app.mount("/static", StaticFiles(directory='static'), name='static')