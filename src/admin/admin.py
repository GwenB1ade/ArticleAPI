from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin.contrib.mongoengine import ModelView as MongoModelView
from database import engine

from utils.mongodb.connect import comments_colleclion, db
import schemas

from .auth import UsernameAndPasswordProvider

import models

admin = Admin(
    engine,
    auth_provider = UsernameAndPasswordProvider()
)

class UserView(ModelView):
    fields = ['uuid', 'articles', 'likes', 'username', 'email']


admin.add_view(
    ModelView(models.ArticleModel, name = 'Articles')
)

admin.add_view(
    UserView(models.UserModel, name = 'Users')
)

admin.add_view(
    ModelView(models.LikeModel, name = 'Likes')
)