from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    done = db.Column(db.Boolean)

    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        return f'<Client id:{self.id} title:{self.title} description:{self.description} done: {self.done}>'