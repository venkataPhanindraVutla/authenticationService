
# File: app/db/init_db.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.role import Role

async def init_db(db: AsyncSession):
    result = await db.execute(select(Role).limit(1))
    if not result.scalars().first():
        db.add_all([
            Role(name="admin", description="Administrator"),
            Role(name="user", description="Normal User")
        ])
        await db.commit()