from .connect import client, db, comments_colleclion
from schemas.comment_schema import CommentSchema, CommentReplySchema



class CommentsMongoService():
    collection = comments_colleclion
    
    @classmethod
    async def add_comment(cls, comment: CommentSchema) -> None:
        await cls.collection.insert_one(comment.model_dump())
        
    
    @classmethod
    async def add_reply_for_comment(cls, reply: CommentReplySchema) -> None:
        await cls.collection.update_one(
            {'uuid': reply.comment_uuid},
            {'$push': {'answers': reply.model_dump()}}
        )
    
    @classmethod
    async def get_comments(cls, article_uuid: str) -> list[dict]:
        comments_dict = cls.collection.find(
            {'article_uuid': article_uuid}
        )

        return await comments_dict.to_list()
    
    
    @classmethod
    async def delete_comments(cls, article_uuid: str) -> None:
        await cls.collection.delete_many(
            {'article_uuid': article_uuid}
        )
    
    
    @classmethod
    async def delete_one_comment(cls, comment_uuid: str, author_uuid: str) -> None:
        await cls.collection.delete_one(
            {
                'uuid': comment_uuid,
                'author_uuid': author_uuid
            }
        )
    
    
    @classmethod
    async def get_all_comments(cls) -> dict:
        comments = await cls.collection.find({})
        return comments
    
    
    @classmethod
    def convert_dict_to_schema(cls, comment: dict) -> CommentSchema:
        answers = []
        for ans in comment.get('answers'):
            answers.append(
                CommentReplySchema(
                    uuid = ans.get('uuid'),
                    body = ans.get('body'),
                    author_username = ans.get('author_username'),
                    author_uuid = ans.get('author_uuid'),
                    comment_uuid = ans.get('comment_uuid'),
                )
            )
        return CommentSchema(
            uuid = comment.get('uuid'),
            body = comment.get('body'),
            author_username = comment.get('author_username'),
            author_uuid = comment.get('author_uuid'),
            article_uuid = comment.get('article_uuid'),
            answers = answers
        )
