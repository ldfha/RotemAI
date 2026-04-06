from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from markupsafe import escape
from db import get_conn, fetchall_jikwonpay
from analysis import analysis_func, predict_func

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dbshow')
def dbshow():
    year = request.args.get("year", "").strip()
    year = int(year)
    # print(year, type(year))
    
    rdata = fetchall_jikwonpay()
    # print(rdata)
    df, models, rsquared, intercept, slope = analysis_func(rdata)
    # print(rsquared, intercept, slope)
    
    # 예측
    result = predict_func(year, models)
    # print(result)

    # 직급별 연봉평균
    avg_df = df.groupby("직급")["연봉"].mean().reset_index()
    avg_df['연봉'] = np.round(avg_df['연봉'], 2)
    print(avg_df)

    return jsonify({
        "result": result,
        "rsquared": rsquared,
        "intercept": intercept,
        "slope": slope,
        "avg_df": avg_df.to_dict(orient="records")
    })    



# #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   연봉      30 non-null     int64
#  1   직급      30 non-null     str
#  2   근무년수    30 non-null     int64

#     # 직원 정보 html로 전송
#     if not df.empty:
#         jikwondata = df[['직원번호','직원명','부서명','연봉','직급','근무년수']]
#     else:
#         jikwondata = "직원 정보가 없어요"
#     jikwondata=jikwondata.to_html(index=False)

#     # 부서명, 직급별 연봉 통계
#     if not df.empty:
#         stats_df = pd.pivot_table(df,
#                 index=['부서명','직급'],
#                 values='연봉',
#                 aggfunc=['sum','mean'])
#         statsdata=stats_df.to_html()
#     else:
#         statsdata = "통계 정보가 없어요"

#     # 부서명별 연봉합, 평균 세로막대 그래프
#     dept_df = (
#             df.groupby('부서명')['연봉']
#             .agg(
#                 연봉합 = 'sum',
#                 평균 = 'mean',
#             )
#         )
#     print(dept_df.columns)
#     # dept_df.plot(kind='bar')
#     img_src = 'static/img/plot_image.png'
#     # plt.savefig(img_src)
#     # plt.close()
#     # 성별, 직급별 빈도표
#     ctab = pd.crosstab(df['성별'], df['직급'])
#     ctab = ctab.to_html()

#     # 부서별 최고 연봉자 출력(부서명, 직원명, 연봉)
#     result = df.loc[df.groupby('부서명')['연봉'].idxmax(), ['부서명', '직원명', '연봉']]
#     result = result.to_html()

#     # 부서별 직원 비율
#     total = df['직원번호'].count()
#     dept_count = df.groupby('부서명')['직원번호'].agg('count')
#     dept_ratio = (dept_count / total * 100).round(2)
#     dept_ratio.name='비율'
#     dept_ratio = dept_ratio.to_frame().to_html()

#     return render_template("dbshow.html", 
#                            dept=escape(dept),   # xss 방지
#                            jikwondata=jikwondata,
#                            statsdata=statsdata,
#                            img_src=img_src,
#                            ctab=ctab,
#                            result=result,
#                            dept_ratio=dept_ratio
#                         )

if __name__=='__main__':
    app.run(debug=True)