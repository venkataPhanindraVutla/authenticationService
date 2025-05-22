from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import Token
from app.services.auth import authenticate_user, login_user, logout_user
from app.services.user import create_user, is_user_authenticated, is_user_admin
from app.db.session import get_db

router = APIRouter()

@router.post("/signup", response_model=UserOut)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        created_user = await create_user(db, user)
        if created_user is None:
             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists")
        return created_user
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error in signup endpoint: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error during signup")


@router.post("/signin", response_model=Token)
async def signin(email: str, password: str, db: AsyncSession = Depends(get_db)):
    try:
        user = await authenticate_user(db, email, password)
        if user is None:
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return login_user(user.id)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error in signin endpoint: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error during signin")


@router.get("/isAuthenticated")
async def is_authenticated(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        if await is_user_authenticated(db, user_id):
            return {"message": "User is authenticated"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authenticated")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error in isAuthenticated endpoint: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error during authentication check")


@router.get("/isAdmin")
async def is_admin(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        if await is_user_admin(db, user_id):
            return {"message": "User is an admin"}
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not an admin")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error in isAdmin endpoint: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error during admin check")


@router.post("/logout")
async def logout(user_id: int):
    try:
        logout_user(user_id)
        return {"message": "User logged out successfully"}
    except Exception as e:
        print(f"Error in logout endpoint: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error during logout")