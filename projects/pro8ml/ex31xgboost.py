# XGBoost : Boosting 알고리즘을 구현한 분류/예측 모델
# Boosting은 약한 분류기에 대해 샘플의 일부를 보완해하며 순차적으로 학습해 강한 분류기를 만듦

# breast_cancer dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
# pip install xgboost lightgbm
import xgboost as xgb
from lightgbm import LGBMClassifier  # xgboost보다 성능 우수하나 자료가 적으면 과적합 발생
import lightgbm as lgb

data = load_breast_cancer()

# DataFrame으로 변환 (컬럼명 포함)
x = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target  # 0: malignant(악성), 1: benign(양성)

print(x[:3], x.shape)   # (569, 30)
print(y[:3], y.shape)

# 클래스별 샘플 수 확인 — 불균형 여부 체크
print('레이블 분포 : ', {name:(y == i).sum() for i, name in enumerate(data.target_names)})
# 'malignant'(악성): 212, 'benign'(양성): 357

# stratify=y : 클래스 비율 유지 (불균형 데이터 대응)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=12, stratify=y
)
print(x_train.shape, x_test.shape)  # (455, 30) (114, 30)

# 모델 1
xgb_clf = xgb.XGBClassifier(
    booster='gbtree',      # 'gbtree':트리 기반, 'gblinear':선형 모델
    max_depth=6,           # 개별 결정트리 최대 깊이
    n_estimators=200,      # 약한 분류기(트리)의 개수
    eval_metric='logloss', # 이진 분류 평가 지표
    random_state=42
)
xgb_clf.fit(x_train, y_train)

# 모델 2
lgb_clf = LGBMClassifier(
    n_estimators=200,
    random_state=42,
    verbose=-1   # 학습 로그 숨기기 (경고 메시지 제거)
)
lgb_clf.fit(x_train, y_train)

# 예측 / 평가
pred_xgb = xgb_clf.predict(x_test)
pred_lgb = lgb_clf.predict(x_test)

print(f'XGBClassifier  acc : {accuracy_score(y_test, pred_xgb):.5f}')  # 0.96491
print(f'LGBMClassifier acc : {accuracy_score(y_test, pred_lgb):.5f}')  # 0.99123

print()
# 피처 중요도 : gain 기준으로 통일
# XGBoost : get_booster().get_score()로 gain 값 추출
booster = xgb_clf.get_booster()
xgb_gain = pd.Series(booster.get_score(importance_type='gain'))
# LightGBM : booster_.feature_importance()로 gain 값 추출
lgb_gain = pd.Series(
    lgb_clf.booster_.feature_importance(importance_type='gain'),
    index=x_train.columns  # 컬럼명 인덱스로 설정
)
# print(xgb_gain)
# print(lgb_gain)

# 각 피처의 중요도를 전체 합 대비 비율(%)로 변환
# 0으로 나누기 방지 : xgb_gain.sum() != 0 조건 추가
xgb_gain_pct = 100 * xgb_gain / (xgb_gain.sum() if xgb_gain.sum() != 0 else 1)
lgb_gain_pct = 100 * lgb_gain / (lgb_gain.sum() if lgb_gain.sum() != 0 else 1)

# 사용하지 않은 피처 → 0으로 채움 (두 모델 컬럼 통일)
xgb_gain_pct = xgb_gain_pct.reindex(x_train.columns).fillna(0)
lgb_gain_pct = lgb_gain_pct.reindex(x_train.columns).fillna(0)

# 두 모델의 중요도를 하나의 DataFrame으로 합치기
comp_df = pd.DataFrame({
    'XGBoost (gain %)': xgb_gain_pct,
    'LightGBM (gain %)': lgb_gain_pct,
}).sort_values('XGBoost (gain %)', ascending=False)

print(comp_df.head(10))  # 중요 피처(변수) top-10

# 시각화
topk = 5                    # 상위 5개 피처만 시각화
top = comp_df.head(topk)[::-1]  # 내림차순 → 뒤집기 (barh는 아래서 위로 출력)

# 1행 2열 서브플롯 : XGBoost / LightGBM 나란히
fig, axes = plt.subplots(1, 2, figsize=(8, 5))

# 두 모델의 최대 중요도값 → x축 범위 통일 (공정한 비교)
xmax = float(np.ceil(top.max().max()))

# zip으로 axes와 컬럼명을 묶어서 반복
for ax, col in zip(axes, ['XGBoost (gain %)', 'LightGBM (gain %)']):
    ax.barh(top.index, top[col])                        # 수평 막대 그래프
    ax.set_title(f'{col.split()[0]} Feature importance') # 'XGBoost' or 'LightGBM'
    ax.set_xlabel('Importance (%)')
    ax.set_xlim(0, xmax)   # x축 범위 통일 → 두 모델 시각적으로 공정 비교

plt.tight_layout()
plt.show()

