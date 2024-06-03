from flask_login import LoginManager
from app import app
from db.database import User
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    print(type(user_id))
    return User.query.get(user_id)