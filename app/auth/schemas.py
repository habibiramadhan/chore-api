from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str
