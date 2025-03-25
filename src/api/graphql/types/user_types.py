import strawberry
from strawberry.experimental.pydantic import type
import schemas
import schemas.user_schemas


@type(model = schemas.ViewUserSchema, all_fields = True)
class UserType:
    pass


@type(model = schemas.LoginUserSchema, all_fields = True)
class LoginFormType:
    pass


@type(model = schemas.AccessTokenAnswerSchema, all_fields = True)
class AccessTokenAnswerType:
    pass