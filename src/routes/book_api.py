from fastapi import APIRouter, HTTPException
from src.services.books2 import Book
from src.schema.book_schema import *

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/")
async def read_all_books():
    return Book.get_all()

@router.post("/add")
async def add_book(book:add_Book):
    Book(**book.model_dump()).add_book()

@router.put("/update/{book_id}")
async def update_book(book_id: int, data:update_Book):
    book = next((b for b in Book.get_all() if b.id == book_id), None)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found.")
    book.update_book(data)
    return {
        "message": "Book Details changed successfully.",
        "book": book
    }
