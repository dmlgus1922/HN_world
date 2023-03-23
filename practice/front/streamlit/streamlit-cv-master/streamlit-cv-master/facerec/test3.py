from streamlit_webrtc import webrtc_streamer
import av
import streamlit as st


@st.cache
def video_frame_callback(frame):
    img = frame.to_ndarray(format="yuv420p")

    flipped = img[:,::-1]

    return av.VideoFrame.from_ndarray(flipped, format="yuv420p")




webrtc_streamer(key="example", video_frame_callback=video_frame_callback)


st.button('test')