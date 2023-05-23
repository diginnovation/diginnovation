from gpsdclient import GPSDClient
import time
import json
import redis
import RPi.GPIO

rds = redis.Redis(decode_responses=True)

# GPS is connected via RS485 to usb adapter, gps data acquired using gpsd daemon
# configured in /etc/default/gpsd (setting serial port) current configuration is /dev/ttyUSB0
gpsd_client = GPSDClient()

GPIO = RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED
LED_2 = 26;
GPIO.setup(LED_2, GPIO.OUT)

while True:
	GPIO.output(LED_2, True)
	# read gpsd
	lat = lon = speed = alt = 0.0
	gps_time = bearing = None
	print("getting gps data...")
	for r in gpsd_client.dict_stream(filter=['TPV'], convert_datetime=True):
		if 'track' in r:
			bearing = r['track']

		if all(key in r for key in ["lat","lon", 'time', 'speed', 'altHAE',]):
			lat = r['lat']
			lon = r['lon']
			alt = r['altHAE']
			# bearing = r['track']		# not used because query might take very long time
			speed = r['speed']
			gps_time = r['time']
			break
	print("Got gps data!")

	data = {
		"utc_timestamp": int(gps_time.strftime('%s') if gps_time else 0),
		"latitude": lat,
		"longitude":  lon,
		"speed": speed,
		"altitude": alt,
		# "bearing": bearing,
	}

	if bearing != None:
		data["bearing"] = bearing
	else:
		last_bearing = rds.hget('data', 'bearing')
		if last_bearing:
			data["bearing"] = last_bearing

	print(json.dumps(data, indent=4))
	rds.hset('data', mapping=data)
	GPIO.output(LED_2, False)


	time.sleep(.2)
