import streamlit as st
import cv2
# import streamlit_webrtc as webrtc
# from audio_recorder_streamlit import audio_recorder
from st_custom_components import st_audiorec
import base64
import json
import paho.mqtt.client as mqtt
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

########################## 세션 생성 ##########################
#-------------------------------------------------------------------

# 사용자 이름
if 'name' not in st.session_state:
    st.session_state.name = ''

# 이름 등록 결과
if 'name_regis' not in st.session_state:
    st.session_state.name_regis = False

#-------------------------------------------------------------------

# 사진 촬영 버튼 이름(한 번 클릭 시 재촬영으로 바뀌기 위함)
if 'photo_take_btn_name' not in st.session_state:
    st.session_state.photo_take_btn_name = '촬영' 

# 사진 촬영 횟수(촬영 버튼, 등록 버튼 갱신될 때마다 unique 키 만들기 위함)
if 'photo_take_num' not in st.session_state:
    st.session_state.photo_take_num = 0

# 촬영한 사진
if 'temp_photo' not in st.session_state:
    st.session_state.temp_photo = []

# 등록할 사진(캠 화면 프레임)
if 'photo' not in st.session_state:
    st.session_state.photo = []

#-------------------------------------------------------------------

# 사용자 음성
if 'audio' not in st.session_state:
    st.session_state.audio = ''

# # 음성 등록 
# if 'audio_regis' not in st.session_state:
#     st.session_state.audio_regis = False

# 음성 등록 결과
if 'audio_check' not in st.session_state:
    st.session_state.audio_check = ''

########################## 함수 생성(MQTT) ##########################

def user_regis_pub(topic_name, data):
    base_topic = 'aihome/powervoice/'

    if topic_name == 'photo':
        topic = base_topic + 'face_engine/register'
    
    regis_client = mqtt.Client() # puclisher 이름
    regis_client.connect("localhost", 1883)
    regis_client.loop_start()
    # common topic 으로 메세지 발행
    regis_client.publish(topic, data, 1) # topic, message
    regis_client.loop_stop()
    # 연결 종료
    regis_client.disconnect()



########################## 함수 생성(UI/UX) ##########################

def change_name_func():
    # st.session_state.name = st.session_state.name
    if not st.session_state.name:
        st.session_state.name_regis = '❗이름을 확인하세요'
    else:
        st.session_state.name_regis = f'✅ {st.session_state.name}님, 반가워요'
    # NAME_CHECK.write(st.session_state.name_regis)
    return st.session_state.name_regis

def name_regis_func():
    if not st.session_state.name:
        st.session_state.name_regis = '❗이름을 확인하세요'
    else:
        st.session_state.name_regis = f'✅ {st.session_state.name}님, 반가워요'


def photo_regis_func():
    cv2.imwrite('taked_photo.png', st.session_state.photo) # 우선 사진 저장으로 

    # photo_bytes = st.session_state.photo.tobytes()
    # photo_base64 = base64.b64encode(photo_bytes)

    # json_dict = {
    #     'file_name': f'aihome_powervoice_register_{st.session_state.name}.png',
    #     'file_body': photo_base64
    # }

    # json_data = json.dumps(json_dict)
    # photo_list = st.session_state.photo.tolist()
    # photo_bytearray = bytearray(photo_bytes)
    photo_data = base64.urlsafe_b64encode(st.session_state.photo).decode('utf-8')
    data = json.dumps({
        'file_name': f'aihome_powervoice_register_{st.session_state.name}.png',
        'file_body': photo_data
    })


    user_regis_pub('photo', data)

    # PHOTO_CHECK.write(f'✅ 사진 등록 완료!')


def photo_take_func():
    st.session_state.photo_take_btn_name = '재촬영'
    st.session_state.photo = st.session_state.temp_photo
    CAPTURED_PICTURE.image(st.session_state.photo, channels='BGR')
    PHOTO_REGIS_BTN.button(
        '등록', 
        key='photo_regis_key' + str(st.session_state.photo_take_num),
        on_click = photo_regis_func
        )
    st.session_state.photo_take_num += 1


def audio_regis_func():
    pass

################################### UI ###################################

############## 상단 제목 및 영상 ##############

st.markdown('<h1 style="text-align: center">사용자 등록</h1>', unsafe_allow_html=True)
blank1, cam_area, blank2 = st.columns(3)

with blank1:
    pass

with cam_area:
    WEB_CAM = st.image([])

with blank2:
    pass

st.markdown('<hr/>', unsafe_allow_html=True)


############## 사용자 명 ##############

# name_check_area, name_text_area, name_input_area, name_regis_area = st.columns(4)

# with name_check_area:
#     NAME_CHECK = st.container()

# with name_text_area:
#     st.write('사용자 명')

# with name_input_area:
#     st.session_state.name = st.text_input(
#         '이름', label_visibility='collapsed', 
#         on_change=change_name_func
#         )
    
# with name_regis_area:
#     st.button('등록', key='name_regis_key', on_click=name_regis_func)

# if st.session_state.name_regis:
#     NAME_CHECK.write(change_name_func())

name_check_area, name_text_area, name_input_regis_area = st.columns([1,1,2])

with name_check_area:
    NAME_CHECK = st.container()

with name_text_area:
    st.write('사용자 명')

