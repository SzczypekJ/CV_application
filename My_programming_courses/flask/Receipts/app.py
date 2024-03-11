from flask import Flask, request, url_for, redirect
import os

app = Flask(__name__)


@app.route('/')
def index():
    message = f"""<H1>To find receipts click the link:</H1>
    <a href="{url_for("receipts", _external=True)}" target="_blank">Receipts</a>"""
    return message


@app.route("/rate_receipt", methods=["GET", "POST"])
def rate_receipt():
    if request.method == "GET":
        body = f"""
            <form id="rating" action="{url_for("rate_receipt", _external=True)}" method="POST">
                <label for="note">What is your note for the receipt?</label><br>
                <select id="note" name="note">
                    <option value="5">It is great!</option>
                    <option value="4">It is very good</option>
                    <option value="3">It is just good</option>
                    <option value="2">It was poor</option>
                    <option value="1">It was horrible!</option>
                </select></br>

                <label for=comment>Write down your comments:</label><br>
                <textarea id="comment" name="comment" rows="3" cols="50">
                </textarea><br>

                <label for="decision">Would you cook it for your family?</label><br>
                <input type="checkbox" id="decision" name="decision"><br>
    
                <input type="submit" value="Share my feedback">
            </form>
        """
        return body
    else:
        note = 3
        comment = ""
        decision = False
        if "note" in request.form:
            note = request.form["note"]

        if "comment" in request.form:
            comment = request.form["comment"]

        if "decision" in request.form:
            decision = True

        message = f'''Your rating was: {note}<br> 
                    Your comment was: {comment}<br> 
                    Your decision was {decision} '''
        return message


@app.route('/cook')
def receipts():
    body = f'''<a href="{url_for("cook",receipt="Pancakes", step=1, _external=True)}" target="_blank">Pancakes</a> <br />
              <a href="{url_for("cook", receipt="Soup", step=1, _external=True)}" target="_blank">Soup</a>'''
    return body


@app.route('/cook/<string:receipt>/<int:step>')
def cook(receipt, step):
    print(request.query_string)
    print('----')
    print(request.args)

    font_size = "200%"
    if "font-size" in request.args:
        font_size = request.args["font-size"]

    body = f'''<H1 style="font-size: {font_size}">In the receipt {receipt} you are on step {step}</H1>
                <H1 style="font-size: {font_size}">At the link below you can find a formula in which you can say what do you think about the receipt:</H1>
                <a href="{url_for("rate_receipt", _external=True)}" target="_blank">Rate_receipt</a>
    '''
    return body


@app.route("/not_implemented/<string:message>")
def not_implemented(message):
    font_size = "500%"
    return f'<H1 style="font-size: {font_size}; color:red">{message}</h1>'


@app.route("/new_receipt")
def new_receipt():
    return redirect(url_for("not_implemented", message="Function new_receipt is not ready yet"))


@app.route("/delete_receipt/<name>")
def delete_receipt(name):
    return redirect(url_for("not_implemented", message="Function delete_receipt is not ready yet"))


@app.route("/download/<string:file>")
def download(file):
    subpath = "download/"+file
    local_file_path = os.path.join(app.static_folder, subpath)  # type: ignore

    if (os.path.isfile(local_file_path)):
        print('file found')
        return redirect(url_for('static', filename=subpath))
    else:
        print('sorry file not found')
        return 'File not found!'


if __name__ == '__main__':
    app.run()
