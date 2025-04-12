import streamlit as st

from article_api import comments as comments_api
from article_api import users as users_api

import schemas

from utils.user_utils import not_auth


def create_reply():
    st.title('Reply comment')
    token = users_api.get_token_from_session()
    if token:
        comment_uuid = st.text_input('Comment UUID')
        body = st.text_input('Body')
        if st.button('Send'):
            res = comments_api.create_reply(body, comment_uuid, token)
            st.success(res)
    
    else:
        not_auth()

        

create_reply()