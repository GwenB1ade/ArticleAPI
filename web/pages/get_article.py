import streamlit as st

from article_api import articles as articles_api
from article_api import comments as comments_api


def get_article():
    st.title('Get Article by UUID')
    uuid = st.text_input("UUID Article")
    if st.button("Get"):
        res = articles_api.get_article_by_uuid(uuid)
        if res:
            st.title(f"{res.title}")
            st.write(f"{res.body}")
            
            comments = comments_api.get_comments(uuid)
            if comments:
                with st.expander(f'Comments'):
                    for c in comments:
                        st.write(f'*{c.author_username}*: {c.body}')
                        if c.answers:
                            for ans in c.answers:
                                st.write(f'____ *{ans.author_username}*: {ans.body}')

        else:
            st.error(f"There is no article on such a UUID")


get_article()
