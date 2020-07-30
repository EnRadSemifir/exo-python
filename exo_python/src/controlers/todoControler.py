from flask_classful import FlaskView, route
from flask import jsonify
from flask import abort
from flask import request
from flask import jsonify
import services.todoService as todoService


class TodosView(FlaskView):
    route_base = '/api/todos/'

    @route('/')
    def get_todos(self):
        todos = todoService.get_todos()
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
