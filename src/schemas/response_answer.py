from pydantic import BaseModel

class ResponseAnswerSchemas(BaseModel):
    detail: str|dict
    

class AccessTokenAnswerSchema(BaseModel):
    access_token: str
    token_type: str