# 특성공학기법 - 좋은 성능을 내기 위해 입력 자료를 변형하거나 가공하는 방법
# - 차원 축소
#   1) feature selection : 변수 선택
#   2) feature extraction : 차원 축소(방법 : 주성분분석(PCA))
# - Scaling (정규화 표준화)
# - Transform
#   1) Binning(비닝) : 연속적 자료를 구간으로 분류(연속형 -> 범주형)
#   2) Dummy : 범주형을 연속형으로 변환
# - feature creation : 특성 생성 - 기존 자료로 의미있는 새로운 변수 생성
# (예: 날짜로 년,월,일, 요일, 분기 등의 변수 생성, 연봉으로 보너스 변수 생성 ...)

# 고유 벡터 : 어떤 선형 변환을 취했을 때 방향은 변화없고 크기만 변하는 벡터를 말함.
# 벡터가 얼마나 같은 방향을 향하고 있는가?
# 고유값 : 고유벡터의 크기가 변한 만큼의 값

# PCA(주성분분석) : 선형대수 관점에서 입력데이터의 공분산행렬을 고유값 분해하고
# 이렇게 구한 고유벡터에 입력 데이터를 선형변환하는 것이다.
# 이 고유벡터가 PCA의 주성분 벡터로서 입력 데이터의 분산이 큰 방향을 나타낸다.
# 입력 데이터의 성질을 최대한 유지한 상태로 고차원을 저차원 데이터로 변환하는 기법.

# iris data로 차원 축소
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn import svm, metrics
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
n = 10
x = iris.data[:n, :2]
print('차원 축소 전 x :', x, x.shape, type(x))
print(x.T)

# 시각화
plt.plot(x.T, 'o:')
plt.xticks(range(2), ['꽃받침길이', '꽃받침너비'])
plt.grid(True)
plt.legend(['표본 {}'.format((i + 1) for i in range(n))])
plt.title('아이리스 크기 특성')
plt.xlabel('특성의 종류')
plt.ylabel('특성값')
plt.xlim(-0.5, 2)
plt.ylim(2.5, 6)
plt.show()