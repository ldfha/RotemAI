create table sangdata(
code int primary key,
sang varchar(20),
su int,
dan INT); 

insert into sangdata values(1,'장갑',3,10000);
insert into sangdata values(2,'벙어리장갑',2,12000);
insert into sangdata values(3,'가죽장갑',10,50000);
insert into sangdata values(4,'가죽점퍼',5,650000);

create table buser(
buserno int primary key, 
busername varchar(10) not null,
buserloc varchar(10),
busertel varchar(15));

insert into buser values(10,'총무부','서울','02-100-1111');
insert into buser values(20,'영업부','서울','02-100-2222');
insert into buser values(30,'전산부','서울','02-100-3333');
insert into buser values(40,'관리부','인천','032-200-4444');

create table jikwon(
jikwonno int primary key,
jikwonname varchar(10) not null,
busernum int not null,
jikwonjik varchar(10) default '사원', 
jikwonpay int,
jikwonibsail date,
jikwongen varchar(4),
jikwonrating char(3),
CONSTRAINT ck_jikwongen check(jikwongen='남' or jikwongen='여'));

insert into jikwon values(1,'홍길동',10,'이사',9900,'2008-09-01','남','a');
insert into jikwon values(2,'한송이',20,'부장',8800,'2010-01-03','여','b');
insert into jikwon values(3,'이순신',20,'과장',7900,'2010-03-03','남','b');
insert into jikwon values(4,'이미라',30,'대리',4500,'2014-01-04','여','b');
insert into jikwon values(5,'이순라',20,'사원',3000,'2017-08-05','여','b');
insert into jikwon values(6,'김이화',20,'사원',2950,'2019-08-05','여','c');
insert into jikwon values(7,'김부만',40,'부장',8600,'2009-01-05','남','a');
insert into jikwon values(8,'김기만',20,'과장',7800,'2011-01-03','남','a');
insert into jikwon values(9,'채송화',30,'대리',5000,'2013-03-02','여','a');
insert into jikwon values(10,'박치기',10,'사원',3700,'2016-11-02','남','a');
insert into jikwon values(11,'김부해',30,'사원',3900,'2016-03-06','남','a');
insert into jikwon values(12,'박별나',40,'과장',7200,'2011-03-05','여','b');
insert into jikwon values(13,'박명화',10,'대리',4900,'2013-05-11','남','a');
insert into jikwon values(14,'박궁화',40,'사원',3400,'2016-01-15','여','b');
insert into jikwon values(15,'채미리',20,'사원',4000,'2016-11-03','여','a');
insert into jikwon values(16,'이유가',20,'사원',3000,'2016-02-01','여','c');
insert into jikwon values(17,'한국인',10,'부장',8000,'2006-01-13','남','c');
insert into jikwon values(18,'이순기',30,'과장',7800,'2011-11-03','남','a');
insert into jikwon values(19,'이유라',30,'대리',5500,'2014-03-04','여','a');
insert into jikwon values(20,'김유라',20,'사원',2900,'2019-12-05','여','b');
insert into jikwon values(21,'장비',20,'사원',2950,'2019-08-05','남','b');
insert into jikwon values(22,'김기욱',40,'대리',5850,'2013-02-05','남','a');
insert into jikwon values(23,'김기만',30,'과장',6600,'2015-01-09','남','a');
insert into jikwon values(24,'유비',20,'대리',4500,'2014-03-02','남','b');
insert into jikwon values(25,'박혁기',10,'사원',3800,'2016-11-02','남','a');
insert into jikwon values(26,'김나라',10,'사원',3500,'2016-06-06','남','b');
insert into jikwon values(27,'박하나',20,'과장',5900,'2012-06-05','여','c');
insert into jikwon values(28,'박명화',20,'대리',5200,'2013-06-01','여','a');
insert into jikwon values(29,'박가희',10,'사원',4100,'2016-08-05','여','a');
insert into jikwon values(30,'최미숙',30,'사원',4000,'2015-08-03','여','b');

create table gogek(
gogekno int primary key,
gogekname varchar(10) not null,
gogektel varchar(20),
gogekjumin char(14),
gogekdamsano int,
CONSTRAINT FK_gogekdamsano foreign key(gogekdamsano) references jikwon(jikwonno));

