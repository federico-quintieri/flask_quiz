from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import Quiz, db, User
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from random import choice
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


API_KEY = "223083a5fe10974ce94a87a634656dd5"  # metti la tua chiave qui


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = []
    city = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&lang=it&appid={API_KEY}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            weather_data = []

            weather_data = []

    forecast_list = data.get("list", [])
    for day_index in range(3):  # voglio 3 giorni
        idx = day_index * 8  # ogni 24h = 8 * 3h
        if idx >= len(forecast_list):  # protezione contro index out of range
            break
        day_data = forecast_list[idx]
        date = datetime.fromtimestamp(day_data["dt"])
        day_name = date.strftime("%A")
        temp_day = day_data["main"]["temp_max"]
        temp_night = day_data["main"]["temp_min"]
        weather_data.append(
            {"day": day_name, "temp_day": temp_day, "temp_night": temp_night}
        )

        print(request.method, request.form)
        print(weather_data)
    return render_template("home.html", weather=weather_data)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        login = request.form["login"]
        nickname = request.form["nickname"]
        password = request.form["password"]

        if User.query.filter_by(login=login).first():
            return "Login già esistente"

        if User.query.filter_by(nickname=nickname).first():
            return "Nickname già esistente"

        user = User(
            login=login, nickname=nickname, password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(login=request.form["login"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("home"))
        return "Credenziali errate"
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    if request.method == "POST":
        selected = int(request.form["answer"])
        question_id = int(request.form["question_id"])
        question = Quiz.query.get(question_id)

        if selected == question.correct:
            current_user.score += 1
            db.session.commit()

    question = choice(Quiz.query.all())  # domanda casuale
    return render_template("quiz.html", question=question, score=current_user.score)


@app.route("/leaderboard")
def leaderboard():
    # prende tutti gli utenti ordinati per punteggio decrescente
    users = User.query.order_by(User.score.desc()).all()
    return render_template("leaderboard.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
