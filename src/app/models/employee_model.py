from typing import cast

from sqlalchemy import ForeignKey, Integer, UnicodeText
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.company_model import Company

from ..database import Base
from .mixins import TimestampMixin


class Employee(Base, TimestampMixin):  # type: ignore
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column("name", UnicodeText)
    email: Mapped[str] = mapped_column("email", UnicodeText)
    company_id: Mapped[int] = mapped_column("company_id", Integer, ForeignKey("companies.id"))

    company = cast(Company, relationship("Company"))  # テーブル名ではなくクラス名になるので注意！
