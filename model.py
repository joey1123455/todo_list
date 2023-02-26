from pydantic import BaseModel
from typing import List

#model todo models inherits specific task format
# class Item(BaseModel):
#     item: str
#     status: str


#model for createing a task
class Todo(BaseModel):
    id: int
    item: str

    class Config:
        Schema_extra = {
            'Example': {
                'id': 1,
                'item': 'Example schema!'
            }
        }


#model for updating individual item
class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            'Example': {
                'item': 'Read the next chapter of the book'
            }
        }


#model to retrieve todo list
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            'example': {
                'todos': [
                    { 'item': 'Example schema 1!'},
                    { 'item': 'Example schema 2!'}
                ],
            }
        }