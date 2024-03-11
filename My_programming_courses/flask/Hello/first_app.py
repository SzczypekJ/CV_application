from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    time_now = datetime.now().strftime('%H:%M:%S')
    return '<h1>Hello World: {}</h1>'.format(time_now)


@app.route('/links')
def links():
    body = '''<a href="http://www.google.com" target="_blank">Google</a> <br />
              <a href="http://www.bing.com" target="_blank">Default search engine to find Google</a>'''
    return body


if __name__ == '__main__':
    app.run()
