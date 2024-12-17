from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from projectX.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    user = decode_token(token)
    return user

def decode_token(token: str) -> User:
    return User(login="lal", password="kek")
