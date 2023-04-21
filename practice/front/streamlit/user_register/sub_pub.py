import paho.mqtt.client as mqtt
import json
import base64

def on_message(client, userdata, message):
    received_msg = json.loads(message.payload.decode('utf-8'))
    print(received_msg)
    print("message received ", received_msg.keys())
    print("message topic= ", message.topic)
    print("message qos=", message.qos)
    print("message retain flag= ", message.retain)
    if message:
        client.publish("/aihome/powervoice/face_engine/register/result", "ok", 1)
        # client.disconnect()

broker_address = "localhost"

client1 = mqtt.Client()
client1.on_message = on_message

client1.connect(broker_address, 1883)

client1.subscribe("/aihome/powervoice/face_engine/register", 1)

client1.loop_forever()
