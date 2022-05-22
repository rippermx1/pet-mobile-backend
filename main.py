from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Card(BaseModel):
    name: str
    description: str
    price: float
    is_available: bool


@app.get("/")
def ping():
    return {"message": "pong"}

@app.get("/cards", response_model=List[Card])
def cards():
    return [
        {"name": "cat", "description": "cat", "price": 1.0, "is_available": True},
        {"name": "dog", "description": "dog", "price": 1.0, "is_available": True},
        {"name": "snake", "description": "snake", "price": 1.0, "is_available": True}
    ]