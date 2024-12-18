from typing import Annotated

from fastapi import Depends, Query, Body
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from dependency_injector.wiring import Provide, inject

from projectX.app.services.auth_service import AuthService
from projectX.app.di_container import Container


templates = Jinja2Templates(directory='projectX/templates')
tag = "auth"
prefix = f"/{tag}"

router = APIRouter(
    prefix=prefix,
)


@router.post(
    "/register",
    tags=[tag],
    summary="Регистрация нового пользователя",
)
@inject
def register(
    login: Annotated[str, Query(max_length=20, min_length=5, description="Логин нового пользователя")],
    password: Annotated[str, Query(max_length=20, min_length=5, description="Пароль нового пользователя")],
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
):
    auth_service.register(login=login, password=password)


@router.post(
    "/get_access_token",
    tags=[tag],
    summary="Получение токена по логину и паролю",
)
@inject
def get_access_token(
    login:str = Body(...),
    password:str = Body(...),
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
):
    return auth_service.get_access_token(login=login, password=password)
