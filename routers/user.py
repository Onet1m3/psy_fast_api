from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from repositories.schemas.user_schemas import UserBase, UserDisplay, UserAuth
from db.database import get_db
from repositories.db_models.user_db import create, show_current_user
from _core.auth_backend import get_current_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("", response_model=Union[UserDisplay, dict])
def create_user(request: UserBase, db: Session=Depends(get_db)):
    return create(db, request)

@router.get("/me", response_model=UserDisplay)
def get_current_user(db: Session=Depends(get_db), current_user: UserAuth=Depends(get_current_user)):
    return current_user