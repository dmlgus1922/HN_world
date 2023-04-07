import base64
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
cam = cv2.VideoCapture(0)

ret, frame = cam.read()

# print(frame)
cv2.imshow('test', frame)
frame = cv2.flip(frame, 1)

print(np.shape(frame))
print(np.shape([[[0 for _ in range(3)] for _ in range(640)] for _ in range(480)]))
# 키보드 입력 대기
cv2.waitKey(0)

cv2.imwrite('test.png', frame)

# 윈도우 창 닫기
cv2.destroyAllWindows()

# img = Image.fromarray(cv2.bitwise_not(frame))

# img.show()

# print('array를 인코딩: \n', base64.b64encode(frame))
# print('이미지를 인코딩: \n', base64.b64encode(img))

# resized_img = img.resize((600, 800))

# resized_img.show()