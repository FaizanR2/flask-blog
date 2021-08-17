from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

# creating database

db = SQLAlchemy()
DB_NAME = 'database.db'


# creating a flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'helloworld' # for hashing
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # importing blueprints

    from .views import views  # the . before the file signifies relative import
    from .auth import auth  # if you are inside a python package and are importing from another file, use a . 

    # Registering blueprints from other folders

    app.register_blueprint(views, url_prefix="/") #url prefix creates a category for routes to use present in views
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post, Comment, Upvote

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Checking database


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Database Created")

