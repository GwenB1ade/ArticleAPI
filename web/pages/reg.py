import streamlit as st

from schemas.users import UserDataSchema, RegUserSchema
from article_api import users as users_api


def reg():
    st.title("Reg")

    username = st.text_input("Username")
    email = st.text_input("email")
    password = st.text_input("Password", type="password")

    if st.button("Reg"):
        reg_data = RegUserSchema(username=username, email=email, password=password)

        detail = users_api.registration(reg_data)
        st.success(detail)


reg()
