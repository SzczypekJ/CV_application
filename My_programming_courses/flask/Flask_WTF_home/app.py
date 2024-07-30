import binascii
import hashlib
import os
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import DateField, PasswordField, StringField, IntegerField, BooleanField, RadioField
from wtforms.validators import DataRequired, ValidationError, NumberRange
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, Date
from datetime import date
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user, fresh_login_required
from urllib.parse import urlparse, urljoin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WTForms12344321'
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'First, please log in using this form:'
login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = 'You need to log on again'


class TrainDelay(db.Model):
    __tablename__ = 'TrainDelay'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    train_number = db.Column(String(30), nullable=False, unique=True)
    is_delayed = db.Column(Boolean, default=False)
    delay_minutes = db.Column(Integer, default=0)
    delay_reason = db.Column(String(100))

    def __repr__(self) -> str:
        return f"{self.train_number} - {self.delay_minutes}"


class TrainInfo(FlaskForm):
    def start_with2letters(form, field):
        if not (len(field.data) >= 2 and field.data[0:2].isalpha()):
            raise ValidationError("Train number must start with 2 letters")

    train_number = StringField('Train number', validators=[DataRequired("Enter train number"),
                                                           start_with2letters])
    is_delayed = BooleanField('Is delayed')
    delay_minutes = IntegerField("Delay minutes", validators=[DataRequired("Enter delay"),
                                                              NumberRange(min=0, message='The delay must be a number >= 0')])
    delay_reason = RadioField('Delay reason', choices=['None', 'Weather', 'Failure', 'Other'],
                              default='None')


class TrainDelayOnStation(db.Model):
    __tablename__ = 'TrainDelayOnStation'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    train_number = db.Column(String(30), nullable=False)
    is_delayed = db.Column(Boolean, default=False)
    delay_minutes = db.Column(Integer, default=0)
    delay_reason = db.Column(String(100))
    station = db.Column(String(50))
    day = db.Column(Date)

    def __repr__(self) -> str:
        return f"{self.station} - {self.train_number} - {self.delay_minutes}"


class TrainInfoOnStation(TrainInfo):
    station = StringField('Station', validators=[
                          DataRequired("Enter station name")])
    day = DateField('Day', validators=[DataRequired(
        'Enter date')], default=date.today())


class User(db.Model, UserMixin):
    __tablename__ = 'users'
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
    return User.query.get(int(id))


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


@app.route('/delay_on_station', methods=['GET', 'POST'])
@login_required
def delay_on_station():
    form = TrainInfoOnStation()
    if form.validate_on_submit():
        train_delay_on_station = TrainDelayOnStation()
        form.populate_obj(train_delay_on_station)
        db.session.add(train_delay_on_station)
        db.session.commit()
        return f'''<H1>Hello</H1>
                    <ul>
                        <li>{form.train_number.label} : {form.train_number.data}</li>
                        <li>{form.is_delayed.label} : {form.is_delayed.data}</li>
                        <li>{form.delay_minutes.label} : {form.delay_minutes.data}</li>
                        <li>{form.delay_reason.label} : {form.delay_reason.data}</li>
                        <li>{form.station.label} : {form.station.data}</li>
                    </ul>
                    Following record was added to the table in database: {train_delay_on_station}'''
    return render_template('index.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TrainInfo()
    if form.validate_on_submit():
        train_delay = TrainDelay()
        form.populate_obj(train_delay)
        db.session.add(train_delay)
        db.session.commit()
        return f'''<H1>Hello</H1>
                    <ul>
                        <li>{form.train_number.label} : {form.train_number.data}</li>
                        <li>{form.is_delayed.label} : {form.is_delayed.data}</li>
                        <li>{form.delay_minutes.label} : {form.delay_minutes.data}</li>
                        <li>{form.delay_reason.label} : {form.delay_reason.data}</li>
                    </ul>
                    Following record was added to the table in database: {train_delay}'''
    return render_template('index.html', form=form)


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
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
