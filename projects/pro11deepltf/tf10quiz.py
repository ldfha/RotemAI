# https://raw.githubusercontent.com/pykwon/python/refs/heads/master/data/train.csv

# 자전거 공유 시스템 분석용 데이터 train.csv를 이용하여 대여횟수에 영향을 주는 변수들을 골라 다중선형회귀분석 모델을 작성하시오.
# 모델 학습시에 발생하는 loss를 시각화하고 설명력을 출력하시오.
# 새로운 데이터를 input 함수를 사용해 키보드로 입력하여 대여횟수 예측결과를 콘솔로 출력하시오.

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation 
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

datas = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/data/train.csv")
print(datas[:3])

datas['datetime'] = pd.to_datetime(datas['datetime'])
datas['hour'] = datas['datetime'].dt.hour # '시간'을 숫자로 추출!
datas['month'] = datas['datetime'].dt.month # '월'도 추가하면 좋음
datas = datas.drop(columns="datetime", axis=1)

# 상관계수 행렬
corr_matrix = datas.corr()
# 대여횟수(count)와 다른 변수들 간의 상관관계
print(corr_matrix['count'].sort_values(ascending=False))

x_data = datas.drop(columns=["count", "casual", "registered"], axis=1)
print(x_data[:3])
y_data = datas["count"]
print(y_data[:3])
print(x_data.shape, y_data.shape)   # (10886, 10) (10886,)

print('train / test split을 한 모델 작성')
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.3, random_state=123)

print(x_train.shape, x_test.shape)  # (7620, 10) (3266, 10)

# 정규화
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = Sequential()
model.add(Input(shape=(x_train.shape[1], )))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=21, activation='relu'))
model.add(Dense(units=1, activation='linear'))

model.compile(loss='mse', optimizer='adam', metrics=['mse'])
history = model.fit(x_train, y_train, epochs=100, verbose=0, validation_split=0.15, batch_size=32)
print('evaluate result :', model.evaluate(x_test, y_test, verbose=0))

# loss 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['val_loss'], label='val_loss')
plt.plot(history.history['loss'], label='loss')
plt.legend()
plt.show()

from sklearn.metrics import r2_score
pred = model.predict(x_test)
print('설명력 :', r2_score(y_test, pred))
print('실제값 :', y_test[:3])
print('예측값 :', pred[:3])

# 시각화
plt.plot(y_test.values[:50], 'b', label='real')
plt.plot(pred[:50], 'r--', label='predict')
plt.legend()
plt.show()


# 키보드로 값 입력받아 예측하기
print("\n--- 새로운 데이터 예측 (season, holiday, workingday, weather, temp, atemp, humidity, windspeed, hour, month) ---")
user_input = input("10개 값을 쉼표로 구분하여 입력: ")
try:
    new_data = np.array([[float(i) for i in user_input.split(',')]])
    new_data_scaled = scaler.transform(new_data)
    result = model.predict(new_data_scaled)
    print(f"예측 대여 횟수: {result[0][0]:.2f}회")
except:
    print("입력 형식 오류 (예: 1,0,1,1,20,25,50,15)")