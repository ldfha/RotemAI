import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import wilcoxon

# [one-sample t 검정 : 문제1]  
# 영사기( 프로젝터 )에 사용되는 구형 백열전구의 수명은 250 시간이라고 알려졌다. 
# 한국 연구소에서 수명이 50 시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명 시간 관련 자료를 얻었다. 
# 한국 연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
# 수집된 자료 :  305 280 296 313 287 240 259 266 318 280 325 295 315 278

# 귀무 : 새로운 백열전구의 수명은 300시간이다.
# 대립 : 새로운 백열전구의 수명은 300시간이 아니다.
data = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print(stats.shapiro(data))  # pvalue 0.8208613
# alpha 0.05 < pvalue 이므로 정규성 만족

result = stats.ttest_1samp(data, popmean=300) # 데이터, 예상 평균
print(result)
# TtestResult(statistic=-1.55643565, pvalue=0.143606254517609, df=13)
# 유의수준 0.05 < pvalue 이므로 귀무가설 채택
# 새로운 백열전구의 수명은 300시간이다.


# [one-sample t 검정 : 문제2] 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. 
# A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.  
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", ""),
#           null인 관찰값은 제거.

# 귀무 : 노트북 평균 사용 시간이 5.2시간이다.
# 대립 : 노트북 평균 사용 시간이 5.2시간이 아니다.
data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/one_sample.csv")
print(data2.head())
data2['time'] = pd.to_numeric(data2['time'], errors='coerce')
data2.dropna(inplace=True)

print(stats.shapiro(data2['time']))  # pvalue 0.72423033
# alpha 0.05 < pvalue 이므로 정규성 만족

print(data2['time'].mean())     # 5.5568807
result2 = stats.ttest_1samp(data2['time'], popmean=5.2)
print(result2)
# TtestResult(statistic=3.94605, pvalue=0.0001416, df=108)
# 유의수준 0.05 > pvalue 이므로 귀무가설 기각


# [one-sample t 검정 : 문제3] 
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오. (월별)
data3 = pd.read_excel("quiz2t.xls")
data3 = data3.iloc[:, 3:].T
data3.columns=['요금']
data3.dropna(inplace=True)
print(data3.head())
# 귀무 : 전국 평균 미용 요금이 15000원이다.
# 대립 : 전국 평균 미용 요금이 15000원이 아니다.
print(stats.shapiro(data3))  # pvalue 0.08795706
# alpha 0.05 < pvalue 이므로 정규성 만족

print(data3['요금'].mean())     # 20003.9375
result3 = stats.ttest_1samp(data3['요금'], popmean=15000.0)
print(result3)
# TtestResult(statistic=7.174362, pvalue=3.2057661925789945e-06, df=15)
# alpha 0.05 > pvalue 이므로 귀무가설 기각
# 전국 평균 미용 요금이 15000원이 아니다.