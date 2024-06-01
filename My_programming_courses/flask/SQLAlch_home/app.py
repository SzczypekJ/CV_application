from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

Base = declarative_base()

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Author(db.Model):
    __tablename__ = 'Author'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50))
    special = db.Column(Boolean)


def __repr__(self):
    return '<id: {}, name: {}, special: {}>'.format(self.id, self.name, self.special)


@app.route('/')
def index():
    db.create_all()
    return '<h1>Hello World!!!</h1>'


if __name__ == '__main__':
    app.run()
