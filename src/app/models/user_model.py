from sqlalchemy import Boolean, UnicodeText
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base
from .mixins import TimestampMixin


class User(Base, TimestampMixin):  # type: ignore
    __tablename__ = "users"
    username: Mapped[str] = mapped_column("username", UnicodeText, primary_key=True)
    full_name: Mapped[str] = mapped_column("full_name", UnicodeText)
    email: Mapped[str] = mapped_column("email", UnicodeText)
    hashed_password: Mapped[str] = mapped_column("hashed_password", UnicodeText)
    invalid: Mapped[bool] = mapped_column("invalid", Boolean)
