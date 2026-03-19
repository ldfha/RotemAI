# 연산
from pandas import Series, DataFrame
import numpy as np

s1 = Series([1,2,3], index=['a','b','c'])
s2 = Series([4,5,6,7], index=['a','b','d','c'])
print(s1)
print(s2)
print(s1 + s2)  # 같은 index끼리 연산, 불일치시 NaN 반환
# python 덧셈
print(s1.add(s2))
# numpy 함수 계승

print(s1.mul(s2))   # sub, div도 가능

print()
df1 = DataFrame(np.arange(9).reshape(3, 3), 
                columns=list('kbs'),    # kbs 문자열이 분리되어서 들어감 
                index=['서울','대전','부산'])    
df2 = DataFrame(np.arange(12).reshape(4, 3), 
                columns=list('kbs'),    # kbs 문자열이 분리되어서 들어감 
                index=['서울','대전','제주','광주'])    
print(df1)
print(df2)
print(df1+df2)  # 대응되는 서울, 대전만 연산되고 나머지는 NaN
print(df1.add(df2, fill_value=0))   # NaN은 0으로 채운 후 연산에 참여
# sub, mul, div도 가능

print('NaN(결측값) 처리 --------')
df = DataFrame([[1.4, np.nan], [7, -4.5], [np.nan, np.nan], [0.5, -1]],
               columns=['one','two'])
print(df)
print()

print(df.isnull())  # null있으면 True, 없으면 False
print(df.notnull()) # null있으면 False, 없으면 False
print()

# NaN이 하나라도 있으면 해당 row를 지움
print(df.dropna())  
print(df.dropna(how='any'))
print()

# 모두 NaN값이면 지움
print(df.dropna(how='all'))
print()

# 'one'열 칼럼의 NaN 삭제
print(df.dropna(subset=['one']))    # '특정 열에 NaN이 있는 삭제
print()
print(df.dropna(subset=['two']))

print()
print(df.dropna(axis='rows'))
print(df.dropna(axis='columns'))    # NaN이 있는 col을 삭제

print()
print(df)
imsi = df.drop(1)   # 원본은 삭제 안됨. 삭제된 결과가 새로운  dataFrame으로 생성됨
print(imsi)
print(df)
print()
# df.drop(1, inplace=True)
# print(df)

print()
# 계산 관련 메소드
print(df.sum())         # 열의 합 - NaN은 연산에서 제외
print(df.sum(axis=0))
print(df.sum(axis=0, skipna=True))  
# print(df.sum(axis=0, skipna=False))  # NaN 연산에 포함

print(df.sum(axis=1))   # 행의 합

print()
print(df.describe())    # 요약 통계량 출력
print(df.info())

print()
words = Series(['봄', '여름', '가을', '봄'])
print(words.describe())
