"""
문4)직원별 관리 고객 수 출력 (관리 고객이 없으면 출력에서 제외)

직원번호 직원명 관리 고객 수
1 홍길동 3
2 한송이 1
"""
import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        sql = """
            select jikwonno, jikwonname, count(*) gogeksu
            from jikwon inner join gogek on jikwon.jikwonno=gogek.gogekdamsano
            group by jikwonno
            """
        cursor.execute(sql)
        datas = cursor.fetchall()
  
        print("직원번호 직원명 관리고객수")
        for jikwonno, jikwonname, gogeksu in datas:
            print(jikwonno, jikwonname, gogeksu)

    except Exception as e:
        print('err : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__=='__main__':
    chulbal()