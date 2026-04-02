# 공분산 / 상관계수
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv")
print(data.head())
print(data.describe())

print('표준편차')
print(np.std(data.친밀도))
print(np.std(data.적절성))
print(np.std(data.만족도))

plt.hist([np.std(data.친밀도), np.std(data.적절성), np.std(data.만족도)])
plt.show()

print('공분산')
print(np.cov(data.친밀도, data.적절성))
print(np.cov(data.친밀도, data.만족도))
print()
print(data.corr())
print(data.corr(method='pearson'))      # 연속형 변수 | 정규성을 따름
# print(data.corr(method='spearman'))     # 서열형 변수 | 정규성을 따르지 않음
# print(data.corr(method='kendall'))      # spearman과 유사

print()
# 만족도에 따른 다른 특성 사이의 상관관계
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))

# 시각화
data.plot(kind='scatter', x='만족도', y='적절성')
plt.show()

from pandas.plotting import scatter_matrix
attr = ['친밀도', '적절성', '만족도']
scatter_matrix(data[attr], figsize=(10, 6))
plt.show()

import seaborn as sns
sns.heatmap(data.corr(), annot=True)
plt.show()