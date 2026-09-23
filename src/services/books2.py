from src.schema.book_schema import *

BOOKS = {}

class Book:

    def __init__(self, title: str, author: str, description: str, rating: int):
        self.id= max(BOOKS.keys(), default=0) + 1
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

    def add_book(self):
        BOOKS[self.id]=self

    def update_book(self, data:update_Book):
        for field, value in data.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(self, field, value)

    @staticmethod
    def get_book_by_rating(rating: int):
        return [b for b in BOOKS.values() if b.rating == rating]

    @staticmethod
    def get_book_by_id(book_id: int):
        return BOOKS.get(book_id)

    @staticmethod
    def get_all():
        return list(BOOKS.values())