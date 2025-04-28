import pymongo
import multiprocessing
from datetime import datetime


def air_mongo():
    # 호스트 ip 입력
    MQTT_HOST = '192.168.20.230'

    # 몽고디비 서버 연결
    client = pymongo.MongoClient(host=MQTT_HOST, port=27017)

    # 디비 출력
    print('DB 확인:', client.list_database_names(), '\n')

    # sebu3.airsensor 컬렉션 접근
    db = client['sebu3']
    collection = db['airsensor']

    # 데이터 저장 때의 시간인 datetime 필드로 가장 최근 데이터 얻기
    latest_data = collection.find().sort([('datetime', pymongo.DESCENDING)]).limit(1)
    latest_data = latest_data[0]

    # 데이터 type은 dictionary 
    print('가장 마지막 저장 데이터:\n', latest_data, '\n')

    payload = latest_data['payload']
    # 전송된 디바이스 목록
    device_info = payload['device']

    for device in device_info:
        room_id = payload[device]['rid']
        if room_id == 1 and 'IAQ' in device:
            pm10 = payload[device]['param']['pm10']
            pm2d5 = payload[device]['param']['pm2d5']
            print(f'\nqueue 데이터 저장\n미세먼지: {pm10}, 초미세먼지: {pm2d5}\n')
            break

    # 혹은 IAQ1 센서로만 고정
    # pm10_iaq1 = payload['IAQ1']['param']['pm10']
    # pm2d5_iaq1 = payload['IAQ1']['param']['pm2d5']
    # print(f'IAQ1 미세먼지: {pm10_iaq1}, 초미세먼지: {pm2d5_iaq1}')

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
