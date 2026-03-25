# c) 키보드로 사번, 직원명을 입력받아 로그인에 성공하면 console에 아래와 같이 출력하시오.
#       조건 :  try ~ except MySQLdb.OperationalError as e:      사용
#      사번  직원명  부서명   직급  부서전화  성별
#      ...
#      인원수 : * 명
#     - 성별 연봉 분포 + 이상치 확인    <== 그래프 출력
#     - Histogram (분포 비교) : 남/여 연봉 분포 비교    <== 그래프 출력
import pymysql
import MySQLdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

def quiz():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
    #      키보드로 사번, 직원명을 입력받아 로그인
        no, name = input('사번, 직원명 입력\n').split(' ')
        print(no)
        print(name)
        sql = """
            select jikwonno as 사번, jikwonname as 직원명
            from jikwon
            where jikwonno=%s and jikwonname=%s
        """
        cursor.execute(sql, (no, name))
        if not cursor.fetchall():
            print('로그인 실패')
            return
        print('로그인 성공')
        # 사번  직원명  부서명   직급  부서전화  성별
        sql = """
            select 
                jikwonno as 사번, 
                jikwonname as 직원명, 
                busername as 부서명,
                jikwonjik as 직급,
                busertel as 부서전화,
                jikwongen as 성별,
                jikwonpay as 연봉
            from jikwon inner join buser on jikwon.busernum=buser.buserno
        """
        df = pd.read_sql(sql, conn)
        print(df)
        print('인원수 :', df['사번'].count())

#     - 성별 연봉 분포 + 이상치 확인    <== 그래프 출력
        pdf = df.pivot_table(values='연봉', index='성별')
        print(df[df['성별']=='여'])
        FQ1 = df[df['성별']=='여']['연봉'].quantile(0.25)
        MQ1 = df[df['성별']=='남']['연봉'].quantile(0.25)
        FQ3 = df[df['성별']=='여']['연봉'].quantile(0.75)
        MQ3 = df[df['성별']=='남']['연봉'].quantile(0.75)
        FIQR = FQ3 - FQ1
        MIQR = MQ3 - MQ1

        lower_bound_f = FQ1 - 1.5 * FIQR
        upper_bound_f = FQ3 + 1.5 * FIQR
        lower_bound_m = MQ1 - 1.5 * MIQR
        upper_bound_m = MQ3 + 1.5 * MIQR

        outliers_f = df[
            (df['성별'] == '여') &
            ((df['연봉'] < lower_bound_f) | (df['연봉'] > upper_bound_f))
        ]

        filtered_f = df[
            (df['성별'] == '여') &
            (df['연봉'] >= lower_bound_f) &
            (df['연봉'] <= upper_bound_f)
        ]

        outliers_m = df[
            (df['성별'] == '남') &
            ((df['연봉'] < lower_bound_m) | (df['연봉'] > upper_bound_m))
        ]

        filtered_m = df[
            (df['성별'] == '남') &
            (df['연봉'] >= lower_bound_m) &
            (df['연봉'] <= upper_bound_m)
        ]

        # 4. 이상치 출력
        print("여성 이상치")
        print(outliers_f)

        print("남성 이상치")
        print(outliers_m)

        plt.boxplot(
            [df[df['성별']=='남']['연봉'], df[df['성별']=='여']['연봉']],
            labels=['남', '여'])
        plt.ylabel('연봉')
        plt.title('성별 연봉 분포 및 이상치')
        plt.show()

        plt.subplot(2, 1, 1)
        plt.hist(x=df[df['성별']=='남']['연봉'], bins=10)
        plt.title('남자')
        plt.subplot(2, 1, 2)
        plt.hist(x=df[df['성별']=='여']['연봉'], bins=10, color='red')
        plt.title('여자')
        plt.tight_layout()
        plt.show()

    except MySQLdb.OperationalError as e:
        print('처리 오류 : ', e)
        
    finally:
        cursor.close()
        conn.close()

if __name__=='__main__':
    quiz()