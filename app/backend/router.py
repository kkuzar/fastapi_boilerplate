import uuid
from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse, Response

router = APIRouter()


@router.get("/health", tags=["utility"])
async def health():
    mark = str(uuid.uuid4())
    return JSONResponse(
        status_code=HTTPStatus.OK, content={"status": "okay", "id": mark}
    )


@router.get("/", tags=["utility"])
async def root_page():
    return Response(status_code=HTTPStatus.OK, content="Curious?")
