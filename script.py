from googlemaps 
import googlemaps
import apikey
import json

gmaps = googlemaps.Client(key=apikey.key())

"""
departure = "40 Saint George Street Toronto, ON M5S 2E4 Canada"
destination = "349 College Street Toronto, ON M5T 1S5 Canada"
"""

departure = "Sydney"
destination = "Melbourne"

routes = gmaps.directions(departure, destination, mode = "walking")

steps = routes[0]['legs'][0]['steps']

waypoints = map(lambda waypoint: waypoint['start_location'], steps)
waypoints.append(steps[-1]['end_location'])
print waypoints