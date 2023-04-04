# from datetime import datetime
from datetime import datetime

from pydantic import BaseModel


class EmployeeIn(BaseModel):
    name: str | None
    email: str | None


class Employee(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
