import paho.mqtt.client as mqtt
import json
import time

def user_regis_pub(topic_name, data):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("MQTT connect OK\n")
        else:
            print("Bad connection Returned code=", rc)
    
    def on_message(client, userdata, message):
        global RESULT
        result_msg = json.loads(str(message.payload.decode('utf-8')))
        RESULT = result_msg['result']
        print('received mqtt msg:', result_msg)

        client.loop_stop()
        client.disconnect()
    
    def on_disconnect(client, userdata, flags, rc=0):
        print('MQTT disconnected\n')

    def on_subscribe(client, userdata, mid, granted_qos):
        print('subcribed:', sub_topic)

    def on_publish(client, userdata, mid):
        print('published to ', pub_topic, '\n')

    # address = ''
    address = 'localhost'

    base_topic = '/sometopic'
    if topic_name == 'photo':
        pub_topic = base_topic + 'engine/register'
        sub_topic = base_topic + 'engine/register/result'
    elif topic_name == 'audio_start':
        pub_topic = base_topic + 'engine/register/start'
        sub_topic = base_topic + 'engine/register/result'
    elif topic_name == 'audio_end':
        pub_topic = base_topic + 'engine/register/end'
        sub_topic = base_topic + 'engine/register/result'
    elif topic_name == 'user':
        pub_topic = base_topic + 'user/register'
        sub_topic = base_topic + 'user/register/result'
    elif topic_name == 'delete':
        pub_topic = base_topic + 'user/delete'
        sub_topic = base_topic + 'user/delete/result'

    regis_client = mqtt.Client() # publisher 이름
    regis_client.on_connect = on_connect
    regis_client.on_message = on_message
    regis_client.on_disconnect = on_disconnect
    regis_client.on_subscribe = on_subscribe
    regis_client.on_publish = on_publish
    
    regis_client.connect(address, 1883)
    regis_client.subscribe(sub_topic, 1)
    regis_client.loop_start()
    regis_client.publish(pub_topic, data, 1) # topic, message
    time.sleep(10)


data = json.dumps({'user_name' : '김의현'})
# user_regis_pub('user', data)
# user_regis_pub('audio_start', data)
user_regis_pub('delete', data)
