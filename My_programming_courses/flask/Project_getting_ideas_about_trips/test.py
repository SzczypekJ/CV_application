from flask import Flask, render_template, url_for, request, flash
import os
import csv

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SomethingWhatNoOneWillGuess'


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


def existing_trips():
    data = read_csv_data()
    print('data: ', data)


with app.test_request_context():
    existing_trips()
