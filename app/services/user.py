# File: app/services/user.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.crud.user import create_user as create_user_crud, get_user
from app.crud.role import get_role_by_name

async def create_user(db: AsyncSession, user: UserCreate):
    try:
        return await create_user_crud(db, user)
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error creating user in service: {e}")
        return None

async def is_user_authenticated(db: AsyncSession, user_id: int):
    try:
        user = await get_user(db, user_id)
        return user is not None
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error checking if user is authenticated: {e}")
        return False

async def is_user_admin(db: AsyncSession, user_id: int):
    try:
        user = await get_user(db, user_id)
        if not user:
            return False
        # Assuming user.roles is awaitable or loaded
        return any(role.name == "admin" for role in user.roles)
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error checking if user is admin: {e}")
        return False