# 귀무/대립가설 설정 연습
# 1) 어느 공장에서 생산하는 제품의 분산은 7로 알려져 있다. 
# 그런데 일부에서는 분산이 7보다 작다는 말도 나오고 있다. 
# 그래서 어느 말이 더 타당한지를 알아보기 위해 검정을 하려고 한다. 
# 이때 귀무가설과 대립가설을 설정하시오.

# 귀무가설 : 제품의 분산은 7이다.
# 대립가설 : 제품의 분산은 7보다 작다.


# 2) 어느 제품의 불량률은 3%로 알려져 있다. 
# 그런데 불량에 대한 항의 민원전화가 많이 와서, 
# 불량률이 3%보다 더 클 수도 있다는 소리가 나오고 있다. 
# 그래서 실제로 어떠한지를 알아보기 위해 검정을 하는데, 
# 이때 귀무가설과 대립가설을 설정하시오.

# 귀무가설 : 제품의 불량률은 0.03(3%)이다.
# 대립가설 : 제품의 불량률은 0.03(3%)보다 크다.


# 3) 동일한 제품을 생산하는 기계1과 기계2가 있는데, 
# 지금까지는 기계 1에서 생산한 제품의 분산이 큰 것으로 알고 있다. 
# 실제로 그러한지를 검정하려고 하는데, 이때 귀무가설과 대립가설을 설정하시오.

# 귀무가설 : 기계 1의 분산과 기계 2의 분산은 같다.
# 대립가설 : 기계 1의 분산이 기계 2의 분산보다 크다.


import pandas as pd
import scipy.stats as stats

# * 카이제곱 검정
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.

# 귀무가설 : 부모학력 수준이 자녀의 진학여부와 관련이 없다.
# 가설 : 부모학력 수준이 자녀의 진학여부와 관련이 있다.
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/cleanDescriptive.csv")
# print(data.head(3))
# print(data['level2'].unique())
# print(data['pass2'].unique())
ctab = pd.crosstab(index=data['level2'], columns=data['pass2'])    # 빈도수
print(ctab)
chi2, p, dof, expected = stats.chi2_contingency(ctab)
print('chi2 : ', chi2)  # 2.7669512
print('p : ', p)    # 0.2507056
print('dof : ', dof)    # 자유도 : 2
print('expected : ', expected)  # 예측된 기대도수

# 판정1 : 유의수준 0.05 < p:0.2507056   이므로 귀무가설 수용
# 부모학력 수준이 자녀의 진학여부와 관련이 없다.



# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.
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
            sql = """
            select jikwonjik, jikwonpay from jikwon
            """
            data = pd.read_sql(sql, conn).dropna()
            # print(data.head(3))

except Exception as e:
    print('error : ', e)

cut = [1000, 2999, 4999, 6999, 10000]
labels = [1, 2, 3, 4]
data['pay_group'] = pd.cut(data['jikwonpay'], bins=cut, labels=labels)

ctab = pd.crosstab(columns=data['jikwonjik'], index=data['pay_group'])
print(ctab)
chi2, p, dof, expected = stats.chi2_contingency(ctab)
print('chi2 : ', chi2)  # 37.40349
print('p : ', p)    # 0.000192115
print('dof : ', dof)    # 자유도 : 12
print('expected : ', expected)  # 예측된 기대도수

# 판정1 : 유의수준 0.05 > p:0.000192115   이므로 귀무가설 기각
# 직급과 연봉은 관련이 있다.