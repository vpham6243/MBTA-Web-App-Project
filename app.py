from flask import Flask, render_template, request, redirect
import mbta_helper

import urllib.request
import json
import pprint

print(mbta_helper.find_stop_near("Chinatown"))

app = Flask(__name__)

@app.route("/mbta")
def get_station():
    """Display the form for user to input a city name"""
    return render_template("index.html")


@app.post("/weather")
def post_weather():
    """
    Display the result after submitting the form
    """
    location = request.form["city"]
    temp = get_temp(city_name)
    return render_template("weather-result.html", city=city_name.title(), temp=temp)

if __name__ == "__main__":
    app.run(debug=True)
