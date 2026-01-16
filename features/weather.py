import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # set in your environment

def get_weather(city: str) -> str:
    if not API_KEY:
        return "Weather service not configured. Please set OPENWEATHER_API_KEY."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return f"Could not fetch weather data: {e}"

    if data.get("cod") != 200:
        msg = data.get("message", "unknown error")
        return f"Weather API error: {msg}"

    main = data.get("main", {})
    weather_list = data.get("weather", [])
    desc = weather_list[0]["description"] if weather_list else "N/A"
    temp = main.get("temp", "N/A")
    feels_like = main.get("feels_like", "N/A")

    return f"In {city}, it is {temp}°C (feels like {feels_like}°C) with {desc}."
