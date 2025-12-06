import os
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.backend.router import router as viewer_router


load_dotenv(override=True)


app = FastAPI(
    version="0.0.1",
    title="default",
    description="description",
    debug=True,
)


app.include_router(viewer_router)

def _parse_origins(raw: str | None) -> List[str]:
    if not raw:
        return ["http://localhost", "http://127.0.0.1"]
    return [o.strip() for o in raw.split(",") if o.strip()]


origins = _parse_origins(os.getenv("ALLOW_ORIGINS"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
