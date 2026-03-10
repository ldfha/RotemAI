from flask import Flask, render_template, request, redirect, url_for, flash, session, get_flashed_messages
from dotenv import load_dotenv
import pymysql
import os

app = Flask(__name__)
app.secret_key = "abcdef123456"

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )


@app.get('/')
def root():
    return redirect(url_for("login_form"))


@app.get('/login')
def login_form():
    return render_template("login.html")


@app.post('/login')
def login_post():
    jikwonno_raw = (request.form.get("jikwonno") or "").strip()
    jikwonname = (request.form.get("jikwonname") or "").strip()

    if not jikwonno_raw.isdigit() or not jikwonname:
        flash("직원 번호는 숫자, 직원이름은 필수입니다.")
        return redirect(url_for("login_form"))

    jikwonno = int(jikwonno_raw)
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            # 로그인 확인
            cur.execute("""
                SELECT jikwonno, jikwonname
                FROM jikwon
                WHERE jikwonno = %s AND jikwonname = %s
            """, (jikwonno, jikwonname))
            me = cur.fetchone()

            if not me:
                flash("로그인 실패: 직원정보가 일치하지 않습니다.")
                return redirect(url_for("login_form"))

            # 로그인 성공 시 직원 목록 조회
            cur.execute("""
                SELECT 
                    jikwonno,
                    jikwonname,
                    busername,
                    jikwonjik,
                    jikwonpay,
                    YEAR(jikwonibsail) AS jikwonibsail_year
                FROM jikwon
                INNER JOIN buser
                    ON busernum = buserno
                ORDER BY jikwonno
            """)
            rows = cur.fetchall()

            # 세션 저장
            session["jikwonno"] = me["jikwonno"]
            session["jikwonname"] = me["jikwonname"]

            return render_template("jikwonlist.html", login_user=me, rows=rows)

    finally:
        conn.close()

@app.get("/gogek/<int:jikwonno>")
def gogek_list(jikwonno:int):
    if "jikwonno" not in session:
        flash("로그인 후 고객정보 이용하세요")
        return redirect(url_for("login_form"))

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""select gogekno, gogekname, gogektel
                        from gogek
                        where gogekdamsano = %s order by gogekno""",(jikwonno, ))
            customers = cur.fetchall()

            cur.execute("""
                        select jikwonname from jikwon
                        where jikwonno=%s""",(jikwonno,))
            emp = cur.fetchone()

        return render_template("gogek_list.html", customers=customers, empname=(emp["jikwonname"] if emp else ""), empno=jikwonno)
    finally:
        conn.close()

@app.get('/jikwons')
def jikwon_list():
    if "jikwonno" not in session:
        flash("로그인 후 사용하세요")
        return redirect(url_for("login_form"))

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    jikwonno,
                    jikwonname,
                    busername,
                    jikwonjik,
                    jikwonpay,
                    YEAR(jikwonibsail) AS jikwonibsail_year
                FROM jikwon
                INNER JOIN buser
                    ON busernum = buserno
                ORDER BY jikwonno
            """)
            rows = cur.fetchall()

            login_user = {"jikwonno":session["jikwonno"], "jikwonname":session["jikwonname"]}
            return render_template("jikwonlist.html", rows=rows, login_user=login_user)
    finally:
        conn.close()

@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_form"))

if __name__ == '__main__':
    app.run(debug=True)