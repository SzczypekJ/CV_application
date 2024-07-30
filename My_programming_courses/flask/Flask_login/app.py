import os
import binascii
import hashlib
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user, fresh_login_required
from urllib.parse import urlparse, urljoin

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'First, please log in using this form:'
login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = 'You need to log on again'


class User(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), unique=True)
    password = db.Column(String(100))
    first_name = db.Column(String(50))
    last_name = db.Column(String(50))

    def __repr__(self):
        return 'User: {},{}'.format(self.name, self.first_name)

    @staticmethod
    def get_hashed_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password_hash, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password_hash[:64]
        stored_password = stored_password_hash[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode(
            'utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


@login_manager.user_loader
def load_user(id):
    return User.query.filter(User.id == id).first()


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc


class LoginForm(FlaskForm):
    name = StringField('User name')
    password = PasswordField('Password')
    remember = BooleanField('Remember me')


@app.route('/init')
def init():
    db.create_all()

    admin = User.query.filter_by(name='admin').first()
    if admin is None:
        admin = User(id=1, name='admin', password=User.get_hashed_password(
            'Passw0rd'), first_name='King', last_name='Kong')
        db.session.add(admin)
        db.session.commit()

    return '<h1>Initial configuration done!</h1>'


@app.route('/')
def index():
    return '<h1>Hello!</h1>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user and User.verify_password(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Logged in successfully!', 'success')
            next = request.args.get('next')
            if next and is_safe_url(next):
                return redirect(next)
            else:
                return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return '<h1>You are logged out</h1>'


@app.route('/docs')
@login_required
def docs():
    return '<h1>You have access to protected docs. You are {}</h1>'.format(current_user.name)


@app.route('/secrets')
@fresh_login_required
def secrets():
    return '<h1>You have access to protected secrets</h1>'


if __name__ == '__main__':
    app.run(debug=True)
