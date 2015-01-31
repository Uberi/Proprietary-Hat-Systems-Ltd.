from googlemaps import googlemaps
import apikey
import json

gmaps = googlemaps.Client(key=apikey.key())

#departure = "40 Saint George Street Toronto, ON M5S 2E4"
#destination = "349 College Street Toronto, ON M5T 1S5 Canada"

departure = "Sydney"
destination = "Melbourne"

routes = gmaps.directions(departure, destination, mode="walking")

steps = routes[0][u'legs'][0][u'steps']

waypoints = map(lambda waypoint: waypoint[u'start_location'], steps)
waypoints.append(steps[-1][u'end_location'])
print waypoints