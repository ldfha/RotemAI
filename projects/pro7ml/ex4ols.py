# 최소제곱해를 선형 행렬 방정식으로 얻기
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.5, 2.1])
# plt.scatter(x, y)
# plt.grid(True)
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A)

# 본래 데이터를 직선으로 표현하기 위해 선형대수학 이용
import numpy.linalg as lin
# y = wx + b의 w, b 구하기
weight, bias = lin.lstsq(A, y)[0]   # 최소제곱법 연산(내부적으로 편미분 사용)
print(bias)    # 0.96(기울기)  -0.9899999999999993(절편)
print()
# 회귀식 y^ = 0.96 * x + -0.9899999999999993
print(0.96 * 0 + -0.9899999999999993)   # 실제값 -1, 예측값 -0.98999
print(0.96 * 1 + -0.9899999999999993)   # 실제값 0.2, 예측값 -0.02999
print(0.96 * 2 + -0.9899999999999993)   # 실제값 0.5, 예측값 0.93000
print(0.96 * 3 + -0.9899999999999993)   # 실제값 2.1, 예측값 1.89000

plt.scatter(x, y, marker='o', label='실제값')
plt.plot(x, weight * x + bias, c='r', label='최적화된 선형직선')
plt.grid(True)
plt.show()

# 경험하지 않은 x값에 대한 y값은?
x = 1.23456
yhat = weight * x + bias
print('예측결과 : ', yhat)  # 0.1951776000000005

x = 7.654321
yhat = weight * x + bias
print('예측결과 : ', yhat)  # 6.358148159999999