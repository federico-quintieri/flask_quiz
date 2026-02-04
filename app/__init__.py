from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
    )
    app.secret_key = "supersecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    
    # blueprint registration
    from app.security import auth
    from app.controllers.auth_controller import auth_bp
    from app.controllers.quiz_controller import quiz_bp
    from app.controllers.weather_controller import weather_bp
    

    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(weather_bp)

    with app.app_context():
        db.create_all()

    return app
