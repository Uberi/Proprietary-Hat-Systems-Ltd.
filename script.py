from googlemaps import googlemaps
import apikey
import json
import math
import android,time,datetime

droid = android.Android()
gmaps = googlemaps.Client(key=apikey.key())

departure = "40 Saint George Street Toronto, ON M5S 2E4 Canada"
destination = "349 College Street Toronto, ON M5T 1S5 Canada"

# departure = raw_input("departure: ")
# destination = raw_input("destination: ")

# Initialize waypoints
routes = gmaps.directions(departure, destination, mode = "walking")
steps = routes[0]['legs'][0]['steps']
waypoints = map(lambda waypoint: waypoint['start_location'], steps)
waypoints.append(steps[-1]['end_location'])

# Methods
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

# Android Sensor stuff
latitude = "initial value"
longitude = "initial value"
indexVal = 1
lostSignal = False

droid.startLocating()
droid.eventWaitFor("location")
location = droid.readLocation().result
droid.stopLocating()
location = droid.getLastKnownLocation().result

while True:
 print "~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~\nNew reading: #" + str(time.time) +"\n"

 droid.startSensingTimed(1,100)
 droid.eventWaitFor("sensors")
 heading = droid.sensorsReadOrientation().result[0]
 print heading

 # IGNORE THIS SHIT FOR NOW BOYS
 # if location != {}:
 #  if location['gps'] == None:
 #   if location['network'] == {}:
 #    latitude = str(location['passive']['latitude'])
 #    longitude = str(location['passive']['longitude'])
 #    print "Reading passive data (from last known location):"
 #    print longitude
 #    print latitude
 #    lostSignal = True
 #   elif location['network'] != {}:
 #    latitude = str(location['network']['latitude'])
 #    longitude = str(location['network']['longitude'])
 #    print "Reading data from network:"
 #    print latitude
 #    print longitude
 #    lostSignal = True

 # print "\nFull available information:\n"
 # for locInfo in location.iteritems():
 #    print str(locInfo)
 # print "\n"

 now = datetime.datetime.now()
 ora = now.hour
 minut = now.minute
 secunda = now.second
 ziua = now.day
 luna = now.month
 an = now.year
 print str(ora)+":"+str(minut)+":"+str(secunda)+" / "+str(ziua)+"-"+str(luna)+"-"+str(an)

 time.sleep(1/1000)