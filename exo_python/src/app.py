from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from controlers.todoControler import TodosView

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@192.168.99.100:3306/todos'
db = SQLAlchemy(app)
TodosView.register(app)


if __name__ == "__main__":
    app.run(debug=True)
