from typing import Iterator

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from .settings import settings

# DBの設定
# dialect+driver://username:password@host:port/database
DATABASE = "%s://%s:%s@%s:%s/%s" % (
    settings.DB_DRIVER,
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST,
    settings.DB_PORT,
    settings.DB_NAME,
)

print(DATABASE)

engine = create_engine(DATABASE, connect_args={"connect_timeout": 30}, echo=True)  # Trueだと実行のたびにSQLが出力される

# 実際の DB セッション
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = SessionLocal.query_property()


# Dependency Injection用
def get_db() -> Iterator[Session]:
    db = None
    try:
        db = SessionLocal()
        yield db
    except BaseException:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="session open error.")
    finally:
        if db is not None:
            db.close()
