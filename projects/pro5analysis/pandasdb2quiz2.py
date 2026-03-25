# b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))

import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
    sql = """
        select jikwonno as 사번, jikwonname as 이름, jikwongen as 성별, jikwonpay as 연봉, busername as 부서명 from jikwon inner join buser on jikwon.busernum=buser.buserno
    """
    df = pd.read_sql(sql, conn)
    result = df.pivot_table(values='연봉', index='성별', aggfunc='mean')
    print(result)

#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
    # buser_ypay = df.groupby(['부서명'])['연봉'].mean()  # 직급별
    # print(buser_ypay)
    plt.bar(range(len(result.index)), result['연봉'], alpha=0.4)     # 가로 막대
    plt.xticks(range(len(result.index)), result.index)
    plt.xlabel('평균 연봉')
    plt.ylabel('성별')
    plt.show()

#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
    ctab = pd.crosstab(df['부서명'], df['성별'], margins=True)
    print('교차표\n', ctab)
    print()

except Exception as e:
    print('처리 오류 : ', e)
    
finally:
    cursor.close()
    conn.close()