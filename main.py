from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # Only get 10 published blogs
    return {'data': f'{limit} blogs from the db'} if published else {'data': 'all blogs'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # Fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit = 10):
    # Fetch (limit) comments of blog with id = id
    return {'data': {'1', '2'}}