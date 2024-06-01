import datetime
from flask import Flask, redirect, render_template, url_for, request, flash, g, session
import os
import sqlite3
import datetime

import random
import string
import hashlib
import binascii
# btw - user name
# Wza - pass
app = Flask(__name__)

app.config['SECRET_KEY'] = 'SomethingWhatNoOneWillGuess'

app_info = {
    'db_file': 'C:/Users/szczy/Desktop/STUDIA/dodat/flask/NicerApp_Home/data/notifications.db'
}


def get_db():
    if not hasattr(g, 'sqlite_db'):
        conn = sqlite3.connect(app_info['db_file'])
        conn.row_factory = sqlite3.Row
        g.sqlite_db = conn
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


class PriorityType:
    def __init__(self, code, description, selected) -> None:
        self.code = code
        self.description = description
        self.selected = selected


class NotificationPriorities:
    def __init__(self) -> None:
        self.list_of_priorities = []

    def load_priorities(self):
        self.list_of_priorities.append(
            PriorityType('high', 'HIGH PRIORITY', False))
        self.list_of_priorities.append(PriorityType(
            'medium', 'MEDIUM', False))
        self.list_of_priorities.append(
            PriorityType('normal', 'NOT URGENT', True))
        self.list_of_priorities.append(PriorityType('low', 'REMARK', False))

    def get_priority_by_code(self, code):
        for priority in self.list_of_priorities:
            if priority.code == code:
                return priority

        return PriorityType('normal', 'NOT URGENT', True)


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
        db = get_db()
        sql_statement = 'SELECT * FROM users WHERE name=?'
        cur = db.execute(sql_statement, [self.user])
        user_record = cur.fetchone()

        if user_record != None and self.verify_password(user_record['password'], self.password):
            return user_record
        else:
            self.user = None
            self.password = None
            return None

    def get_user_info(self):
        db = get_db()
        sql_statement = 'SELECT * from users WHERE name=?'
        cur = db.execute(sql_statement, [self.user])
        db_user = cur.fetchone()

        if db_user == None:
            self.is_valid = False
            self.is_admin = False
            self.email = ''
        elif db_user['is_active'] != 1:
            self.is_valid = False
            self.is_admin = False
            self.email = db_user['email']
        else:
            self.is_valid = True
            self.is_admin = db_user['is_admin']
            self.email = db_user['email']


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = UserPass(session.get('user'))
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
    login = UserPass(session.get('user'))
    login.get_user_info()
    return render_template('index.html', active_menu='home', login=login)


@app.route('/init_app')
def init_app():
    # check if there are users defined (at least one active admin required)
    db = get_db()
    sql_statement = 'SELECT COUNT(*) as cnt FROM users WHERE is_active and is_admin;'
    cur = db.execute(sql_statement)
    active_admins = cur.fetchone()

    if active_admins != None and active_admins['cnt'] > 0:
        flash('Application is already set-up. Nothing to do')
        return redirect(url_for('index'))

    # if not - create/update admin account with a new password and admin privileges, display random username
    user_pass = UserPass()
    user_pass.get_random_user_pasword()
    sql_statement = '''INSERT INTO users(name, email, password, is_active, is_admin)
                    values(?,?,?,True,True);'''

    db.execute(sql_statement, [user_pass.user,
               'noone@nowhere.no', user_pass.hash_password()])
    db.commit()
    flash('User {} with password {} has been created'.format(
        user_pass.user, user_pass.password))
    return redirect(url_for('index'))


@app.route('/about')
def about():
    login = UserPass(session.get('user'))
    login.get_user_info()
    return render_template('about.html', active_menu='about', login=login)


def is_between_22_and_6():
    now = datetime.datetime.now().time()
    start_time = datetime.datetime.strptime('22:00:00', '%H:%M:%S').time()
    end_time = datetime.datetime.strptime('06:00:00', '%H:%M:%S').time()

    if start_time <= now or now <= end_time:
        return True
    else:
        return False


@app.route("/notification", methods=["GET", "POST"])
def notification():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    notification_priorities = NotificationPriorities()
    notification_priorities.load_priorities()

    if request.method == "GET":
        return render_template("notification.html", active_menu='notification', list_of_priorities=notification_priorities.list_of_priorities,
                               login=login)
    else:
        flash('Notification has been sent')
        room_number = ""
        if "room_number" in request.form:
            room_number = request.form["room_number"]

        guest_name = ""
        if "guest_name" in request.form:
            guest_name = request.form["guest_name"]

        notification_text = ""
        if "notification_text" in request.form:
            notification_text = request.form["notification_text"]

        priority = "normal"
        if "priority" in request.form:
            priority = request.form["priority"]

        priority_type = notification_priorities.get_priority_by_code(priority)
        print('found', priority_type.code)

        if priority == 'medium':
            if is_between_22_and_6():
                priority = 'high'
                priority_type.code = 'high'
                flash('Rising priority from medium to high')

        db = get_db()
        sql_command = 'INSERT INTO notifications(room_number, guest_name, notification, priority) values(?, ?, ?, ?)'
        db.execute(sql_command, [room_number,
                   guest_name, notification_text, priority])
        db.commit()
        return render_template("notification_content.html", active_menu='notification', room_number=room_number, guest_name=guest_name,
                               notification_text=notification_text,
                               priority_type=priority_type,
                               login=login)


@app.route("/history")
def history():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    db = get_db()
    sql_command = 'select * from notifications;'
    cur = db.execute(sql_command)
    notifications = cur.fetchall()

    return render_template('history.html', active_menu='history', notifications=notifications, login=login)


