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

print(MAPBOX_BASE_URL)