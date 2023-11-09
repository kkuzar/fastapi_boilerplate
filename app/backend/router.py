import uuid
from http import HTTPStatus

from dotenv import load_dotenv
from fastapi import APIRouter
from starlette.responses import JSONResponse, Response


load_dotenv(verbose=True)

router = APIRouter()


@router.get("/health", tags=["utility"])
async def health():
    mark = str(uuid.uuid4())
    return JSONResponse(
        status_code=HTTPStatus.OK, content={"status": "okay", "id": mark}
    )


@router.get("/", tags=["utility"])
async def root_page():
    return Response(status_code=HTTPStatus.ACCEPTED, content="Curious?")
