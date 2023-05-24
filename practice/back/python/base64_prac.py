import base64
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 파일 불러오기
data = cv2.imread('./recognize.png')
shape = data.shape

# base64 인코딩
b64_encoded_data = base64.urlsafe_b64encode(data)

# 문자열 변환
str_decoded_data = b64_encoded_data.decode('utf-8')

# base64 디코딩
b64_decoded_data = base64.urlsafe_b64decode(str_decoded_data)

# numpy array
arr_data = np.frombuffer(b64_decoded_data, np.uint8)

# reshape
reshape_data = arr_data.reshape(shape)

print(type(reshape_data), reshape_data)

print(data == reshape_data)