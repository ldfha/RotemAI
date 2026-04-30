import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation 
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datas = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/auto-mpg.csv", na_values='?')
print(datas.head(2))
print(datas.info())

del datas['car name']
datas = datas.dropna()
print(datas.isna().sum())

datas.drop(['cylinders', 'acceleration', 'model year', 'origin'], axis='columns', inplace=True)
print(datas.head(2))

# 데이터 분포 확인
# sns.pairplot(datas[['mpg', 'displacement', 'horsepower', 'weight']],
#             diag_kind='kde')
# plt.plot()

# train / test split
# feature / label 나누지 말아야함
train_dataset = datas.sample(frac=0.7, random_state=123)
print(train_dataset[:2], train_dataset.shape)
test_dataset = datas.drop(train_dataset.index)
print(test_dataset[:2], test_dataset.shape)

# 표준화 : (요소값 - 평균) / 표준편차
train_stat = train_dataset.describe()
train_stat.pop('mpg')
print(train_stat)
train_stat = train_stat.transpose()
print(train_stat)

def stdscale_func(x):
    return (x - train_stat['mean']) / train_stat['std']

# print(stdscale_func(train_dataset[:3]))

# 표준화한 feature 추출
# train_x
st_train_data = stdscale_func(train_dataset)
st_train_data = st_train_data.drop(['mpg'], axis='columns')
print(st_train_data[:3])
# test_x
st_test_data = stdscale_func(test_dataset)
st_test_data = st_test_data.drop(['mpg'], axis='columns')
print(st_test_data[:3])

# label추출
train_label = train_dataset.pop('mpg')
print(train_label[:3])
test_label = test_dataset.pop('mpg')
print(test_label[:3])

# model
def build_model():
    network = Sequential([
        Input(shape=(3, )),
        Dense(units=32, activation='relu'),
        Dense(units=16, activation='relu'),
        Dense(units=1, activation='linear'),
    ])
    opti = tf.keras.optimizers.Adam(learning_rate=0.01)
    network.compile(optimizer=opti, loss='mean_squared_error',
                    metrics=['mean_squared_error', 'mean_absolute_error'])
    
    return network

model = build_model()
print(model.summary())

EPOCHS = 5000

# 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', # 뭘 기준으로 정할지를 결정. loss, val_loss
    patience=5,     # 몇 번의 epoch까지 더 기다릴지 결정. 보통 10
    # baseline=0.01,   # 최소한의 성능
    restore_best_weights=True
)

history = model.fit(x=st_train_data, y=train_label, batch_size=32,
                    epochs=EPOCHS, verbose=2,
                    validation_split=0.2,
                    callbacks = [early_stop]
                    )

df = pd.DataFrame(history.history)
print(df.head(3))
print(df.columns)

# 시각화
def plt_history(df):
    hist = df
    hist['epoch'] = history.epoch
    # print(hist.head())

    plt.figure(figsize=(8, 14))
    plt.subplot(2, 1, 1)
    plt.xlabel('epoch')
    plt.ylabel('mae [mpg]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label='train err')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label='vaildation err')
    plt.legend()
    # MSE
    plt.subplot(2, 1, 2)
    plt.xlabel('epoch')
    plt.ylabel('MSE [mpg]')
    plt.plot(hist['epoch'], hist['mean_squared_error'], label='train err')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label='vaildation err')
    plt.legend()
    plt.show()
    
plt_history(df)

# 모델 평가하기(R2)
loss, mse, mae = model.evaluate(st_test_data, test_label)
print(f'loss : {loss:.3f}')
print(f'mse : {mse:.3f}')
print(f'mae : {mae:.3f}')
# loss : 15.041
# mse : 15.041
# mae : 3.172
print('R2(결정계수, 설명력) :', r2_score(test_label, model.predict(st_test_data)))
#  -0.2743784 : 결정계수가 음수가 나온 이유
# 어딘가에서 설계가 잘못되었다는 뜻
# 조기종료 baseline 삭제 :  0.735552166 : 너무 빨리 끝나서
# learning_rate = 0.001로 조절 : 0.7235237
# restore_best_weights=True 조기종료 옵션 추가 : 0.726395

# 새로운 값으로 예측
new_data = pd.DataFrame({
    'displacement' : [300, 400],
    'horsepower' : [120, 150],
    'weight' : [2000, 4000]
})
new_st_data = stdscale_func(new_data)
new_data_pred = model.predict(new_st_data).ravel()
print(f'새 mpg 예측결과 : {new_data_pred}') #  [20.811623 16.989494]