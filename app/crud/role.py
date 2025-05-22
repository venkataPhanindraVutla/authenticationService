# File: app/crud/role.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.role import Role

async def get_role_by_name(db: AsyncSession, name: str):
    try:
        result = await db.execute(select(Role).filter(Role.name == name))
        return result.scalars().first()
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error getting role by name: {e}")
        return None

async def get_role(db: AsyncSession, role_id: int):
    try:
        result = await db.execute(select(Role).filter(Role.id == role_id))
        return result.scalars().first()
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error getting role by ID: {e}")
        return None