from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_migrate import Migrate

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def page_not_found(e):
    return render_template("error.html", code=404, description="Page not found")


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    app.register_error_handler(404, page_not_found)

    from .auth import auth
    app.register_blueprint(auth)
    from .main import main
    app.register_blueprint(main)
    return app

