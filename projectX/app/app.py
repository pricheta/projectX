import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from projectX.app.routers.index_router import router as index_router
from projectX.app.routers.auth_router import router as auth_router
from projectX.app.di_container import Container

app = FastAPI()

app.router.include_router(index_router)
app.router.include_router(auth_router)

app.container = Container()

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")
