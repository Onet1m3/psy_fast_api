from pydantic import BaseModel, validator, constr, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v


class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True