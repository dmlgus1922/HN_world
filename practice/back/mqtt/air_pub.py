import paho.mqtt.client as mqtt
import json

f = open('./data/air_data.json')
air_data = f.read()
air_json = json.loads(air_data)

print(air_json)