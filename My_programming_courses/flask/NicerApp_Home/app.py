from flask import Flask, render_template, url_for, request, flash
import os
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SomethingWhatNoOneWillGuess'


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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



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

    notification_priorities = NotificationPriorities()
    notification_priorities.load_priorities()

    if request.method == "GET":
        return render_template("notification.html", list_of_priorities=notification_priorities.list_of_priorities)
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

        return render_template("notification_content.html", room_number=room_number, guest_name=guest_name,
                               notification_text=notification_text,
                               priority_type=priority_type)


if __name__ == 'main':
    app.run()
