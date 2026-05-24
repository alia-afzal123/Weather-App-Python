# simple_test.py
import requests

API_KEY = "7601f05738bf4bd89af200605262305 "  # <-- YAHAN PASTE KARO
city = "Lahore"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

print(f"Testing URL: {url}")
print("-" * 50)

response = requests.get(url)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")