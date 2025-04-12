from fastapi import HTTPException
from typing import Union
from models.user import UserModel
from .base import BaseServices
from database import session_creater

import bcrypt

from schemas.user_schemas import (
    CreateUserSchema,
    UserSchema,
    ViewUserSchema,
    LoginUserSchema,
)


class UserService(BaseServices):
    model = UserModel

    @classmethod
    def create_user(cls, data: CreateUserSchema) -> UserModel:
        """Создать пользователя"""
        with session_creater() as s:
            user = s.query(cls.model).filter_by(email=data.email).first()

            if user:
                raise HTTPException(
                    status_code=400, detail="There is a user with such an email address"
                )

            user = cls.model(
                username=data.username,
                password=cls.__hash_password(data.password),
                email=data.email,
            )

            s.add(user)
            s.commit()

            return user

    @classmethod
    def login_user(cls, login_data: LoginUserSchema):
        """Авторизация пользователя"""
        with session_creater() as s:
            user = s.query(cls.model).filter_by(email=login_data.email).first()

            if not user:
                raise HTTPException(
                    status_code=400, detail="Invalid password or email address"
                )

            if cls.__check_password(login_data.password, user.password):
                return user

    @classmethod
    def login_user_by_username(cls, username: str, password: str) -> UserModel:
        """Авторизация пользователя по имени и паролю пользователя"""
        with session_creater() as s:
            user = s.query(cls.model).filter_by(username=username).first()

            if cls.__check_password(password, user.password):
                return user

            raise HTTPException(status_code=400, detail="Invalid password or username")

    @classmethod
    def get_user_by_uuid(cls, uuid: str) -> UserModel:
        """Получить данные пользователя через UUID"""
        return cls.get_object_by_uuid(uuid)

    @classmethod
    def change_username(
        cls, new_username: str, email: str = None, uuid: str = None
    ) -> None:
        """Поменять имя пользователя. Требуеться новое имя и email или UUID"""
        with session_creater() as s:
            if email:
                user = s.query(cls.model).filter_by(email=email).first()

            elif uuid:
                user = s.query(cls.model).filter_by(uuid=uuid).first()

            else:
                raise Exception("Необходимо передать email или uuid")

            user.username = new_username
            s.commit()

            return None

    @classmethod
    def __hash_password(cls, password: str) -> str:
        """Захэшировать пароль"""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    @classmethod
    def __check_password(cls, password: str, hashed_password: str) -> bool:
        """Проверить пароль с хэшированным паролем"""
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
