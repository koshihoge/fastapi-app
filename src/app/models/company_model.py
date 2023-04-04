from sqlalchemy import Column, Integer, UnicodeText

from ..database import Base
from .mixins import TimestampMixin


class Company(Base, TimestampMixin):  # type: ignore
    __tablename__ = "companies"
    id: int | Column[int] = Column("id", Integer, primary_key=True, autoincrement=True)
    name: str | Column[str] = Column("name", UnicodeText)
    url: str | Column[str] = Column("url", UnicodeText)
