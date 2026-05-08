# 손글씨 이미지 읽기
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('num.png')
img = np.array(im.resize((28, 28), Image.Resampling.LANCZOS).convert('L'))
# L 모드 : 흑백 이미지 픽셀값이 0~255범위 (0:검정, 255:흰색)
print(img.shape)

plt.imshow(img, cmap='Greys')
plt.show()

data = img.reshape([1, 784]).astype('float32')
print(data, data.shape)

# 정규화
data = data / 255
print(data)

# 이 밑에 뭐지