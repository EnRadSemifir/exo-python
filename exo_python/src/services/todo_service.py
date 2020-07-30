import repositories.todo_repo as todoRepo

# défintion d'une méthode pour récupérer les todos dans la base de données avec le repo


def get_todos():
    todos = todoRepo.get_todos()
    return todos


def get_todo_by_id(todo_id):
    return todo_id


def create_todo():
    return "ok"


def update_todo(todo_id):
    return todo_id


def delete_todo(todo_id):
    return todo_id
