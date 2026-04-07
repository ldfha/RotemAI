# [로지스틱 분류분석 문제1]
# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.
 
import pandas as pd
import io

# 1. 데이터 문자열 정의
data_str = """요일,외식유무,소득수준
토,0,57
토,0,39
토,0,28
화,1,60
토,0,31
월,1,42
토,1,54
토,1,65
토,0,45
토,0,37
토,1,98
토,1,60
토,0,41
토,1,52
일,1,75
월,1,45
화,0,46
수,0,39
목,1,70
금,1,44
토,1,74
토,1,65
토,0,46
토,0,39
일,1,60
토,1,44
일,0,30
토,0,34"""

# 2. io.StringIO를 사용하여 문자열을 파일처럼 읽어 데이터프레임 생성
df = pd.read_csv(io.StringIO(data_str))
# 3. 결과 확인
print(df.head(3))
# 데이터프레임 정보 확인
print(df.info())

# ----
# 주말 데이터만 따로 추출
df_weekend = df[df['요일'].isin(['토', '일'])]
print(df_weekend['요일'].unique())

# 모델 생성
import numpy as np
import statsmodels.formula.api as smf
formula = '외식유무 ~ 소득수준'   # '연속형 ~ 범주형 + ...'
result = smf.logit(formula=formula, data=df_weekend).fit()
print(result.summary())     # Logit Regression Results

# 예측값, 실제값 확인
pred = result.predict(df_weekend[:10])
print('예측값 :', np.around(pred.values))             # [1. 0. 0. 0. 1. 1. 0. 0. 1. 1.]
print('실제값 :', df_weekend['외식유무'][:10].values)  # [0 0 0 0 1 1 0 0 1 1]

# 모델 정확도 확인
print('수치에 대한 집계표(Confusion matrix, 혼돈행렬) 확인 ---')
conf_tab = result.pred_table()
print(conf_tab)

from sklearn.metrics import accuracy_score
pred2 = result.predict(df_weekend)
print('분류 정확도 :', accuracy_score(df_weekend['외식유무'], np.around(pred2)))    # 0.904761

# glm 활용
import statsmodels.api as sm
result2 = smf.glm(formula=formula, data=df_weekend, family=sm.families.Binomial()).fit()

glm_pred = result2.predict(df_weekend[:10])
print('glm 예측값 :', np.around(glm_pred.values))
print('glm 실제값 :', df_weekend['외식유무'][:10].values)

glm_pred2 = result2.predict(df_weekend)
print('glm 분류 정확도 :', accuracy_score(df_weekend['외식유무'], np.around(glm_pred2)))   # 0.904761

# 소득수준 입력 받아서 결과 예측
newdata = int(input('소득수준 입력(양의 정수) : '))
newdf = pd.DataFrame({'소득수준' : [newdata]})
new_pred = result.predict(newdf).values[0]
new_pred2 = result2.predict(newdf).values[0]
print('logit() 예측 결과 :', np.around(new_pred))
print('glm() 예측 결과 :', np.around(new_pred2))
print('외식 함' if np.around(new_pred) == 1.0 else '외식 안함')