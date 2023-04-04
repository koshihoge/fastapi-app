from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from ..models.company_model import Company
from ..schemas.company_schema import CompanyIn as CompanyInSchema


def read_companies(db: Session) -> List[Company]:
    try:
        items = db.query(Company).all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error.")

    return items


def read_company(db: Session, id: int) -> Company | None:
    try:
        item = db.query(Company).filter_by(id=id).first()
        if item is None:
            raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Record not found.")

    return item


def post_company(db: Session, company: CompanyInSchema) -> Company:
    try:
        model = Company(**company.dict())
        model.created_at = model.updated_at = datetime.now()
        db.add(model)
        db.commit()
        db.flush()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error.")

    return model


def put_company(db: Session, id: int, company: CompanyInSchema) -> Company | None:
    try:
        item = db.query(company).filter_by(id=id).first()
        if item is not None:
            if company.name is not None:
                item.name = company.name
            if company.url is not None:
                item.url = company.url
            item.updated_at = datetime.now()
            db.commit()
            db.flush()
        else:
            raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Record not found.")

    return item


def delete_company(db: Session, id: int) -> Company | None:
    item = db.query(Company).filter_by(id=id).first()
    if item is not None:
        db.delete(item)
        db.commit()
        db.flush()
    else:
        raise

    return item
