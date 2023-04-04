from typing import Annotated, List

from fastapi import Depends, Path
from sqlalchemy.orm import Session

from ...cruds import employee as crud
from ...database import get_db
from ...models.employee_model import Employee
from ...module.custom_class import HandleTrailingSlashRouter
from ...schemas.employee_schema import Employee as EmployeeSchema
from ...schemas.employee_schema import EmployeeIn as EmployeeInSchema

router = HandleTrailingSlashRouter()


@router.get("", response_model=List[EmployeeSchema])  # type: ignore
async def read_employees(db: Session = Depends(get_db)) -> List[Employee]:
    return crud.read_employees(db=db)


@router.get("/{id}", response_model=EmployeeSchema | None)  # type: ignore
async def read_employee(
    id: Annotated[int, Path(title="The ID of the item to get")], db: Session = Depends(get_db)
) -> Employee:
    return crud.read_employee(id=id, db=db)


@router.post("", response_model=EmployeeSchema)  # type: ignore
async def post_employee(
    employee: EmployeeInSchema,
    db: Session = Depends(get_db),
) -> Employee:
    return crud.post_employee(employee=employee, db=db)


@router.put("/{id}", response_model=EmployeeSchema | None)  # type: ignore
async def put_employee(
    id: Annotated[int, Path(title="The ID of the item to update")],
    employee: EmployeeInSchema,
    db: Session = Depends(get_db),
) -> Employee:
    return crud.put_employee(id=id, employee=employee, db=db)


@router.delete("/{id}", response_model=EmployeeSchema | None)  # type: ignore
async def delete_employee(
    id: Annotated[int, Path(title="The ID of the item to delete")],
    db: Session = Depends(get_db),
) -> Employee:
    return crud.delete_employee(id=id, db=db)
