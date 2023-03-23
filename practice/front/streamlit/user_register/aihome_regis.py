import streamlit as st
import streamlit.components.v1 as components
import cv2
from PIL import Image
from streamlit_webrtc import webrtc_streamer
import av


# 세션 등록
if 'name' not in st.session_state:
    st.session_state.name = ''

# if 'name_regis' not in st.session_state:
#     st.session_state.name_regis = False

if 'picture_regis' not in st.session_state:
    st.session_state.picture_regis = False

if 'cam' not in st.session_state:
    st.session_state.cam = []

if 'picture' not in st.session_state:
    st.session_state.picture = []

# if 'video_flag' not in st.session_state:
#     st.session_state.video_flag = False

if 'take_pic_btn' not in st.session_state:
    st.session_state.take_pic_btn = False

if 'name_regis_check' not in st.session_state:
    st.session_state.name_regis_check = False

if 'cam_test' not in st.session_state:
    st.session_state.cam_test = 0


# @st.cache
# def video_frame_callback(frame):
#     img = frame.to_ndarray(format="yuv420p")

#     flipped = img[:,::-1]

#     return av.VideoFrame.from_ndarray(flipped, format="yuv420p")


# def take_pic_btn_txt():
#     HTML = f'''
#         <script>
#         const btns = window.parent.document.querySelectorAll('button')
#         for (let i = 0; i < btns.length; i++) {{
#             if (btns[i].innerText == 'Take Photo') {{
#                 btns[i].innerText = '사진 촬영'
#             }}
#         }}
#     </script>
#     '''
#     components.html(f'{HTML}')
def take_picture():
    st.session_state.picture_regis = True

st.markdown('<h1 style="text-align: center">사용자 등록</h1>', unsafe_allow_html=True)

blank1, cam_area, blank2 = st.columns(3)

with blank1:
    pass

with cam_area:
    WEB_CAM = st.image([])

    # st.session_state.picture = webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

    # st.camera_input('사진', label_visibility='hidden')

with blank2:
    pass

st.markdown('<br/>', unsafe_allow_html=True)

name_check_area, name_text_area, name_input_area, name_regis_area = st.columns(4)

with name_check_area:
    NAME_CHECK = st.container()
    FACE_CHECK = st.container()

with name_text_area:
    st.write('사용자명')
    st.write('사진 캡쳐')

with name_input_area:
    st.session_state.name = st.text_input('이름', label_visibility='collapsed')
    CAPTURED_PICTURE = st.image([])

with name_regis_area:
    st.button('등록', key='name_regis')
    st.button('촬영', key='take_picture', on_click=take_picture)
    CAPTURED_PIC_SAVE = st.container()

if st.session_state.name_regis:
    if not st.session_state.name:
        NAME_CHECK.write('❗이름을 확인하세요')
    else:
        NAME_CHECK.write('✅')


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
        
        if st.session_state.picture_regis:
            st.session_state.cam = frame
            CAPTURED_PICTURE.image(st.session_state.cam, channels='BGR')
            CAPTURED_PIC_SAVE.button('저장', key='picture_save')
            st.session_state.picture_regis = False
        
        WEB_CAM.image(frame, channels='BGR')

    video_feed.release()

# if st.session_state.picture_regis:
#     # st.text(test)
#     CAPTURED_PICTURE.image(st.session_state.cam, channels='BGR')
#     CAPTURED_PIC_SAVE.button('저장', key='picture_save')

st.write(st.session_state)
show_cam() # 영상 표출 때문에 무한루프 중
