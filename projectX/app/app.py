from fastapi import FastAPI

from projectX.app.routers.index_router import router as index_router
from projectX.app.routers.auth_router import router as auth_router
from projectX.app.di_container import Container

app = FastAPI()

app.router.include_router(index_router)
app.router.include_router(auth_router)

app.container = Container()
