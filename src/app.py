from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {
        'id': 1,
        'title': u'Faire les courses',
        'description': u'Acheter du fromage rapé, du desktop et de l\'huile moteur',
        'done': False
    },
    {
        'id': 2,
        'title': u'Apprendre Flask',
        'description': u'Mettre en place des webservices',
        'done': False
    }
]


@app.route('/todos')
def get_todos():
    return jsonify(tasks)


@app.route('/todos/<int:todo_id>')
def get_todo_by_id(todo_id):
    result = [todo for todo in tasks if todo['id'] == todo_id]
    if len(result) == 0:
        abort(404)
    return jsonify(result[0])


@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or not 'title' in request.json:
        abort(400)
    todo = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'done': False
    }
    tasks.append(todo)
    return jsonify(todo), 201


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    result = [todo for todo in tasks if todo['id'] == todo_id]
    todo = result[0]
    todo['title'] = request.json['title']
    todo['description'] = request.json['description']
    todo['done'] = request.json['done']
    return jsonify(todo), 200


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    result = [todo for todo in tasks if todo['id'] == todo_id]
    tasks.remove(result[0])
    return jsonify(tasks), 200


if __name__ == "__main__":
    app.run(debug=True)
