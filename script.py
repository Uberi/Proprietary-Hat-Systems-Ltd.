from googlemaps import googlemaps
import apikey
import json
import math

gmaps = googlemaps.Client(key=apikey.key())

"""
departure = "40 Saint George Street Toronto, ON M5S 2E4 Canada"
destination = "349 College Street Toronto, ON M5T 1S5 Canada"
"""

departure = raw_input("departure: ")
destination = raw_input("destination: ")

routes = gmaps.directions(departure, destination, mode = "walking")

steps = routes[0]['legs'][0]['steps']

waypoints = map(lambda waypoint: waypoint['start_location'], steps)
waypoints.append(steps[-1]['end_location'])

def getAngularDisplacement(targetCoord, currentCoord, displacementVector):
	targetVector = [targetCoord[0] - currentCoord[0], targetCoord[1] - currentCoord[1]]
	dotProductResult = targetVector[0] * displacementVector[0] + targetVector[1] * displacementVector[1]
	targetVectorMagnitude = math.sqrt(targetVector[0] ** 2 + targetVector[1] ** 2)
	displacementVectorMagnitude = math.sqrt(displacementVector[0] ** 2 + displacementVector[1] ** 2)
	print "Target Vector: ", targetVector
	print "Target Vector Magnitude: ", targetVectorMagnitude
	print "Displacement Vector: ", displacementVector
	print "Displacement Vector Magnitude: ", displacementVectorMagnitude
	print "Dot Product Result: ", dotProductResult
	return math.acos(dotProductResult / (targetVectorMagnitude * displacementVectorMagnitude))

t = [3,4]
c = [0,0]
d = [0,1]

print getAngularDisplacement(t,c,d)