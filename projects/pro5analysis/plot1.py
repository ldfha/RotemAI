# matploplib : 플로팅 라이브러리. 그래프 생성을 위한 다양한 함수를 제공
# 시각화의 중요성

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')  # 한글  
plt.rcParams['axes.unicode_minus'] = False  # -마이너스 안깨지게

# x = ["서울", "인천", "수원"]
x = ("서울", "인천", "수원")
# x = {"서울", "인천", "수원"}    # TypeError: unhashable type: 'set'
y = [5, 3, 7]
plt.xlim([-1, 3])
plt.ylim([0, 10])
# tick 설정 : y축의 라벨을 인위적으로 표시
plt.yticks(list(range(0, 11, 3)))
plt.plot(x, y)
plt.show()

data = np.arange(1, 11, 2)
plt.plot(data)  # x축의 구간은 자동 설명
x = [0,1,2,3,4]
for a, b in zip(x, data):
    plt.text(a, b, str(b))
plt.show()

x = np.arange(10)
y = np.sin(x)
print(x, y)
plt.plot(x, y)
# plt.plot(x, y, 'bo')
plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.show()

# hold : 복수의 plot으로 여러개의 차트를 겹쳐 그림
x = np.arange(0, np.pi * 3, 0.1)
print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(figsize=(10,5))  # 그래프 전체 크기(w, h)
plt.plot(x, y_sin, 'r') # 선
plt.scatter(x, y_cos)   # 선점도
plt.xlabel('x축')
plt.ylabel('y 축')
plt.title('sine & cosine')
plt.legend(['sine', 'cosine'])
plt.show()

print()
# subplot : 하나의 Figure를 여러개의 Axes(plot)으로 나누기
plt.subplot(2, 1, 1)    # 2행 1열의 1행
plt.plot(x, y_sin)
plt.title('sine')
plt.subplot(2, 1, 2)    # 2행 1열의 2행
plt.plot(x, y_cos)
plt.title('cosine')
plt.show()

irum = [ 'a', 'b', 'c', 'd', 'e']
kor = [80,50,70,70,90]
eng = [60,70,80,90,100]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bo--')
plt.ylim([50,100])
plt.title('시험 점수')
plt.legend(['국어','영어'], loc = 4)
plt.grid(True)

fig = plt.gcf()
plt.show()
fig.savefig('plot1.png')