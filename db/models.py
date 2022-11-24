from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)


class PostCategory(Base):
    __tablename__ = "post_category"
    id = Column(Integer, primary_key=True)
    section = Column(String, unique=True)
    is_activ = Column(Boolean, default=True)


class Post(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True)
#     subject = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name='Выбор раздела', related_name='baner')
    title = Column(String, unique=True)
#     image = models.ImageField("Баннер", upload_to='img/banner', null=True, blank=True)
    is_activ = Column(Boolean, default=True)
    text = Column(Text)
    created_at = Column(DateTime)
#     slug = models.SlugField('URL', max_length=50, default="diary")