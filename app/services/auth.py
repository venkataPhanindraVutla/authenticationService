# File: app/services/auth.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.hash import verify_password
from app.core.security import create_access_token
from app.crud.user import get_user_by_email


async def authenticate_user(db: AsyncSession, email: str, password: str):
    try:
        user = await get_user_by_email(db, email)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error authenticating user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error during authentication")


def login_user(user_id: int):
    try:
        return {
            "access_token": create_access_token(data={"user_id": user_id}),
            "token_type": "bearer"
        }
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error logging in user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error during login")


def logout_user(user_id: int):
    try:
        # In a real application, you might invalidate a token or clear a session here.
        # For this example, we'll just acknowledge the logout.
        print(f"User {user_id} logged out.")
        pass
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error logging out user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error during logout")