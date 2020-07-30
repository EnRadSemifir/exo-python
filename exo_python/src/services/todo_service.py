import repositories.todo_repo as todoRepo
from models.todo import Todo

# défintion d'une méthode pour récupérer les todos dans la base de données avec le repo


def get_todos():
    todos = todoRepo.get_todos()
    return todos


def get_todo_by_id(todo_id):
    return todo_id


def create_todo(todoDto):
    todo = Todo(todoDto['title'], todoDto['description'], todoDto['done'])
    return todoRepo.create_todo(todo)


def update_todo(todo_id):
    return todo_id


def delete_todo(todo_id):
    return todo_id
