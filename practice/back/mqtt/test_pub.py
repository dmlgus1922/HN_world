import paho.mqtt.client as mqtt
import json

f = open('./data/air_data.json')
air_data = f.read()
air_json = json.loads(air_data)

print(air_json)
# data = j

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


# 새로운 클라이언트 생성
client = mqtt.Client()
# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
# address : localhost, port: 1883 에 연결
client.connect('', 1883)
client.loop_start()
# common topic 으로 메세지 발행
client.publish('김의현/출근상태', '출근 중', 1)
client.loop_stop()
# 연결 종료
client.disconnect()