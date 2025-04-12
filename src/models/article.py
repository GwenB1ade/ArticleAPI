from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UUID, String, ForeignKey
from database import Base, session_creater
import uuid

from schemas.article_schemas import ArticleSchema

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import UserModel
    from .like import LikeModel


class ArticleModel(Base):
    __tablename__ = "Article"
    uuid: Mapped[str] = mapped_column(
        UUID(as_uuid=False), default=uuid.uuid4, primary_key=True
    )
    title: Mapped[str] = mapped_column(String(length=120))
    body: Mapped[str]

    author_uuid: Mapped[str] = mapped_column(ForeignKey("User.uuid"))
    author: Mapped["UserModel"] = relationship(back_populates="articles", lazy="joined")

    likes: Mapped[list["LikeModel"]] = relationship(
        back_populates="article", uselist=True, lazy="joined"
    )

    def convert_to_schema(self):
        with session_creater() as s:
            article = s.query(ArticleModel).filter_by(uuid=self.uuid).first()
            return ArticleSchema(
                uuid=str(self.uuid),
                title=self.title,
                body=self.body,
                author=article.author.convert_to_schema(),
                likes=len(article.likes),
            )
