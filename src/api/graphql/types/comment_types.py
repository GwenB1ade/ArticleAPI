from strawberry.experimental.pydantic import type
from strawberry import auto
import schemas


@type(model=schemas.CommentReplySchema, all_fields=True)
class CommentReplyType:
    pass


@type(model=schemas.CommentSchema)
class CommentType:
    uuid: auto
    body: auto
    author_username: auto
    author_uuid: auto
    article_uuid: auto
    answers: list[CommentReplyType]
