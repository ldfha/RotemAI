# [GaussanNB 문제] 
# 독버섯(poisonous)인지 식용버섯(edible)인지 분류
# https://www.kaggle.com/datasets/uciml/mushroom-classification
# feature는 중요변수를 찾아 선택, label:class
# 참고 : from xgboost import plot_importance
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
import xgboost as xgb
from xgboost import plot_importance
import matplotlib.pyplot as plt
import koreanize_matplotlib

pd.set_option("display.max_columns", None)
data = pd.read_csv('mushrooms.csv')
print(data.head(2))
print(data.info())

# 데이터 전처리
data = data.dropna()

x = data.drop('class', axis=1)
# LabelEncoding
le = LabelEncoder()
for col in x.columns:
    x[col] = le.fit_transform(x[col])

y = data['class'].map({'p':0, 'e':1})
print(x.head(2))
print(y[:2])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=12, stratify=y
)
print(x_train.shape, x_test.shape)  # (6499, 22) (1625, 22)

# 피처 중요도 시각화를 위한 xgboost 모델 생성
xgb_clf = xgb.XGBClassifier(n_estimators=10, random_state=12)
xgb_clf.fit(x_train, y_train)
xgb_roc_score = roc_auc_score(y_test, xgb_clf.predict_proba(x_test)[:, 1])
print(f'xgb_roc_score : {xgb_roc_score:.5f}')   # 0.83591

print("--- 피처 중요도 ---")
# 시각화
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
plot_importance(xgb_clf, ax=ax, max_num_features=20)
plt.show()

feat_imp = pd.Series(xgb_clf.feature_importances_, index=x.columns)
top_features = feat_imp.head(10).index.tolist()
print("선택된 피처:", top_features)
# odor                        0.935815
# spore-print-color           0.034108
# stalk-color-below-ring      0.008580
# cap-surface                 0.007708
# stalk-root                  0.006435
# population                  0.003589
# stalk-surface-above-ring    0.003144
# gill-size                   0.000552
# habitat                     0.000068

# 중요한 피처만 사용하여 모델 생성하기
x = x[top_features]
print(x.head(2))

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=12, stratify=y
)

model = GaussianNB()
model.fit(x_train, y_train)

# 예측 및 평가
pred = model.predict(x_test)
print('실제값 :', y_test[:5].values)    # [0 1 1 1 0]
print('예측값 :', pred[:5])             # [0 1 1 1 0]

print('accuracy score :', accuracy_score(y_test, pred))     # 0.871384
print('confusion matrix :\n', confusion_matrix(y_test, pred))
print(f"총 갯수: {len(y_test)}, 오류수: {(y_test != pred).sum()}")
# 총 갯수: 1625, 오류수: 209
print()
# 교차 검증
scores = cross_val_score(model, x, y, cv=5)
print(f'교차 검증 결과에서 각 fold:{scores}, 평균:{scores.mean()}') # 평균:0.822256
print()

# feature 중요도 분석
# feature가 정규분포를 따른다는 가정하에 클래스별 평균
# GaussianNB의 멤버 theta_ : 각 클래스별 feature 평균
mean_0 = model.theta_[0] # class=0 (p)
mean_1 = model.theta_[1] # class=1 (e)

importnace = np.abs(mean_1 - mean_0)
feat_impo = pd.DataFrame({
    'feature':x.columns,
    'importance':importnace
}).sort_values(by='importance', ascending=False)
print('feature 중요도')
print(feat_impo)

# bar그래프로 시각화
plt.figure(figsize=(10, 8))
plt.bar(feat_impo['feature'][:10], feat_impo['importance'][:10], color='b')
plt.xticks(rotation=45)
plt.xlabel('feature')
plt.ylabel('importance')
plt.title('중요 변수 상위 10개')
plt.tight_layout()
plt.show()