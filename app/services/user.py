# File: app/services/user.py
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.crud.user import create_user as create_user_crud, get_user
from app.crud.role import get_role_by_name

def create_user(db: Session, user: UserCreate):
    return create_user_crud(db, user)

def is_user_authenticated(db: Session, user_id: int):
    user = get_user(db, user_id)
    return user is not None

def is_user_admin(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        return False
    return any(role.name == "admin" for role in user.roles)