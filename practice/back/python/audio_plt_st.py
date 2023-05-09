import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pyaudio
from PIL import Image
import io
import base64
import matplotlib.image as mpimg
import seaborn as sns

# 파형을 그리는 함수
def plot_waveform(waveform):
    # 그래프 초기화
    plt.clf()
    # 그래프 그리기
    plt.plot(waveform)
    plt.ylim([-1, 1])
    # 그래프 이미지 반환
    return plt.gcf()

# streamlit 웹 애플리케이션 코드
def main():
    # 마이크로부터 샘플을 읽어들이는 코드와 파형을 계산하는 코드 생략
    
    # streamlit 웹 애플리케이션 구성
    st.title("Real-time Waveform Visualization")
    st.text("Press 'Start' to begin streaming from microphone")
    
    # 그래프 초기화
    fig = plt.figure(figsize=(5,1.5))

    plt.ion()

    # ax = fig.add_subplot(111)
    # line, = ax.plot([])

    chunk = 1024  # 한 번에 읽어들일 샘플의 개수
    format = pyaudio.paInt16  # 샘플의 비트 수
    channels = 1  # 채널 개수 (모노)
    rate = 44100  # 샘플링 레이트 (Hz)

    p = pyaudio.PyAudio()  # PyAudio 객체 생성
    stream = p.open(format=format, channels=channels, rate=rate,
                    input=True, frames_per_buffer=chunk)  # 스트림 열기

    # 'Start' 버튼을 누르면 데이터 스트리밍을 시작함
    if st.button('Start'):
        # con = st.pyplot(fig)
        con = st.empty()
        while True:
            # plt.clf()
            # 마이크로부터 샘플을 읽어들임
            data = stream.read(chunk)
            # 파형을 계산함
            waveform = np.frombuffer(data, dtype=np.int16)
            # plt.plot(waveform, color='red')
            # plt.ylim([-1200, 1200])
            # plt.xlim([-100, 1100])
            # plt.xticks([])
            # plt.yticks([])

            # plt.show(block=False)
            # plt.savefig('temp.png')
            # audio_img = Image.open('temp.png')
            # st.pyplot(fig)
            # con.pyplot(fig)
            # con.image(audio_img)
            # plt.pause(0.03)
            sns.lineplot(data=waveform)

if __name__ == '__main__':
    main()