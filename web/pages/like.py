import streamlit as st

from article_api import articles as articles_api
from article_api import users as users_api

from utils.user_utils import not_auth


def like_article():
    token = users_api.get_token_from_session()
    if token:
        st.title("Like Article")
        uuid = st.text_input("Article UUID")

        if st.button("Like or Unlike"):
            result = articles_api.like_article(token, uuid)
            st.info(result)

    else:
        not_auth()


like_article()
