from flask import Flask, redirect, render_template, url_for, request, flash, g, session
from datetime import date
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Date, Text, Boolean

import random
import string
import hashlib
import binascii


# wtk - User
# nmF - password
app = Flask(__name__)

app.config['SECRET_KEY'] = 'SomethingWhatNoOneWillGuess'

app.config.from_pyfile('config.cfg')

Base = declarative_base()

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Transaction(db.Model):
    __tablename__ = 'Transaction'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    currency = db.Column(String(5))
    amount = db.Column(Integer)
    user = db.Column(String(30))
    trans_date = db.Column(Date)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(100))
    email = db.Column(String(100))
    password = db.Column(Text)
    is_active = db.Column(Boolean)
    is_admin = db.Column(Boolean)


class Currency:
    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self) -> str:
        return '<Currency {}>'.format(self.code)


class CantorOffer:
    def __init__(self):
        self.currencies = []
        self.denied_codes = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'Dollar', 'flag_usa.png'))
        self.currencies.append(Currency('EUR', 'Euro', 'flag_europe.png'))
        self.currencies.append(Currency('JPY', 'Yen', 'flag_japan.png'))
        self.currencies.append(Currency('GBP', 'Pound', 'flag_UK.png'))

        self.denied_codes.append('USD')

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency

        return Currency('unknown', 'unknown', 'flag_pirates.png')


class UserPass:
    def __init__(self, user='', password=''):
        self.user = user
        self.password = password
        self.email = ''
        self.is_valid = False
        self.is_admin = False

    def hash_password(self):
        """Hash a password for storing."""
        # the value generated using os.urandom(60)
        os_urandom_static = b"ID_\x12p:\x8d\xe7&\xcb\xf0=H1\xc1\x16\xac\xe5BX\xd7\xd6j\xe3i\x11\xbe\xaa\x05\xccc\xc2\xe8K\xcf\xf1\xac\x9bFy(\xfbn.`\xe9\xcd\xdd'\xdf`~vm\xae\xf2\x93WD\x04"
        salt = hashlib.sha256(os_urandom_static).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512', self.password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode(
            'utf-8'), salt.encode('ascii'),  100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def get_random_user_pasword(self):
        random_user = ''.join(random.choice(
            string.ascii_lowercase)for i in range(3))
        self.user = random_user

        # + string.digits + string.punctuation
        password_characters = string.ascii_letters
        random_password = ''.join(random.choice(
            password_characters)for i in range(3))
        self.password = random_password

    def login_user(self):
        user_record = User.query.filter(User.name == self.user).first()

        if user_record != None and self.verify_password(user_record.password, self.password):
            return user_record
        else:
            self.user = None
            self.password = None
            return None

    def get_user_info(self):
        db_user = User.query.filter(User.name == self.user).first()

        if db_user == None:
            self.is_valid = False
            self.is_admin = False
            self.email = ''
        elif db_user.is_active != 1:
            self.is_valid = False
            self.is_admin = False
            self.email = db_user.email
        else:
            self.is_valid = True
            self.is_admin = db_user.is_admin
            self.email = db_user.email


@app.route('/init_app')
def init_app():
    db.create_all()
    # check if there are users defined (at least one active admin required)
    active_admins = User.query.filter(
        User.is_active == True, User.is_admin == True).count()

    if active_admins > 0:
        flash('Application is already set-up. Nothing to do')
        return redirect(url_for('index'))

    # if not - create/update admin account with a new password and admin privileges, display random username
    user_pass = UserPass()
    user_pass.get_random_user_pasword()

    new_admin = User(name=user_pass.user, email='noone@nowhere.no',
                     password=user_pass.hash_password(), is_active=True, is_admin=True)  # type: ignore
    db.session.add(new_admin)
    db.session.commit()
    flash('User {} with password {} has been created'.format(
        user_pass.user, user_pass.password))
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()

    if request.method == 'GET':
        return render_template('login.html', active_menu='login', login=login)
    else:
        user_name = '' if 'user_name' not in request.form else request.form['user_name']
        user_pass = '' if 'user_pass' not in request.form else request.form['user_pass']

        login = UserPass(user_name, user_pass)
        login_record = login.login_user()

        if login_record != None:
            session['user'] = user_name
            flash('Logon successful, welcome {}'.format(user_name))
            return redirect(url_for('index'))
        else:
            flash('Logon failed, try again')
            return render_template('login.html', active_menu='login', login=login)


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        flash('You are logged out')
    return redirect(url_for('login'))


@app.route('/')
def index():
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()
    return render_template('index.html', active_menu='home', login=login)


