import streamlit as st
import cv2
from PIL import Image

# 세션 등록
if 'name' not in st.session_state:
    st.session_state.name = ''

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

st.title("사용자 등록")
col1, col2 = st.columns(2)

# 크게 좌우 2분할
with col1:

    # 이름 입력 란
    name_input_col, name_check_col = st.columns([2,1])
    with name_input_col:
        st.text_input('이름', placeholder='이름을 입력해주세요.', key='name')
        # st.session_state.name = name + '님, 반가워요' if name != '' else '이름을 입력해주세요!'

    with name_check_col:
        # 등록 버튼 아래로 내리기 용 빈 div
        st.markdown('<div style="margin-top:35px"></div>', unsafe_allow_html=True)
        st.session_state.name_regis_check = st.button('등록')

    if st.session_state.name_regis_check:
        st.write(st.session_state.name)

    # 큰 분할 왼쪽 다시 3분할
    pic_text, taked_picture, pic_regis_btn = st.columns(3)

    # 사진촬영 텍스트
    with pic_text:
        st.text('사진촬영')
    
    # 촬영한 사진
    with taked_picture:
        pic_con = st.container()
        pic_con.image([])
        
    
    with pic_regis_btn:
        st.button('사진등록', key='video_flag')

    st.write(st.session_state)

with col2:
    FRAME_WINDOW = st.image([])
    # con_test = st.container()
    st.session_state.take_pic_btn = st.button('사진촬영')
        
    video_feed = cv2.VideoCapture(0)

    while True:
        ret, frame = video_feed.read()
        if not ret:
            st.warning('No video feed')
            break
        
        st.session_state.cam = cv2.flip(frame, 1)
        FRAME_WINDOW.image(st.session_state.cam, channels='BGR')

        if st.session_state.take_pic_btn:
            # captured_frame = capture_frame(video_feed)
            frame = cv2.cvtColor(st.session_state.cam, cv2.COLOR_BGR2RGB)
            st.session_state.picture = Image.fromarray(frame)
            pic_con.caption('촬영 사진')

            pic_con.image(st.session_state.picture, channels='BGR')
            st.session_state.take_pic_btn = False
            # video_feed.release()
            # break
        

