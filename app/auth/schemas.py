from pydantic import BaseModel



#===============================================================
# SCHEMAS FOR AUTH
#===============================================================

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):  # Ganti nama UserOut menjadi UserResponse
    username: str
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str
