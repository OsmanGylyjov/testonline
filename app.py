from flask import Flask, redirect, url_for
from flask_login import LoginManager
from models import db, User
from routes.auth import auth_bp
from routes.exam import exam_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online_exam.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Redirect
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(exam_bp, url_prefix='/exam')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)