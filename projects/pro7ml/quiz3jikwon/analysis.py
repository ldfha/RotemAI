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
    rsquared = r2_score(df['연봉'], df[['근무년수']])
    intercept = lm.intercept_
    slope = lm.coef_
    return df, lm, rsquared, intercept, slope[0]

def predict_func(year, model):
    pred = np.round(model.predict([[year]]).flatten(), 2)

    return pred[0]