from fastapi import HTTPException

BOOKS = {}

class Book:

    def __init__(self, title: str, author: str, description: str, rating: int, published_year: int):
        self.id= max(BOOKS.keys(), default=0) + 1
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_year=published_year

    def add_book(self):
        BOOKS[self.id]=self

    def update_book_by_id(self, data):
        for field, value in data.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(self, field, value)

class BookRepository:

    @staticmethod
    def delete_book_by_id(book_id: int):
        if book_id not in BOOKS:
            raise HTTPException(status_code=404, detail="Book not found.")
        del BOOKS[book_id]

    @staticmethod
    def filter_book(filters: dict):
        books= list(BOOKS.values())
        for key, value in filters.items():
            books= [b for b in books if str(getattr(b, key, None))==str(value)]
        return books
    
    @staticmethod
    def search(query: str) -> list:
        """Fuzzy search across title + author + description."""
        q = query.lower()
        return [b for b in BOOKS.values()
                if q in b.title.lower()
                or q in b.author.lower()
                or q in (b.description or "").lower()]
    
    @staticmethod
    def get_book_by_id(book_id: int):
        return BOOKS.get(book_id)

    @staticmethod
    def get_all():
        return list(BOOKS.values())

    @staticmethod
    def filter_book_by_published_date(published_year:int):
        return [b for b in BOOKS.values() if b.published_year == published_year]