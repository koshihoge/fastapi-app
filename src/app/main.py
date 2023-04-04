from fastapi import APIRouter, FastAPI

# from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from .routers import datasys

router = APIRouter()
router.include_router(
    datasys.user_router,
    prefix="",
    tags=["User"],
)
router.include_router(
    datasys.employee_router,
    prefix="/employees",
    tags=["社員"],
)
router.include_router(
    datasys.company_router,
    prefix="/companies",
    tags=["会社"],
)
# router.include_router(data.router, prefix=f"{route_name}/data", tags=["data"])

description = """
FastAPIのテンプレートです. 🚀

## Employees

You can **read put employee**.

You can also:

* **Create employee** (_not implemented_).
* **Update employee** (_not implemented_).
* **Delete employee** (_not implemented_).

## Companies

You can **read put company**.

You can also:

* **Create company** (_not implemented_).
* **Update company** (_not implemented_).
* **Delete company** (_not implemented_).
"""

app = FastAPI(title="fastapi-app", description=description, version="0.0.1", default_response_class=ORJSONResponse)

# origins = ["http://localhost", "http://localhost:8080"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(router)
