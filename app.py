from flask import Flask
from flask_login import LoginManager
from models import db, Admin
from flask_migrate import Migrate
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
import os

def create_app():

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    login_manager = LoginManager(app)
    migrate = Migrate(app, db)
    csrf = CSRFProtect(app)
    db.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    from auth.routes import auth_bp
    from products.routes import products_bp
    from posts.routes import posts_bp
    from dashboard.routes import dashboard_bp
    from public.routes import index_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(index_bp)

    return app

if __name__ == '__main__':

    app = create_app()
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)