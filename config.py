import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.urandom(32)
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'sendertestmail@yandex.ru'
    MAIL_PASSWORD = 'zaq1@WSX11'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_DEFAULT_SENDER = "sendertestmail@yandex.ru"

    @staticmethod
    def init_app(app):
        pass

# доделать почту


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Artes228@localhost:5432/users"
    #SQLALCHEMY_DATABASE_URI = 'sqlite://auth/develop.db'
    #DATABASE_URL = "postgresql:///demo_project"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Artes228@localhost:5432/users'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///auth/develop.db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
