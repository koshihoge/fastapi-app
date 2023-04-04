# from datetime import datetime
from datetime import datetime

from pydantic import BaseModel


class CompanyIn(BaseModel):
    name: str | None
    url: str | None


class Company(BaseModel):
    id: int
    name: str
    url: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
