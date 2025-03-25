import strawberry
import strawberry.fastapi
import strawberry.utils

from .resolvers import (
    ArticleQuery,
    ArticleMutation,
    CommentQuery,
    CommentMutation,
    UserQuery,
    UserMutation
)

@strawberry.type
class Query(
    ArticleQuery,
    CommentQuery,
    UserQuery
):
    pass

@strawberry.type
class Mutation(
    ArticleMutation,
    CommentMutation,
    UserMutation
):
    pass


schema = strawberry.Schema(query = Query, mutation = Mutation)
router = strawberry.fastapi.GraphQLRouter(schema, prefix = '/graphql')