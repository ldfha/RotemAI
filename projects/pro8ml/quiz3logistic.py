# [로지스틱 분류분석 문제3]
# Kaggle.com의 https://www.kaggle.com/truesight/advertisingcsv  file을 사용
# 얘를 사용해도 됨   'testdata/advertisement.csv' 
# 참여 칼럼 : 
#    - Daily Time Spent on Site : 사이트 이용 시간 (분)
#    - Age : 나이,
#    - Area Income : 지역 소득,
#    - Daily Internet Usage :일별 인터넷 사용량(분),
#    - Clicked Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )
# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# 데이터 간 단위가 큰 경우 표준화 작업을 시도한다.
# 모델 성능 출력 : 정확도, 정밀도, 재현율, ROC 커브와 AUC 출력
# 새로운 데이터로 분류 작업을 진행해 본다.

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler    # 표준화
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/advertisement.csv")
print(data.head(2), data.shape)     # (20, 6)

x = data[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage']]
y = data['Clicked on Ad']

print(x.head(2), x.shape)
print(y.head(2), y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# (105, 2) (45, 2) (105,) (45,)
print(x_train[:3], ' ', x_test[:3], ' ', y_train[:3], ' ', y_test[:3])

# 데이터 표준화
sc = StandardScaler()
sc.fit(x_train)     # 독립변수(feature) 표준화
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])
print(x_test[:3])

model = LogisticRegression(C=1.0, solver='lbfgs', random_state=0)
model.fit(x_train, y_train)

# 분류 예측
y_pred = model.predict(x_test)
print('예측값 :', y_pred[:5])
print('실제값 :', y_test[:5])

# 모델 성능 출력
acc_score = accuracy_score(y_test, y_pred)
prec_score = precision_score(y_test, y_pred)
rec_score = recall_score(y_test, y_pred)
print('모델 정확도 :', acc_score)
print('모델 정밀도 :', prec_score)
print('모델 재현율 :', rec_score)

from sklearn import metrics

# ROC curve의 판별경계선 설정용 결정함수 사용
f_value = model.decision_function(x_test)
df = pd.DataFrame(np.vstack([f_value, y_pred, y_test]).T, columns=['f', 'y_pred', 'y_test'])
fpr, tpr, thresholds = metrics.roc_curve(y, model.decision_function(x))
# print('fpr :', fpr)
# print('tpr :', tpr)
# thresholds : 분류결정 임계값(결정함수값)

plt.plot(fpr, tpr, 'o-', label='LogisticRegression')
plt.plot([0, 1], [0, 1], 'k--', label='landom classifier line(AUC:0.5)')
plt.plot([rec_score], 'ro', ms=6)   # 위양성률, 재현율 출력
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC Curve')
plt.legend()
plt.show()

print('ACU(Area Under the Curve) : ROC 커브의 면적. 1에 근사할수록 좋은 모델')
print('AUC :', metrics.auc(fpr, tpr))   # 0.97479 매우 성능이 우수한 모델

