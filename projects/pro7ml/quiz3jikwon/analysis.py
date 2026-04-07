from sklearn.linear_model import LinearRegression   # summary()지원 안함
from sklearn.metrics import r2_score, mean_squared_error
import statsmodels.api
import pandas as pd
import numpy as np

def analysis_func(rdata:list[dict]):
    df = pd.DataFrame(rdata)
    # print(df)
    df = df.dropna(subset = ["연봉", "직급", "근무년수"]) 
    lm = LinearRegression().fit(df[['근무년수']], df['연봉'])
    rsquared = np.round(r2_score(df['연봉'], lm.predict(df[['근무년수']])) * 100, 2)
    intercept = np.round(lm.intercept_, 4)
    slope = np.round(lm.coef_[0], 4)
    return df, lm, rsquared, intercept, slope

def predict_func(year, model):
    pred = np.round(model.predict([[year]]).flatten(), 2)

    return pred[0]