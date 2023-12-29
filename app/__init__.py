import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    }
metadata = MetaData(naming_convention=convention) 

db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
mail = Mail()

access_key = os.environ.get('FLASK_SECRET_KEY')
migrate = Migrate()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    migrate.init_app(app, db)
    app.app_context().push()      
    
       
    from app.user.routes import user
    from app.main.routes import main
    from app.admin.routes import admin
    from app.aluno.routes import aluno
    from app.acervo.routes import acervo
    from app.errors.handlers import errors

    app.register_blueprint(user)
    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(aluno)
    app.register_blueprint(acervo)
    app.register_blueprint(errors)     
    
    return app
    