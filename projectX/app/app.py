from fastapi import FastAPI

from projectX.app.routers.index import router as index

app = FastAPI()
app.router.include_router(index)
