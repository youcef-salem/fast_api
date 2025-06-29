from sqlmodel import create_engine,text
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
        statement = text("SELECT'helo';")

        respond = await conn.execute(statement)

        print(respond.all())
    