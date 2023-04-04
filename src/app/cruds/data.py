import io
import os

from boto3.session import Session
from fastapi import HTTPException, Response
from mypy_boto3_s3.client import S3Client
from PIL import Image
from sqlalchemy.orm import Session as OrmSession
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from ..settings import settings

client: S3Client = Session().client(service_name="s3", region_name=settings.REGION_NAME)


def read_data(db: OrmSession) -> Response:
    try:
        print("crud: read_data start.")
        path = os.path.abspath("./src/app/resources/image001.jpg")
        img = Image.open(path)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="JPEG")
        print("crud: read_data end.")
        return Response(content=img_byte_arr.getvalue(), media_type="image/jpeg")
    except BaseException as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="File not found.")


def read_one_data(db: OrmSession, article_id: str, plan_id: int) -> Response:
    try:
        print("crud: read_one_data start.")

        if settings.BUCKET_NAME is None:
            raise BaseException("バケット名が設定されていません！")

        response = client.get_object(
            Bucket=settings.BUCKET_NAME,
            Key=f"{article_id}/{plan_id}/images/_001_plan.JPG",
        )
        print("crud: read_one_data end.")
        return Response(content=response["Body"].read(), media_type="image/jpeg")
    except BaseException as e:
        print(e)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="File not found.")
