from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UUID, String, ForeignKey
from database import Base
import uuid

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import UserModel
    from .article import ArticleModel


class LikeModel(Base):
    __tablename__ = "Like"
    uuid: Mapped[str] = mapped_column(
        UUID(as_uuid=False), default=uuid.uuid4, primary_key=True
    )

    article_uuid: Mapped[str] = mapped_column(ForeignKey("Article.uuid"))
    article: Mapped["ArticleModel"] = relationship(back_populates="likes")

    user_liked_uuid: Mapped[str] = mapped_column(ForeignKey("User.uuid"))
    user_liked: Mapped["UserModel"] = relationship(back_populates="likes")
