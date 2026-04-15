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
x = iris.data[:n, :2]       # sepal length, width 열만 선택
print('차원 축소 전 x :', x, x.shape, type(x))
print(x.T)

# 시각화
# plt.plot(x.T, 'o:')
# plt.xticks(range(2), ['꽃받침길이', '꽃받침너비'])
# plt.grid(True)
# plt.legend(['표본 {}'.format((i + 1) for i in range(n))])
# plt.title('아이리스 크기 특성')
# plt.xlabel('특성의 종류')
# plt.ylabel('특성값')
# plt.xlim(-0.5, 2)
# plt.ylim(2.5, 6)
# plt.show()

# 시각화2 : 산점도
df = pd.DataFrame(x)
print(df)
# ax = sns.scatterplot(x=df[0], y=df[1], marker='s', s=100, color='b')
ax = sns.scatterplot(x=0, y=1, data=df, marker='s', s=100, color='b')
# 각 점에 대해 text 표시
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.03, '표본{}'.format(i + 1))
plt.xlabel('꽃받침길이')
plt.ylabel('꽃받침폭')
plt.title('Iris 특성')
plt.axis('equal')
plt.show()

# 위 두개의 그래프 결과 두 변수는 공통적인 특징이 있으므로 차원축소의 근거가 있다고 판단
# PCA를 진행
# 순서1: 입력 데이터의 공분산 행렬을 생성한다.
# 순서2: 공분산 행렬의 고유벡터, 고유값(고유벡터의 크기)을 계산한다.
# 순서3: 고윳값이 큰 순서대로 k개(PCA 변환 차수)만큼 고유벡터를 추출한다.
# 순서4: 고윳값이 가장 큰 순으로 추출된 고유벡터를 이용해 새롭게 입력 데이터를 변환한다.
# sklearn의 PCA를 이용하면 순서대로 진행을 함

pca1 = PCA(n_components=1)  # 변환할 차원수
x_low = pca1.fit_transform(x)   # 특징 행렬을 낮은 차원의 근사행렬로 변환
print('x_low :', x_low, ' ', x_low.shape)
# 주성분 값 원복하기
x2 = pca1.inverse_transform(x_low)
print('원복 후 x2 :', x2, ' ', x2.shape)
print('원본 :', x[0, :])    # [5.1 3.5]
print('주성분 :', x_low[0]) # [0.30270263]
print('원복 :', x2[0, :])   # [5.06676112 3.53108532]

# 주성분 분석값을 기반으로 시각화
# pca 방향벡터
pc1 = pca1.components_[0]   # components_ : 주성분 벡터
mean = x.mean(axis=0)   # 데이터 평균(중심점)

df = pd.DataFrame(x)
# 시각화
ax = sns.scatterplot(x=0, y=1, data=df, marker='s', s=100, color='b')
# 각 점에 대해 text 표시
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.03, '표본{}'.format(i + 1))

# PCA 축 (화살표)
plt.quiver(
    mean[0], mean[1],   # 시작점
    pc1[0], pc1[1],     # 방향
    scale=3, color='r', width=0.01
)
plt.xlabel('꽃받침길이')
plt.ylabel('꽃받침폭')
plt.title('Iris 특성 + 제1주성분')
plt.axis('equal')
plt.grid(True)
plt.show()

print('***' * 10)
# 원본 열 4개를 차원축소해 2개의 열로 변환 후 SVM 분류 모델을 작성
x = iris.data
print(x[0, :])  # [5.1 3.5 1.4 0.2]
pca2 = PCA(n_components=2)
x_low2 = pca2.fit_transform(x)
print('x_low2 :', x_low2[0, :], ' ', x_low2.shape)  # [-2.68412563  0.31939725]
# 변동성 비율 확인
print(pca2.explained_variance_ratio_)   # [0.92461872 0.05306648]
x4 = pca2.inverse_transform(x_low2)
print('최초 자료 :', x[0, :])   # [5.1 3.5 1.4 0.2]
print('차원축소 :', x_low2[0])  # [-2.68412563  0.31939725]
print('차원복귀 :', x4[0, :])   # [5.08303897 3.51741393 1.40321372 0.21353169]
print()
iris1 = pd.DataFrame(x, columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
print(iris1.head(3))
iris2 = pd.DataFrame(x_low2, columns=['var1', 'var2'])
print(iris2.head(3))

from sklearn import svm, metrics
feature1 = iris1.values
print(feature1[:3])
label = iris.target
print(label[:3])

print('원본 데이터로 SVM 분류 모델 작성')
model1 = svm.SVC(C=0.1, random_state=0).fit(feature1, label)
pred1 = model1.predict(feature1)
print('model1 정확도 :', metrics.accuracy_score(label, pred1))

feature2 = iris2.values
print(feature2[:3])
print(label[:3])


print('PCA 데이터로 SVM 분류 모델 작성')
model2 = svm.SVC(C=0.1, random_state=0).fit(feature2, label)
pred2 = model2.predict(feature2)
print('model2 정확도 :', metrics.accuracy_score(label, pred2))
