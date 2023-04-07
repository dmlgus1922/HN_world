import paho.mqtt.client as mqtt


print(1)
client = mqtt.Client("python_pub") # puclisher 이름
client.connect("localhost", 1883)
client.loop_start()
# common topic 으로 메세지 발행
client.publish("김의현/출근상태", "끝", 1) # topic, message
client.loop_stop()
# 연결 종료
client.disconnect()