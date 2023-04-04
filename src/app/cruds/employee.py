from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from ..models.employee_model import Employee
from ..schemas.employee_schema import EmployeeIn as EmployeeInSchema


def read_employees(db: Session) -> List[Employee]:
    try:
        items = db.query(Employee).all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error.")

    return items


def read_employee(db: Session, id: int) -> Employee | None:
    try:
        item = db.query(Employee).filter_by(id=id).first()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Record not found.")

    return item


def post_employee(db: Session, employee: EmployeeInSchema) -> Employee:
    try:
        model = Employee(**employee.dict())
        model.created_at = model.updated_at = datetime.now()
        db.add(model)
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error.")

    return model


def put_employee(db: Session, id: int, employee: EmployeeInSchema) -> Employee | None:
    try:
        item = db.query(Employee).filter_by(id=id).first()
        if item is not None:
            if employee.name is not None:
                item.name = employee.name
            if employee.email is not None:
                item.email = employee.email
            item.updated_at = datetime.now()
            db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Record not found.")

    return item


def delete_employee(db: Session, id: int) -> Employee | None:
    item = db.query(Employee).filter_by(id=id).first()
    if item is not None:
        db.delete(item)
        db.commit()

    return item
