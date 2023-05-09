import paho.mqtt.client as mqtt


print(1)
client = mqtt.Client("python_pub") # puclisher 이름
client.connect("58.72.111.186", 1883)
client.loop_start()
# common topic 으로 메세지 발행
client.publish("test/test_topic", "test_message", 1) # topic, message
client.loop_stop()
# 연결 종료
client.disconnect()