from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, ValidationError, Email
import os
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from datetime import date
import hashlib
import binascii

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)


class BookForm(FlaskForm):
    def validate_amount_event(form, field):
        if field.data % 2 != 1:
            raise ValidationError("This number must be even!")

    title = StringField('Book title', validators=[DataRequired("Enter book title"),
                                                  Length(min=5, max=50, message="The title must have 5-50 characters")],
                        default='Unknown')
    amount = IntegerField('Amount', validators=[
                          DataRequired(message="Enter amount"),
                          validate_amount_event])
    available = BooleanField('Available')
    cover = FileField("Book cover", validators=[FileRequired(),
                                                FileAllowed(['jpg', 'png'], "Sorry, we accept only png and jpg")])

    offer_date = DateField('Offer date', format='%Y-%m-%d')


class Book:
    def __init__(self, title, amount, available, email, offer_date):
        self.title = title
        self.amount = amount
        self.available = available
        self.email = email
        self.offer_date = offer_date


class BookFormEmail(BookForm):
    email = StringField("e-mail", validators=[Email()])


@app.route('/', methods=['GET', 'POST'])
def index():
    book = Book(title="How to take a nice photo",
                amount=11, available=True, email='', offer_date=date.today())
    form = BookFormEmail(obj=book)
    del form.available
    if form.validate_on_submit():
        f = form.cover.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.root_path, 'static', 'covers', filename))

        form.populate_obj(book)
        return f'''<H1>Hello</H1>
                    <ul>
                        <li>{form.title.label}: {book.title}</li>
                        <li>{form.amount.label}: {book.amount}</li>
                        <li>available: {book.available}</li>
                        <li>e-mail: {book.email}</li>
                        <li>offer date: {book.offer_date}</li>
                        <li><img src="{url_for('static', filename='covers/{}'.format(filename))}"></li>
                    </ul>'''

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
