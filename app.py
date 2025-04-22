from flask import Flask
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
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
