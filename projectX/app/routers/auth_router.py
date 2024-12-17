from typing import Annotated

from fastapi import Depends, Query
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from dependency_injector.wiring import Provide, inject

from projectX.app.services.auth_service import AuthService
from projectX.app.di_container import Container

router = APIRouter()
templates = Jinja2Templates(directory='projectX/templates')
tag = "auth"


@router.post(f"/{tag}/register/", tags=[tag])
@inject
def register(
    login: Annotated[str, Query(max_length=20, min_length=5, description="Логин нового пользователя")],
    password: Annotated[str, Query(max_length=20, min_length=5, description="Пароль нового пользователя")],
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
):
    auth_service.register(login=login, password=password)


@router.post(f"/{tag}/get_access_token/", tags=[tag])
@inject
def get_access_token(
    login: Annotated[str, Query(max_length=20, min_length=5, description="Логин пользователя")],
    password: Annotated[str, Query(max_length=20, min_length=5, description="Пароль пользователя")],
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
):
    return auth_service.get_access_token(login=login, password=password)
