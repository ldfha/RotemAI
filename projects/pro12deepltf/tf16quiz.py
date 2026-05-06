# 문제2) 21세 이상의 피마 인디언 여성의 당뇨병 발병 여부에 대한 dataset을 이용하여 당뇨 판정을 위한 분류 모델을 작성한다.
# 피마 인디언 당뇨병 데이터는 아래와 같이 구성되어 있다.
#   Pregnancies: 임신 횟수
#   Glucose: 포도당 부하 검사 수치
#   BloodPressure: 혈압(mm Hg)
#   SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm)
#   Insulin: 혈청 인슐린(mu U/ml)
#   BMI: 체질량지수(체중(kg)/키(m))^2
#   DiabetesPedigreeFunction: 당뇨 내력 가중치 값
#   Age: 나이
#   Outcome: 5년 이내 당뇨병 발생여부 - 클래스 결정 값(0 또는 1)
# 당뇨 판정 칼럼은 outcome 이다.   1 이면 당뇨 환자로 판정

# train / test 분류 실시
# 모델 작성은 Sequential API, Function API 두 가지를 사용한다.
# ModelCheckPoint, EarlyStopping 사용
# loss, accuracy에 대한 시각화를 실시한다.

import pandas as pd
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/pima-indians-diabetes.data.csv")
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df.columns = columns
df = df.dropna()
print(df.head(3))
print(df.info())

# feature, label로 구분
x = df.drop(['Outcome'], axis=1)
y = df['Outcome']
print(x[:2])
print(y[:2])

# train / test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# 스케일링
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


# 시각화 함수
def plotFunc(history):
    plt.figure(figsize=(12, 5))
    # loss
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()

    # acc
    plt.subplot(1, 2, 2)
    plt.plot(history.history['acc'], label='acc')
    plt.plot(history.history['val_acc'], label='val_acc')
    plt.xlabel('epochs')
    plt.ylabel('acc')
    plt.legend()
    plt.show()

# 모델 저장
MODEL_DIR = './quizmodel/'
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)
seq_modelpath = MODEL_DIR + 'seq_quizmodel.keras'
func_modelpath = MODEL_DIR + 'func_quizmodel.keras'


# Sequential model
print('===== Sequential API =====')
seq_model = Sequential([
    Input(shape=(x_train_scaled.shape[1], )),
    Dense(units=16, activation='relu'),
    Dense(units=8, activation='relu'),
    Dense(units=1, activation='sigmoid'),
])

seq_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
print(seq_model.summary())

# 조기 종료
seq_early_stop = EarlyStopping(
    monitor='val_loss',
    patience=15,
    restore_best_weights=True
)

# 체크포인트
seq_chkpoint = ModelCheckpoint(
    filepath=seq_modelpath,
    monitor='val_loss',
    save_best_only=True,
    mode='min'
)

# sequential 모델 학습
seq_history = seq_model.fit(
    x_train_scaled, y_train,
    validation_data=(x_test_scaled, y_test),
    epochs=1000, batch_size=16, verbose=2,
    callbacks = [seq_early_stop, seq_chkpoint]
)

loss, acc = seq_model.evaluate(x_test_scaled, y_test, verbose=0)
print(f'테스트 결과 손실:{loss:.4f}, 정확도:{acc:.4f}')     # 손실:0.5055, 정확도:0.6948
plotFunc(seq_history)


# Function model
print('===== Function API =====')

inputs = Input(shape=(x_train_scaled.shape[1], ))
outputs = Dense(units=32, activation='relu')(inputs)
outputs = Dense(units=16, activation='relu')(outputs)
outputs = Dense(units=1, activation='sigmoid')(outputs)
func_model = Model(inputs=inputs, outputs=outputs)
func_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['acc']
)

print(func_model.summary())

# 조기 종료
func_early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

# 체크포인트
func_chkpoint = ModelCheckpoint(
    filepath=func_modelpath,
    monitor='val_loss',
    save_best_only=True,
    mode='min'
)

# Function model 학습
func_history = func_model.fit(
    x_train_scaled, y_train,
    validation_data=(x_test_scaled, y_test),
    epochs=1000, batch_size=16, verbose=2,
    callbacks = [func_early_stop, func_chkpoint]
)

loss, acc = func_model.evaluate(x_test_scaled, y_test, verbose=0)
print(f'테스트 결과 손실:{loss:.4f}, 정확도:{acc:.4f}')     # 손실:0.5030, 정확도:0.6883
plotFunc(func_history)
