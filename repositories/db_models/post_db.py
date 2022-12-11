from sqlalchemy.orm.session import Session
from db.models import DbPost


def get_list(db: Session):
    posts = db.query(DbPost).filter(DbPost.is_activ==True).all()
    return posts


