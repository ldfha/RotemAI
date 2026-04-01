import numpy as np
import scipy.stats as stats
# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
# 수집된 자료 :  
#   남자 : 0.9 2.2 1.6 2.8 4.2 3.7 2.6 2.9 3.3 1.2 3.2 2.7 3.8 4.5 4 2.2 0.8 0.5 0.3 5.3 5.7 2.3 9.8
#   여자 : 1.4 2.7 2.1 1.8 3.3 3.2 1.6 1.9 2.3 2.5 2.3 1.4 2.6 3.5 2.1 6.6 7.7 8.8 6.6 6.4
male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

# 문제 : 남녀 콜레스테롤 수치에 차이가 있는가?
# 귀무 : 차이가 없다.
# 대립 : 차이가 있다.

# 표본 추출 - 비복원
np.random.seed(123)
male_sample = np.random.choice(male, 15, replace=False)
female_sample = np.random.choice(female, 15, replace=False)

# 정규성 검정
print('남성 :', stats.shapiro(male_sample))  # 0.103701   정규성 만족
print('여성 :', stats.shapiro(female_sample))  # 0.0005095 정규성 불만족

# 등분산성
print('등분산성 : ', stats.levene(male_sample, female_sample))
# statistic=0.39371342, pvalue=0.535437
# pvalue=0.535437 >= 0.05 등분산성 만족

print(np.mean(male_sample))    # 3.51333
print(np.mean(female_sample))  # 3.07333
print('평균의 차이 :', np.mean(male_sample) - np.mean(female_sample) )    #0.44000

result = stats.ttest_ind(male_sample, female_sample, equal_var=True)
print(result)
# statistic=0.55416641, pvalue=0.5838642, df=28.0
# alpha 0.05 < pvalue 0.5838642 이므로 귀무가설 채택
# 남녀 콜레스테롤 차이가 없다.


# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
import pymysql
import pandas as pd
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
            where busername in ("영업부", "총무부")
            """
            df = pd.read_sql(sql, conn)
            print(df.head())
except Exception as e:
    print('error : ', e)

ydata = df.loc[df['busername'] =='영업부']
cdata = df.loc[df['busername'] =='총무부']

# 결측값 채우기
ydata.fillna(ydata['jikwonpay'].mean(), inplace=True)
cdata.fillna(cdata['jikwonpay'].mean(), inplace=True)


print(np.mean(ydata['jikwonpay']))    # 4908.3333
print(np.mean(cdata['jikwonpay']))  # 5414.2857
print('평균의 차이 :', np.mean(ydata['jikwonpay']) - np.mean(cdata['jikwonpay']))    # -505.95238095238165

# 문제 : 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지
# 귀무 : 차이가 없다.
# 대립 : 차이가 있다.

# 등분산성
print('등분산성 : ', stats.levene(ydata['jikwonpay'], cdata['jikwonpay']))
# statistic=0.011723, pvalue=0.9150443
# pvalue=0.9150443 >= 0.05 등분산성 만족

# 정규성 검정
print('영업부 :', stats.shapiro(ydata['jikwonpay']))  # 0.025608   정규성 불만족
print('총무부 :', stats.shapiro(cdata['jikwonpay']))  # 0.02604493

# 정규성을 불만족 했으므로 mannwhitneyu
result2 = stats.mannwhitneyu(ydata['jikwonpay'], cdata['jikwonpay'])
print(result2)
# statistic=33.0, pvalue=0.4721334
# alpha 0.05 < pvalue 0.4721334 이므로 귀무가설 채택
# 정규성은 불만족하지만 총무부, 영업부 직원의 연봉 평균에 차이가 있다고 볼 수 없다.


# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 수집된 자료 :  
#    중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
#    기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

mid = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(np.mean(mid))    # 74.1666666
print(np.mean(final))  # 81.666666
print('평균의 차이 :', np.mean(mid) - np.mean(final))    # -7.5

# 귀무 : 학업 능력이 변화하지 않았다.
# 대립 : 학업 능력이 변화했다.

# 정규성 검정
print('중간 :', stats.shapiro(mid).pvalue)  # 0.3681471   정규성 만족
print('기말 :', stats.shapiro(final).pvalue)  # 0.1930029

result3 = stats.ttest_rel(mid, final)
print(result3)
# statistic=-2.6281127, pvalue=0.02348619, df=11
# alpha 0.05 > pvalue 0.0234 이므로 귀무가설 기각
# 이 학급의 학업 능력이 변화했다고 볼 수 있다.