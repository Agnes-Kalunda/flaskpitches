import os


class Config:
    """
    General parent configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'DATABASE_URL: postgres://ujhrbwbeziqfai:3345dcdf35a29df4d33f85903a36413cfcec3a6f6530302bce6258a6c55e3c33@ec2-107-22-238-112.compute-1.amazonaws.com:5432/da3c2q4n8jr56i'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("postgresql+psycopg2://moringa:access@localhost/pitches")    
    DEBUG= True


class DevConfig(Config):
    
    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}