from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# API details
API_KEY = '5bf2dd8448d4777bf5e71c9e4160deb2'
CURRENT_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FUTURE_WEATHER_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_current_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(CURRENT_WEATHER_URL, params=params)
    data = response.json()

    # Check if there is an error in the response
    if response.status_code != 200:
        return {"error": data.get("message", "Unknown error occurred")}

    return data

def get_future_weather(city, future_date):
    print(f"Fetching future weather for {city} on {future_date}")
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(FUTURE_WEATHER_URL, params=params)
    data = response.json()

    # Print the API response
    print(f"API response: {data}")

    # Check if there is an error in the response or if 'list' key is missing
    if response.status_code != 200 or 'list' not in data:
        print(f"Error: {data.get('message', 'Unknown error occurred')}")
        return None

    # Find the closest match for the future date
    for forecast in data['list']:
        forecast_date = datetime.utcfromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
        print(f"Checking forecast for {forecast_date}")
        if forecast_date == future_date:
            print("Matching forecast found!")
            return forecast

    # If no matching forecast found, return None
    print("No matching forecast found.")
    return None

@app.route('/current-weather', methods=['GET'])
def current_weather_route():
    city = request.args.get('city')
    current_weather = get_current_weather(city)
    
    if "error" in current_weather:
        return jsonify(current_weather), 404

    # Customize the response with specific details
    result = {
        "city requested is test": current_weather["name"],
        "temperature": current_weather["main"]["temp"],
        "description": current_weather["weather"][0]["description"],
        "wind_speed": current_weather["wind"]["speed"]
    }
    return jsonify(result)

@app.route('/future-weather', methods=['GET'])
def future_weather_route():
    city = request.args.get('city')
    future_date = request.args.get('date')
    future_weather = get_future_weather(city, future_date)

    if future_weather:
        return jsonify(future_weather)
    else:
        return jsonify({"error": "Weather data for the given date is not available."}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
