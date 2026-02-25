"""
문2-1) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력
해당 직원이 근무하는 부서 내의 직원 전부를 직급별 오름차순으로 출력. 직급이 같으면 이름별 오름차순한다.
 
직원번호 입력 : _______
직원명 입력 : _______
직원번호 직원명 부서명 부서전화 직급 성별
1 홍길동 총무부 111-1111 이사 남
...
직원 수 :

이어서 로그인한 해당 직원이 관리하는 고객 자료도 출력한다.

고객번호 고객명 고객전화 나이
1 사오정 555-5555 34
관리 고객 수 :
"""
import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)  
def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        jik_no = input('직원 번호 입력 : ')
        jik_name = input('직원 이름 입력 : ')
        sql = """
            select jikwonno as 직원번호, jikwonname as 직원명,
            busername as 부서명, busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별
            from jikwon join buser on buser.buserno=jikwon.busernum
            where buserno=(select busernum from jikwon where jikwonno=%s and jikwonname=%s)
            order by field(jikwonjik, '사원', '대리', '과장', '부장'), jikwonname
            """
        cursor.execute(sql, (jik_no, jik_name))
        datas = cursor.fetchall()

        if len(datas) == 0:
            print("로그인 실패")
            return
        
        print("직원번호 직원명 부서명 부서전화 직급 성별")
        for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas:
            print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)
        print("사원 수 : ", len(datas))
        print()
        gsql="""
            select gogekno, gogekname, gogektel, year(now())-concat('19', substr(gogekjumin,1,2))
            from gogek
            where gogekdamsano=%s
        """
        cursor.execute(gsql, (jik_no,))
        datas = cursor.fetchall()
        if len(datas) == 0:
            print("담당 고객 없음")
            return
        print("고객번호 고객명 고객전화 나이")
        for gogekno, gogekname, gogektel, age in datas:
            print(gogekno, gogekname, gogektel, age)
        print("담당 고객 수 : ", len(datas))
    except Exception as e:
        print('err : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__=='__main__':
    chulbal()