from flask import Flask
from .config import Config
from .extensions import db, migrate, bcrypt, login_manager
from .models import User
from .routes import main
from .auth import auth
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Configuration for CORS
    CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5173"}})

    app.config.from_object(Config)
    app.config['DEBUG'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
