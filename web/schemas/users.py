from pydantic import BaseModel, EmailStr


class RegUserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserDataSchema(BaseModel):
    uuid: str
    username: str


class TokenSchema(BaseModel):
    token: str
