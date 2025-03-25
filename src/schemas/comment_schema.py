from pydantic import BaseModel

class CommentSchema(BaseModel):
    uuid: str
    body: str
    author_username: str
    author_uuid: str
    article_uuid: str
    answers: list['CommentReplySchema'] = []
    

class CommentReplySchema(BaseModel):
    uuid: str
    body: str
    author_username: str
    author_uuid: str
    comment_uuid: str
    
    