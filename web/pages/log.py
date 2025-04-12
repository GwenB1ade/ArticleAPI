import streamlit as st

from article_api import users as users_api
from schemas.users import LoginSchema


def login():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        token = users_api.get_token(email=email, password=password)
        st.session_state["token"] = token
        userdata = users_api.get_userdata(token)
        st.write(f"Hello {userdata.username}")


login()
