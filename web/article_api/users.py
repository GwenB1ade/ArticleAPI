from typing import Optional
import streamlit as st
import requests

from dependencies import BACKEND_URL
from schemas.users import UserDataSchema, RegUserSchema


def get_userdata(token: str):
    userdata = requests.get(
        f"{BACKEND_URL}/auth/me", headers={"Authorization": f"Bearer {token}"}
    ).json()

    return UserDataSchema(username=userdata.get("username"), uuid=userdata.get("uuid"))


def get_userdata_from_session() -> Optional[dict]:
    token = st.session_state.get("token")
    if token:
        userdata = get_userdata(token)
        return userdata


def get_token_from_session() -> Optional[str]:
    token = st.session_state.get("token")
    return token


def registration(userdata: RegUserSchema) -> str:
    message = requests.post(f"{BACKEND_URL}/auth/reg", json=userdata.model_dump())
    return message.json().get("detail")


def get_token(email: str, password: str) -> str:
    data = requests.post(
        f"{BACKEND_URL}/auth/log", json={"email": email, "password": password}
    )

    token = data.json().get("access_token")
    return token
