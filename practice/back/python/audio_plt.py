import pyaudio
import numpy as np
import matplotlib.pyplot as plt

chunk = 1024  # 한 번에 읽어들일 샘플의 개수
format = pyaudio.paInt16  # 샘플의 비트 수
channels = 1  # 채널 개수 (모노)
rate = 44100  # 샘플링 레이트 (Hz)

p = pyaudio.PyAudio()  # PyAudio 객체 생성
stream = p.open(format=format, channels=channels, rate=rate,
                input=True, frames_per_buffer=chunk)  # 스트림 열기

while True:
    # 마이크에서 샘플 데이터 읽어오기
    data = stream.read(chunk)
    # 바이트 데이터를 numpy 배열로 변환하기
    samples = np.frombuffer(data, dtype=np.int16)
    # 파형 그리기
    plt.plot(samples)
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()