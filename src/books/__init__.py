from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting...")
    await init_db()
    yield
    print("server has been stopped...")

version = "v1"

app = FastAPI(
    version=version,
    title="bookly",
    description="This is a short API documentation of a book store",
    lifespan=lifespan
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])






