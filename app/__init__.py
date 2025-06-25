from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS

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

    CORS(app)  # ⬅️ Permitir solicitudes desde el navegador

    return app
