import os
from flask import Flask
from flask_login import LoginManager
from .models import db, User

def create_app():
    app = Flask(__name__)

    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
    os.makedirs(db_path, exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_path, "siem.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'siem-super-secret-key-2024')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access the dashboard.'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            analyst = User(username='analyst', role='analyst')
            analyst.set_password('analyst123')
            db.session.add(analyst)
            db.session.commit()

    from .routes import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app