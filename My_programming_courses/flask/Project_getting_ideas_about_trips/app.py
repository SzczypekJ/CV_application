from flask import Flask, render_template, url_for, request, flash
import os
import csv

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SomethingWhatNoOneWillGuess'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_trip', methods=["GET", "POST"])
def new_trip():
    if request.method == "GET":
        return render_template('new_trip.html')
    else:
        trip_name = '' if 'trip_name' not in request.form else request.form['trip_name']
        email = '' if 'your_email' not in request.form else request.form['your_email']
        short_description = '' if 'short_description' not in request.form else request.form[
            'short_description']

        completness = False if 'completness' not in request.form else request.form[
            'completness'] == 'yes'
        contact_ok = False if 'contact_ok' not in request.form else True

        data = {'trip_name': trip_name, 'email': email, 'short_description': short_description,
                'completness': completness, 'contact_ok': contact_ok}
        append_csv_data(data)

        return render_template('new_trip_results.html', trip_name=trip_name, your_email=email,
                               short_description=short_description, completness=completness, contact_ok=contact_ok)


@app.route('/existing_trips', methods=["GET", "POST"])  # type: ignore
def existing_trips():
    data = read_csv_data()
    if request.method == "GET":
        return render_template("existing_trips.html", trips=data)
    else:
        selected_trip_name = request.form["trip_name"]
        selected_trip = {}
        for trip in data:
            if trip['trip_name'] == selected_trip_name:
                selected_trip = trip
                break
        return render_template("existing_trips_result.html", selected_trip=selected_trip)


def read_csv_data():
    full_file_path = os.path.join(
        app.static_folder, "trips.txt")  # type: ignore
    fieldnames = ['trip_name', 'email',
                  'short_description', 'completness', 'contact_ok']
    entries = []
    with open(full_file_path, 'r', encoding="utf-8") as f:
        csv_reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in csv_reader:
            entries.append(row)
    return entries


def append_csv_data(data):
    full_file_path = os.path.join(
        app.static_folder, "trips.txt")  # type: ignore
    fieldnames = ['trip_name', 'email',
                  'short_description', 'completness', 'contact_ok']
    if not os.path.exists(full_file_path):
        with open(full_file_path, 'w+', newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

    with open(full_file_path, 'a', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data)


if __name__ == 'main':
    app.run()