insert into gogek values(1,'이나라','02-535-2580','850612-1156777',5);
insert into gogek values(2,'김혜순','02-375-6946','700101-1054777',3);
insert into gogek values(3,'최부자','02-692-8926','890305-1065777',3);
insert into gogek values(4,'김해자','032-393-6277','770412-2028777',13);
insert into gogek values(5,'차일호','02-294-2946','790509-1062777',2);
insert into gogek values(6,'박상운','032-631-1204','790623-1023777',6);
insert into gogek values(7,'이분','02-546-2372','880323-2558777',2);
insert into gogek values(8,'신영래','031-948-0283','790908-1063777',5);
insert into gogek values(9,'장도리','02-496-1204','870206-2063777',4);
insert into gogek values(10,'강나루','032-341-2867','780301-1070777',12);
insert into gogek values(11,'이영희','02-195-1764','810103-2070777',3);
insert into gogek values(12,'이소리','02-296-1066','810609-2046777',9);
insert into gogek values(13,'배용중','02-691-7692','820920-1052777',1);
insert into gogek values(14,'김현주','031-167-1884','800128-2062777',11);
insert into gogek values(15,'송운하','02-887-9344','830301-2013777',2);

-- select : db 서버로부터 클라이언트로 자료를 읽는 명령
-- select 칼럼명 as 별명,...from 테이블명 where 조건 order by 기준키, ...
SELECT * FROM jikwon; 	-- 모든 칼럼 읽기
SELECT jikwonno, jikwonname FROM jikwon;
SELECT jikwonno, jikwongen, busernum, jikwonname FROM jikwon;	-- 순서는 선택 가능
SELECT jikwonno AS 직원번호, jikwonname AS 직원명 FROM jikwon;
SELECT 10, '안녕', 12 / 3 AS 결과 FROM DUAL;
SELECT jikwonname, jikwonpay, jikwonpay * 0.05 AS tax FROM jikwon;
SELECT jikwonname, CONCAT(jikwonname, '님') AS jikwonetc FROM jikwon;

-- 정렬(sort)
SELECT * FROM jikwon ORDER BY jikwonpay ASC;	-- 오름차순
SELECT * FROM jikwon ORDER BY jikwonpay DESC;	-- 내림차순
SELECT * FROM jikwon ORDER BY jikwonjik;
SELECT * FROM jikwon ORDER BY jikwonjik ASC, busernum DESC, jikwongen ASC, jikwonpay;
SELECT jikwonname, jikwonpay, jikwonpay / 100 * 100 AS pay FROM jikwon ORDER BY pay DESC;

-- 중복 배제
SELECT distinct jikwonjik FROM jikwon;
SELECT DISTINCT jikwonjik, jikwonname  FROM jikwon; -- X 중복 배제시엔 해당 칼럼 하나만 적어야함

-- 연산자 : () > 산술(* / > + -) > 관계(비교) > is null, like, in > between, not > and > or

SELECT * FROM jikwon WHERE jikwonjik='대리';
SELECT * FROM jikwon WHERE jikwonno=3;
SELECT * FROM jikwon WHERE jikwonibsail='2010-03-03';
SELECT * FROM jikwon WHERE jikwonno=5 OR jikwonno=7;
SELECT * FROM jikwon WHERE jikwonjik='사원'AND jikwongen='여' AND jikwonpay <= 3000;
SELECT * FROM jikwon WHERE jikwonjik='사원'AND (jikwongen='여' OR jikwonibsail >= '2017-01-01');

SELECT * FROM jikwon WHERE jikwonno >= 5 AND jikwonno <= 10;
SELECT * FROM jikwon WHERE jikwonno BETWEEN 5 AND 10;
SELECT * FROM jikwon WHERE jikwonibsail BETWEEN '2017-01-01' AND '2019-12-31';

SELECT * FROM jikwon WHERE jikwonno < 5 OR jikwonno > 20;
SELECT * FROM jikwon WHERE jikwonno NOT BETWEEN 5 AND 20;

SELECT * FROM jikwon WHERE jikwonpay > 5000;
SELECT * FROM jikwon WHERE jikwonpay > 2000 + 3000;

