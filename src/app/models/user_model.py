from sqlalchemy import Boolean, Column, UnicodeText

from ..database import Base
from .mixins import TimestampMixin


class User(Base, TimestampMixin):  # type: ignore
    __tablename__ = "users"
    username: int | Column[str] = Column("username", UnicodeText, primary_key=True)
    full_name: str | Column[str] = Column("full_name", UnicodeText)
    email: str | Column[str] = Column("email", UnicodeText)
    hashed_password: str | Column[str] = Column("hashed_password", UnicodeText)
    invalid: bool | Column[bool] = Column("invalid", Boolean)
