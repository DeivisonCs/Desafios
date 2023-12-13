#   Ended at 32:00

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from users import bp_Students

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'MyKeY0192'
app.register_blueprint(bp_Students, url_prefix='/student')
# db = SQLAlchemy(app)
db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def index():
    return "teste"

if __name__ == "__main__":
    app.run()