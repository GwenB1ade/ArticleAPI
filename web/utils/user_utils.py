import streamlit as st


def auth_headers(token: str):
    headers = {"Authorization": f"Bearer {token}"}

    return headers


def not_auth():
    st.error("You are not logged in")
