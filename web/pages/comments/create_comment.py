import streamlit as st

from article_api import comments as comments_api
from article_api import users as users_api

import schemas

from utils.user_utils import not_auth


def create_comment():
    st.title("Send comment")
    article_uuid = st.text_input("Article UUID")
    body = st.text_input("Body")
    token = users_api.get_token_from_session()
    if token:
        if st.button("Send"):
            res = comments_api.create_comment(body, article_uuid, token)
            st.success(res)

    else:
        not_auth()


create_comment()
