import strawberry
from strawberry.fastapi import GraphQLRouter
from service.user_service import UserService

import schemas
from utils.jwt.auth_jwt import UserJwt

from api.graphql import types


@strawberry.type
class Query:

    @strawberry.field
    def get_user(self, user_uuid: str) -> types.UserType:
        user = UserService.get_user_by_uuid(uuid=user_uuid).convert_to_schema()
        return types.UserType(uuid=user.uuid, username=user.username)


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_user(self, username: str, password: str, email: str) -> types.UserType:
        user = UserService.create_user(
            schemas.CreateUserSchema(username=username, password=password, email=email)
        )

        return types.UserType(uuid=user.uuid, username=user.username)

    @strawberry.mutation
    def get_token(self, email: str, password: str) -> types.AccessTokenAnswerType:
        user = UserService.login_user(
            schemas.LoginUserSchema(email=email, password=password)
        )

        token = UserJwt.create_jwt_token(user.convert_to_schema())

        return types.AccessTokenAnswerType(access_token=token, token_type="bearer")


schema = strawberry.Schema(query=Query, mutation=Mutation)
router = GraphQLRouter(schema, prefix="/graphql/user", tags=["GraphQL"])
