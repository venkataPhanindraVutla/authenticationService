# File: app/utils/jwt.py
from jose import jwt, JWTError
from app.core.config import settings

def decode_jwt_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None