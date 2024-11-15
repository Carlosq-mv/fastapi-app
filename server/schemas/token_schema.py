from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(Token):
    username: str | None = None
    email: str | None = None


