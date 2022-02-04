from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


db = SQLAlchemy() #instantiating SQLAlchemy
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__) #instanting Flask app
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.activity import Activity
    from app.models.user import User
    from app.models.location import Location


    db.init_app(app) #attaches SQLA to Flask app
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import activity_bp
    app.register_blueprint(activity_bp)

    from .routes import user_bp
    app.register_blueprint(user_bp)

    from .routes import location_bp
    app.register_blueprint(location_bp)



    return app
