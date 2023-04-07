import paho.mqtt.client as mqtt

        
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc), 'dis')


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, message):
        print("message received ", str(message.payload.decode("utf-8")))
        print("message topic= ", message.topic)
        print("message qos=", message.qos)
        print("message retain flag= ", message.retain)


broker_address = "localhost"

client1 = mqtt.Client()

client1.on_connect = on_connect
client1.on_disconnect = on_disconnect
client1.on_subscribe = on_subscribe
client1.on_message = on_message


client1.connect(broker_address, 1883)

client1.subscribe("김의현/출근상태", 1)

client1.loop_forever()