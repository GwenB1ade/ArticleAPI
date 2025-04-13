from typing import Union
import requests

from dependencies import BACKEND_URL
from utils import auth_headers
import schemas


def get_my_articles(token: str) -> list[schemas.ArticleSchema]:
    data = requests.get(f"{BACKEND_URL}/articles/", headers=auth_headers(token))
    if data.status_code != 200:
        return None
    articles = data.json().get("articles")
    articles_schemas = []
    for article in articles:
        articles_schemas.append(_convert_json_to_article(article))
    return articles_schemas


def create_article(
    token: str, title: str, body: str
) -> Union[schemas.ArticleSchema, str]:
    res = requests.post(
        f"{BACKEND_URL}/articles",
        json={"title": title, "body": body},
        headers=auth_headers(token),
    )

    if res.json().get("uuid"):
        article = _convert_json_to_article(res.json())
        return article
    else:
        return res.json().get("detail")


def get_article_by_uuid(uuid: str):
    response = requests.get(f"{BACKEND_URL}/articles/{uuid}")
    if response.json():
        article = _convert_json_to_article(response.json())
        return article

    else:
        return response.json()


def delete_article(token, uuid: str):
    response = requests.delete(
        f"{BACKEND_URL}/articles/{uuid}", headers=auth_headers(token)
    )
    try:
        return response.json().get("detail")
    except:
        return f"Error, possibly invalid UUID"


def search_articles(text: str) -> list[schemas.ArticleDocumentSchema]:
    json = requests.post(f"{BACKEND_URL}/articles/search?text={text}").json()
    articles = []
    if json.get("articles_docs"):
        for article in json.get("articles_docs"):
            articles.append(_convert_json_to_article(article, is_docs=True))

    return articles


def like_article(token: str, article_uuid: str):
    response = requests.post(
        f"{BACKEND_URL}/articles/like/{article_uuid}", headers=auth_headers(token)
    )
    return response.json().get("detail")


def get_my_likes(token: str):
    response = requests.get(
        f"{BACKEND_URL}/articles/likes/", headers=auth_headers(token)
    )
    articles = []
    if response.json().get("articles"):
        for art in response.json().get("articles"):
            articles.append(_convert_json_to_article(art))

    return articles


def _convert_json_to_article(
    json: dict, is_docs: bool = False
) -> Union[schemas.ArticleDocumentSchema, schemas.ArticleSchema]:
    if is_docs:
        article = schemas.ArticleDocumentSchema(
            uuid=json.get("uuid"),
            title=json.get("title"),
            body=json.get("body"),
            author_username=json.get("author_username"),
        )

        return article

    article = schemas.ArticleSchema(
        uuid=json.get("uuid"),
        title=json.get("title"),
        body=json.get("body"),
        author=schemas.UserDataSchema(
            username=json.get("author").get("username"),
            uuid=json.get("author").get("uuid"),
        ),
        likes=json.get("likes"),
    )

    return article
