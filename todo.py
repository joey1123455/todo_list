from fastapi import APIRouter, Path, status, HTTPException
from model import *

todo_router = APIRouter() 
todo_list = []

@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    context = {'message': 'Todo added successfully'}
    return context


@todo_router.get('/todo', response_model=TodoItems)
async def retrieve_todos() -> dict:
    context = {'todos': todo_list}
    return context


@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int = Path(..., title='''The ID of the
of the todo to retrieve.''')) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            context = {'todo': todo}
            return context
    # context = {'message': 'Todo with supplied id does not exist.'}
    # return context
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Todo with ID: {todo_id} not found!' 
    )


@todo_router.put('/todo/{todo_id}')
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title = '''
The ID of the todo to be edited''')) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            context = {'message': 'Todo updated successfully.'}
            return context
    # context = {'message': 'Todo with supplied id cant be found.'}
    # return context
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Todo with ID: {todo_id} not found!' 
    )


@todo_router.delete('/todo/{todo_id}/')
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            context = {'message': 'Todo selected has been deleted'}
            return context
    # context = {'message': 'Todo with specified ID not found'}
    # return context
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Todo with ID: {todo_id} not found!' 
    )


@todo_router.delete('/todo')
async def delete_all_todo() -> dict:
    todo_list.clear()
    context = {'message': 'All todos deleted'}
    return context