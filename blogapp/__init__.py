from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from blogapp.config import Config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView




db = SQLAlchemy()
bcrypt = Bcrypt()
admin = Admin()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)    
    mail.init_app(app)
    Migrate(app,db)
    bootstrap = Bootstrap(app)
    from blogapp.users.routes import users
    admin.add_view(ModelView(models.User,models.db.session))
    from blogapp.posts.routes import posts
    admin.add_view(ModelView(models.Post,models.db.session))
    from blogapp.users.routes import users
    from blogapp.posts.routes import posts
    from blogapp.main.routes import main
    from blogapp.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
