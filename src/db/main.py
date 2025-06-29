from sqlmodel import create_engine,text ,SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
engine = AsyncEngine(
    create_engine(
    url= Config.Database_url,
    echo= True 
    
)
)
async def init_db():
    async with engine.begin() as conn :
        from src.books.models import Book
        await conn.run_sync(    SQLModel.metadata.create_all)

    