SELECT * FROM jikwon WHERE jikwonname = '홍길동';
SELECT * FROM jikwon WHERE jikwonname >= '박';
SELECT ASCII('a'), ASCII('A'), ASCII('가'), ASCII('나') FROM DUAL;
SELECT * FROM jikwon WHERE jikwonname BETWEEN '김' AND '이';

-- in 멤버 조건 연산
SELECT * FROM jikwon WHERE jikwonjik='대리' OR jikwonjik='과장' OR jikwonjik='부장';
SELECT * FROM jikwon WHERE jikwonjik IN('대리', '과장', '부장');
SELECT * FROM jikwon WHERE jikwonno IN(3, 12, 29);

-- like 조건 연산 : %(0개 이상의 문자열), _(한개 문자)
SELECT * FROM jikwon WHERE jikwonname LIKE '이%';
SELECT * FROM jikwon WHERE jikwonname LIKE '이순%';
SELECT * FROM jikwon WHERE jikwonname LIKE '%라';
SELECT * FROM jikwon WHERE jikwonname LIKE '이%라';

SELECT * FROM jikwon WHERE jikwonname LIKE '이__';
SELECT * FROM jikwon WHERE jikwonname LIKE '이_라';

SELECT * FROM jikwon WHERE jikwonname LIKE '__';

SELECT * FROM jikwon WHERE jikwonpay LIKE '3___';

SELECT * FROM gogek WHERE gogekjumin LIKE '_______1%';
SELECT * FROM gogek WHERE gogekjumin LIKE '%-1%';

-- is null
UPDATE jikwon SET jikwonjik=NULL WHERE jikwonno=5;
SELECT * FROM jikwon;
SELECT * FROM jikwon WHERE jikwonjik=NULL; 	-- X
SELECT * FROM jikwon WHERE jikwonjik IS NULL;

-- limit
SELECT * FROM jikwon LIMIT 3;
SELECT * FROM jikwon ORDER BY jikwonno DESC LIMIT 3;
SELECT * FROM jikwon LIMIT 5, 3;		-- (시작행, 갯수)

SELECT jikwonno AS 직원번호, jikwonname AS 직원명, jikwonjik AS 직급, 
	jikwonpay AS 연봉, jikwonpay / 12 AS 보너스, jikwonibsail AS 입사일 FROM jikwon 
	WHERE jikwonjik IN ('과장', '부장', '사원')
	AND jikwonpay >= 4000 AND jikwonibsail BETWEEN '2015-1-1' AND '2019-12-31'
	ORDER BY jikwonjik, jikwonpay DESC LIMIT 3;
	
-- 내장함수 : 데이터 조작의 효율성 증진이 목적
-- 단일 행 함수 : 각 행에 대해 작업한다. 행 단위 처리
-- 문자 함수
SELECT LOWER('Hello'), UPPER('Hello') FROM DUAL;
SELECT SUBSTR('hello world', 3), SUBSTR('hello world', 3, 3), SUBSTR('hello world', -3, 3) FROM DUAL;
SELECT LENGTH('hello world'), INSTR('hello world', 'e') FROM DUAL;
SELECT REPLACE('010.111.1234', '.', '-') FROM DUAL;
-- ...

-- jikwon 테이블에서 이름에 '이'가 포함된 직원이 있으면 '이'부터 두글자 출력하기
SELECT jikwonname, SUBSTR(jikwonname, INSTR(jikwonname, '이'), 2) FROM jikwon WHERE jikwonname LIKE('%이%');

-- 숫자 함수
SELECT ROUND(45.678, 2), ROUND(45.678), ROUND(45.678, 0), ROUND(45.678, -1) FROM DUAL;
SELECT jikwonname, jikwonpay, jikwonpay * 0.25 AS tax, ROUND(jikwonpay * 0.25, 0) FROM jikwon; 

SELECT TRUNCATE(45.678, 0), TRUNCATE(45.678, 1), TRUNCATE(45.678, -1) FROM DUAL;
SELECT MOD(15, 2), 15 / 2 FROM DUAL;
SELECT GREATEST(23, 25, 5, 1, 12), LEAST(23, 25, 5, 1, 12) FROM DUAL;

