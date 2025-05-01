from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import Token
from app.services.auth import authenticate_user, login_user
from app.services.user import create_user, is_user_authenticated, is_user_admin
from app.db.session import get_db

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/signin", response_model=Token)
def signin(email: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    return login_user(user.id)

@router.get("/isAuthenticated")
def is_authenticated(user_id: int, db: Session = Depends(get_db)):
    if is_user_authenticated(db, user_id):
        return {"message": "User is authenticated"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authenticated")

@router.get("/isAdmin")
def is_admin(user_id: int, db: Session = Depends(get_db)):
    if is_user_admin(db, user_id):
        return {"message": "User is an admin"}
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not an admin")