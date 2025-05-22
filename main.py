from fastapi import FastAPI
from app.api.rotes import auth,user
from app.core.config import settings
from app.db.session import async_engine
from app.db.base_class import Base

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])