-- 날짜 함수
SELECT NOW(), NOW() + 2, SYSDATE(), CURDATE() FROM DUAL;
SELECT NOW(), SLEEP(3), NOW();				-- 하나의 query 내에서는 동일 값
SELECT SYSDATE(), SLEEP(3), SYSDATE();		-- 실행 시점값 출력

SELECT ADDDATE('2020-08-01', 3), ADDDATE('2020-08-01', -3), SUBDATE('2020-08-01', 3);
SELECT DATE_ADD(NOW(), INTERVAL 1 MINUTE),
DATE_ADD(NOW(),INTERVAL 5 DAY),
DATE_ADD(NOW(),INTERVAL 5 MONTH) FROM DUAL;

SELECT DATEDIFF(NOW(), '2025-5-5');

-- 형변환 함수
SELECT DATE_FORMAT(NOW(), '%Y%m%d'), DATE_FORMAT(NOW(), '%Y년%m월%d일');
SELECT jikwonname, jikwonibsail, DATE_FORMAT(jikwonibsail, '%W') FROM jikwon WHERE busernum=10;

SELECT STR_TO_DATE('2026-02-12', '%Y-%m-%d');
SELECT STR_TO_DATE('2026-02-12 13:16:34', '%Y-%m-%d %H:%i:%S');

-- 기타 함수
-- rank() : 순위 결정
SELECT jikwonno, jikwonname, jikwonpay,
RANK() OVER (ORDER BY jikwonpay) AS result,
DENSE_RANK() OVER (ORDER BY jikwonpay) AS result2
 FROM jikwon;

-- nvl(value1, value2) : value1이 null이면 value2를 취함
SELECT jikwonname, jikwonjik, nvl(jikwonjik, '임시직') FROM jikwon;

-- nvl2(value1, value2, value3) : value1이 null이 아니면 value2, null이면 value3 취함
SELECT jikwonname, jikwonjik, nvl2(jikwonjik, '정규직', '임시직') FROM jikwon;

-- nullif(value1, value2) : 두 개의 값이 일치하면 null, 아니면 value1 취함
SELECT jikwonname, jikwonjik, NULLIF(jikwonjik, '대리') FROM jikwon;

-- 조건 표현식
-- 형식1) CASE 표현식 WHEN 비교값1 THEN 결과값1 WHEN 비교값2 THEN 결과값2 … [ELSE 결과값n] END AS 별명
SELECT  case 10 / 5 when 5 then '안녕' when 2 then '반가워' ELSE '잘가' END AS 결과 FROM DUAL;
SELECT jikwonname, jikwonpay, jikwonjik,
case jikwonjik
when '이사' then jikwonpay * 0.05
when '부장' then jikwonpay * 0.04
when '과장' then jikwonpay * 0.03
else jikwonpay * 0.02
END donation FROM jikwon;

-- 형식2) 
-- case when 조건1 then 결과값1 when 조건2 then 결과값2 ... [else 결과값 n] END AS 별명
SELECT jikwonname, 
case when jikwongen='남' then '남성' 
when jikwongen='여' then '여성' 
END AS gender FROM jikwon;

SELECT jikwonname, jikwonpay,
case when jikwonpay >= 7000 then '우수연봉'
when jikwonpay >= 5000 then '보통연봉'
ELSE '저조' 
END AS result FROM jikwon WHERE jikwonjik IN ('대리', '과장');

-- if(조건) 참값, 거짓값 as 별명
SELECT jikwonname, jikwonpay, jikwonjik, 
TRUNCATE(jikwonpay/1000, 0)
FROM jikwon;
SELECT jikwonname, jikwonpay, jikwonjik, 
if(TRUNCATE(jikwonpay/1000, 0) >= 5, 'good', 'normal') AS result 
FROM jikwon;


SELECT * FROM jikwon;
-- 문제 1. 10년 이상 근무하면 '감사합니다', 그 외는 '열심히' 라고 표현 ( 2010 년 이후 직원만 참여 )
-- 특별수당(pay를 기준) : 10년 이상 5%, 나머지 3% (정수로 표시:반올림)

