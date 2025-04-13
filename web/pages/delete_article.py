import streamlit as st

from article_api import articles as articles_api
from article_api import users as users_api

from utils.user_utils import not_auth


def delete_article():
    st.title("Delete Article")
    token = users_api.get_token_from_session()
    if token:
        uuid = st.text_input("UUID Article")
        if st.button("Delete"):
            res = articles_api.delete_article(token, uuid)
            return st.warning(res)

    else:
        not_auth()


delete_article()
