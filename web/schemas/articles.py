from pydantic import BaseModel
from .users import UserDataSchema


class ArticleSchema(BaseModel):
    uuid: str
    title: str
    body: str
    author: UserDataSchema
    likes: int


class ArticleDocumentSchema(BaseModel):
    uuid: str
    title: str
    body: str
    author_username: str
