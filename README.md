# Real-Time Weather Monitoring System

This is a real-time weather monitoring system that retrieves weather data from OpenWeatherMap and provides rollups, aggregates, and alert notifications.

## Requirements

- Python 3.9
- Docker
- MongoDB

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/weather-monitoring-system.git
cd weather-monitoring-system

2. Install dependencies:
pip install -r requirements.txt

3. Set up Docker containers:
docker-compose up

4. Obtain an API key from OpenWeatherMap and set it in api_client.py

5. Run the app:
python app.py

## Features
Real-time weather data retrieval for Indian metros.
Daily weather summaries with average, max, and min temperatures.
Threshold alerts for high temperatures.
Data visualization for temperature trends.

### Next Steps:

- **Test the system**: Run your app locally and test the functionality with real weather data.
- **Deploy using Docker**: Use Docker Compose to deploy the app and MongoDB easily.
And add your API key in `api_client.py`. This should give a good end-to-end setup for real-time weather monitoring system.


