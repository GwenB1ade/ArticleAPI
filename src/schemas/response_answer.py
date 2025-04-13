from typing import Union
from pydantic import BaseModel
from .article_schemas import ArticleSchema, ArticleDocumentSchema
from .comment_schema import CommentSchema


class ResponseAnswerSchemas(BaseModel):
    detail: str | dict


class AccessTokenAnswerSchema(BaseModel):
    access_token: str
    token_type: str


class ResponseArticlesList(BaseModel):
    articles: list[ArticleSchema]


class ResponseArticlesDocsList(BaseModel):
    articles_docs: list[ArticleDocumentSchema]


class ResponseCommentsList(BaseModel):
    comments: list[CommentSchema]
