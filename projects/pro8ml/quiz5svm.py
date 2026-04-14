# [SVM 분류 문제] 심장병 환자 데이터를 사용하여 분류 정확도 분석 연습
# https://www.kaggle.com/zhaoyingzhu/heartcsv
# https://github.com/pykwon/python/tree/master/testdata_utf8         Heartcsv
# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
# 임의의 값을 넣어 분류 결과를 확인하시오.     
# 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ
# feature 칼럼 : 문자 데이터 칼럼은 제외
# label 칼럼 : AHD(중증 심장질환)
# 데이터 예)
# "","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"
# "1",63,1,"typical",145,233,1,2,150,0,2.3,3,0,"fixed","No"
# "2",67,1,"asymptomatic",160,286,0,2,108,1,1.5,2,3,"normal","Yes"

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler  # 정규화 클래스

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Heart.csv", index_col=0)
print(df.head(2), df.shape)     # (303, 14)
df = df.dropna()    
print(df.shape)     # (297, 14)
print(df.info())

label = df['AHD']
x = df.drop(['ChestPain', 'Thal', 'AHD'], axis=1)
print(label[:2])
print(x[:2])

x_train, x_test, y_train, y_test = train_test_split(x, label, random_state=12, test_size=0.3)
print(x_test.shape, x_train.shape)  # (91, 11) (212, 11)

# 정규화 (0 ~ 1 사이의 범위 내 자료료 변환)
scaler = MinMaxScaler()
x_train_scaled = scaler.fit_transform(x_train)   # 2차원 입력
x_test_scaled = scaler.transform(x_test)

print(x[:5])
print(x_train_scaled[:5])

model = svm.SVC(C=10.0, kernel='rbf').fit(x_train_scaled, y_train)
print(model)

pred = model.predict(x_test_scaled)
print('예측값 :', pred[:10])
print('실제값 :', y_test[:10])

sc_score = metrics.accuracy_score(y_test, pred)
print('sc_score :', sc_score)   # 0.7888

# 교차 검증 모델
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, x, label, cv=3)
print('3회 각 정확도 :', cross_vali)
print('평균 정확도 :', cross_vali.mean())

# 가상의 새로운 환자 2명 데이터 생성 (11개 Feature)
new_patients = pd.DataFrame([
    [45, 1, 120, 230, 0, 0, 160, 0, 0.5, 1, 0], # 건강할 것으로 예상되는 젊은 환자
    [65, 0, 150, 290, 1, 2, 110, 1, 2.0, 2, 2]  # 심장 질환 위험이 높아 보이는 고령 환자
], columns=x.columns)

# 정규화
new_patients_scaled = scaler.transform(new_patients)

# 예측 수행
new_predictions = model.predict(new_patients_scaled)

print("--- 새로운 환자 예측 결과 ---")
for i, result in enumerate(new_predictions):
    print(f"환자 {i+1}의 AHD(심장질환) 예측: {result}")
