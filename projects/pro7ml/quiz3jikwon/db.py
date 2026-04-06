import os
import pymysql

def get_conn():
    return pymysql.connect(
        host=os.getenv("DB_HOST", '127.0.0.1'),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PSW", "123"),
        database=os.getenv("DB_NAME", "test"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

def fetchall_jikwonpay() -> list[dict]:
    sql = "select jikwonpay as 연봉, jikwonjik as 직급, year(now())-year(jikwonibsail) as 근무년수 from jikwon"
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
    finally:
        conn.close()
