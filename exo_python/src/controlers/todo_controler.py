from flask_classful import FlaskView, route
from flask import jsonify
from flask import abort
from flask import request
import services.todo_service as todoService

# crréation d'une classe qui hérite de FlaskView


class TodosControler(FlaskView):
    # définition d'une route de base
    route_base = '/api/todos/'

    # dééfinition de l'extension de la route de base
    @route('/')
    def get_todos(self):  # definition d'une méthode pour récupérer les todos depuis le service
        todos = todoService.get_todos()  # todos récupérer depuis le service
        if len(todos) == 0:
            abort(400)
        return jsonify(todos)

    @route('/<int:todo_id>')
    def get_todo_by_id(self, todo_id):
        todo = todoService.get_todo_by_id(todo_id)
        return jsonify(todo)

    @route('/', methods=['POST'])
    def create_todo(self):
        todo = todoService.create_todo()
        return jsonify(todo)

    @route('/<int:todo_id>', methods=['PUT'])
    def update_todo(self, todo_id):
        todo = todoService.update_todo(todo_id)
        return jsonify(todo)

    @route('/<int:todo_id>', methods=['DELETE'])
    def delete_todo(self, todo_id):
        result = todoService.delete_todo(todo_id)
        return jsonify(result)
