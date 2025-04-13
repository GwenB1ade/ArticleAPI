from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UUID
from database import Base
import uuid

from typing import TYPE_CHECKING, Union

from schemas.user_schemas import UserSchema, ViewUserSchema

if TYPE_CHECKING:
    from .article import ArticleModel
    from .like import LikeModel


class UserModel(Base):
    __tablename__ = "User"
    uuid: Mapped[str] = mapped_column(
        UUID(as_uuid=False), default=uuid.uuid4, primary_key=True
    )
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str]

    articles: Mapped[list["ArticleModel"]] = relationship(
        back_populates="author", uselist=True
    )

    likes: Mapped[list["LikeModel"]] = relationship(
        back_populates="user_liked", uselist=True
    )

    def convert_to_schema(
        self, full: bool = False
    ) -> Union[UserSchema, ViewUserSchema]:
        if full:
            schema = UserSchema(
                uuid=str(self.uuid),
                username=self.username,
                password=self.password,
                email=self.email,
            )

        else:
            schema = ViewUserSchema(uuid=str(self.uuid), username=self.username)

        return schema
