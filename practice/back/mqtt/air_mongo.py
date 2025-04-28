import pymongo
from datetime import datetime

def air_check(client):
    print('DB 확인:', client.list_database_names(), '\n')

    db = client['sebu3']
    collection = db['airsensor']
    latest_data = collection.find().sort([('datetime', pymongo.DESCENDING)]).limit(1)
    latest_data = latest_data[0]
    print('가장 마지막 저장 데이터:\n', latest_data, '\n')

    payload = latest_data['payload']
    device_info = payload['device']

    for device in device_info:
        room_id = payload[device]['rid']
        if room_id == 1 and 'IAQ' in device:
            pm10 = payload[device]['param']['pm10']
            pm2d5 = payload[device]['param']['pm2d5']
            print(f'\nqueue 데이터 저장\n미세먼지: {pm10}, 초미세먼지: {pm2d5}\n')
            break

    if pm10 <= 30:
        pm10_condition = '좋음'
    elif pm10 <= 80:
        pm10_condition = '보통'
    elif pm10 <= 150:
        pm10_condition = '나쁨'
    else:
        pm10_condition = '매우 나쁨'

    if pm2d5 <= 15:
        pm2d5_condition = '좋음'
    elif pm2d5 <= 35:
        pm2d5_condition = '보통'
    elif pm2d5 <= 75:
        pm2d5_condition = '나쁨'
    else:
        pm2d5_condition = '매우 나쁨'

    return [pm10_condition, pm2d5_condition]


def air_mongo(air_queue):
    # 호스트 ip 입력
    MQTT_HOST = '192.168.20.230'

    # 몽고디비 서버 연결
    client = pymongo.MongoClient(host=MQTT_HOST, port=27017)

    air_data = air_check(client)
    air_queue.put(air_data)

    start_time = datetime.now()

    while True:
        now_time = datetime.now()
        seconds = now_time - start_time
        seconds = seconds.seconds

        if seconds == 5:
            if not air_queue.empty():
                air_queue.get()
            air_data = air_check(client)
            air_queue.put(air_data)
            start_time = now_time
