from pydantic import BaseModel, Field
# from typing import Optional

# class Book(BaseModel):
#     title: str
#     author: str
#     category: str

class add_Book(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    description: str = Field(default=None, min_length=10, max_length=100)
    rating: int= Field(ge=1, le=5)

class update_Book(BaseModel):
    title: str = Field(default=None, min_length=1, max_length=50)
    author: str = Field(default=None, min_length=1, max_length=50)
    description: str = Field(default=None, min_length=1, max_length=100)
    rating: int = Field(default=None, ge=1, le=5)