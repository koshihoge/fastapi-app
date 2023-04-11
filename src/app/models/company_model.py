from sqlalchemy import Integer, UnicodeText
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base
from .mixins import TimestampMixin


class Company(Base, TimestampMixin):  # type: ignore
    __tablename__ = "companies"
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column("name", UnicodeText)
    url: Mapped[str] = mapped_column("url", UnicodeText)