@app.route("/delete_notification/<int:notification_id>")
def delete_notification(notification_id):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    db = get_db()
    sql_statement = 'DELETE FROM notifications WHERE id = ?;'
    db.execute(sql_statement, [notification_id])
    db.commit()

    return redirect(url_for('history'))


@app.route('/edit_notification/<int:notification_id>', methods=['GET', 'POST'])
def edit_notification(notification_id):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    db = get_db()
    notification_priorities = NotificationPriorities()
    notification_priorities.load_priorities()

    if request.method == "GET":
        sql_statement = 'SELECT * FROM notifications WHERE id=?;'
        cur = db.execute(sql_statement, [notification_id])
        notif_obj = cur.fetchone()

        if notif_obj == None:
            flash('No such notification!')
            return redirect(url_for('history'))
        else:
            return render_template('edit_notification.html', notif_obj=notif_obj,
                                   list_of_priorities=notification_priorities.list_of_priorities, active_menu='history',
                                   login=login)

    else:
        room_number = ""
        if "room_number" in request.form:
            room_number = request.form["room_number"]

        guest_name = ""
        if "guest_name" in request.form:
            guest_name = request.form["guest_name"]

        notification_text = ""
        if "notification_text" in request.form:
            notification_text = request.form["notification_text"]

        priority = "normal"
        if "priority" in request.form:
            priority = request.form["priority"]

        priority_type = notification_priorities.get_priority_by_code(priority)
        print('found', priority_type.code)

        if priority == 'medium':
            if is_between_22_and_6():
                priority = 'high'
                priority_type.code = 'high'
                flash('Rising priority from medium to high')

        sql_command = '''UPDATE notifications SET room_number=?,
                                                guest_name=?,
                                                notification=?,
                                                priority=?
                                                WHERE id=?'''
        db.execute(sql_command, [room_number, guest_name,
                                 notification_text, priority, notification_id])
        db.commit()

        flash('Transaction was updated')

        return redirect(url_for('history'))


@app.route('/users')
def users():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid or not login.is_admin:
        return redirect(url_for('login'))

    db = get_db()
    sql_command = 'SELECT * FROM users;'
    cur = db.execute(sql_command)
    users = cur.fetchall()

    return render_template('users.html', active_menu='users', users=users, login=login)


@app.route('/user_status_change/<action>/<user_name>')
def user_status_change(action, user_name):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    db = get_db()

    if action == 'active':
        db.execute("""UPDATE users SET is_active = (is_active + 1) % 2
                   WHERE name = ? and name <> ?""",
                   [user_name, login.user])
        db.commit()
    elif action == 'admin':
        db.execute("""UPDATE users SET is_admin = (is_admin + 1) % 2
                   WHERE name = ? and name <> ?""",
                   [user_name, login.user])
        db.commit()

    return redirect(url_for('users'))


@app.route('/edit_user/<user_name>', methods=['GET', 'POST'])
def edit_user(user_name):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    db = get_db()
    cur = db.execute(
        'SELECT name, email FROM users WHERE name = ?', [user_name])
    user = cur.fetchone()
    message = None

    if user == None:
        flash('No such user')
        return redirect(url_for('users'))

    if request.method == 'GET':
        return render_template('edit_user.html', active_menu='users', user=user, login=login)
    else:
        new_email = '' if 'email' not in request.form else request.form['email']
        new_password = '' if 'user_pass' not in request.form else request.form['user_pass']

        if new_email != user['email']:
            sql_statement = 'UPDATE users SET email = ? WHERE name = ?'
            db.execute(sql_statement, [new_email, user_name])
            db.commit()
            flash('Email was changed')

        if new_password != '':
            user_pass = UserPass(user_name, new_password)
            sql_statement = 'UPDATE users SET password = ? WHERE name = ?'
            db.execute(sql_statement, [user_pass.hash_password(), user_name])
            db.commit()
            flash('Password was changed')

        return redirect(url_for('users'))


@app.route('/delete_user/<user_name>')
def delete_user(user_name):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    db = get_db()
    sql_statement = 'DELETE FROM users WHERE name = ? and name <> ?'
    db.execute(sql_statement, [user_name, login.user])
    db.commit()

    return redirect(url_for('users'))


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    db = get_db()
    message = None
    user = {}

    if request.method == 'GET':
        return render_template('new_user.html', active_menu='users', user=user, login=login)
    else:
        user['user_name'] = '' if not 'user_name' in request.form else request.form['user_name']
        user['email'] = '' if not 'email' in request.form else request.form['email']
        user['user_pass'] = '' if not 'user_pass' in request.form else request.form['user_pass']

        cursor = db.execute(
            'SELECT COUNT(*) as cnt FROM users WHERE name = ?', [user['user_name']])
        record = cursor.fetchone()
        is_user_name_unique = (record['cnt'] == 0)

        cursor = db.execute(
            'SELECT COUNT(*) as cnt FROM users WHERE email = ?', [user['email']])
        record = cursor.fetchone()
        is_user_email_unique = (record['cnt'] == 0)

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
            sql_statement = '''INSERT INTO users(name, email, password, is_active, is_admin)
                                values(?,?,?,True, False);'''

            db.execute(sql_statement, [
                       user['user_name'], user['email'], password_hash])
            db.commit()
            flash('User {} created'.format(user['user_name']))
            return redirect(url_for('users'))
        else:
            flash('Correct error: {}'.format(message))
            return render_template('new_user.html', active_menu='users', user=user, login=login)


if __name__ == 'main':
    app.run()
