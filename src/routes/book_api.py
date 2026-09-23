from fastapi import APIRouter, HTTPException
from src.services.books2 import Book
from src.schema.book_schema import *

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/")
async def read_all_books():
    return Book.get_all()

@router.get("/{book_id}")
async def fetch_book_by_id(book_id: int):
    book = Book.get_book_by_id(book_id)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return vars(book)

@router.post("/add")
async def add_book(book: add_Book):
    Book(**book.model_dump()).add_book()

@router.put("/update/{book_id}")
async def update_book(book_id: int, data:update_Book):
    book = Book.get_book_by_id(book_id)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found.")
    book.update_book(data)
    return {
        "message": "Book Details changed successfully.",
        "book": vars(book)
    }
