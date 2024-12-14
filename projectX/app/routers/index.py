from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='projectX/templates')

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request})

