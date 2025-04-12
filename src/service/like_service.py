from database import session_creater
from sqlalchemy import and_
from sqlalchemy.exc import DataError
from models import LikeModel, UserModel
from schemas.article_schemas import ArticleSchema
from .base import BaseServices

from exceptions import article_not_found


class LikeService(BaseServices):
    model = LikeModel

    @classmethod
    def like_article(cls, article_uuid: str, user_uuid: str) -> str:
        """Поставить или убрать лайк"""
        with session_creater() as s:
            try:
                is_liked = (
                    s.query(cls.model)
                    .filter(
                        cls.model.article_uuid == article_uuid,
                        cls.model.user_liked_uuid == user_uuid,
                    )
                    .first()
                )

            except DataError:
                raise article_not_found

            if not is_liked:
                like = cls.model(article_uuid=article_uuid, user_liked_uuid=user_uuid)
                s.add(like)

                res = f"You liked the article."

            else:
                s.delete(is_liked)
                res = "You have removed your like"

            s.commit()
            return res

    @classmethod
    def get_likes_articles(cls, user_uuid: str) -> list[ArticleSchema]:
        """Получить статьи, которые лайкнул пользователь"""
        with session_creater() as s:
            user = s.query(UserModel).filter_by(uuid=user_uuid).first()

            articles = []
            for like in user.likes:
                articles.append(like.article.convert_to_schema())

            return articles
