import os
import json 
import pprint
import urllib.request
import mbta_helper


from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# print(mbta_helper.find_nearest_mbta_stop("Boston Common"))

# Get API keys from environment variables
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")


# Useful base URLs (you need to add the appropriate parameters for each API request)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as resp:
        response_text = resp.read().decode("utf-8")
        return json.loads(response_text)




def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_encoded = urllib.parse.quote(place_name)
    # REMOVE &types=poi to allow general locations
    url = f"{MAPBOX_BASE_URL}/{place_encoded}.json?access_token={MAPBOX_TOKEN}"
    data = get_json(url)

    features = data.get("features", [])
    if not features:
        print(f"No location found for '{place_name}'")
        return None

    coordinates = features[0]["geometry"]["coordinates"]
    return str(coordinates[1]), str(coordinates[0])  # lat, lon


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    data = get_json(url)

    try:
        stop = data["data"][0]
        name = stop["attributes"]["name"]
        wheelchair = stop["attributes"]["wheelchair_boarding"] == 1
        return name, wheelchair
    except (IndexError, KeyError):
        return None



def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    coords = get_lat_lng(place_name)
    if coords:
        lat, lon = coords
        return get_nearest_station(lat, lon)
    else:
        return "No location found", False

def find_nearest_mbta_stop(place_name: str) -> tuple[str, bool]:
    return find_stop_near(place_name)

def main():
    """
    You should test all the above functions here
    """
   
    print(find_nearest_mbta_stop("Boston Common"))
    print(get_lat_lng("Boston Common"))


if __name__ == "__main__":
    main()
