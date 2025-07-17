import requests
import openrouteservice
import time
import os
from dotenv import load_dotenv

ORS_API_KEY = os.getenv("ORS_API_KEY")
client = openrouteservice.Client(key=ORS_API_KEY)

def autocomplete_address(query, retries=3):
    """Fetch auto-completed address suggestions from OpenStreetMap's Nominatim API."""
    API_URL = f"https://nominatim.openstreetmap.org/search?format=json&q={query}"
    for attempt in range(retries):
        try:
            headers = {"User-Agent": "EcoAI-Hub/1.0"}
            response = requests.get(API_URL, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data:
                    return data[0]['display_name']
                else:
                    return None
            else:
                time.sleep(2)
        except requests.exceptions.RequestException:
            time.sleep(2)
    return None

def get_coordinates(address):
    """Get latitude and longitude for a given address."""
    API_URL = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
    try:
        headers = {"User-Agent": "EcoAI-Hub/1.0"}
        response = requests.get(API_URL, headers=headers)
        if response.status_code != 200:
            return None
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def get_travel_distance(source, destination, mode="driving-car"):
    """Calculate travel distance & duration using OpenRouteService."""
    transport_modes = {"Car": "driving-car", "Bicycle": "cycling-regular", "Walk": "foot-walking", "Public Transport": "driving-car"}
    try:
        coords = [(source[1], source[0]), (destination[1], destination[0])]
        route = client.directions(coordinates=coords, profile=transport_modes.get(mode, "driving-car"), format="geojson")
        distance_meters = route['features'][0]['properties']['segments'][0]['distance']
        duration_seconds = route['features'][0]['properties']['segments'][0]['duration']
        distance_km = round(distance_meters / 1000, 2)
        duration_minutes = round(duration_seconds / 60, 2)
        return distance_km, duration_minutes
    except Exception:
        return None, None

def get_address_from_coordinates(lat, lon):
    """Convert latitude & longitude into an address using OpenStreetMap API."""
    API_URL = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"

    try:
        headers = {"User-Agent": "EcoAI-Hub/1.0"}
        response = requests.get(API_URL, headers=headers)
        data = response.json()

        if "display_name" in data:
            return data["display_name"]
        else:
            return None
    except requests.exceptions.RequestException:
        return None

