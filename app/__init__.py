from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from SQLAlchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy



def create_app(config_name):
    app = Flask(__name__)
    
    #app configurations
    
    app.config.from_object(config_options[config_name])
    
    #flask extensions
    
    bootstrap.init_app(app)
    db.init_app(app)
    
    return app