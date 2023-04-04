from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from ..models.user_model import User
from ..schemas.user_schema import UserIn as userInSchema


def read_users(db: Session) -> List[User]:
    try:
        items = db.query(User).all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error.")

    return items


def read_user(db: Session, username: str) -> User | None:
    try:
        item = db.query(User).filter_by(username=username).first()
        if item is None:
            raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Record not found.")

    return item


def post_user(db: Session, user: userInSchema) -> User:
    try:
        model = User(**user.dict())
        model.created_at = model.updated_at = datetime.now()
        db.add(model)
        db.commit()
        db.flush()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error.")

    return model


def put_user(db: Session, username: str, user: userInSchema) -> User | None:
    try:
        item = db.query(User).filter_by(username=username).first()
        if item is not None:
            if user.full_name is not None:
                item.full_name = user.full_name
            if user.email is not None:
                item.email = user.email
            if user.invalid is not None:
                item.invalid = user.invalid
            item.updated_at = datetime.now()
            db.commit()
            db.flush()
        else:
            raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Record not found.")

    return item


def delete_user(db: Session, username: str) -> User | None:
    item = db.query(User).filter_by(username=username).first()
    if item is not None:
        db.delete(item)
        db.commit()
        db.flush()
    else:
        raise

    return item
