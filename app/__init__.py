from flask import Flask
from .extensions import db, jwt,migrate
from .routes.auth_routes import auth_bp
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)
    

    return app
