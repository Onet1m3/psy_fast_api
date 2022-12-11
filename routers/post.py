from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from repositories.schemas.post_schemas import PostsDisplay
from db.database import get_db
from repositories.db_models.post_db import get_list
# from _core.auth_backend import get_current_user

router = APIRouter(
    prefix="/post",
    tags=["post"]
)

@router.get("/all", response_model=List[PostsDisplay])
def get_all_posts(db: Session=Depends(get_db)):
    return get_list(db)