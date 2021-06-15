
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["MAIL_DEFAULT_SENDER"] = 'HerbertTheConquerer@gmail.com'  # os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = 'doodle123!'
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = 'TODO'


# SQLAlchemy is used as ORM for the data storage of registrants:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_registry.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Pycharm does not detect .Column etc.
class Registrant(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(150), unique=False, nullable=False)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    sports = db.Column(db.String(500), unique=False, nullable=False)

    def __repr__(self):
        return f'*{self.id}: {self.email}, {self.first_name} {self.last_name}, {self.sports}*'


# allowed sports between which the registrants can choose
SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee"
]


@app.route('/')
def index():
    return render_template("index.html", sports=SPORTS)


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    sport = request.form.get("sport")

    if not first_name:
        return render_template("error.html", message="Missing first name")
    if not last_name:
        return render_template("error.html", message="Missing last name")
    if not email:  # TODO: validate email and send confirmation email?
        return render_template("error.html", message="Missing email")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    registrant = Registrant(
        email=email,
        first_name=first_name,
        last_name=last_name,
        sports=sport
    )

    db.session.add(registrant)
    db.session.commit()
    db.session.close()

    return redirect("/registrants")


@app.route('/registrants')
def registrants():
    registrants_lst = Registrant.query.all()
    return render_template("registrants.html", registrants=registrants_lst)  # a dict


if __name__ == "__main__":
    app.run(port=1337, debug=True)  # debug is turned off in deployment (hard security weakness)
