# pandas의 DataFrame의 자료를 원격 DB의 테이블에 저장
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data ={
    'code':[10,11,12],
    'sang':['사이다','콜라','환타'],
    'su':[20, 22, 5],
    'dan':[3000, '2500', '2300']
}
frame = pd.DataFrame(data)
print(frame)

try:
    engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/test?charset=utf8")
    # 데이터 넣기
    frame.to_sql(name='sangdata', con=engine, if_exists='append', index=False)
    df = pd.read_sql("select * from sangdata", engine)
    print(df)
except Exception as e:
    print("처리 오류:", e)

"""
.env 파일
DV_USER=root
DB_PASS=123

from dotenv import load_dotenv

"""