@app.route("/exchange", methods=["GET", "POST"])
def exchange():
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    offer = CantorOffer()
    offer.load_offer()

    if request.method == "GET":
        return render_template("exchange.html", active_menu='exchange', offer=offer, login=login)
    else:
        amount = 100
        if "amount" in request.form:
            amount = request.form["amount"]

        currency = "EUR"
        if "currency" in request.form:
            currency = request.form["currency"]

        if currency in offer.denied_codes:
            flash('The currency {} cannot be accepted'.format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash('The selected currency is unknown and cannot be accepted')
        else:
            new_tran = Transaction(
                currency=currency, amount=amount, user='admin', trans_date=datetime.now())  # type: ignore
            db.session.add(new_tran)
            db.session.commit()
            flash('Request to exchange {} was accepted'.format(currency))

        return render_template("exchange_results.html", active_menu='exchange', currency=currency, amount=amount,
                               currency_info=offer.get_by_code(currency), login=login)


@app.route("/history")
def history():
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    transactions = Transaction.query.all()

    return render_template('history.html', active_menu='history', transactions=transactions, login=login)


@app.route('/delete_transaction/<int:transaction_id>')
def delete_transaction(transaction_id):
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    del_tran = Transaction.query.filter(
        Transaction.id == transaction_id).first()
    db.session.delete(del_tran)
    db.session.commit()

    return redirect(url_for('history'))


@app.route('/edit_transaction/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    offer = CantorOffer()
    offer.load_offer()

    if request.method == "GET":  # Sprawdzenie metody żądania
        transaction = Transaction.query.filter(
            Transaction.id == transaction_id).first()

        if transaction is None:
            flash('No such transaction!')
            return redirect(url_for('history'))
        else:
            return render_template('edit_transaction.html', transaction=transaction, offer=offer, active_menu='history',
                                   login=login)

    else:
        amount = 100
        if "amount" in request.form:
            amount = request.form["amount"]

        currency = "EUR"
        if "currency" in request.form:
            currency = request.form["currency"]

        if currency in offer.denied_codes:
            flash('The currency {} cannot be accepted'.format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash('The selected currency is unknown and cannot be accepted')
        else:
            transaction = Transaction.query.filter(
                Transaction.id == transaction_id).first()
            transaction.currency = currency  # type: ignore
            transaction.amount = amount  # type: ignore
            transaction.user = 'admin'  # type: ignore
            transaction.trans_date = date.today()  # type: ignore
            db.session.commit()

            flash('Transaction was updated')

        return redirect(url_for('history'))


@app.route('/users')
def users():
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()
    if not login.is_valid or not login.is_admin:
        return redirect(url_for('login'))

    users = User.query.all()

    return render_template('users.html', active_menu='users', users=users, login=login)


@app.route('/user_status_change/<action>/<user_name>')
def user_status_change(action, user_name):
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    if action == 'active':
        user = User.query.filter(
            User.name == user_name, User.name != login.user).first()
        if user:
            user.is_active = (user.is_active + 1) % 2
            db.session.commit()
    elif action == 'admin':
        user = User.query.filter(
            User.name == user_name, User.name != login.user).first()
        if user:
            user.is_admin = (user.is_admin + 1) % 2
            db.session.commit()

    return redirect(url_for('users'))


@app.route('/edit_user/<user_name>', methods=['GET', 'POST'])
def edit_user(user_name):
    login = UserPass(session.get('user'))  # type: ignore
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    user = User.query.filter(User.name == user_name).first()
    message = None

    if user == None:
        flash('No such user')
        return redirect(url_for('users'))

    if request.method == 'GET':
        return render_template('edit_user.html', active_menu='users', user=user, login=login)
    else:
        new_email = '' if 'email' not in request.form else request.form['email']
        new_password = '' if 'user_pass' not in request.form else request.form['user_pass']

        if new_email != user.email:
            user.email = new_email
            db.session.commit()
            flash('Email was changed')

        if new_password != '':
            user_pass = UserPass(user_name, new_password)
            user.password = user_pass.hash_password()
            db.session.commit()
            flash('Password was changed')

        return redirect(url_for('users'))


@app.route('/delete_user/<user_name>')
def delete_user(user_name):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    user = User.query.filter(User.name == user_name,
                             User.name != login.user).first()
    if user:
        flash('User {} has been removed'.format(user_name))

    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users'))


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    message = None
    user = {}

    if request.method == 'GET':
        return render_template('new_user.html', active_menu='users', user=user, login=login)
    else:
        user['user_name'] = '' if not 'user_name' in request.form else request.form['user_name']
        user['email'] = '' if not 'email' in request.form else request.form['email']
        user['user_pass'] = '' if not 'user_pass' in request.form else request.form['user_pass']

        is_user_name_unique = (User.query.filter(
            User.name == user['user_name']).count() == 0)
        is_user_email_unique = (User.query.filter(
            User.name == user['email']).count() == 0)

        if user['user_name'] == '':
            message = 'Name cannot be empty'
        elif user['email'] == '':
            message = 'Email cannot be empty'
        elif user['user_pass'] == '':
            message = 'Password cannot be empty'
        elif not is_user_name_unique:
            message = 'User with name {} already exist'.format(
                user['user_name'])
        elif not is_user_email_unique:
            message = 'User with email {} already exist'.format(user['email'])

        if not message:
            user_pass = UserPass(user['user_name'], user['user_pass'])
            password_hash = user_pass.hash_password()
            new_user = User(name=user['user_name'], email=user['email'], password=password_hash,
                            is_active=True, is_admin=False)  # type: ignore
            db.session.add(new_user)
            db.session.commit()
            flash('User {} created'.format(user['user_name']))
            return redirect(url_for('users'))
        else:
            flash('Correct error: {}'.format(message))
            return render_template('new_user.html', active_menu='users', user=user, login=login)


if __name__ == 'main':
    app.run()
