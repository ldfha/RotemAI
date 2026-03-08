from flask import Flask, render_template, request, redirect, url_for, flash
# pip install pymysql
import pymysql
import os
from flask import get_flashed_messages  # 저장해둔 message를 꺼내는 함수
# flash("에러~") -> 메세지를 세션에 잠시 저장 후 get_flashed_messages()하면 메세지를 읽음
# flash : 임시 메세지 출력용 (내부적으로 session에 저장해 둠 - secret-key)

app = Flask(__name__);

app.secret_key = "abcdef123456" # session/flash를 위한 쿠키 서명용 비밀키

# MariaDB 연결 정보
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123")
DB_NAME = os.getenv("DB_NAME", "test")

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",   # 전 세계 문자(한글 포함) + 이모지 처리 가능
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )
# DictCursor : Select 결과를 Dict 타입 형태로 받게 해줌
# {'code':1,'sang':'마우스',...} -> row['code'], row['sang']

@app.get('/')
def root():
    return redirect(url_for("show_list"))

@app.get('/show')
def show_list():
    conn = get_conn()   # db와 연결
    try:
        # with문을 사용하면 cursor.close()를 안해줘도 됨
        with conn.cursor() as cur:
            cur.execute("select code, sang, su, dan from sangdata order by code")
            rows = cur.fetchall()

        messages = list(get_flashed_messages())
        return render_template("list.html", rows=rows, messages=messages)

    # except pymysql.err.IntegrityError as e:
        # ...
    except Exception as e:
            flash(f"DB 자료 읽기 오류 : {e}")
            return redirect(url_for("show_list"))
    finally:
        conn.close()

@app.get("/add")
def add_form():
    messages = list(get_flashed_messages())
    return render_template("add_form.html", messages=messages)  # 추가 form 호출

@app.post("/add")
def add_save():     # 추가 처리
    sang = (request.form.get("sang") or "").strip()
    su_raw = (request.form.get("su") or "").strip()
    dan_raw = (request.form.get("dan") or "").strip()
    if not sang or not su_raw.isdigit() or not dan_raw.isdigit():
        flash("sang은 필수, su/dan은 숫자만 허용")
        return redirect(url_for("add_form"))

    su = int(su_raw)    # 연산없이 추가이므로 숫자화 안해도 됨
    dan = int(dan_raw)

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # code는 자동증가 프로그래밍 하기
            cur.execute("select max(code) as max_code from sangdata")
            row = cur.fetchone()
            max_code = row["max_code"] if row else None
            next_code = max_code + 1 if max_code is not None else 1

            # db에 추가하기
            cur.execute("insert into sangdata(code,sang,su,dan) values(%s,%s,%s,%s)", (next_code,sang,su,dan))
        
        conn.commit()    
        return redirect(url_for("show_list"))
    except Exception as e:
        conn.rollback()
        flash(f"저장 실패 : {e}")
        return redirect(url_for("add_form"))
    finally:
        conn.close()

@app.get("/edit/<int:code>")
def edit_form(code:int):    # 수정 폼 호출
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("select * from sangdata where code=%s", (code,))
            row = cur.fetchone()
        if not row:
            flash("해당 자료가 없어요")
            return redirect(url_for("show_list"))
        
        messages = list(get_flashed_messages())
        return render_template("edit_form.html", row=row, messages=messages)
    except Exception as e:
        pass
    finally:
        conn.close()    

@app.post("/edit/<int:code>")
def edit_save(code:int):     # 수정 처리
    sang = (request.form.get("sang") or "").strip()
    su_raw = (request.form.get("su") or "").strip()
    dan_raw = (request.form.get("dan") or "").strip()
    if not sang or not su_raw.isdigit() or not dan_raw.isdigit():
        flash("sang은 필수, su/dan은 숫자만 허용")
        return redirect(url_for("edit_form", code=code))

    su = int(su_raw)    # 연산없이 추가이므로 숫자화 안해도 됨
    dan = int(dan_raw)

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # db에 수정하기
            cur.execute("update sangdata set sang=%s,su=%s,dan=%s where code=%s", (sang,su,dan,code))
        
        conn.commit()    
        return redirect(url_for("show_list"))
    except Exception as e:
        conn.rollback()
        flash(f"수정 실패 : {e}")
        return redirect(url_for("edit_form", code=code))
    finally:
        conn.close()

@app.post("/delete/<int:code>")
def delete_row(code:int):   # 삭제하기
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # db에 수정하기
            cur.execute("delete from sangdata where code=%s", (code,))
        
        conn.commit()    
        return redirect(url_for("show_list"))
    except Exception as e:
        conn.rollback()
        flash(f"삭제 실패 : {e}")
        return redirect(url_for("show_list"))
    finally:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)