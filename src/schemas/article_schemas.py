from pydantic import BaseModel

from typing import TYPE_CHECKING
from .user_schemas import ViewUserSchema


class CreateArticleSchema(BaseModel):
    title: str
    body: str
    

class ArticleSchema(BaseModel):
    uuid: str
    title: str
    body: str
    author: ViewUserSchema
    likes: int
    
    def convert_to_document(self):
        return ArticleDocumentSchema(
            uuid = self.uuid,
            title = self.title,
            body = self.body,
            author_username = self.author.username
        )
    

class ArticleDocumentSchema(BaseModel):
    uuid: str
    title: str
    body: str
    author_username: str
    
    def __str__(self):
        return f'Title: {self.title}'