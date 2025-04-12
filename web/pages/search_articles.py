import streamlit as st
import pandas as pd

from article_api import articles as articles_api


def search_articles():
    st.title("Find Articles")
    text = st.text_input("Search for articles")
    if st.button("Search"):
        articles = articles_api.search_articles(text)
        data = {
            "UUID": [i.uuid for i in articles],
            "Title": [i.title for i in articles],
            "Author": [i.author_username for i in articles],
        }

        df = pd.DataFrame(data)
        st.dataframe(df)


search_articles()
