from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from db.database import get_db
from sqlalchemy.orm.session import Session
from db.models import DbUser
from _core.hashing import Hash
from _core.auth_backend import create_access_token
from fastapi.param_functions import Form
from typing import Any, Dict, List, Optional, Union

router = APIRouter(
    tags=["authentication"]
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    print(request)
    user = db.query(DbUser).filter(DbUser.username==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    access_token = create_access_token(data={'username': user.username})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username
    }
