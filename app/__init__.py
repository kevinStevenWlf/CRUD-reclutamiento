from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models

    from app.routes import register_blueprints
    register_blueprints(app)

    # print("Rutas registradas:")
    # for rule in app.url_map.iter_rules():
    #     print(rule)


    return app
