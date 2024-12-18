from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from projectX.models.user import UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserModel:
    user = decode_token(token)
    return user

def decode_token(token: str) -> UserModel:
    return UserModel(login="lal", password="kek")
