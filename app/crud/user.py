# File: app/crud/user.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.hash import hash_password

async def get_user_by_email(db: AsyncSession, email: str):
    try:
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalars().first()
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error getting user by email: {e}")
        return None

async def get_user(db: AsyncSession, user_id: int):
    try:
        result = await db.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error getting user by ID: {e}")
        return None

async def create_user(db: AsyncSession, user: UserCreate):
    try:
        hashed_password = hash_password(user.password)
        db_user = User(email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user
    except Exception as e:
        await db.rollback()
        # Log the error or handle it appropriately
        print(f"Error creating user: {e}")
        return None