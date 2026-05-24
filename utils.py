# utils.py

def kelvin_to_celsius(kelvin):
    """Kelvin ko Celsius mein convert karo"""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Kelvin ko Fahrenheit mein convert karo"""
    return (kelvin - 273.15) * 9/5 + 32

def get_weather_icon(weather_main):
    """Weather ke hisaab se emoji dikhao"""
    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Haze": "🌫️"
    }
    return icons.get(weather_main, "🌡️")