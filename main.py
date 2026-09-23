from fastapi import FastAPI
from src.routes.book_api import router as book_router

app = FastAPI()

app.include_router(book_router)