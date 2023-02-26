from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    context = {'message': 'Hello World!'}
    return context


app.include_router(todo_router)