SELECT jikwonname AS 직원명, 
YEAR(NOW())-YEAR(jikwonibsail) AS 근무년수,
if(YEAR(NOW())-YEAR(jikwonibsail) >= 10, '감사합니다', '열심히') AS 표현,
if(YEAR(NOW())-YEAR(jikwonibsail) >= 10, ROUND(jikwonpay*0.05), ROUND(jikwonpay*0.03)) AS 특별수당
FROM jikwon WHERE jikwonibsail >= '2010-01-01';

-- 문제 2. 입사 후 8년 이상이면 왕고참, 5년 이상이면 고참, 3년 이상이면 보통, 나머지는 일반으로 표현
SELECT jikwonname AS 직원명, jikwonjik AS 직급,
DATE_FORMAT(jikwonibsail, '%Y.%m.%d') AS 입사년월일,
case
	when YEAR(NOW())-YEAR(jikwonibsail) >= 8 then '왕고참'
	when YEAR(NOW())-YEAR(jikwonibsail) >= 5 then '고참'
	when YEAR(NOW())-YEAR(jikwonibsail) >= 3 then '보통'
	ELSE '일반' END AS 구분,
case
	when busernum = 10 then '총무부'
	when busernum = 20 then '영업부'
	when busernum = 30 then '전산부'
	when busernum = 40 then '관리부'
	END AS 부서
FROM jikwon;

-- 문제3. 각 부서번호별로 실적에 따라 급여를 다르게 인상하려 한다. 
SELECT jikwonno AS 사번, jikwonname AS 직원명, busernum AS 부서, jikwonpay AS 연봉,
case
	when busernum = 10 then round(jikwonpay*1.1)
	when busernum = 30 then round(jikwonpay*1.2)
	ELSE jikwonpay
	END AS 인상연봉,
if(YEAR(NOW())-YEAR(jikwonibsail) >= 8, 'O', 'X')AS 장기근속
FROM jikwon;


-- 집계 함수(복수행 함수) : 전체 자료를 그룹별로 구분해 통계 결과를 얻기 위한 함수 
SELECT SUM(jikwonpay) AS 평균 FROM jikwon ;
SELECT MAX(jikwonpay) AS 최댓값, MIN(jikwonpay) AS 최솟값 FROM jikwon;

UPDATE jikwon SET jikwonpay=NULL WHERE jikwonno=5;
SELECT * FROM jikwon;

SELECT AVG(jikwonpay), AVG(nvl(jikwonpay ,0)) FROM jikwon;
SELECT SUM(jikwonpay) / 29, SUM(jikwonpay) / 30 FROM jikwon;

SELECT COUNT(jikwonno), COUNT(jikwonpay) FROM jikwon;
SELECT COUNT(*) AS 인원수 FROM jikwon;

SELECT STDDEV(jikwonpay) AS 표준편차, VAR_SAMP(jikwonpay) AS 분산 FROM jikwon;

SELECT COUNT(*) AS 인원, VAR_SAMP(jikwonpay) AS 분산 FROM jikwon WHERE busernum = 10;
SELECT COUNT(*) AS 인원, VAR_SAMP(jikwonpay) AS 분산 FROM jikwon WHERE busernum = 20;

-- 과장은 몇명?
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonjik='과장';
-- 2010년 이전에 입사한 남직원은 몇명?
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonibsail < '2010-01-01' AND jikwongen ='남';
-- 2015년 이후 입사한 여직원의 연봉합, 연봉평균, 인원수는?
SELECT SUM(jikwonpay) AS 연봉합, AVG(jikwonpay) AS 연봉평균, COUNT(*) AS 인원수 FROM jikwon WHERE jikwonibsail > '2015-01-01' AND jikwongen = '여';


-- group 함수 : group by 절 : 소계 출력
-- select 그룹칼럼명, 계산 함수, ... from 테이블명 where 조건 group by 그룹칼럼명 having 출력조건
-- 그룹 칼럼에 대해 order by 할 수 없다. 단, 출력 결과는 order by 가능

-- 성별 연봉 평균 인원수 출력
SELECT jikwongen, AVG(jikwonpay), COUNT(*) FROM jikwon GROUP BY jikwongen;

-- 부서별 연봉 합
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum;

-- 부서별 연봉 합 : 연봉합이 35,000 이상
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum HAVING SUM(jikwonpay) >= 35000;

