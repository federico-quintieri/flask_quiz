from flask import Blueprint, render_template, request
from app.services.weather_service import fetch_weather

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/", methods=["GET", "POST"])
def home():
    city = "Roma"  # default
    if request.method == "POST":
        form_city = request.form.get("city")
        if form_city:
            city = form_city

    weather_data = fetch_weather(city)

    return render_template("home.html", weather=weather_data, city=city)
