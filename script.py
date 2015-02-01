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

# Variables
k_constant = 0.1
target_angle = 0 # PLACEHOLDER -the target angle that we want the servo to point at
current_angle = 0 # PLACEHOLDER - the current best estimate of where the servo is pointing
current_velocity = 0
time_length_of_iteration = 1/2
geofencing_radius = 10 # In Metres
last_heading = 0

# Initialize waypoints
routes = gmaps.directions(departure, destination, mode = "walking")
steps = routes[0]['legs'][0]['steps']
waypoints = map(lambda waypoint: waypoint['start_location'], steps)
waypoints.append(steps[-1]['end_location'])

# Methods
def get_angular_displacement(target_coord, current_coord, displacement_vector):
    target_vector = [target_coord[0] - current_coord[0], target_coord[1] - current_coord[1]]
    dot_product_result = target_vector[0] * displacement_vector[0] + target_vector[1] * displacement_vector[1]
    target_vector_magnitude = math.sqrt(target_vector[0] ** 2 + target_vector[1] ** 2)
    displacement_vector_magnitude = math.sqrt(displacement_vector[0] ** 2 + displacement_vector[1] ** 2)
    print "Target Vector: ", target_vector
    print "Target Vector Magnitude: ", target_vector_magnitude
    print "Displacement Vector: ", displacement_vector
    print "Displacement Vector Magnitude: ", displacement_vector_magnitude
    print "Dot Product Result: ", dot_product_result
    return math.acos(dot_product_result / (target_vector_magnitude * displacement_vector_magnitude))

def set_target(x):
	target_angle = x
	
def get_adjusted_velocity ():
    return k_constant * (current_angle - target_angle)

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

previous_time = time.time()

# Main Program Loop
while True:
    current_time = time.time()
    print "~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~\nNew reading: #" + str(current_time) +"\n"

    # Heading calculations
    droid.startSensingTimed(1,100)
    droid.eventWaitFor("sensors")
    current_heading = droid.sensorsReadOrientation().result[0]

    # Current Heading calculations
    current_angle += current_heading - last_heading# + current_velocity * (current_time - previous_time)
    #current_velocity = get_adjusted_velocity()

    print "Current Angle: ", current_angle
    print "Current Heading: ", current_heading
    print "Current Velocity: ", current_velocity
    print "Last Heading: ", last_heading
    print "Delta Time: ", current_time - previous_time
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

    # now = datetime.datetime.now()
    # ora = now.hour
    # minut = now.minute
    # secunda = now.second
    # ziua = now.day
    # luna = now.month
    # an = now.year
    # print str(ora)+":"+str(minut)+":"+str(secunda)+" / "+str(ziua)+"-"+str(luna)+"-"+str(an)

    previous_time = current_time
    last_heading = current_heading

    time.sleep(time_length_of_iteration)