-- 부서별 연봉 합 : 여성만
SELECT busernum, SUM(jikwonpay) FROM jikwon WHERE jikwongen='여' GROUP BY busernum;

-- 부서별 연봉 합 : 연봉합이 15,000 이상인 여성만
SELECT busernum, SUM(jikwonpay) AS paytotal FROM jikwon WHERE jikwongen='여' 
GROUP BY busernum HAVING paytotal >= 15000;

-- 주의
SELECT busernum, SUM(jikwonpay) FROM jikwon ORDER BY busernum GROUP BY busernum;
SELECT busernum, SUM(jikwonpay) FROM jikwon  GROUP BY busernum ORDER BY SUM(jikwonpay) DESC;


-- 문제
-- 1. 직급별 급여의 평균 (NULL인 직급 제외)
SELECT jikwonjik, AVG(nvl(jikwonpay, 0)) 
FROM jikwon WHERE jikwonjik IS NOT NULL 
GROUP BY jikwonjik; 

-- 2. 부장,과장에 대해 직급별 급여의 총합
SELECT jikwonjik, SUM(jikwonpay) 
FROM jikwon WHERE jikwonjik='부장' OR jikwonjik='과장' 
GROUP BY jikwonjik;

-- 3. 2015년 이전에 입사한 자료 중 년도별 직원수 출력
SELECT YEAR(jikwonibsail), COUNT(*)
FROM jikwon WHERE jikwonibsail < '2015-01-01'
GROUP BY YEAR(jikwonibsail);

-- 4. 직급별 성별 인원수, 급여합 출력 (NULL인 직급은 임시직으로 표현)
SELECT nvl(jikwonjik, '임시직'), jikwongen, COUNT(*), SUM(jikwonpay) 
FROM jikwon 
GROUP BY jikwonjik, jikwongen;

-- 5. 부서번호 10,20에 대한 부서별 급여 합 출력
SELECT busernum, SUM(jikwonpay) 
FROM jikwon WHERE busernum IN(10, 20)
GROUP BY busernum;

-- 6. 급여의 총합이 7000 이상인 직급 출력(NULL인 직급은 임시직으로 표현)
SELECT nvl(jikwonjik, '임시직'), SUM(jikwonpay) AS totalpay
FROM jikwon
GROUP BY jikwonjik HAVING totalpay >= 7000;

-- 7. 직급별 인원수, 급여합계를 구하되 인원수가 3명 이상인 직급만 출력(NULL인 직급은 임시직으로 표현)
SELECT nvl(jikwonjik, '임시직'), COUNT(*) AS inwon, SUM(jikwonpay) AS totalpay 
FROM jikwon 
GROUP BY jikwonjik HAVING inwon >= 3;


-- join !!! : 하나 이상의 테이블에서 원하는 자료 추출
-- 반드시 공통 칼럼이 필요
DESC buser;
DESC jikwon;
DESC gogek;

SELECT * FROM buser;
INSERT INTO buser(buserno, busername) VALUES(50, '기획실');

SELECT * FROM jikwon;
ALTER TABLE jikwon MODIFY busernum INT NULL;
UPDATE jikwon SET busernum=NULL WHERE jikwonno=5;

SELECT * FROM gogek;

SELECT test.jikwon.jikwonname FROM jikwon;
SELECT mytab.jikwonname FROM jikwon AS mytab;

-- cross join : 한 쪽 테이블의 모든 행과 다른 쪽 테이블의 모든 행을 조인하는 기능
SELECT jikwonname, busername FROM jikwon, buser;
SELECT jikwonname, busername FROM jikwon CROSS JOIN buser;

-- cross join 중 self join
SELECT a.jikwonname, b.jikwonname FROM jikwon a, jikwon b;

-- EQUI join : 조인 조건식에 '='을 사용. 두 테이블은 '같다' 조건으로 join
-- 대부분의 pk-fk join은 EQUI join
SELECT jikwonname, busername FROM jikwon, buser
WHERE jikwon.busernum = buser.buserno;

