import streamlit as st

from article_api import users as users_api
from article_api import articles as articles_api

from utils.user_utils import not_auth


def create_article():
    token = users_api.get_token_from_session()
    st.title("Create Article")
    if token:
        title = st.text_input("Title")
        body = st.text_area("Body")
        if st.button("Create"):
            res = articles_api.create_article(token, title, body)
            if type(res) == type(str):
                st.warning(res)
            else:
                st.success("Created")
                st.title(f"{res.title}")
                st.write(f"{res.body}")

    else:
        not_auth()


create_article()
