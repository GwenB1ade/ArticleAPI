from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from admin.admin import admin
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
import asyncio

from database import async_session_creater, create_db, drop_db
from rich.console import Console


import exceptions
from config import settings

# from utils.mongodb.connect import ping
from utils.limiter_api import limiter, RateLimitExceeded, _rate_limit_exceeded_handler
from utils.elasticsearch.article_search import AsyncArticleSearch

from api.gRPC.server import serve


app = FastAPI(title="Article API", version="0.0.1", root_path="/api/v1")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

admin.mount_to(app)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse("/docs")


# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET)


# Exceptions
app.add_exception_handler(
    status.HTTP_500_INTERNAL_SERVER_ERROR, exceptions.exception_500
)
app.add_exception_handler(HTTPException, exceptions.exception_http)


# Routing
from api.rest.auth.router import router as auth_router
from api.rest.article.router import router as article_router
from api.rest.comments.router import router as comments_router


# from api.graphql.resolvers.user import router as graphql_user_router
# from api.graphql.resolvers.article import router as grapgql_article_router
# from api.graphql.resolvers.comment import router as graphql_comment_router

from api.graphql.router import router as graphql_router


app.include_router(auth_router)
app.include_router(article_router)
app.include_router(comments_router)

# app.include_router(graphql_user_router)
# app.include_router(grapgql_article_router)
# app.include_router(graphql_comment_router)

app.include_router(graphql_router)


# CLI
import typer

cli = typer.Typer()


@cli.command()
def run():
    """Запускает основное FastAPI приложение с поддержкой GraphQL"""
    create_db()
    uvicorn.run("main:app", reload=True)


@cli.command()
def grpc():
    """Запускает gRPC приложение"""
    # UI = grpcui -proto article.proto -plaintext localhost:50051
    asyncio.run(serve())


@cli.command()
def drop():
    console = Console()
    asyncio.run(AsyncArticleSearch.drop_elastic())
    drop_db()

    console.print(
        f"[green]INFO[/green]: The Postgresql and ElasticSearch databases have been reset"
    )


if __name__ == "__main__":
    cli()
