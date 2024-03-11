from flask import Flask, request, url_for, redirect
import os

app = Flask(__name__)


@app.route('/')
def index():
    menu = f'''
        Go <a href="{url_for("exchange", _external=True)}"> here</a> to exchange money<br>
        To exchange 50 CHF go <a href="{url_for("cantor", currency="CHF", amount=50, _external=True)}"> here</a><br>
        <img src="{url_for("static", filename="currencies/euro.jpg")}"><br>
        {url_for("static", filename="currencies/euro.jpg")}<br>
        {os.path.join(app.static_folder, "currencies/euro.jpg")}
    '''

    return f'<h1>Hello Word</h1><br>{menu}'


@app.route("/exchange", methods=["GET", "POST"])
def exchange():
    if request.method == "GET":
        body = f"""
            <form id="exchange_form" action="{url_for("exchange", _external=True)}" method="POST">
                <label for="currency">Currency</label>
                <input type="text" id="currency" name="currency" value="EUR"><br>
                <label for="amount">Amount</label>
                <input type="text" id="amount" name="amount" value="100"><br>
                <input type="submit" value="Send">
            </form>
        """
        return body
    else:
        currency = "EUR"
        if "currency" in request.form:
            currency = request.form["currency"]

        amount = 100
        if "amount" in request.form:
            amount = request.form["amount"]

        body = f"You want to exchange {amount} {currency}"

        return redirect(url_for("cantor", currency=currency, amount=amount))


@app.route("/cantor/<string:currency>/<int:amount>")
def cantor(currency, amount):
    message = f"<h1>You selected {currency} and amount {amount}</h1>"
    return message


@app.route('/about')
def about():
    a = 10
    b = 0
    return '<h1>We are programmers: {}</h1>'.format(a/b)


if __name__ == "__main__":
    app.run()
