import strawberry
import strawberry.fastapi

from utils.mongodb.comments import CommentsMongoService
import schemas
from api.graphql import types

from uuid import uuid4


@strawberry.type
class Query:

    @strawberry.field
    async def get_article_comments(self, article_uuid: str) -> list[types.CommentType]:
        comments = await CommentsMongoService.get_comments(article_uuid)

        result = []
        for c in comments:
            replies = []
            for reply in c.get("answers"):
                replies.append(
                    types.CommentReplyType(
                        uuid=reply.get("uuid"),
                        body=reply.get("body"),
                        author_username=reply.get("author_username"),
                        author_uuid=reply.get("author_uuid"),
                        comment_uuid=reply.get("comment_uuid"),
                    )
                )
            result.append(
                types.CommentType(
                    uuid=c.get("uuid"),
                    body=c.get("body"),
                    author_username=c.get("author_username"),
                    author_uuid=c.get("author_uuid"),
                    article_uuid=c.get("article_uuid"),
                    answers=replies,
                )
            )

        return result


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def send_comment(
        self,
        body: str,
        author_username: str,
        author_uuid: str,
        article_uuid: str,
    ) -> None:
        await CommentsMongoService.add_comment(
            schemas.CommentSchema(
                uuid=str(uuid4()),
                body=body,
                author_username=author_username,
                author_uuid=author_uuid,
                article_uuid=article_uuid,
            )
        )


schema = strawberry.Schema(query=Query, mutation=Mutation)
router = strawberry.fastapi.GraphQLRouter(
    schema, prefix="/graphql/comment", tags=["GraphQL"]
)
