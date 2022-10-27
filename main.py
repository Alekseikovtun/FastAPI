from typing import List
from fastapi import FastAPI, Query, Path, Body
from schemas import Author, Book, BookOut


app = FastAPI()


# @app.get('/')  #first page
# def home():
#     return {'key': 'Hello'}


# @app.get('/{pk}')
# def get_item(pk: int, q: int = None):
#     return {'key': pk, 'q': q}


# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {'user': pk, 'item': item}


# @app.post('/book')
# def create_book(item: Book, author: Author, quantity: int = Body(...)):
#     return {'item': item, 'author': author, "quantity": quantity}


# @app.post('/author')
# def create_author(author: Author = Body(..., embed=True)):
#     return {'author': author}


# @app.get('/book')
# def get_book(q: List[str] = Query(
#     ["test", "test2"],  #initial values
#     description='Search book',
#     deprecated=True
#     )
#         ):
#     return q


# @app.get('/book/{pk}')  #gt=value (min value), le=value (max value)
# def get_single_book(
#     pk: int = Path(..., gt=1, le=20),
#     pages: int = Query(None, gt=10, le=500)
#         ):
#     return {'pk': pk, 'pages': pages}

@app.post(
    '/book',
    response_model=BookOut,
    # response_model_include={'pages', 'date'}  #Include the selected parameters
    # response_model_exclude={'pages', 'date'} #Excludes the selected parameters
    # response_model_exclude_unset=True  #Excludes default properties
)
def create_book(item: Book):
    # book = item.dict()
    # book['id'] = 3
    return BookOut(**item.dict(), id=3)
    # return book
