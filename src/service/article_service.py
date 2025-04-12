from typing import Optional

from fastapi import HTTPException
from .base import BaseServices
from .user_service import UserService
from database import session_creater, async_session_creater, AsyncSession
from models import ArticleModel, UserModel

from sqlalchemy.future import select
from sqlalchemy.exc import DataError

from schemas.article_schemas import CreateArticleSchema, ArticleSchema

from exceptions import article_not_found


class ArticleService(BaseServices):
    model = ArticleModel

    @classmethod
    def create_article(
        cls, data: CreateArticleSchema, author_uuid: str
    ) -> ArticleModel:
        """Создание статьи"""
        with session_creater() as s:
            user = UserService.get_user_by_uuid(author_uuid)

            article = cls.model(title=data.title, body=data.body, likes=[])

            article.author = user
            s.add(article)
            s.commit()
            s.refresh(user)

            return article

    @classmethod
    def get_article_by_uuid(cls, uuid: str) -> Optional[ArticleModel]:
        """Получение статьи по UUID"""
        with session_creater() as s:
            try:
                article = s.query(cls.model).filter_by(uuid=uuid).first()
                if not article:
                    raise article_not_found

                return article
            except DataError:
                raise article_not_found

    @classmethod
    def delete_article_by_uuid(cls, article_uuid: str, user_uuid: str) -> None:
        """Удаление статьи по UUID"""
        with session_creater() as s:
            try:
                s.query(cls.model).filter_by(
                    uuid=article_uuid, author_uuid=user_uuid
                ).delete()

                s.commit()
            except DataError:
                raise article_not_found

    @classmethod
    def get_articles(
        cls, author_uuid: str, page: int = 1, page_size: Optional[int] = None
    ) -> list[ArticleModel]:
        """
        Получение статей по UUID пользователя.
        Page: номер страницы
        Page_size: Размер страницы
        """
        with session_creater() as s:
            if page_size:
                offset = (page - 1 if page else page) * page_size
                articles = (
                    s.query(cls.model)
                    .filter(cls.model.author_uuid == author_uuid)
                    .offset(offset)
                    .limit(page_size)
                    .all()
                )

            else:
                articles = (
                    s.query(cls.model)
                    .filter(cls.model.author_uuid == author_uuid)
                    .all()
                )

            return articles

    @classmethod
    def get_articles_by_username(
        cls, author_username: str
    ) -> Optional[list[ArticleModel]]:
        """Получение статей по имени пользователя"""
        with session_creater() as s:
            user = s.query(UserModel).filter_by(username=author_username).first()

            articles = user.articles if user else None

            return articles
