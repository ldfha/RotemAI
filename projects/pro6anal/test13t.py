# 복부 수술 전후의 몸무게 차이는 있는가?
# 귀무 : 수술 전후 몸무게 차이는 없다.
# 대립 : 수술 전후 몸무게 차이는 있다.
baseline = [72, 75, 78, 74, 77, 73, 76, 79, 74]
follow_up = [70, 73, 75, 72, 74, 71, 73, 76, 72]

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

print(np.mean(baseline))
print(np.mean(follow_up))
print('평균의 차이 :', np.mean(baseline) - np.mean(follow_up) )

# 시각화
plt.bar(np.arange(2), [np.mean(baseline), np.mean(follow_up)])
plt.xlim(0, 1)
plt.xlabel('수술 전후', fontdict={'fontsize':12, 'fontweight':'bold'})
plt.show()

result = stats.ttest_rel(baseline, follow_up)
print(result)
# static 3.668116, pvalue 0.006326650, df 8
# 해석 : pvalue 0.006326650 < alpha 0.05 이므로 귀무가설 기각
# 복부 수술 전 몸무게와 복부 수술 후 몸무게의 변화는 있다. 라는 의견을 받아 들임