import streamlit as st
import cv2
import streamlit_webrtc as webrtc
from audio_recorder_streamlit import audio_recorder

########################## 세션, 함수 생성 ##########################

# 사용자 이름
if 'name' not in st.session_state:
    st.session_state.name = ''

if 'name_regis' not in st.session_state:
    st.session_state.name_regis = False

# 사진 촬영
if 'photo_take' not in st.session_state:
    st.session_state.photo_take = False

# 촬영한 사진(캠 화면 프레임)
if 'photo' not in st.session_state:
    st.session_state.photo = []

# 사진 등록
if 'photo_regis' not in st.session_state:
    st.session_state.photo_regis = False

if 'photo_regis_check' not in st.session_state:
    st.session_state.photo_regis_check = False

if 'audio' not in st.session_state:
    st.session_state.audio = ''

if 'take_pic_btn' not in st.session_state:
    st.session_state.take_pic_btn = False


if 'cam_test' not in st.session_state:
    st.session_state.cam_test = 0


def take_picture():
    if st.session_state.photo_regis_check:
        return
    else:
        st.session_state.photo_take = True



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

name_check_area, name_text_area, name_input_area, name_regis_area = st.columns(4)

with name_check_area:
    NAME_CHECK = st.container()

with name_text_area:
    st.write('사용자 명')

with name_input_area:
    st.session_state.name = st.text_input('이름', label_visibility='collapsed')
    
with name_regis_area:
    st.session_state.name_regis = st.button('등록', key='name_regis_key')


############## 사진 캡쳐 ##############

photo_check_area, photo_text_area, photo_input_area, photo_regis_area = st.columns(4)

with photo_check_area:
    PHOTO_CHECK = st.container()

with photo_text_area:
    st.write('사진 캡쳐')

with photo_input_area:
    CAPTURED_PICTURE = st.container()
    
with photo_regis_area:
    PHOTO_TAKE_BTN = st.container()

    st.session_state.take_pic_btn = PHOTO_TAKE_BTN.button('촬영', key='take_pic_btn_key')
    
    PHOTO_SAVE_BTN = st.container()


############## 음성 등록 ##############

audio_check_area, audio_text_area, audio_input_area, audio_regis_area = st.columns(4)

with audio_check_area:
    VOICE_CHECK = st.container()

with audio_text_area:
    st.write('음성 등록')

with audio_input_area:
    st.text_input('audio', label_visibility='collapsed')

with audio_regis_area:
    st.session_state.audio = audio_recorder(text='',icon_name='record-vinyl', icon_size='1x')


############## 등록 결과 ##############

result_check_area, result_text_area, result_message_area = st.columns([1,1,2])

with result_check_area:
    RESULT_CHECK = st.container()

with result_text_area:
    st.write('사용자 등록')

with result_message_area:
    st.text('등록 결과 완료')



############################# 기능 (버튼 클릭 등) #############################

# 이름 등록 버튼 클릭 시
if st.session_state.name_regis:
    if not st.session_state.name:
        NAME_CHECK.write('❗이름을 확인하세요')
    else:
        NAME_CHECK.write(f'✅ {st.session_state.name}님, 반가워요')

# 촬영 버튼 클릭 시
if st.session_state.take_pic_btn:
    # if st.session_state.photo_regis:
    #     st.session_state.photo_regis = False
    take_picture()
    PHOTO_TAKE_BTN.button('재촬영', key='take_agian')
    st.session_state.take_pic_btn = False




# @st.cache_resource
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

         # 촬영 후 사진 등록 버튼 클릭 시 (기능 구현 필요)
        if st.session_state.photo_regis:
            cv2.imwrite('taked_photo.png', st.session_state.photo) # 우선 사진 저장으로 
            st.session_state.photo_take = False
            st.session_state.photo_regis = False
            st.session_state.photo_regis_check = True
            # st.session_state.take_pic_btn = False
            PHOTO_CHECK.write(f'✅ 사진 등록 완료!')
            # CAPTURED_PICTURE.write('사진등록완료')
    
        
        if 'photo_take' in st.session_state and st.session_state.photo_take:
            st.session_state.photo_take = False 
            st.session_state.photo = frame
            CAPTURED_PICTURE.image(st.session_state.photo, channels='BGR')
            st.session_state.photo_regis = PHOTO_SAVE_BTN.button('등록', key='photo_regis_key')
            
            # False로 안 바뀌는 이유 알아낼 필요. 계속 True로 인식되어 등록을 눌러도 사진이 변경된다.
            # 등록을 눌렀을 때 photo_take를 False로 바꾸면??

       
        
        WEB_CAM.image(frame, channels='BGR')




    video_feed.release()


# 세션 확인 용
st.container().write(st.session_state)
show_cam() # 영상 표출 때문에 무한루프 중
