import datetime
from database import store_weather_data, get_stored_data

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def process_weather_data(weather_data):
    for city_weather in weather_data:
        temp_k = city_weather['main']['temp']
        temp_c = kelvin_to_celsius(temp_k)
        weather_summary = {
            "city": city_weather['name'],
            "timestamp": city_weather['dt'],
            "temp": temp_c,
            "feels_like": kelvin_to_celsius(city_weather['main']['feels_like']),
            "condition": city_weather['weather'][0]['main']
        }
        store_weather_data(weather_summary)

def get_daily_summary():
    stored_data = get_stored_data()
    summary_by_day = {}
    
    for data in stored_data:
        date = datetime.datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d')
        city = data['city']
        if date not in summary_by_day:
            summary_by_day[date] = {}
        if city not in summary_by_day[date]:
            summary_by_day[date][city] = {"temps": [], "conditions": []}
        
        summary_by_day[date][city]["temps"].append(data["temp"])
        summary_by_day[date][city]["conditions"].append(data["condition"])
    
    daily_summary = []
    for date, cities_data in summary_by_day.items():
        for city, metrics in cities_data.items():
            avg_temp = sum(metrics["temps"]) / len(metrics["temps"])
            max_temp = max(metrics["temps"])
            min_temp = min(metrics["temps"])
            dominant_condition = max(set(metrics["conditions"]), key=metrics["conditions"].count)
            daily_summary.append({
                "city": city,
                "date": date,
                "avg_temp": avg_temp,
                "max_temp": max_temp,
                "min_temp": min_temp,
                "dominant_condition": dominant_condition
            })
    return daily_summary

def get_alerts():
    alerts = []
    stored_data = get_stored_data()
    for i in range(1, len(stored_data)):
        prev = stored_data[i - 1]
        curr = stored_data[i]
        if curr['temp'] > 35 and prev['temp'] > 35:
            alerts.append(f"Heat alert in {curr['city']}: {curr['temp']}°C")
    return alerts
