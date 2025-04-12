from fastapi import Request
import strawberry
from strawberry.types import Info
from strawberry.fastapi.router import GraphQLRouter

from api.graphql import types

from service.article_service import ArticleService
from service import CommentsMongoService
from dependencies.auth_dep import active_user_graphql, get_active_user_for_graphql
import schemas

from utils.elasticsearch.article_search import AsyncArticleSearch


@strawberry.type
class Query:

    @strawberry.field
    def get_article_by_uuid(self, uuid: str) -> types.ArticleType:
        article = ArticleService.get_article_by_uuid(uuid=uuid)

        return types.ArticleType.from_pydantic(article.convert_to_schema())

    @strawberry.field
    def get_my_articles(
        self, info: Info, page: int = 1, page_size: int = 10
    ) -> list[types.ArticleType]:
        active_user = get_active_user_for_graphql(info)
        articles = ArticleService.get_articles(
            author_uuid=active_user.uuid, page=page, page_size=page_size
        )

        list_articles = []
        for art in articles:
            list_articles.append(
                types.ArticleType.from_pydantic(art.convert_to_schema())
            )

        return list_articles


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_article(self, title: str, body: str, info: Info) -> types.ArticleType:
        active_user = get_active_user_for_graphql(info)

        article = ArticleService.create_article(
            schemas.CreateArticleSchema(title=title, body=body),
            author_uuid=active_user.uuid,
        )

        return types.ArticleType.from_pydantic(article.convert_to_schema())

    @strawberry.mutation
    async def delete_article(
        self, article_uuid: str, info: Info
    ) -> types.DetailResponseType:
        active_user = active_user_graphql(info)
        ArticleService.delete_article_by_uuid(article_uuid, active_user.uuid)
        await CommentsMongoService.delete_comments(article_uuid)
        await AsyncArticleSearch.delete_article(article_uuid)

        return types.DetailResponseType(detail="The article has been deleted")


def get_context(
    request: Request,
):
    return {
        "request": request,
    }


schema = strawberry.Schema(query=Query, mutation=Mutation)
router = GraphQLRouter(
    schema, prefix="/graphql/article", context_getter=get_context, tags=["GraphQL"]
)
