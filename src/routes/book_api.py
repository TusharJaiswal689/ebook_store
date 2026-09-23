from fastapi import APIRouter, HTTPException, Path, Query, Request
from src.services.books2 import Book, BookRepository
from src.schema.book_schema import *

router = APIRouter(prefix="/books", tags=["Books"])

#-----GET-----

@router.get("")
async def read_all_books():
    return BookRepository.get_all()

@router.get("/{book_id}")
async def fetch_book_by_id(book_id: int= Path(gt=0)):
    book = BookRepository.get_book_by_id(book_id)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return vars(book)

@router.get("/")
async def filter_books_by_kwargs(request: Request):
    filters= dict(request.query_params)
    books = BookRepository.filter_book(filters)
    return [vars(book) for book in books]

@router.get("/search/")
async def search_book_by_likeness(query: str):
    books = BookRepository.search(query)
    return [vars(book) for book in books]

    
#-----POST-----

@router.post("/add")
async def add_book(book: add_Book):
    Book(**book.model_dump()).add_book()


#-----PUT-----

@router.put("/update/{book_id}")
async def update_book(data: update_Book, book_id: int= Path(gt=0), ):
    book = BookRepository.get_book_by_id(book_id)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found.")
    book.update_book_by_id(data)
    return {
        "message": "Book Details changed successfully.",
        "book": vars(book)
    }


#-----DELETE-----
@router.delete("/delete/{book_id}")
async def delete_book(book_id: int= Path(gt=0)):
    BookRepository.delete_book_by_id(book_id)
    return {
        "message": f"Book with id {book_id} deleted successfully."
    }