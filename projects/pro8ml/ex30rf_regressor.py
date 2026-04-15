# RandomForest는 분류, 회귀 모두 가능. sklearn 모듈은 대개 그러하다.
# 캘리포니아 주택 가격 데이터로 회귀분석

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Classifier가 아닌 Regressor
from sklearn.metrics import r2_score, mean_squared_error

# fetch_california_housing : 캘리포니아 주택 가격 데이터
# as_frame=True : pandas DataFrame 형태로 반환
housing = fetch_california_housing(as_frame=True)

print(housing.DESCR)            # 데이터 설명문
print(housing.data[:2])         # feature 값 (상위 2행)
print(housing.target[:2])       # label 값 (주택 가격, 상위 2행)
print(housing.feature_names[:2])# feature 컬럼명

df = housing.frame  # data + target 합친 전체 DataFrame
print(df.head(3))
print(df.info())

x = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)
# 20640개 → train 14448개 (70%) / test 6192개 (30%)
# 회귀 문제라 stratify 불필요 (연속값은 비율 유지 개념 없음)

# RandomForestRegressor : 회귀용 랜덤포레스트
# n_estimators=200 : 결정트리 200개 생성
rfmodel = RandomForestRegressor(n_estimators=200, random_state=42)
rfmodel.fit(x_train, y_train)

# 예측 및 평가
y_pred = rfmodel.predict(x_test)
# MSE (Mean Squared Error) : 오차 제곱의 평균 → 낮을수록 좋음
print(f'MSE : {mean_squared_error(y_test, y_pred):.3f}')    # 0.254
# R2 (결정계수) : 0~1, 높을수록 좋음 (1이면 완벽)
print(f'R2(결정계수) : {r2_score(y_test, y_pred):.3f}')      # 0.807

# 변수 중요도 시각화
importances = rfmodel.feature_importances_
# np.argsort : 오름차순 정렬했을 때의 인덱스 반환
# [::-1]     : 뒤집기 → 내림차순 (중요도 높은 순)
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(8, 5))
plt.bar(range(x.shape[1]), importances[indices], align='center')
plt.xticks(range(x.shape[1]), x.columns[indices], rotation=45)
plt.xlabel('feature name')
plt.ylabel('feature importances')
plt.tight_layout()
plt.show()

# np.argsort 동작 원리
# importances = [0.05, 0.53, 0.14, 0.09, 0.08, 0.04, 0.09, 0.08]
# #               0     1     2     3     4     5     6     7    ← 인덱스

# np.argsort(importances)      # [5, 0, 7, 4, 6, 3, 2, 1]  ← 작은 것부터 인덱스
# np.argsort(importances)[::-1]# [1, 2, 3, 6, 4, 7, 0, 5]  ← 큰 것부터 인덱스
#                              #  ↑ MedInc(1)이 가장 중요

# 값을 직접 정렬하는 게 아니라 "정렬했을 때의 인덱스" 를 반환
# 이 인덱스로 다른 배열도 같은 순서로 정렬 가능

# importances = [0.05, 0.53, 0.14]
# idx = np.argsort(importances)[::-1]  # [1, 2, 0]

# importances[idx]          # [0.53, 0.14, 0.05]  ← 중요도 정렬
# x.columns[idx]            # ['MedInc', 'AveOccup', 'HouseAge']  ← 컬럼명도 같이 정렬
# print('중요 변수 순위정보 저장')


# indices로 컬럼명과 중요도를 같은 순서(내림차순)로 정렬해서 저장
ranking = pd.DataFrame({
    'feature': x.columns[indices],
    'importance': importances[indices]
})
print(ranking)
#       feature  importance
# 0      MedInc    0.525400  ← 중위소득이 집값에 가장 큰 영향
# 1    AveOccup    0.138819
# 2   Longitude    0.086695
# 3    Latitude    0.086512
# 4    HouseAge    0.054694
# 5    AveRooms    0.045933
# 6  Population    0.032089
# 7   AveBedrms    0.029859

# 파라미터 튜닝
from sklearn.model_selection import RandomizedSearchCV
# GridSearchCV와 달리 사용자가 지정한 범위, 분포에서 임의로 일부 혼합만 샘플링해 탐색
# 연속적 값 범위도 가능. 무작위이기 때문에 최적 조합을 못 찾을 수도 있다.

# 탐색할 파라미터 범위 정의
param_dist = {
    'n_estimators': [200, 400, 800],            # 트리 개수
    'max_depth': [None, 10, 20, 30],            # 트리 최대 깊이
    'min_samples_leaf': [1, 2, 4],              # 리프노드 최소 샘플 수
    'min_samples_split': [2, 4, 8],             # 노드 분할 최소 샘플 수
    'max_features': [None, 'sqrt', 'log2', 1.0, 0.8, 0.6]  # 분할 시 고려할 최대 특성 수
}
# 전체 조합 수 : 3 × 4 × 3 × 3 × 6 = 648가지

search = RandomizedSearchCV(
    RandomForestRegressor(random_state=42),  # 모델
    param_distributions=param_dist,          # 탐색 범위
    n_iter=20,       # 648가지 중 20개만 랜덤 샘플링
    scoring='r2',    # 회귀 → r2 기준으로 평가
    cv=3,            # 3겹 교차검증
    random_state=42,
    verbose=1        # 진행 상황 출력
)

search.fit(x_train, y_train)  # 탐색 + 학습 수행

print('best_params : ', search.best_params_)
best = search.best_estimator_   # 최적 파라미터로 재학습된 모델
print('best_score : ', search.best_score_)
print('final R2 : ', r2_score(y_test, best.predict(x_test)))
# GridSearchCV    : 648가지 전부 탐색 × cv=3 → 1944번 학습 (느림)
# RandomizedSearchCV : 20가지만 랜덤 탐색 × cv=3 →   60번 학습 (빠름)