# 상관관계 문제)
# https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 
# tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 또한 sales와 관계를 알기 위해 sales에 상관 관계를 정렬한 후 
# TV, radio, newspaper에 대한 영향을 해석하시오.
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/Advertising.csv", index_col='no')
print(data.head())
print(data.describe())

print()
print('표준편차')
print(np.std(data.tv))
print(np.std(data.radio))
print(np.std(data.newspaper))

print()
print('공분산')
print(np.cov(data.tv, data.radio))
print(np.cov(data.tv, data.newspaper))
print(np.cov(data.radio, data.newspaper))

print()
co_re = data.corr()
print(co_re)
#                  tv     radio  newspaper     sales
# tv         1.000000  0.054809   0.056648  0.782224
# radio      0.054809  1.000000   0.354104  0.576223
# newspaper  0.056648  0.354104   1.000000  0.228299
# sales      0.782224  0.576223   0.228299  1.000000

print()
# sales에 따른 다른 특성 사이의 상관관계
print(co_re['sales'].sort_values(ascending=False))
# tv 0.782224 : 강한 상관관계. sales에 가장 큰 영향을 미침
# radio 0.576223 : 중간 상관관계
# newspaper 0.228299 : 낮은 상관관계. sales와 관련성이 가장 적다

# 히트맵 시각화
import seaborn as sns
sns.heatmap(co_re, annot=True)
plt.show()