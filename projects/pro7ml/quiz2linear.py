# 회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량에 대한 데이터는 아래와 같다.
#  - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 운동 10시간 초과는 이상치로 한다.  
# 구분,지상파,종편,운동
# 1,0.9,0.7,4.2
# 2,1.2,1.0,3.8
# 3,1.2,1.3,3.5
# 4,1.9,2.0,4.0
# 5,3.3,3.9,2.5
# 6,4.1,3.9,2.0
# 7,5.8,4.1,1.3
# 8,2.8,2.1,2.4
# 9,3.8,3.1,1.3
# 10,4.8,3.1,35.0
# 11,NaN,3.5,4.0
# 12,0.9,0.7,4.2
# 13,3.0,2.0,1.8
# 14,2.2,1.5,3.5
# 15,2.0,2.0,3.5

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [
    [1, 0.9, 0.7, 4.2],
    [2, 1.2, 1.0, 3.8],
    [3, 1.2, 1.3, 3.5],
    [4, 1.9, 2.0, 4.0],
    [5, 3.3, 3.9, 2.5],
    [6, 4.1, 3.9, 2.0],
    [7, 5.8, 4.1, 1.3],
    [8, 2.8, 2.1, 2.4],
    [9, 3.8, 3.1, 1.3],
    [10, 4.8, 3.1, 35.0],
    [11, np.nan, 3.5, 4.0],  # NaN 처리
    [12, 0.9, 0.7, 4.2],
    [13, 3.0, 2.0, 1.8],
    [14, 2.2, 1.5, 3.5],
    [15, 2.0, 2.0, 3.5]
]

# 컬럼명 지정하여 생성
df = pd.DataFrame(data, columns=['구분', '지상파', '종편', '운동'])
df = df.set_index('구분')
# 결측값 채우기
df = df.fillna(df.mean())
print(df.head(3))

# 운동시간 이상치 제거. 
df = df[(df['운동'] <= 10)]

x = df.지상파
y = df.운동
y2 = df.종편

# 방법 (1) : stats.linregress 시용
# 운동시간 예측 모델 생성
model1 = stats.linregress(x, y)
print('기울기 :', model1.slope)     # -0.6684550167105406
print('절편 :', model1.intercept)   # 4.709676019780582
print('p값 :', model1.pvalue)       # 6.347578533142471e-05

# 시각화
plt.scatter(x, y)
plt.plot(x, model1.slope * x + model1.intercept, c='r')
# plt.show()

# 운동시간 예측 모델 생성
model2 = stats.linregress(x, y2)
print('기울기 :', model2.slope)     # 0.7726869861042756
print('절편 :', model2.intercept)   # 0.29516333605064626
print('p값 :', model2.pvalue)       # 2.2838747299772618e-05

# 시각화
plt.scatter(x, y2)
plt.plot(x, model2.slope * x + model2.intercept, c='r')
# plt.show()

# 시청 시간을 입력받아 운동, 종편 예측
# jisangpa = float(input('지상파 시청 시간 입력 : '))
jisangpa = 4.0
print('운동 예측 :', np.polyval([model1.slope, model1.intercept], [jisangpa]))  # [2.03585595]
print('종편 예측 :', np.polyval([model2.slope, model2.intercept], [jisangpa]))  # [3.38591128]

print('~~~~~~~~~~~~~~~~~~')

# 방법 (2) statsmodels ols()
import statsmodels.formula.api as smf
print(x.ndim)  # 1
# print(df[['지상파', '운동']])

# 운동시간 예측 모델
olsmodel1 = smf.ols(formula="운동 ~ 지상파", data=df[['지상파', '운동']]).fit()
print(olsmodel1.summary())

print(olsmodel1.params['지상파'])           # -0.6684550167105405
print(olsmodel1.params['Intercept'])    # 4.709676019780581

# 종편 예측 모델
olsmodel2 = smf.ols(formula="종편 ~ 지상파", data=df[['지상파', '종편']]).fit()
print(olsmodel2.summary())

print(olsmodel2.params['지상파'])           # 0.772686986104275
print(olsmodel2.params['Intercept'])    # 0.2951633360506467

# 예측값 확인
jisangpa_df = {'지상파':[jisangpa]}
print('운동 예측값 :', olsmodel1.predict(jisangpa_df))   # 2.035856
print('종편 예측값 :', olsmodel2.predict(jisangpa_df))   # 3.385911

print('~~~~~~~~~~~~~~~~~~')

# 방법 (3) LinearRegression
from sklearn.linear_model import LinearRegression
LRmodel1 = LinearRegression().fit(df[['지상파']], df[['운동']])   # 최소제곱법으로 기울기, 절편을 반환
print('기울기(slope) :', LRmodel1.coef_)   # [[-0.66845502]]
print('절편(bias) :', LRmodel1.intercept_) # [4.70967602]

LRmodel2 = LinearRegression().fit(df[['지상파']], df[['종편']])   # 최소제곱법으로 기울기, 절편을 반환
print('기울기(slope) :', LRmodel2.coef_)   # [[0.77268699]]
print('절편(bias) :', LRmodel2.intercept_) # [0.29516334]

# 예측값 확인
print('지상파 예측값 :', LRmodel1.predict([[jisangpa]]))    # [[2.03585595]]
print('종편 예측값 :', LRmodel2.predict([[jisangpa]]))      # [[3.38591128]]

