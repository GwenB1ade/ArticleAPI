import streamlit as st


def main():
    pages = {
        "Home": [st.Page("pages/home.py", title="🏠 Home")],
        "Account": [
            st.Page("pages/reg.py", title="Registration"),
            st.Page("pages/log.py", title="Login"),
        ],
        "Article": [
            st.Page("pages/my_articles.py", title="My articles"),
            st.Page("pages/create_article.py", title="Create article"),
            st.Page("pages/get_article.py", title="Get Article"),
            st.Page("pages/delete_article.py", title="Delete Article"),
            st.Page("pages/search_articles.py", title="Search Articles"),
            st.Page("pages/like.py", title="Like Article"),
            st.Page("pages/my_likes.py", title="My Likes"),
        ],
        "Comment": [
            st.Page("pages/comments/create_comment.py", title="Send comment"),
            st.Page("pages/comments/create_reply.py", title="Reply comment"),
        ],
    }

    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":
    main()
    # streamlit run main.py --server.runOnSave True
