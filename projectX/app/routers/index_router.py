from typing import Annotated

from fastapi import Request, Security
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates

from projectX.models.user import User
from projectX.dependencies.get_current_user import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory='projectX/templates')
tag = "main"

@router.get("/", tags=[tag])
def index(request: Request, user: Annotated[User, Security(get_current_user)]):
    return templates.TemplateResponse(name='index.html', context={'request': request, "user": user})

