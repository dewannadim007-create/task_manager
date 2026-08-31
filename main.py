from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from db import get_db

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    """Check database connection"""
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "✅ Database connected!"}
    except Exception as e:
        return {"status": "❌ Database connection failed", "error": str(e)}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None, db: AsyncSession = Depends(get_db)):
    return {"item_id": item_id, "q": q}