import requests
from datetime import datetime

API_KEY = "223083a5fe10974ce94a87a634656dd5"  # metti la tua chiave qui


def fetch_weather(city: str, days: int = 3):
    """
    Chiama l'API OpenWeatherMap e ritorna una lista di dizionari
    con le previsioni per i prossimi 'days' giorni.
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&lang=it&appid={API_KEY}"
    res = requests.get(url)
    if res.status_code != 200:
        return []

    data = res.json()
    forecast_list = data.get("list", [])
    weather_data = []

    # Mappatura giorni inglese -> italiano
    giorni_it = [
        "lunedì",
        "martedì",
        "mercoledì",
        "giovedì",
        "venerdì",
        "sabato",
        "domenica",
    ]

    for day_index in range(days):
        idx = day_index * 8  # ogni 24h = 8 intervalli da 3h
        if idx >= len(forecast_list):
            break
        day_data = forecast_list[idx]
        date = datetime.fromtimestamp(day_data["dt"]).date()
        day_name = giorni_it[date.weekday()]
        temp_day = day_data["main"]["temp_max"]
        temp_night = day_data["main"]["temp_min"]

        weather_data.append(
            {
                "date": date,
                "day": day_name,
                "temp_day": temp_day,
                "temp_night": temp_night,
            }
        )

    return weather_data