with name_input_regis_area:
    name_input_area, name_regis_area = st.columns(2)

    with name_input_area:
        st.session_state.name = st.text_input(
            '이름', label_visibility='collapsed', 
            on_change=change_name_func
            )
        
    with name_regis_area:
        st.button('등록', key='name_regis_key', on_click=name_regis_func)

    if st.session_state.name_regis:
        NAME_CHECK.write(change_name_func())
st.markdown('<hr/>', unsafe_allow_html=True)

############## 사진 촬영 ##############

# photo_check_area, photo_text_area, photo_input_area, photo_regis_area = st.columns(4)

# with photo_check_area:
#     PHOTO_CHECK = st.container()

# with photo_text_area:
#     st.write('사진 촬영')

# with photo_input_area:
#     CAPTURED_PICTURE = st.container()
    
# with photo_regis_area:
#     st.button(
#         st.session_state.photo_take_btn_name,
#         key='photo_take_key' + str(st.session_state.photo_take_num), 
#         on_click=photo_take_func
#         )
    
#     PHOTO_REGIS_BTN = st.container()

photo_check_area, photo_text_area, photo_input_regis_area = st.columns([1,1,2])

with photo_check_area:
    PHOTO_CHECK = st.container()

with photo_text_area:
    st.write('사진 촬영')

with photo_input_regis_area:
    photo_input_area, photo_regis_area = st.columns(2)
    
    with photo_input_area:
        CAPTURED_PICTURE = st.container()
        
    with photo_regis_area:
        st.button(
            st.session_state.photo_take_btn_name,
            key='photo_take_key' + str(st.session_state.photo_take_num), 
            on_click=photo_take_func
            )
        
        PHOTO_REGIS_BTN = st.container()



st.markdown('<hr/>', unsafe_allow_html=True)

############## 음성 등록 ##############

# test,test2,test3 = st.columns(3)
# with test3:
#     wav_audio_data = st_audiorec()
# wav_audio_data = st_audiorec()

# if wav_audio_data is not None:
#     st.audio(wav_audio_data, format='audio/wav')
# print(wav_audio_data)
# st.audio()

audio_check_area, audio_text_area, audio_input_regis_area = st.columns([1,1,2])

with audio_check_area:
    VOICE_CHECK = st.container()

with audio_text_area:
    st.write('음성 등록')

# with audio_input_area:
#     st.session_state.audio = audio_recorder(text='',icon_name='record-vinyl', icon_size='1x')


with audio_input_regis_area:
    # st.session_state.audio_check = st.button('등록', key = 'audio_regis_key')
    st_audiorec()
    chunk = 1024  # 한 번에 읽어들일 샘플의 개수
    format = pyaudio.paInt16  # 샘플의 비트 수
    channels = 1  # 채널 개수 (모노)
    rate = 44100  # 샘플링 레이트 (Hz)

    p = pyaudio.PyAudio()  # PyAudio 객체 생성
    stream = p.open(format=format, channels=channels, rate=rate,
                    input=True, frames_per_buffer=chunk)  # 스트림 열기
    # while True:
    #     # 마이크에서 샘플 데이터 읽어오기
    #     data = stream.read(chunk)
    #     # 바이트 데이터를 numpy 배열로 변환하기
    #     samples = np.frombuffer(data, dtype=np.int16)
    #     # 파형 그리기
    #     plt.plot(samples)
    #     st.pyplot()
    #     plt.pause(0.1)
    #     plt.clf()
        
    _1, audio_regis_btn_area = st.columns(2)
    with audio_regis_btn_area:
        if st.session_state.audio:
            st.button('등록')
st.button('audio_regis_hidden', key='audio_regis_hidden')

st.markdown('<hr/>', unsafe_allow_html=True)

############## 등록 결과 ##############

result_check_area, result_text_area, result_message_area = st.columns([1,1,2])

with result_check_area:
    RESULT_CHECK = st.container()

with result_text_area:
    st.write('사용자 등록')

with result_message_area:
    st.text('등록 결과 완료')



############################# 기능 (버튼 클릭 등) #############################

# 음성 등록 버튼 클릭 시
# if st.session_state.audio_check != '':
#     if not st.session_state.audio:
#         st.session_state.audio_check = '❗음성을 등록해주세요'
#         VOICE_CHECK.write(st.session_state.audio_check)
#         st.session_state.audio_check = ''
#         # st.session_state.audio_regis = False
#     else:
#         st.session_state.audio_check = f'✅ 음성을 등록했어요'
#         VOICE_CHECK.write(st.session_state.audio_check)
#         st.session_state.audio_check = ''

@st.cache_resource
def video_capture():
    return cv2.VideoCapture(0)

def show_cam():
    video_feed = video_capture()
    while True:
        ret, frame = video_feed.read()
        if not ret:
            st.warning('No video feed')
            break
        
        frame = cv2.flip(frame, 1)

        WEB_CAM.image(frame, channels='BGR')
        st.session_state.temp_photo = frame
    video_feed.release()


# 세션 확인 용
st.container().write(st.session_state)
# show_cam() # 영상 표출 때문에 무한루프 중
st.markdown(
    """
    <button onclick="test()">
        asd
    </button>
        <script>
            const test = () => {
                const btns = document.getElementsByTagName('button')
                for (let btn of btns) {
                    if (btn.innerText === 'asd') {
                        btn.style.display = 'none'
                    }
                }
            }
        </script>
    """, unsafe_allow_html=True
)
