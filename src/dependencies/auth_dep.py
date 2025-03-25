from strawberry import Info
from schemas.user_schemas import ViewUserSchema
from utils.jwt.auth_jwt import UserJwt

from typing import Annotated

from fastapi import HTTPException, Request, Depends
from fastapi.security import OAuth2PasswordBearer

from api.graphql.types import UserType

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'auth/token')


def get_active_user(token: str = Depends(oauth2_scheme)):
    if token:
        userdata = UserJwt.decode_token(token)
        return userdata
    
    raise HTTPException(
        status_code = 400,
        detail = 'To receive a response, you must log in.'
    )


def get_active_user_for_graphql(info: Info):
    request: Request = info.context['request']
    token = request.headers.get('Authorization').split(' ')[1]
    if token:
        userdata = UserJwt.decode_token(token)
        return userdata
    
    raise HTTPException(
        status_code = 400,
        detail = 'To receive a response, you must log in.'
    )


active_user = Annotated[ViewUserSchema, Depends(get_active_user)]
active_user_graphql = Annotated[UserType, Depends(get_active_user_for_graphql)]