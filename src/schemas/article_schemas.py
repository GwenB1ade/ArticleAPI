from fastapi import HTTPException
from pydantic import BaseModel, field_validator, model_validator

from typing import TYPE_CHECKING
from .user_schemas import ViewUserSchema


class CreateArticleSchema(BaseModel):
    title: str
    body: str

    @model_validator(mode="before")
    @classmethod
    def validate_model(cls, data: dict):
        if not isinstance(data["title"], str) or not isinstance(data["body"], str):
            raise HTTPException(
                status_code=400,
                detail="The title or body fields have an incorrect type. These fields must have a string type.",
            )

        return data


class ArticleSchema(BaseModel):
    uuid: str
    title: str
    body: str
    author: ViewUserSchema
    likes: int

    def convert_to_document(self):
        return ArticleDocumentSchema(
            uuid=self.uuid,
            title=self.title,
            body=self.body,
            author_username=self.author.username,
        )


class ArticleDocumentSchema(BaseModel):
    uuid: str
    title: str
    body: str
    author_username: str

    def __str__(self):
        return f"Title: {self.title}"
