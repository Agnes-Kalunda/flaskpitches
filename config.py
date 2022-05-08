import os
class Config:
    """
    General parent configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daniel:daniel@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    """
    """
    pass

class DevConfig(Config):
    """
    """
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}