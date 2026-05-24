# api.py
import requests
from config import API_KEY, BASE_URL

def get_weather(city_name, unit="celsius"):
    """City ka live weather fetch karo (WeatherAPI.com)"""
    
    url = f"{BASE_URL}?key={API_KEY}&q={city_name}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            current = data["current"]
            location = data["location"]
            
            # Temperatures get karo
            temp_c = current["temp_c"]
            feelslike_c = current["feelslike_c"]
            temp_f = current["temp_f"]
            feelslike_f = current["feelslike_f"]
            
            # Unit ke hisaab se select karo
            if unit == "celsius":
                temp = temp_c
                feels_like = feelslike_c
                temp_unit = "°C"
            else:
                temp = temp_f
                feels_like = feelslike_f
                temp_unit = "°F"
            
            return {
                "success": True,
                "city": location["name"],
                "temperature": round(temp, 1),
                "feels_like": round(feels_like, 1),
                "unit": temp_unit,
                "humidity": current["humidity"],
                "wind_speed": current["wind_kph"],
                "weather_main": current["condition"]["text"],
                "weather_desc": current["condition"]["text"]
            }
        else:
            return {
                "success": False,
                "error": "City not found! 😕"
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": f"Network error: {str(e)}"
        }