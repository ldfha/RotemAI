# 문제1)
# https://github.com/data-8/materials-fa17/blob/master/lec/galton.csv
# data를 이용해 아버지 키로 아들의 키를 예측하는 회귀분석 모델을 작성하시오.
#  - train / test 분리
#  - Sequential api와 function api 를 사용해 모델을 만들어 보시오.
#  - train과 test의 mse를 시각화 하시오
#  - 새로운 아버지 키에 대한 자료로 아들의 키를 예측하시오.

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
data = pd.read_csv("https://raw.githubusercontent.com/data-8/materials-fa17/refs/heads/master/lec/galton.csv")
print(data.head(3))

data = data[data["gender"] == "male"]
xdata = data["father"].values.reshape(-1, 1)
ydata = data["childHeight"].values.reshape(-1, 1)

print(xdata.shape, ydata.shape)

# x, y 정규화
from sklearn.preprocessing import MinMaxScaler

x_scaler = MinMaxScaler()
y_scaler = MinMaxScaler()

x_scaled = x_scaler.fit_transform(xdata)
y_scaled = y_scaler.fit_transform(ydata)

print(x_scaled[:3])

# train / test 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_scaled, shuffle=True, test_size=0.3, random_state=123)
print(x_train[:2], x_train.shape)   # (336, 1)
print(x_test[:2], x_test.shape)     # (145, 1)

print()
# 모델 설계
model = Sequential()
model.add(Input(shape=(1, )))
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=1, activation='linear'))      # activation 생략 가능
print(model.summary())

model.compile(optimizer='adam', loss='mse', metrics=['mse'])

history = model.fit(x_train, y_train, epochs=40, batch_size=32, verbose=2, validation_split=0.2)

ev_loss = model.evaluate(x_test, y_test, verbose=0)
print('ev_loss : ', ev_loss)

# history 값 확인
# print('history : ', history.history)
print('history val_loss : ', history.history['val_loss'])   # valid
print('history val_mse : ', history.history['val_mse'])
print('history loss : ', history.history['loss'])
print('history mse : ', history.history['mse'])

# loss 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['val_loss'], label='val_loss')
plt.plot(history.history['loss'], label='loss')
plt.legend()
plt.show()

from sklearn.metrics import r2_score
print('설명력:', r2_score(y_test, model.predict(x_test)))
# 0.19033156197788148

# predict
pred = model.predict(x_test[:5])
print('예측값 : ', pred.ravel())
print('실제값 : ', y_test[:5].ravel())

# 정규화된 값 원래대로 돌리기
print(y_scaler.inverse_transform(y_test)[:5])   # [[70. ] [66. ] [68.5] [65. ] [68. ]]
print(y_scaler.inverse_transform(pred)[:5])     # [[68.29574] [67.86934] [71.48729] [68.72016] [68.29574]]

print('\n\nFunctional api를 사용한 방법 -------------')
from tensorflow.keras.models import Model
# 입력층 정의
inputs = Input(shape=(1, ), name='input_layer') # name은 텐서보드 등에 사용
# 은닉층 정의
x = Dense(units=16, activation='relu', name='hidden_layer1')(inputs)
x = Dense(units=16, activation='relu', name='hidden_layer2')(x)
# 출력층 정의
outputs = Dense(units=1, activation='linear', name='output_layer')(x)
# 모델 생성 (입력과 출력을 연결)
func_model = Model(inputs, outputs)

func_model.compile(optimizer='adam', loss='mse', metrics=['mse'])

history = func_model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2, validation_split=0.2)   # train data중 20%를 학습 중 검증용 사용

ev_loss = func_model.evaluate(x_test, y_test, verbose=0)
print('ev_loss : ', ev_loss)
print('설명력:', r2_score(y_test, model.predict(x_test)))

# 새아빠 키로 예측하기
# 새로운 아버지 키 데이터 준비 (2차원 배열 형태 유지)
new_father = np.array([[70.0], [67.0], [78.0]]) 

# 기존 학습 시 사용했던 'scaler'를 그대로 사용하여 변환
new_father_scaled = x_scaler.transform(new_father)

print(f"새로운 아버지 키: {new_father}")
print(f"새로운 아버지 키(정규화): {new_father_scaled}")
# 새로운 아버지 키: [[70.]]
# 새로운 아버지 키(정규화): [[0.48484848]]

# 각 모델로 예측
pred_seq_scaled = model.predict(new_father_scaled)
pred_func_scaled = func_model.predict(new_father_scaled)

print(f'Sequential 모델 예측 자식 키(정규화): {pred_seq_scaled}')
print(f'Functional 모델 예측 자식 키(정규화): {pred_func_scaled}')
# Sequential 모델 예측 자식 키(정규화): [[0.5068381 ]
# Functional 모델 예측 자식 키(정규화): [[0.4978323 ]

# 예측된 키를 원래 키로 돌리기(inverse_transform)
pred_seq_original = y_scaler.inverse_transform(pred_seq_scaled)
pred_func_original = y_scaler.inverse_transform(pred_func_scaled)

print(f"Sequential 모델 예측 아들 키: {pred_seq_original}")
print(f"Functional 모델 예측 아들 키: {pred_func_original}")
# Sequential 모델 예측 아들 키: [[69.62993 ]
# Functional 모델 예측 아들 키: [[69.45882 ]