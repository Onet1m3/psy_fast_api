from fastapi import HTTPException, status
from repositories.schemas.user_schemas import UserBase, UserIsAdmin
from sqlalchemy.orm.session import Session
from db.database import MySuperContextManager
from db.models import DbUser
from _core.hashing import Hash

def create(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=(request.email).strip().lower(),
        password=Hash.bcrypt(request.password)
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email {request.email} already exist")

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {username} not found")

    return user

def is_admin(request: UserIsAdmin):
    email, password = request["email"], request["password"]
    with MySuperContextManager() as db:
        user = db.query(DbUser).filter(DbUser.email==email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not Hash.verify(user.password, password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Access is denied")

    return True

def show_current_user():
    pass