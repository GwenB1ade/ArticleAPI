from strawberry.experimental.pydantic import type
from strawberry import auto

import schemas
from . import UserType


@type(model=schemas.ArticleSchema)
class ArticleType:
    uuid: auto
    title: auto
    body: auto
    author: "UserType"
    likes: auto
