from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from repositories.schemas.user_schemas import UserBase, UserDisplay
from db.database import get_db
from repositories.db_models.user_db import create

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("", response_description=Union[UserDisplay, dict])
def create_user(request: UserBase, db: Session=Depends(get_db)):
    return create(db, request)