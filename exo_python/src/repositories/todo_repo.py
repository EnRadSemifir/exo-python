from flask_sqlalchemy import SQLAlchemy
from models.todo import Todo

db = SQLAlchemy()

# récupération des données dans la base de données


def get_todos():
    todos = Todo.query.all()
    return todos


def get_todo_by_id(todo_id):
    return todo_id


def create_todo(todo):
    return "ok"


def update_todo(todo_id):
    return todo_id


def delete_todo(todo_id):
    return todo_id
