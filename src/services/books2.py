from src.schema.book_schema import *

BOOKS = []

class Book:

    def __init__(self, title: str, author: str, description: str, rating: int):
        self.id=self.get_book_id()
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

    def add_book(self):
        BOOKS.append(self)

    def update_book(self, data:update_Book):
        for field, value in data.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(self, field, value)

    @staticmethod
    def get_book_id():
        book_id = 1 if len(BOOKS)==0 else BOOKS[-1].id +1
        return book_id

    @staticmethod
    def get_all():
        return BOOKS