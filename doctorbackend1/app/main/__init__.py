from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    bind=None,
    db._execute_for_all_tables(app, bind, 'create_all')
    # app_context.push()
    # db.create_all() 
    flask_bcrypt.init_app(app)

    return app

    
