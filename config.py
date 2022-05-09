import os


class Config:
    """
    General parent configuration parent class
    """
    SECRET_KEY = os.environ.get('aggie1234')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pitches:access@localhost/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("postgresql+psycopg2://pitches:access@localhost/")    
class DevConfig(Config):
    
    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}