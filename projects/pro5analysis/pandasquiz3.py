import pandas as pd
import numpy as np

df = pd.read_csv('titanic_data.csv')
# print(df)

# 1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
result_cut = pd.cut(df['Age'], bins, labels=labels)
print(pd.Series(result_cut).value_counts())

#  2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 
pdf = df.pivot_table(index=['Sex'], 
                     columns=["Pclass"], 
                     values='Survived')
print(pdf)
print()
pdf = df.pivot_table(index=['Sex','Age'], 
                     columns=["Pclass"], 
                     values='Survived',)
pdf = pdf * 100
pdf = pdf.round(2)
print(pdf)
print()

# AgeGroup으로 묶기
df['AgeGroup'] = pd.cut(df['Age'], bins, labels=labels)
pdf = df.pivot_table(index=['Sex','AgeGroup'], 
                     columns=["Pclass"], 
                     values='Survived',)
pdf = pdf * 100
pdf = pdf.round(2)
print(pdf)
print()
print('---------'*5)
print()

#  1) human.csv 파일을 읽어 아래와 같이 처리하시오.
#      - Group이 NA인 행은 삭제
#      - Career, Score 칼럼을 추출하여 데이터프레임을 작성
#      - Career, Score 칼럼의 평균계산
# https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/human.csv

human = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/human.csv',
                    skipinitialspace=True,   # 공백 제거
                    na_values=['NA'])
# human.columns = human.columns.str.strip()
print(human)
human = human.dropna(subset=['Group'])
print(human)
hdf =  human[['Career', 'Score']]
print(hdf)
print(hdf.mean(axis=0))

#  2) tips.csv 파일을 읽어 아래와 같이 처리하시오.
#      - 파일 정보 확인
#      - 앞에서 3개의 행만 출력
#      - 요약 통계량 보기
#      - 흡연자, 비흡연자 수를 계산  : value_counts()
#      - 요일을 가진 칼럼의 유일한 값 출력  : unique()
#           결과 : ['Sun' 'Sat' 'Thur' 'Fri']
tips = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tips.csv',
                   skipinitialspace=True)
print(tips.info())
print(tips.head(3))
print(tips.describe())
print(tips['smoker'].value_counts())
print(tips['day'].unique())