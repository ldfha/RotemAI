from flask import Flask, render_template, request
import pymysql
import pandas as pd
import numpy as np
from markupsafe import escape
import matplotlib.pyplot as plt
import koreanize_matplotlib


app = Flask(__name__)

db_config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8mb4'
}

def get_conn():
    return pymysql.connect(**db_config)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dbshow', methods=['GET','POST'])
def dbshow():
    dept = request.args.get("dept", "").strip()

    sql = """
        select j.jikwonno as 직원번호, j.jikwonname as 직원명, b.busername as 부서명,
        j.jikwonpay as 연봉, j.jikwonjik as 직급, year(now())-year(j.jikwonibsail) as 근무년수, j.jikwongen as 성별
        from jikwon j
        inner join buser b on j.busernum=b.buserno
        order by j.busernum, 직원명
    """
    # SQL 실행
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            cols = [ c[0] for c in cur.description ]
    df = pd.DataFrame(rows, columns=cols)
    print(df.head(3))

    # 직원 정보 html로 전송
    if not df.empty:
        jikwondata = df[['직원번호','직원명','부서명','연봉','직급','근무년수']]
    else:
        jikwondata = "직원 정보가 없어요"
    jikwondata=jikwondata.to_html(index=False)

    # 부서명, 직급별 연봉 통계
    if not df.empty:
        stats_df = pd.pivot_table(df,
                index=['부서명','직급'],
                values='연봉',
                aggfunc=['sum','mean'])
        statsdata=stats_df.to_html()
    else:
        statsdata = "통계 정보가 없어요"

    # 부서명별 연봉합, 평균 세로막대 그래프
    dept_df = (
            df.groupby('부서명')['연봉']
            .agg(
                연봉합 = 'sum',
                평균 = 'mean',
            )
        )
    print(dept_df.columns)
    # dept_df.plot(kind='bar')
    img_src = 'static/img/plot_image.png'
    # plt.savefig(img_src)
    # plt.close()
    # 성별, 직급별 빈도표
    ctab = pd.crosstab(df['성별'], df['직급'])
    ctab = ctab.to_html()

    # 부서별 최고 연봉자 출력(부서명, 직원명, 연봉)
    result = df.loc[df.groupby('부서명')['연봉'].idxmax(), ['부서명', '직원명', '연봉']]
    result = result.to_html()

    # 부서별 직원 비율
    total = df['직원번호'].count()
    dept_count = df.groupby('부서명')['직원번호'].agg('count')
    dept_ratio = (dept_count / total * 100).round(2)
    dept_ratio.name='비율'
    dept_ratio = dept_ratio.to_frame().to_html()

    return render_template("dbshow.html", 
                           dept=escape(dept),   # xss 방지
                           jikwondata=jikwondata,
                           statsdata=statsdata,
                           img_src=img_src,
                           ctab=ctab,
                           result=result,
                           dept_ratio=dept_ratio
                        )

if __name__=='__main__':
    app.run(debug=True)