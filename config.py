import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = '20eabe5d64b0e216796e834f52d61fd0b70332fc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///admin.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'development.db')}"

    @staticmethod
    def validate():
        Config.validate_config()
        print("Using SQLIte for development.")

class TestingConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_UR = os.getenv(
        'TEST_DATABASE_URI',
        'sqlite:///:memory:'
    )

    @staticmethod
    def validate():
        Config.validate_config()
        if not os.getenv('TEST_DATABASE_URI'):
            print("Using SQLite for testing.")

class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        f"sqlite:///{os.path.join(basedir, 'production.db')}"
    )

    @staticmethod
    def validate():
        Config.validate_config()
        if not os.getenv('DATABASE_URI'):
            raise ValueError("Using SQLite for production.")