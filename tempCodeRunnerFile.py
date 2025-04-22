from flask import Flask, render_template, request, redirect
import mbta_helper



print(mbta_helper.find_stop_near("Chinatown"))

app = Flask(__name__)


@app.route("/mbta")
def get_station():
    """Display the form for user to input a city name"""
    return render_template("index.html")