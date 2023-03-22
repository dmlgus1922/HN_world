import cv2
import streamlit as st

# CONSTANTS
WEBCAMNUM = 0 # from videocapture_index_check.py

st.title("Webcam Face Recognition")
FRAME_WINDOW = st.image([])

@st.cache_data

def capture_face(video_capture):
    for i in range(3):
        video_capture.read()

    video_capture.set(3,320)
    video_capture.set(4,240)

    while True:
        ret, frame = video_capture.read()

        if ret:
            cv2.imshow('video', frame)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        else:
            break

    video_capture.release()
    
    FRAME_WINDOW.image(frame[:, :, ::-1])
    return


if __name__ == "__main__":
    video_capture = cv2.VideoCapture(WEBCAMNUM)    
    capture_face(video_capture)
    # press to restart the scripts
    st.button('contunue......')