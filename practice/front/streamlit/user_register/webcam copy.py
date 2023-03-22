import streamlit as st
import cv2
from PIL import Image

# 세션 등록
if 'name' not in st.session_state:
    st.session_state.name = ''

if 'picture' not in st.session_state:
    st.session_state.picture = []

if 'video_flag' not in st.session_state:
    st.session_state.video_flag = False

# 캠 화면 띄우기
@st.cache
def show_cam():
    FRAME_WINDOW = st.image([])
    
    take_pic = st.button('사진촬영')
        
    video_feed = cv2.VideoCapture(0)

    while True:
        ret, frame = video_feed.read()
        if not ret:
            st.warning('No video feed')
            break
        
        frame = cv2.flip(frame, 1)
        FRAME_WINDOW.image(frame, channels='BGR')
    
        if take_pic:
            # captured_frame = capture_frame(video_feed)
            frame = cv2.resize(frame, picture_size)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            captured_picture = Image.fromarray(frame)
            pic_con.caption('촬영 사진')

            pic_con.image(captured_picture, channels='BGR')
            take_pic = False
            # video_feed.release()
            # break

st.title("사용자 등록 화면")
col1, col2 = st.columns(2)

# 크게 좌우 2분할
with col1:
    # 이름 입력 란
    name_input_col, name_check_col = st.columns([2,1])
    with name_input_col:
        name = st.text_input('이름', placeholder='이름을 입력해주세요.')
        st.session_state.name = name + '님, 반가워요' if name != '' else '이름을 입력해주세요!'

    with name_check_col:
        # 등록 버튼 아래로 내리기 용 빈 div
        st.markdown('<div style="margin-top:35px"></div>', unsafe_allow_html=True)
        name_regis_check = st.button('등록')

    if name_regis_check:
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
        st.session_state.video_flag = st.button('사진등록', key=1)


if st.session_state.video_flag:
    picture_size = (640,480)

    with col2:
        show_cam()
