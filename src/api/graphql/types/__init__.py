from .user_types import UserType, AccessTokenAnswerType, LoginFormType
from .article_types import ArticleType
from .comment_types import CommentReplyType, CommentType


from strawberry import type

@type
class DetailResponseType:
    detail: str