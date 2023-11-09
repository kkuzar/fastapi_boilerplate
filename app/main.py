from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.backend.router import router as viewer_router


app = FastAPI(
    version="0.0.1",
    title="default",
    description="description",
    debug=True,
)


app.include_router(viewer_router)

# Todo, origins need to be done in Envs.
origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
