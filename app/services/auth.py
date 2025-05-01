# File: app/services/auth.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.core.hash import verify_password
from app.core.security import create_access_token
from app.crud.user import get_user_by_email


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user


def login_user(user_id: int):
    return {
        "access_token": create_access_token(data={"user_id": user_id}),
        "token_type": "bearer"
    }