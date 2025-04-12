from pydantic import BaseModel, EmailStr, field_validator
from email_validator import (
    validate_email,
    ValidatedEmail,
    EmailNotValidError,
    EmailSyntaxError,
)
from fastapi import HTTPException


class CreateUserSchema(BaseModel):
    username: str
    password: str
    email: EmailStr

    @field_validator("email", mode="before")
    @classmethod
    def email_validate(cls, field: EmailStr):
        try:
            validate_email(field)

        except EmailNotValidError:
            raise HTTPException(status_code=400, detail="The email was not validated.")

        except EmailSyntaxError:
            raise HTTPException(
                status_code=400,
                detail="Incorrect email address. Check your entry for an error",
            )

        return field


class UserSchema(BaseModel):
    uuid: str
    username: str
    email: EmailStr
    password: str


class ViewUserSchema(BaseModel):
    uuid: str
    username: str


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str