-- non-EQUI join : 조인 조건식에 '=' 이외의 관계 연산자 사용.
CREATE TABLE paygrade(grade INT PRIMARY KEY, lpay INT, hpay INT);
INSERT INTO paygrade VALUES(1, 0, 1999);
INSERT INTO paygrade VALUES(2, 2000, 2999);
INSERT INTO paygrade VALUES(3, 3000, 3999);
INSERT INTO paygrade VALUES(4, 4000, 4999);
INSERT INTO paygrade VALUES(5, 5000, 9999);
SELECT * FROM paygrade;

SELECT jiktab.jikwonname, jiktab.jikwonpay, paytab.grade 
FROM jikwon AS jiktab, paygrade AS paytab
WHERE jiktab.jikwonpay >= paytab.lpay AND jiktab.jikwonpay <= paytab.hpay;

-- inner join : 두 테이블을 조인할 때, 두 테이블에 모두 지정한 열의 데이터가 있는 경우만 추출
SELECT jikwonno, jikwonname, busername FROM jikwon, buser
WHERE busernum=buserno;	-- oracle에서 주로 사용

SELECT jtab.jikwonno, jtab.jikwonname, btab.busername FROM jikwon AS jtab, buser AS btab
WHERE jtab.busernum=btab.buserno;

SELECT jikwonno, jikwonname, busername FROM jikwon, buser
WHERE busernum=buserno AND jikwongen='남'; 
-- where조건에 join조건+record 제한 조건 - 가독성 떨어짐

SELECT jikwonno, jikwonname, busername 
FROM jikwon INNER JOIN buser ON busernum=buserno;

SELECT jikwonno, jikwonname, busername 
FROM jikwon INNER JOIN buser ON busernum=buserno
WHERE jikwongen='남';	-- ANSI

-- outer join : 두 테이블을 조인할 때 1개의 테이블에만 자료가 있어도 결과 추출
-- Left outer join
SELECT jikwonno, jikwonname, busername 
FROM jikwon, buser 
WHERE busernum=buserno(+); 	-- oracle용 : MariaDB X

SELECT jikwonno, jikwonname, busername 
FROM jikwon LEFT OUTER JOIN buser
ON busernum=buserno;

-- Right outer join
SELECT jikwonno, jikwonname, busername 
FROM jikwon, buser 
WHERE busernum(+)=buserno; 	-- oracle용 : MariaDB X

SELECT jikwonno, jikwonname, busername 
FROM jikwon RIGHT OUTER JOIN buser
ON busernum=buserno;

-- full outer join : MariaDB에서는 지원되지 않음
SELECT jikwonno, jikwonname, busername 
FROM jikwon FULL OUTER JOIN buser
ON busernum=buserno;		

SELECT jikwonno, jikwonname, busername 
FROM jikwon LEFT OUTER JOIN buser ON busernum=buserno
UNION
SELECT jikwonno, jikwonname, busername 
FROM jikwon RIGHT OUTER JOIN buser ON busernum=buserno;	
-- MariaDB의 FULL OUTER JOIN은 union 이용

SELECT jikwonno AS 직원번호, jikwonname AS 직원명, busername AS 부서명 
FROM jikwon INNER JOIN buser ON busernum=buserno
WHERE jikwongen='남' AND jikwonname LIKE '김%';

SELECT SUM(jikwonpay) AS hap, COUNT(*) AS COUNT
FROM jikwon INNER JOIN buser ON busernum=buserno
WHERE jikwongen='남';

SELECT * FROM gogek;	 -- buser table과는 join 불가(공통 칼럼 X)
SELECT * FROM jikwon;
SELECT * FROM buser;
-- 문제
-- 문1) 직급이 '사원' 인 직원이 관리하는 고객자료 출력
SELECT gogekname, jikwonname 
FROM gogek INNER JOIN jikwon ON gogekdamsano = jikwonno
WHERE jikwonjik='사원';

-- 문2) 직원별 고객 확보 수  -- GROUP BY 사용
SELECT jikwonname, COUNT(gogekname)
FROM jikwon LEFT OUTER JOIN gogek ON gogekdamsano=jikwonno
GROUP BY jikwonname;

-- 문3) 고객이 담당직원의 자료를 보고 싶을 때 
-- 즉, 고객명을 입력하면,  담당직원 자료 출력  


-- 문4) 직원명을 입력하면 관리고객 자료 출력

