import repositories.todo_repo as todoRepo
from models.todo import Todo
import jsonpickle
import json
# défintion d'une méthode pour récupérer les todos dans la base de données avec le repo


def get_todos():
    result = todoRepo.get_todos()
    todos = []
    for todo in result:
        print(todo)
        # print(json.dumps(todo.__dict__))
    return jsonpickle.encode(result)


def get_todo_by_id(todo_id):
    return todo_id


def create_todo(todoDto):
    todo = Todo(todoDto.title, todoDto.description, todoDto.done)
    data = todoRepo.create_todo(todo)
    todoDto = jsonpickle.encode(data,max_depth=2)
    return todoDto


def update_todo(todo_id):
    return todo_id


def delete_todo(todo_id):
    return todo_id

