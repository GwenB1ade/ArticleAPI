from datetime import timedelta
from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import OAuth2PasswordRequestForm

from schemas.article_schemas import ArticleSchema
from service.like_service import LikeService
from service.user_service import UserService

from schemas.user_schemas import (
    CreateUserSchema,
    ViewUserSchema,
    UserSchema,
    LoginUserSchema,
)
from schemas.response_answer import ResponseAnswerSchemas, AccessTokenAnswerSchema

from dependencies.auth_dep import active_user

from utils.jwt.auth_jwt import UserJwt

router = APIRouter(
    prefix="/auth",
    tags=["Registration / Authorization / User"],
    responses={400: {"description": "Bad Request", "model": ResponseAnswerSchemas}},
)


@router.post("/reg")
async def registration(form_data: CreateUserSchema) -> ResponseAnswerSchemas:
    """Регистрация пользователя"""
    UserService.create_user(form_data)
    return ResponseAnswerSchemas(detail="You have successfully created an account")


@router.post("/token")
async def token(
    form: dict = Depends(OAuth2PasswordRequestForm),
) -> AccessTokenAnswerSchema:
    username, password = form.username, form.password
    user = UserService.login_user_by_username(username=username, password=password)
    token = UserJwt.create_jwt_token(user.convert_to_schema())

    return {"access_token": token, "token_type": "bearer"}


@router.post("/log")
async def login(form: LoginUserSchema) -> AccessTokenAnswerSchema:
    user = UserService.login_user(form)
    token = UserJwt.create_jwt_token(user.convert_to_schema())

    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
async def me(active_user: active_user) -> ViewUserSchema:
    """Получения публичных данных активного аккаунта"""
    return active_user
