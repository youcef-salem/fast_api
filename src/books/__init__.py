from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(version=version,
              title="bookly",
              description="thi is a hort api documenation of a book store "
              )
app.include_router(book_router,prefix=f"/api/{version}/books", tags="books")






