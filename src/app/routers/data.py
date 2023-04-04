import os
import shutil
from datetime import datetime
from pathlib import Path

import requests
from fastapi import Depends, File, HTTPException, Response, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from ..cruds import data as crud
from ..database import get_db
from ..module.custom_class import HandleTrailingSlashRouter
from ..module.send_email import send_system_mail

router = HandleTrailingSlashRouter()


@router.get("")  # type: ignore
async def read_data(db: Session = Depends(get_db)) -> Response:
    print("router: read_data entry.")
    return crud.read_data(db=db)


@router.get("/plan/{article_id}/{plan_id}")  # type: ignore
async def read_one_data(article_id: str, plan_id: int, db: Session = Depends(get_db)) -> Response:
    print("router: read_one_data entry.")
    return crud.read_one_data(article_id=article_id, plan_id=plan_id, db=db)


@router.post("/sendmail")  # type: ignore
async def send_mail(to_email: str, db: Session = Depends(get_db)) -> dict[str, str]:
    if send_system_mail(to_email=to_email, message="メッセージ本文", subject="メッセージタイトル"):
        return {"status": "SUCCESS"}
    else:
        return {"status": "FAILED"}


@router.post("/compress")  # type: ignore
async def file_compress(db: Session = Depends(get_db)) -> Response:
    try:
        path = shutil.make_archive(
            "./src/app/resources/image001.zip",
            format="zip",
            root_dir="./src/app/resources/",
        )
        return Response(content=f"path: {path}")
    except BaseException as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="File not found.")


@router.get("/zipcode")  # type: ignore
async def zip_code(zip_code: str, db: Session = Depends(get_db)) -> Response:
    try:
        url = "https://zipcloud.ibsnet.co.jp/api/search"
        payload = {"zipcode": zip_code}
        res = requests.get(url, params=payload)
        return Response(content=res.text)
    except BaseException as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="File not found.")


@router.get("/filesize")  # type: ignore
async def file_size(db: Session = Depends(get_db)) -> Response:
    try:
        size = os.path.getsize("./src/app/resources/image001.jpg")
        return Response(content=f"size: {size}")
    except BaseException as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="File not found.")


@router.post("uploadfile")  # type: ignore
async def get_uploadfile(upload_file: UploadFile = File(...)) -> Response:
    try:
        path = f"./src/app/files/{upload_file.filename}"
        with open(path, "w+b") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
        return Response(content=f"filename: {path}, type:{upload_file.content_type}")
    except BaseException as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="File not found.")


@router.get("/get_file/{filename:path}")  # type: ignore
async def get_file(filename: str) -> FileResponse:
    """任意ファイルのダウンロード"""
    current = Path()
    file_path = current / "src/app" / "files" / filename

    print(file_path)

    now = datetime.now()

    response = FileResponse(path=file_path, filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}")

    return response
