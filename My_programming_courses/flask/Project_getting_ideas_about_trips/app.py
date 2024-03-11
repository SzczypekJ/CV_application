from flask import Flask, render_template, url_for, request, flash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SomethingWhatNoOneWillGuess'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == 'main':
    app.run()
