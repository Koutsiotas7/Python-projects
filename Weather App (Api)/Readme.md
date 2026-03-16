Flask Weather App

A simple weather web application built with Flask that allows users to search for a city and view the current 
weather conditions using the OpenWeatherMap API.

Features

Search weather by city name
Displays current temperature in Celsius
Shows weather description (e.g., clear sky, rain, clouds)
Uses OpenWeatherMap API
Environment variables for secure API key storage
Built with Python Flask

Technologies Used

Python
Flask
HTML / Jinja2 Templates
Requests
python-dotenv
OpenWeatherMap API

How It Works

1. User enters a city name in the search form.
2. Flask sends a request to the OpenWeatherMap API.
3. The API returns weather data in JSON format.
4. Flask extracts temperature and weather description.
5. The data is displayed dynamically in the HTML template.

Run the Application

Set the Flask environment variables before running the app.

using bash

export FLASK_APP=server.py
export FLASK_DEBUG=1
flask run

After starting the server, open your browser and go to:
http://127.0.0.1:5000
http://127.0.0.1:5000
```
