import requests

API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def get_weather_data(city):
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}"
    response = requests.get(complete_url)
    return response.json()

def fetch_all_cities_weather():
    return [get_weather_data(city) for city in cities]
