import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.
# 수집된 자료 :  
# kind quantity
# 1 64
# 2 72
# 3 68
# 4 77
# 2 56
# 1 NaN
# 3 95
# 4 78
# 2 55
# 1 91
# 2 63
# 3 49
# 4 70
# 1 80
# 2 90
# 1 33
# 1 44
# 3 55
# 4 66
# 2 77

data = pd.DataFrame({
    'kind': [1,2,3,4,2,1,3,4,2,1,2,3,4,1,2,1,1,3,4,2],
    'quantity': [64,72,68,77,56,np.nan,95,78,55,91,63,49,70,80,90,33,44,55,66,77]
})

print('데이터 평균 :', data['quantity'].mean())     # 67.5263157

# 데이터 그룹화
gr1 = data[data.kind == 1]
gr2 = data[data.kind == 2]
gr3 = data[data.kind == 3]
gr4 = data[data.kind == 4]
print(len(gr1), len(gr2), len(gr3), len(gr4))
print(gr1.head(3))

# 결측값 채우기
gr1.fillna(gr1['quantity'].mean(), inplace=True)
gr2.fillna(gr2['quantity'].mean(), inplace=True)
gr3.fillna(gr3['quantity'].mean(), inplace=True)
gr4.fillna(gr4['quantity'].mean(), inplace=True)

# 귀무 : 기름의 종류에 따라 빵에 흡수된 기름의 양에 차이가 없다.
# 대립 : 기름의 종류에 따라 빵에 흡수된 기름의 양에 차이가 있다.
print()
print(stats.levene(gr1['quantity'], gr2['quantity'], gr3['quantity'], gr4['quantity']).pvalue)  
# 0.347329  만족 O
print(stats.bartlett(gr1['quantity'], gr2['quantity'], gr3['quantity'], gr4['quantity']).pvalue)
# 0.195586 만족 O
print()
print(stats.shapiro(gr1['quantity']).pvalue)     # 0.88300 만족 O
print(stats.shapiro(gr2['quantity']).pvalue)     # 0.59239
print(stats.shapiro(gr3['quantity']).pvalue)     # 0.48601
print(stats.shapiro(gr4['quantity']).pvalue)     # 0.41621

print()
print(stats.f_oneway(gr1['quantity'], gr2['quantity'], gr3['quantity'], gr4['quantity']))
# F_onewayResult : statistic=0.322547, pvalue=0.80899799
# 해석 : pvalue < alpha 0.05이므로 귀무 채택
# 기름의 종류에 따라 빵에 흡수된 기름의 양에 차이가 없다.

print('~~~~~~~~~~~~~~~')
# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오. 
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
import pymysql
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

try:
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cur:
            # 부서명, 연봉정보 가져오기
            sql = """
            select busername, jikwonpay 
            from jikwon left outer join buser
            on buser.buserno = jikwon.busernum
            """
            df = pd.read_sql(sql, conn)
            print(len(df))
            # print(df.head())
except Exception as e:
    print('error : ', e)

df.dropna(subset='jikwonpay', inplace=True)
print(len(df))

print('전체 직원 연봉 평균 :', df['jikwonpay'].mean())  # 5305.0
group1 = np.array(df[df.busername == '총무부']['jikwonpay'].astype(float).to_numpy())
group2 = np.array(df[df.busername == '영업부']['jikwonpay'].astype(float).to_numpy())
group3 = np.array(df[df.busername == '전산부']['jikwonpay'].astype(float).to_numpy())
group4 = np.array(df[df.busername == '관리부']['jikwonpay'].astype(float).to_numpy())
print(group1)

# 귀무 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 없다.
# 대립 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있다.

# 등분산성 검정
print(stats.levene(group1, group2, group3, group4).pvalue)      # 0.798075 만족 O
print(stats.bartlett(group1, group2, group3, group4).pvalue)    # 0.629095

# 정규성 검정
print()
print(stats.shapiro(group1).pvalue)     # 0.02604 만족 X
print(stats.shapiro(group2).pvalue)     # 0.02560 만족 X
print(stats.shapiro(group3).pvalue)     # 0.41940 만족 O
print(stats.shapiro(group4).pvalue)     # 0.90780 만족 O

# f_oneway
print()
print(stats.f_oneway(group1, group2, group3, group4))
# F_onewayResult : statistic=0.41244, pvalue=0.745442
# pvalue > alpha 0.05이므로 귀무 기각

# f_oneway() : 정규성 깨지면 stats.kruskal() 사용, 등분산성이 깨지면 welch's ANOVA 사용
# stats.kruskal()
print()
print(stats.kruskal(group1, group2, group3, group4))    # 귀무 기각
# KruskalResult : statistic=1.67125, pvalue=0.64334
# pvalue > alpha 0.05이므로 귀무 기각

# 사후검정
tukResult = pairwise_tukeyhsd(endog=df['jikwonpay'], groups=df['busername'], alpha=0.05)
print(tukResult)
# 시각화
tukResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
