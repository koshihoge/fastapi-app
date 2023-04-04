from datetime import datetime

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None
    email: str | None = None
    invalid: bool | None = None
    created_at: datetime
    updated_at: datetime


class UserIn(User):
    hashed_password: str
