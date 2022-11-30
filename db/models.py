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


class DbPostCategory(Base):
    __tablename__ = "post_category"
    id = Column(Integer, primary_key=True)
    section = Column(String, unique=True)
    is_activ = Column(Boolean, default=True)
    category = relationship("DbPost", back_populates="post_category")

    def __str__(self) -> str:
        return f"{self.section}"


class DbPost(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    image =  Column(String, nullable=True)
    is_activ = Column(Boolean, default=True)
    text = Column(Text)
    created_at = Column(DateTime)
    post_category_id = Column(Integer, ForeignKey("post_category.id"))
    post_category = relationship("DbPostCategory", back_populates="category")
    # slug = Column(String, nullable=True)