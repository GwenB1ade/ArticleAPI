from fastapi import APIRouter, Depends, Request, HTTPException


from service import ArticleService, LikeService, CommentsMongoService

from schemas.response_answer import ResponseAnswerSchemas
from schemas.article_schemas import CreateArticleSchema, ArticleSchema, ArticleDocumentSchema

from dependencies.auth_dep import active_user

from utils.elasticsearch.article_search import AsyncArticleSearch


router = APIRouter(
    prefix = '/articles',
    tags = ['Articles']
)


@router.post('/')
async def create_article(
    active_user: active_user,
    form_data: CreateArticleSchema
) -> ArticleSchema:
    """Создание статьи"""
    
    article = ArticleService.create_article(
        data = form_data,
        author_uuid = active_user.uuid
    )
    
    await AsyncArticleSearch.add_article(
        article.convert_to_schema().convert_to_document()
    )
    
    return article.convert_to_schema()

@router.get('/{article_uuid}')
async def get_article(
    article_uuid: str
) -> ArticleSchema:
    """Получение статьи по uuid"""
    article = ArticleService.get_article_by_uuid(article_uuid)
    return article.convert_to_schema()

@router.get('/')
async def get_my_articles(
    active_user: active_user,
    page: int = None,
    page_size: int = None
) -> list[ArticleSchema]:
    """Получить все свои статьи"""
    articles = ArticleService.get_articles(
        author_uuid = active_user.uuid,
        page = page if page else 0,
        page_size = page_size if page_size else None
    )
    
    articles_schemas = [article.convert_to_schema() for article in articles]
    return articles_schemas


@router.delete('/{article_uuid}')
async def delete_article(
    active_user: active_user,
    article_uuid: str,
) -> ResponseAnswerSchemas:
    ArticleService.delete_article_by_uuid(
        article_uuid,
        active_user.uuid
    )
    
    # Удаление комментариев
    await CommentsMongoService.delete_comments(article_uuid)
    
    # Удаление статьи в elasticsearch
    await AsyncArticleSearch.delete_article(article_uuid)
    
    return ResponseAnswerSchemas(
        detail = 'The article has been deleted. All comments were deleted too.'
    )
    
    

@router.get('/find/{username}')
async def get_user_articles(
    username: str
) -> list[ArticleSchema]:
    """Получение статьей пользователя по имени пользователя"""
    
    articles = ArticleService.get_articles_by_username(
        username
    )
    
    articles_schemas = [i.convert_to_schema() for i in articles]
    return articles_schemas


@router.post('/like/{article_uuid}')
async def like_article(
    active_user: active_user,
    article_uuid: str
) -> ResponseAnswerSchemas:
    """Поставить или убрать лайк статье"""
    res = LikeService.like_article(
        article_uuid = article_uuid,
        user_uuid = active_user.uuid
    )
    
    return ResponseAnswerSchemas(
        detail = res
    )
    

@router.get('/likes')
async def get_likes_articles(
    active_user: active_user
) -> list[ArticleSchema]:
    articles = LikeService.get_likes_articles(active_user.uuid)
    return articles


@router.post('/search', tags = ['Search Articles'])
async def search(
    text: str
) -> list[ArticleDocumentSchema]:
    """Поиск статьей по префиксу, совпадению, имени автора."""
    docs = await AsyncArticleSearch.search(text)
    return docs