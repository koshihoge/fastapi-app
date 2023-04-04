from typing import cast

from sqlalchemy import Column, ForeignKey, Integer, UnicodeText
from sqlalchemy.orm import relationship

from app.models.company_model import Company

from ..database import Base
from .mixins import TimestampMixin


class Employee(Base, TimestampMixin):  # type: ignore
    __tablename__ = "employees"
    id: int | Column[int] = Column("id", Integer, primary_key=True, autoincrement=True)
    name: str | Column[str] = Column("name", UnicodeText)
    email: str | Column[str] = Column("email", UnicodeText)
    company_id: int | Column[int] = Column("company_id", Integer, ForeignKey("companies.id"))

    company = cast(Company, relationship("Company"))  # テーブル名ではなくクラス名になるので注意！
