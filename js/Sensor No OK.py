import time
import json
import falcon
import redis

rds = redis.Redis(decode_responses=True)

class Sensors:
	def on_get(self, req, resp):
		data = rds.hgetall('data')

		for k in ['latitude', 'longitude', 'speed', 'altitude', 'temperature_left', 'temperature_right', 'bearing']:
			if k in data:
				data[k] = float(data[k])

		for k in ['arm_height_left', 'arm_height_right', 'utc_timestamp']:
			if k in data:
				data[k] = int(data[k])

		for k in ['pump_switch_left', 'pump_switch_right', 'pump_switch_main']:
			if k in data:
				data[k] = True if data[k] == 'true' else False

		for k in data:
			if data[k] == "":
				data[k] = None

		resp.text = json.dumps(data, ensure_ascii=False)
		resp.status = falcon.HTTP_200
