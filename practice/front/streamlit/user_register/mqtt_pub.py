import paho.mqtt.client as mqtt


def user_regis_pub(topic_name, data):
    base_topic = 'aihome/powervoice/'

    if topic_name == 'photo':
        topic = base_topic + 'face_engine'
    
    regis_client = mqtt.Client() # puclisher 이름
    regis_client.connect("localhost", 1883)
    regis_client.loop_start()
    # common topic 으로 메세지 발행
    regis_client.publish('topic', data, 1) # topic, message
    regis_client.loop_stop()
    # 연결 종료
    regis_client.disconnect()
