from fastapi import APIRouter, Depends
from uuid import uuid4

from schemas.comment_schema import CommentReplySchema, CommentSchema
from schemas.response_answer import ResponseAnswerSchemas, ResponseCommentsList

from utils.mongodb.comments import CommentsMongoService

from dependencies.auth_dep import active_user

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/{article_uuid}")
async def send_comment(
    article_uuid: str, comment_body: str, active_user: active_user
) -> ResponseAnswerSchemas:
    """Оставить комментарий под статьей"""
    comment = CommentSchema(
        uuid=str(uuid4()),
        body=comment_body,
        author_username=active_user.username,
        author_uuid=active_user.uuid,
        article_uuid=article_uuid,
        answers=[],
    )

    await CommentsMongoService.add_comment(comment)

    return {"detail": "A comment has been sent"}


@router.get("/{article_uuid}")
async def get_article_comments(article_uuid: str) -> ResponseCommentsList:
    """Получить комментарии статьи"""
    comments = await CommentsMongoService.get_comments(article_uuid=article_uuid)

    return ResponseCommentsList(comments = comments)


@router.post("/reply/{comment_uuid}")
async def reply_to_comments(
    comment_uuid: str, reply_text: str, active_user: active_user
) -> ResponseAnswerSchemas:
    """Ответь на комментарий"""
    reply_comment = CommentReplySchema(
        uuid=str(uuid4()),
        body=reply_text,
        author_username=active_user.username,
        author_uuid=active_user.uuid,
        comment_uuid=comment_uuid,
    )

    await CommentsMongoService.add_reply_for_comment(reply_comment)

    return {"detail": "You have successfully replied to the comment"}


@router.delete("/{comment_uuid}")
async def delete_comment(
    active_user: active_user, comment_uuid: str
) -> ResponseAnswerSchemas:
    await CommentsMongoService.delete_one_comment(comment_uuid, active_user.uuid)
    return ResponseAnswerSchemas(detail="The comment has been deleted.")
