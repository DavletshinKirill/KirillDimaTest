import os
basedir = os.path.abspath(os.path.dirname(__file__))

#нельзя хранить пароль в явном виде, переделать


class Config:
    SECRET_KEY = os.urandom(32)
    MAIL_SERVER = 'smtp.yandex.ru' # вынести в переменные среды
    MAIL_PORT = 465 # вынести в переменные среды
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'sendertestmail@yandex.ru' # вынести в переменные среды
    MAIL_PASSWORD = 'dymoazxcfhplgxbz' # вынести в переменные среды
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_DEFAULT_SENDER = "sendertestmail@yandex.ru" # вынести в переменные среды

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
