from functools import wraps
from uuid import uuid4
import service
import schemas
import sys

from utils.elasticsearch.article_search import AsyncArticleSearch

from dependencies.auth_dep import get_active_user

from grpc import ServicerContext
from grpc import aio

from concurrent import futures

from loguru import logger

from . import article_pb2, article_pb2_grpc


logger.remove()
logger.add(sys.stdout, format="<green>{level}</green>: <level>{message}</level>")


def log_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        logger.info(f'The method worked "{func.__name__}"')
        return result

    return wrapper


class Service(article_pb2_grpc.APIServicer):

    @log_handler
    async def CreateArticle(
        self, request, context: ServicerContext
    ) -> article_pb2.ArticleResponse:
        active_user = get_active_user(request.token)
        article = service.ArticleService.create_article(
            data=schemas.CreateArticleSchema(title=request.title, body=request.body),
            author_uuid=active_user.uuid,
        )

        return self.__convert_article_to_grpc_response(article.convert_to_schema())

    @log_handler
    async def GetArticle(self, request, context: ServicerContext):
        article = service.ArticleService.get_article_by_uuid(uuid=request.article_uuid)

        return self.__convert_article_to_grpc_response(article.convert_to_schema())

    @log_handler
    async def GetMyArticles(self, request, context: ServicerContext):
        active_user = get_active_user(request.token)
        articles = service.ArticleService.get_articles(active_user.uuid)

        parsed_articles = []
        for art in articles:
            parsed_articles.append(
                self.__convert_article_to_grpc_response(art.convert_to_schema())
            )

        return article_pb2.ArticlesResponse(articles=parsed_articles)

    @log_handler
    async def SearchArticle(self, request, context: ServicerContext):
        text = request.text
        articles = await AsyncArticleSearch.search(text)
        grpc_response = [
            self.__convert_article_docs_to_grpc_response(i) for i in articles
        ]

        return article_pb2.ArticlesDocsResponse(articles=grpc_response)

    @log_handler
    async def LikeArticle(self, request, context: ServicerContext):
        active_user = get_active_user(request.user_token.user_token)
        response = service.LikeService.like_article(
            article_uuid=request.article_uuid.article_uuid, user_uuid=active_user.uuid
        )

        return self.__convert_detail_to_grpc_response(detail=response)

    @log_handler
    async def GetLikedArticles(self, request, context: ServicerContext):
        active_user = get_active_user(request.user_token)
        liked_articles = service.LikeService.get_likes_articles(active_user.uuid)
        grpc_response = [
            self.__convert_article_to_grpc_response(i) for i in liked_articles
        ]

        return article_pb2.ArticlesResponse(articles=grpc_response)

    @log_handler
    async def SendComment(self, request, context: ServicerContext):
        active_user = get_active_user(request.user_token.user_token)
        await service.CommentsMongoService.add_comment(
            schemas.CommentSchema(
                uuid=str(uuid4()),
                body=request.body,
                author_username=active_user.username,
                author_uuid=active_user.uuid,
                article_uuid=request.article_uuid.article_uuid,
            )
        )

        return self.__convert_detail_to_grpc_response(
            detail="You have successfully commented"
        )

    @log_handler
    async def GetComments(self, request, context: ServicerContext):
        comments = await service.CommentsMongoService.get_comments(request.article_uuid)

        comments = [
            service.CommentsMongoService.convert_dict_to_schema(i) for i in comments
        ]

        grpc_response = [self.__convert_comment_to_grpc_response(c) for c in comments]
        return article_pb2.CommentsResponse(comments=grpc_response)

    @log_handler
    async def CreateAnswer(self, request, context: ServicerContext):
        active_user = get_active_user(request.user_token.user_token)
        await service.CommentsMongoService.add_reply_for_comment(
            schemas.CommentReplySchema(
                uuid=str(uuid4()),
                body=request.body,
                author_username=active_user.username,
                author_uuid=active_user.uuid,
                comment_uuid=request.comment_uuid,
            )
        )

        return self.__convert_detail_to_grpc_response(
            detail="You have successfully replied to the comment"
        )

    def __convert_article_to_grpc_response(
        self, article_schema: schemas.ArticleSchema
    ) -> article_pb2.ArticleResponse:
        return article_pb2.ArticleResponse(
            uuid=str(article_schema.uuid),
            title=article_schema.title,
            body=article_schema.body,
            likes=article_schema.likes,
            userdata=article_pb2.UserData(
                user_uuid=str(article_schema.author.uuid),
                username=article_schema.author.username,
            ),
        )

    def __convert_article_docs_to_grpc_response(
        self, article_docs: schemas.ArticleDocumentSchema
    ) -> article_pb2.ArticleDocumentResponse:
        return article_pb2.ArticleDocumentResponse(
            uuid=str(article_docs.uuid),
            title=article_docs.title,
            body=article_docs.body,
            author_username=article_docs.author_username,
        )

    def __convert_detail_to_grpc_response(self, detail: str):
        return article_pb2.DetailResponse(detail=detail)

    def __convert_comment_to_grpc_response(self, comment_schema: schemas.CommentSchema):
        answers = []
        for ans in comment_schema.answers:
            answers.append(
                article_pb2.Answer(
                    uuid=ans.uuid,
                    body=ans.body,
                    author_username=ans.author_username,
                    author_uuid=ans.author_uuid,
                    comment_uuid=ans.comment_uuid,
                )
            )

        return article_pb2.CommentResponse(
            uuid=comment_schema.uuid,
            body=comment_schema.body,
            author_username=comment_schema.author_username,
            author_uuid=comment_schema.author_uuid,
            article_uuid=comment_schema.article_uuid,
            answers=answers,
        )


async def serve(port: int = 50051):
    server = aio.server(futures.ThreadPoolExecutor(max_workers=10))
    article_pb2_grpc.add_APIServicer_to_server(Service(), server)
    server.add_insecure_port(f"[::]:{port}")
    logger.info(f"The gRPC server is running on port {port} right now.")
    await server.start()
    await server.wait_for_termination()
