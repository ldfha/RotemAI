# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# dataset은 winequality-red.csv 
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv
# Input variables (based on physicochemical tests):
#  1 - fixed acidity
#  2 - volatile acidity
#  3 - citric acid
#  4 - residual sugar
#  5 - chlorides
#  6 - free sulfur dioxide
#  7 - total sulfur dioxide
#  8 - density
#  9 - pH
#  10 - sulphates
#  11 - alcohol
#  Output variable (based on sensory data):
#  12 - quality (score between 0 and 10)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt


data = pd.read_csv("winequality-red.csv")
pd.set_option('display.max_columns', None)
print(data.head(3))
print(data.info())

df_x = data.iloc[:, 0:11]
print(df_x.columns)

df_y = data['quality']

train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.3, random_state=12, stratify=df_y)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

model = RandomForestClassifier(criterion='gini', n_estimators=120)
# n_estimators : 결정트리수
model.fit(train_x, train_y)

pred = model.predict(test_x)
print('예측값 :', pred[:5])
print('실제값 :', np.array(test_y[:5]))
print('맞춘 갯수 :', sum(test_y == pred))
print('전체 대비 맞춘 비율 :', sum(test_y == pred) / len(test_y))
print('분류 정확도 :', accuracy_score(test_y, pred))

# 교차 검증 (KFold)
cross_vali = cross_val_score(model, df_x, df_y, cv=5)
print(cross_vali)
print('교차 검증 평균 정확도 :', np.round(np.mean(cross_vali), 5))

print('중요 변수 확인하기 --------')
print('특성(변수) 중요도 :', model.feature_importances_)

importances = model.feature_importances_
# 컬럼명 + 중요도
feature_df = pd.DataFrame({
    'feature':df_x.columns,
    'importance':importances
}).sort_values(by='importance', ascending=False)
print(feature_df)

import seaborn as sns
plt.figure(figsize=(8, 5))
sns.barplot(x='importance', y='feature', data=feature_df, orient='horizon')
plt.xlabel('Feature importance Score')
plt.ylabel('Features')
plt.tight_layout()
plt.show()

# 새로운 와인 데이터가 들어왔을 때 품질 예측
new_wine = [[7.5, 0.5, 0.3, 2.0, 0.08, 15.0, 50.0, 0.997, 3.3, 0.6, 10.5]]
new_pred = model.predict(new_wine)
print(f"새로운 와인 샘플의 예측 품질 등급: {new_pred[0]}")