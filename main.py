from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    a, b = 1, 2
    return (a+b)
    return {"Hello": "World"}

@app.get("/about")
def about(name: str = 'Na', age: int = 20):
    return {"Hello": {name, age}}

@app.get("/items/{item_id}")
def read_item(item_id: int,
              q: Optional[str] = 'None'):
    return {"item_id": item_id, "q": q}