import os
from datetime import datetime, timedelta, timezone

import jwt
import hashlib
from fastapi import HTTPException
from dependency_injector.wiring import inject
from dotenv import load_dotenv

from projectX.app.repositories.auth_repository import AuthRepository


load_dotenv()

SECRET = os.environ.get("SECRET")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))


class AuthService:
    @inject
    def __init__(
        self,
        auth_repository: AuthRepository,
    ) -> None:
        self.auth_repository = auth_repository

    @staticmethod
    def __get_password_hash(password: str) -> str:
        return  hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def __create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)

    def register(self, login: str, password: str) -> None:
        password = self.__get_password_hash(password)
        self.auth_repository.register(login=login, password=password)

    def get_access_token(self, login: str, password: str) -> str:
        password = self.__get_password_hash(password)
        if self.auth_repository.check_credentials(login=login, password=password):
            data = {"sub": login}
            return self.__create_access_token(data=data)
        raise HTTPException(status_code=403, detail="Некорректный логин или пароль")
