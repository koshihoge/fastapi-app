from typing import Annotated, List

from fastapi import Depends, Path
from sqlalchemy.orm import Session

from ...cruds import company as crud
from ...database import get_db
from ...models.company_model import Company
from ...module.custom_class import HandleTrailingSlashRouter
from ...schemas.company_schema import Company as CompanySchema
from ...schemas.company_schema import CompanyIn as CompanyInSchema

router = HandleTrailingSlashRouter()


@router.get("", response_model=List[CompanySchema])  # type: ignore
async def read_companies(db: Session = Depends(get_db)) -> List[Company]:
    return crud.read_companies(db=db)


@router.get("/{id}", response_model=CompanySchema | None)  # type: ignore
async def read_company(
    id: Annotated[int, Path(title="The ID of the item to get")], db: Session = Depends(get_db)
) -> Company:
    return crud.read_company(id=id, db=db)


@router.post("", response_model=CompanySchema)  # type: ignore
async def post_company(
    company: CompanyInSchema,
    db: Session = Depends(get_db),
) -> Company:
    return crud.post_company(company=company, db=db)


@router.put("/{id}", response_model=CompanySchema | None)  # type: ignore
async def put_company(
    id: Annotated[int, Path(title="The ID of the item to update")],
    company: CompanyInSchema,
    db: Session = Depends(get_db),
) -> CompanySchema:
    return crud.put_company(id=id, company=company, db=db)


@router.delete("/{id}", response_model=CompanySchema | None)  # type: ignore
async def delete_company(
    id: Annotated[int, Path(title="The ID of the item to delete")],
    db: Session = Depends(get_db),
) -> CompanySchema:
    return crud.delete_company(id=id, db=db)
