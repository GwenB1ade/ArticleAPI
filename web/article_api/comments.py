from typing import Union
import requests
from dependencies import BACKEND_URL

from utils.user_utils import auth_headers

import schemas


def create_comment(body: str, article_uuid: str, token: str):
    res = requests.post(f'{BACKEND_URL}/comments/{article_uuid}?comment_body={body}', headers = auth_headers(token))
    return res.json().get('detail')


def create_reply(body: str, comment_uuid: str, token: str):
    res = requests.post(f'{BACKEND_URL}/comments/reply/{comment_uuid}?reply_text={body}', headers = auth_headers(token))
    return res.json().get('detail')
    

def get_comments(article_uuid: str) -> Union[list[schemas.CommentSchema], str]:
    res = requests.get(f'{BACKEND_URL}/comments/{article_uuid}')
    comments = res.json().get('comments')
    if comments:
        comments_schemas = []
        for com in comments:
            comments_schemas.append(_convert_json_to_comment(com))
        
        return comments_schemas
    
    else:
        return res.json().get('detail')
            
            
    
    

def _convert_json_to_comment(json: dict):
    answers = []
    if json['answers']:
        for ans in json['answers']:
            answers.append(schemas.CommentReplySchema(
            uuid = ans['uuid'],
            body = ans['body'],
            author_username = ans['author_username'],
            author_uuid = ans['author_uuid'],
            comment_uuid = ans['comment_uuid']
            ))
        
    return schemas.CommentSchema(
        uuid = json['uuid'],
        body = json['body'],
        author_username = json['author_username'],
        author_uuid = json['author_uuid'],
        article_uuid = json['article_uuid'],
        answers = answers
    )