# [로지스틱 분류분석 문제2] 
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler    # 표준화
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/bodycheck.csv")
print(data.head(2), data.shape)     # (20, 6)

x = data[['게임', 'TV시청']]
y = data['안경유무']
print(x[:3])
print(y[:3])
# # 필요없는 칼럼 삭제
# data2 = pd.DataFrame()
# data2 = data.drop(['번호', '신장', '체중'], axis=1)
# print(data2.head(2), data2.shape)   # (366, 10)
# print(data2['안경유무'].unique())   # [1 0]

# 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# (105, 2) (45, 2) (105,) (45,)
print(x_train[:3], ' ', x_test[:3], ' ', y_train[:3], ' ', y_test[:3])

# train, test = train_test_split(data2, test_size=0.3, random_state=0)
# print(train.shape, test.shape)
# print(train.head(3))
# print(test.head(3))

model = LogisticRegression(C=0.06, solver='lbfgs', random_state=0)
model.fit(x_train, y_train)     # train으로 학습
# 분류 예측
y_pred = model.predict(x_test)
print('예측값 :', y_pred)
print('실제값 :', y_test)

print(f'총 갯수:{len(y_test)}, 오류수:{(y_test != y_pred).sum()}')
# test data

print('분류 정확도 확인')
print(f'{accuracy_score(y_test, y_pred)}')  # 0.97777

# 새로운 입력값으로 분류 확인
game = int(input('게임 입력 : '))
tv = int(input('TV시청 입력 : '))
new_data = pd.DataFrame({'게임':[game], 'TV시청':[tv]})
new_pred = model.predict(new_data)
print('예측결과 :', new_pred)
