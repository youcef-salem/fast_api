from fastapi import APIRouter,Header,status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import books
from src.books.shemas import Book,UpdateBook
book_router = APIRouter()

@book_router.get('/',response_model=List[Book])
async def get_all_books():
    return books 
@book_router.post('/',status_code=status.HTTP_201_CREATED ,response_model=Book )
async def creat_book(Book_data :Book):
    new_book = Book_data.model_dump()
    books.append(new_book)
    return new_book 



@book_router.get('/{book_id}', response_model=Book)
async def get_book(book_id: int) -> dict :
    for book in books :
        if int(book["id"]) == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="book not found  "
    )
         


@book_router.patch('/{book_id}', response_model=Book)
async def update_book(book_id: int, book_update: UpdateBook):
    for book in books:
        if int(book["id"]) == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["publisher"] = book_update.publisher
            book["page_count"] = book_update.page_count
            book["language"] = book_update.language
            return book  # This now returns the updated book as a response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="book not found "
    )





@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if int(book["id"]) == book_id:
            books.remove(book)
            return {}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="book not found  "
    )
         