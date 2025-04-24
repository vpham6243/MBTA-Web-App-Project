from flask import Flask, render_template, request
import mbta_helper

app = Flask(__name__)

@app.route("/")
def get_station():
    """
    Display the form for user to input a location
    """
    return render_template("index.html")


@app.post("/nearest_mbta")
def post_weather():
    """
    Display the result after submitting the form
    """
    place = request.form["place"]
  
    station_name, access_msg, lat, lon = mbta_helper.find_stop_near(place)

    if lat != "N/A":
        temp = mbta_helper.get_temp(lat, lon)
        result = {
            "Nearest Station:": place,
            "station": station_name,
            "accessibility": access_msg,
            "temperature": temp,
            "latitude": lat,
            "longitude": lon
        }
    else:
        result = {
            "Nearest Station:": place,
            "station": "No station found",
            "accessibility": "N/A",
            "temperature": "Weather unavailable",
            "lat": "N/A",
            "lon": "N/A"
            "Please enter another location..."
        }

    return render_template("mbta_station.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)