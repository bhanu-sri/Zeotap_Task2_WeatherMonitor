import matplotlib.pyplot as plt
from database import get_stored_data
import datetime

def plot_temperature_trends():
    data = get_stored_data()
    dates = [datetime.datetime.fromtimestamp(d['timestamp']) for d in data]
    temps = [d['temp'] for d in data]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o')
    plt.title('Temperature Trends')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.savefig('static/temperature_trend.png')

def plot_daily_summaries():
    data = get_stored_data()
    # Add logic for daily summaries visualization
