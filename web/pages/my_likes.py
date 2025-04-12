import streamlit as st
import pandas as pd

from article_api import articles as articles_api
from article_api import users as users_api

from utils.user_utils import not_auth


def my_likes():
    st.title('My likes')
    token = users_api.get_token_from_session()
    if token:
        articles = articles_api.get_my_likes(token)
        if articles:
            data = {
                "UUID": [i.uuid for i in articles],
                "Title": [i.title for i in articles],
                "Author": [i.author.username for i in articles],
                "Likes": [i.likes for i in articles],
            }

            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.error("You don't have a single liked article.")
    
    else:
        not_auth()
        

my_likes()