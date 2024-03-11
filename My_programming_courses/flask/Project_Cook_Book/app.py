from fileinput import filename
from flask import Flask, redirect, url_for, render_template_string, request, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '123GoniszTy!'  # Klucz sesji


@app.route('/')
def index():

    name1 = "how to make a coffee"
    name2 = "how to make a tea"
    menu = f'''
        <h1>Select a receipt:</h1><br>
        <ul>
            <li style="margin-bottom: 10px;"><a href={url_for("receipt", name=name1, step=1)}>{name1}</a></li>
            <li style="margin-bottom: 10px;"><a href={url_for("receipt", name=name2, step=1)}>{name2}</a></li>
        </ul>
        <br>
        <a href="{url_for("comment")}">Leave a comment</a><br>
        <a href="{url_for("show_comments")}">Show comments</a>
    '''
    return menu


@app.route('/receipt/<name>/<int:step>')
def receipt(name, step):
    full_file_path = os.path.join(
        app.static_folder, 'receipts', name+'.txt')  # type: ignore
    print(full_file_path)
    if os.path.isfile(full_file_path):
        with open(full_file_path) as f:
            content = f.readlines()
            if len(content) >= step:
                instruction = content[step-1]

                menu = f'''<ul>
                    <li><a href={url_for('index')}>Home</a></li>
                    <li><a href={url_for('receipt', name=name, step=(step+1 if step<len(content) else step))}>Next</a></li>
                    <li><a href={url_for('receipt', name=name, step=(step-1 if step>1 else 1))}>Previous</a></li>
                    </ul>'''

                body = f'''
                    <h1>The step {step} for receipt {name}:</h1>
                    <p>{instruction}</p>
                    <br>
                    {menu}
                    '''
            else:
                body = f'There is no step number {step} for the receipt {name}!'

    else:
        body = 'The receipt does not exist!'

    return body


@app.route('/comment', methods=['GET', 'POST'])
def comment():

    if request.method == 'GET':
        body = f'''<form id=comment action="{ url_for('comment')}" method= "POST"'>
            <textarea name="data" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Send and return home">
        </form>'''

        return body

    else:
        if "data" in request.form:
            data = request.form["data"]
            data = data.replace('<', '&lt;').replace('>', '&gt;')

            comments_file = os.path.join(
                app.static_folder, 'comments', 'comments.txt')  # type: ignore
            with open(comments_file, 'a') as f:
                f.write("<li>"+data+"</li>")

        return redirect(url_for('index'))


@app.route('/show_comments')
def show_comments():

    comments_file = os.path.join(
        app.static_folder, 'comments', 'comments.txt')  # type: ignore
    with open(comments_file) as f:
        content = f.read()

    body = f'''
        <h1>The comments</h1>
        <ul>
            {content}
        </ul>
        <a href="{ url_for('index') }">Back to home</a>
    '''

    return body


@app.route('/download/<file>')
def download(file):

    subpath = 'download/'+file
    local_file_path = os.path.join(app.static_folder, subpath)  # type: ignore

    if (os.path.isfile(local_file_path)):
        print('file found')
        return redirect(url_for('static', filename=subpath))
    else:
        print('sorry file not found')
        return 'File not found!'


if __name__ == "__main__":
    app.run(debug=True)
