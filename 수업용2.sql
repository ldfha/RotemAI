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
SELECT jikwonno AS 사번, jikwonname AS 직원명, jikwonjik AS 직급, gogekname AS 고객명, gogektel AS 고객전화,
if(gogekjumin LIKE '%-1%', '남', '여') AS 고객성별
FROM gogek INNER JOIN jikwon ON gogekdamsano = jikwonno
WHERE jikwonjik='사원';

SELECT jikwonno AS 사번, jikwonname AS 직원명, jikwonjik AS 직급, gogekname AS 고객명, gogektel AS 고객전화,
CASE
	when SUBSTR(gogekjumin,8,1) IN('1','3') then '남'
	when SUBSTR(gogekjumin,8,1) IN('2','4') then '여' 
END AS 고객성별
FROM gogek INNER JOIN jikwon ON gogekdamsano = jikwonno
WHERE jikwonjik='사원';

-- 문2) 직원별 고객 확보 수  -- GROUP BY 사용
SELECT jikwonno as 사번, jikwonname AS 직원명, COUNT(gogekname) AS 고객수
FROM jikwon LEFT OUTER JOIN gogek ON gogekdamsano=jikwonno
GROUP BY jikwonno;

-- 문3) 고객이 담당직원의 자료를 보고 싶을 때 
-- 즉, 고객명을 입력하면,  담당직원 자료 출력  
SELECT jikwonname AS 직원명, jikwonjik AS 직급 
FROM jikwon INNER JOIN gogek ON gogekdamsano=jikwonno 
WHERE gogekname='강나루';

-- 문4) 직원명을 입력하면 관리고객 자료 출력
SELECT gogekname AS 고객명, gogektel AS 고객전화, gogekjumin AS 주민번호,
YEAR(NOW())-CONCAT('19', SUBSTR(gogekjumin, 1, 2)) +1 AS 나이
FROM gogek INNER JOIN jikwon ON gogekdamsano=jikwonno
WHERE jikwonname='이순신';

SELECT gogekname AS 고객명, gogektel AS 고객전화, gogekjumin AS 주민번호,
timestampdiff(YEAR, date_format(SUBSTR(gogekjumin, 1, 6), '%y%m%d'), NOW()) AS 나이
FROM gogek INNER JOIN jikwon ON gogekdamsano=jikwonno
WHERE jikwonname='이순신';

-- 세 개의 테이블 join
-- 고객과 부서는 조인 불가 (공통 칼럼 없음)
SELECT jikwonname, busername, gogkename FROM jikwon, buser, gogek
WHERE busernum=buserno AND jikwonno=gogekdamsano;

SELECT jikwonname, busername, gogekname
FROM jikwon INNER JOIN buser ON buserno=busernum
INNER JOIN gogek ON gogekdamsano=jikwonno;

-- join 연습 2
-- 문1) 총무부에서 관리하는 고객수 출력 (고객 30살 이상만 작업에 참여)
SELECT busername, COUNT(gogekname)
FROM jikwon INNER JOIN buser ON buserno=busernum
INNER JOIN gogek ON gogekdamsano=jikwonno
WHERE busername='총무부' 
AND timestampdiff(YEAR, date_format(SUBSTR(gogekjumin, 1, 6), '%y%m%d'), NOW()) >= 30
GROUP BY busername;
 

-- 문2) 부서명별 고객 인원수 (부서가 없으면 "무소속")
SELECT nvl(busername, '무소속'), COUNT(gogekname)
FROM jikwon left OUTER JOIN buser ON buserno=busernum
INNER JOIN gogek ON gogekdamsano=jikwonno
GROUP BY buserno;

-- 문3) 고객이 담당직원의 자료를 보고 싶을 때 즉, 고객명을 입력하면  담당직원 자료 출력  
SELECT jikwonname AS 직원명, jikwonjik AS 직급, busername AS 부서명, busertel AS 부서전화, jikwongen AS 성별
FROM jikwon INNER JOIN buser ON buserno=busernum
INNER JOIN gogek ON gogekdamsano=jikwonno
WHERE gogekname='강나루';

-- 문4) 부서와 직원명을 입력하면 관리고객 자료 출력
SELECT gogekname AS 고객명, gogektel AS 고객전화, if(gogekjumin LIKE '______-1%', '남', '여') AS 성별
FROM jikwon INNER JOIN buser ON buserno=busernum
INNER JOIN gogek ON gogekdamsano=jikwonno
WHERE busername='영업부' AND jikwonname='이순신';


-- union
-- 테이블 2개 만들기
CREATE TABLE pum1(bun INT, pummok VARCHAR(20));
INSERT INTO pum1 VALUES(1,'귤'); 
INSERT INTO pum1 VALUES(2,'한라봉');
INSERT INTO pum1 VALUES(3,'바나나'); 
SELECT * FROM pum1; 

CREATE TABLE pum2(mum INT, sangpum VARCHAR(20));
INSERT INTO pum2 VALUES(10,'토마토'); 
INSERT INTO pum2 VALUES(20,'딸기');
INSERT INTO pum2 VALUES(30,'참외'); 
INSERT INTO pum2 VALUES(40,'수박'); 
SELECT * FROM pum2; 

-- union: 구조가 일치하는 두개 이상의 테이블 자료 합쳐 출력, 원래의 테이블 계속 유지
SELECT bun AS 번호, pummok AS 품명 FROM pum1 
UNION SELECT mum,sangpum FROM pum2;


-- subquery : 쿼리 내에 있는 쿼리가 있는 형태(주로 안쪽 결과를 바깥쪽에서 참조)
-- 다른 테이블의 결과를 조건으로 쓰고 싶을 때
-- 계산된 값을 이용하고 싶을 때
-- 복잡한 조건을 단계적으로 나눠 처리하고 싶을 때

-- where 안에 있는 subquery
-- 예1) '이미라' 직원과 직급이 같은 직원 출력
SELECT jikwonjik FROM jikwon WHERE jikwonname='이미라';	-- 대리
SELECT * FROM jikwon WHERE jikwonjik='대리';

-- 두번 처리하지 말고 한번에
SELECT * FROM jikwon WHERE jikwonjik=(SELECT jikwonjik FROM jikwon WHERE jikwonname='이미라')

-- 예2) 직급이 대리 중에서 가장 먼저 입사한 직원 출력
-- 답은 같지만 오답
SELECT * FROM jikwon WHERE jikwonibsail=(SELECT MIN(jikwonibsail) FROM jikwon WHERE jikwonjik='대리');
-- 정답
SELECT * FROM jikwon WHERE jikwonjik='대리' AND jikwonibsail=(SELECT MIN(jikwonibsail) FROM jikwon WHERE jikwonjik='대리');

-- 예3) 인천에서 근무하는 직원 출력
SELECT * FROM jikwon
WHERE busernum=(SELECT buserno FROM buser WHERE buserloc='인천');

-- 예4) 인천 이외에 근무하는 직원 출력
-- err : subquery return 값이 1개 이상
SELECT * FROM jikwon
WHERE busernum=(SELECT buserno FROM buser WHERE NOT buserloc='인천');

-- sol1) IN
SELECT * FROM jikwon
WHERE busernum IN (SELECT buserno FROM buser WHERE NOT buserloc='인천');
-- sol2) 받은 결과를 부정
SELECT * FROM jikwon
WHERE busernum <>(SELECT buserno FROM buser WHERE buserloc='인천');

-- 예5) 고객 중 차일호와 나이가 같은 자료 출력
SELECT * FROM gogek
WHERE SUBSTR(gogekjumin, 1, 2)=
(SELECT SUBSTR(gogekjumin, 1, 2) FROM gogek WHERE gogekname='차일호');


-- subquery 연습 문제
-- 문1) 2010년 이후에 입사한 남자 중 급여를 가장 많이 받는 직원은?
SELECT * FROM jikwon
WHERE jikwongen='남' AND jikwonpay=(
	SELECT MAX(jikwonpay) 
	FROM jikwon 
	WHERE jikwongen='남' AND jikwonibsail > '2010-01-01');
	
-- 정답
SELECT * FROM jikwon
WHERE jikwonibsail >= '2010-01-01' AND jikwongen='남' AND jikwonpay=(
	SELECT MAX(jikwonpay) 
	FROM jikwon 
	WHERE jikwongen='남' AND jikwonibsail >= '2010-01-01');

-- 문2)  평균급여보다 급여를 많이 받는 직원은?
SELECT * FROM jikwon
WHERE jikwonpay > (
	SELECT avg(jikwonpay)
	FROM jikwon
);
 

-- 문3) '이미라' 직원의 입사 이후에 입사한 직원은?
SELECT * FROM jikwon
WHERE jikwonibsail >= (
	SELECT jikwonibsail
	FROM jikwon
	WHERE jikwonname='이미라'
);
 

-- 문4) 2010 ~ 2015년 사이에 입사한 총무부(10),영업부(20),전산부(30) 직원 중 급여가 가장 적은 사람은?
-- (직급이 NULL인 자료는 작업에서 제외)
SELECT * FROM jikwon
WHERE jikwonibsail BETWEEN '2010-01-01' 
	AND '2015-12-31' AND jikwonjik IS NOT NULL AND busernum IN (10, 20, 30) 
	AND jikwonpay=(
		SELECT MIN(jikwonpay)
		FROM jikwon
		WHERE jikwonibsail BETWEEN '2010-01-01' AND '2015-12-31' 
		AND busernum IN (10, 20, 30)
);
 

-- 문5) 한송이, 이순신과 직급이 같은 사람은 누구인가?
SELECT * FROM jikwon
WHERE jikwonjik IN (
	SELECT jikwonjik
	FROM jikwon
	WHERE jikwonname='한송이' OR jikwonname='이순신'
);

SELECT * FROM jikwon
WHERE jikwonjik IN (
	SELECT jikwonjik
	FROM jikwon
	WHERE jikwonname IN ('한송이','이순신')
);

-- 문6) 과장 중에서 최대급여, 최소급여를 받는 사람은?
SELECT * FROM jikwon
WHERE jikwonjik='과장' 
AND (
	jikwonpay=(SELECT MAX(jikwonpay) FROM jikwon WHERE jikwonjik='과장')
	OR
	jikwonpay=(SELECT MIN(jikwonpay) FROM jikwon WHERE jikwonjik='과장')
); 

SELECT * FROM jikwon
WHERE jikwonjik='과장' 
AND (jikwonpay IN ((SELECT MAX(jikwonpay) FROM jikwon WHERE jikwonjik='과장'),
(SELECT MIN(jikwonpay) FROM jikwon WHERE jikwonjik='과장'))
);

-- 문7) 10번 부서의 최소급여보다 많은 사람은?
SELECT * FROM jikwon
WHERE jikwonpay > (
	SELECT MIN(jikwonpay)
	FROM jikwon
	WHERE busernum=10
);

-- 문8) 30번 부서의 평균급여보다 급여가 많은 '대리' 는 몇명인가?
SELECT COUNT(*) FROM jikwon
WHERE jikwonjik='대리'AND jikwonpay > (
	SELECT avg(jikwonpay) 
	FROM jikwon
	WHERE busernum=30
);
 

-- 문9) 고객을 확보하고 있는 직원들의 이름, 직급, 부서명을 입사일 별로 출력하라.
SELECT jikwonname AS 이름, jikwonjik AS 직급, busername AS 부서명
FROM jikwon INNER JOIN buser ON buserno=busernum
WHERE jikwonno IN (
	SELECT gogekdamsano
	FROM gogek)
ORDER BY jikwonibsail;
 
SELECT DISTINCT jikwonname AS 이름, jikwonjik AS 직급, busername AS 부서명
FROM jikwon INNER JOIN buser ON buserno=busernum
INNER JOIN gogek ON gogekdamsano=jikwonno
ORDER BY jikwonibsail;

SELECT jikwonname AS 이름, jikwonjik AS 직급, busername AS 부서명
FROM jikwon LEFT OUTER JOIN buser ON buserno=busernum
WHERE jikwonno IN (
	SELECT DISTINCT gogekdamsano
	FROM gogek)
ORDER BY jikwonibsail;

-- 문10) 이순신과 같은 부서에 근무하는 직원과 해당 직원이 관리하는 고객 출력
-- (고객은 나이가 30 이하면 '청년', 50 이하면 '중년', 그 외는 '노년'으로 표시하고, 고객 연장자 부터 출력)
SELECT * 
FROM gogek 
WHERE gogekdamsano IN (
	SELECT jikwonno
	FROM jikwon
	WHERE busernum=(
		SELECT busernum
		FROM jikwon
		WHERE jikwonname='이순신')
);

SELECT * 
FROM gogek INNER JOIN jikwon ON gogekdamsano=jikwonno
WHERE busernum = (
	SELECT buserno 
	FROM buser INNER JOIN jikwon ON busernum=buserno
	WHERE jikwonname='이순신'
);

SELECT jikwonname AS 직원명, busername AS 부서명, busertel AS 부서전화, jikwonjik AS 직급, gogekname AS 고객명, gogektel AS 고객전화, 
case 
	when (2026- (1900 + SUBSTR(gogekjumin, 1, 2))) <= 30 then '청년' 
	when (2026- (1900 + SUBSTR(gogekjumin, 1, 2))) <= 50 then '중년' 
	when (2026- (1900 + SUBSTR(gogekjumin, 1, 2))) > 50 then '노년' 
	ELSE '없음' 
END AS '고객구분' 
FROM jikwon INNER JOIN buser ON busernum = buserno 
INNER JOIN gogek ON jikwonno = gogekdamsano 
WHERE busernum = (SELECT busernum FROM jikwon WHERE jikwonname = '이순신') 
ORDER BY (2026- (1900 + SUBSTR(gogekjumin, 1, 2))) DESC;

-- 쿼리문은 동일한 결과를 여러 방법으로 수행 가능
-- 총무부에 근무하는 직원들이 관리하는 고객 출력
-- subquery 이용
SELECT gogekno, gogekname, gogektel FROM gogek
WHERE gogekdamsano IN (
	SELECT jikwonno 
	FROM jikwon 
	WHERE busernum=(
		SELECT buserno 
		FROM buser 
		WHERE busername='총무부'));
		
-- join 사용
SELECT gogekno, gogekname, gogektel FROM gogek
INNER JOIN jikwon ON jikwon.jikwonno=gogek.gogekdamsano
INNER JOIN buser ON jikwon.busernum=buser.buserno
WHERE busername='총무부';

-- and, all 연산자 : null 인 자료는 제외하고 작업한다.
-- < any : subquery의 반환값 중 최대값보다 작은 ~ 	<= 도 가능
-- > any : subquery의 반환값 중 최소값보다 큰 ~ 	>= 도 가능
-- < all : subquery의 반환값 중 최소값보다 작은 ~ 
-- > all : subquery의 반환값 중 최대값보다 큰 ~ 	

-- '대리'의 최대값보다 작은 연봉을 받는 직원은?
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon
WHERE jikwonpay < ANY (SELECT jikwonpay FROM jikwon WHERE jikwonjik='대리');

-- 30번 부서의 최고 연봉자 보다 연봉을 많이 받는 직원은?
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon
WHERE jikwonpay > ALL (SELECT jikwonpay FROM jikwon WHERE busernum=30);

-- 30번 부서의 최저 연봉자 보다 연봉을 많이 받는 직원은?
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon
WHERE jikwonpay > ANY (SELECT jikwonpay FROM jikwon WHERE busernum=30);

-- exists 연산자
-- 직원이 있는 부서 출력
SELECT busername, buserloc FROM buser bu
WHERE EXISTS(SELECT 'imsi' FROM jikwon WHERE jikwon.busernum=bu.buserno); -- true 반환

-- 직원이 없는 부서 출력
SELECT busername, buserloc FROM buser bu
WHERE NOT EXISTS(SELECT 'imsi' FROM jikwon WHERE jikwon.busernum=bu.buserno);	-- false 반환

-- from 절에 사용하는 subquery
-- 전체 평균 연봉과 최대 연봉 사이의 연봉을 받는 직원 출력
SELECT jikwonno, jikwonname, jikwonpay 
FROM jikwon a, (SELECT AVG(jikwonpay) avgs, MAX(jikwonpay) maxs FROM jikwon) b
WHERE a.jikwonpay BETWEEN b.avgs AND b.maxs;

-- group by의 having 절에 포함된 subquery
-- 부서별 평균 연봉 중 30번 부서의 평균 연봉보다 큰 자료(부서) 출력
SELECT busernum, AVG(jikwonpay) FROM jikwon
GROUP BY busernum 
HAVING AVG(jikwonpay) > (SELECT AVG(jikwonpay) FROM jikwon WHERE busernum=30);

-- 상관 subquery : outer query의 각 행을 inner query에서 참조하여 수행하는 서브 쿼리
-- 안쪽 질의에서 바깥쪽 질의를 참조하고, 다시 안쪽의 결과를 바깥쪽 질의에서 참조하는 형태
-- 각 부서의 최대 연봉자는?
SELECT * FROM jikwon a
WHERE a.jikwonpay=(SELECT MAX(b.jikwonpay) FROM jikwon b WHERE a.busernum=b.busernum);

-- 연봉 순위 3위 이내의 직원 출력(descending)
SELECT a.jikwonno, a.jikwonname, a.jikwonpay FROM jikwon a
WHERE 3 > (SELECT COUNT(*) FROM jikwon b WHERE b.jikwonpay > a.jikwonpay)
AND jikwonpay IS NOT NULL ORDER BY jikwonpay DESC;

-- subquery를 이용한 table 생성 및 insert 수행
CREATE TABLE jiktab1 AS SELECT * FROM jikwon;	-- jikwon과 동일 테이블 생성, pk는 제외
DESC jiktab1;
SELECT * FROM jiktab1;

CREATE TABLE jiktab2 AS SELECT * FROM jikwon WHERE 1=0;	-- jikwon과 동일 구조의 테이블 생성
DESC jiktab2;
SELECT * FROM jiktab2;

-- insert + subquery
INSERT INTO jiktab2 SELECT * FROM jikwon WHERE jikwonjik='과장';
INSERT INTO jiktab2(jikwonno, jikwonname, busernum) SELECT jikwonno, jikwonname, busernum FROM jikwon WHERE jikwonjik='대리';

-- update + subquery
SELECT * FROM jiktab1;
UPDATE jiktab1 SET jikwonjik=(SELECT jikwonjik FROM jikwon WHERE jikwonname='이순신')
WHERE jikwonno=2;
SELECT * FROM jiktab1;

-- delete + subquery
DELETE FROM jiktab1 WHERE jikwonno IN (SELECT DISTINCT gogekdamsano FROM gogek);
SELECT * FROM jiktab1;

-- 트랜잭션 : DB의 상태를 변경시키는 논리적인 작업 단위
-- 트랜잭션의 4가지 특징 : ACID
-- insert, update, delete 시 트랜잭션 시작됨
-- commit, rollback으로 트랜잭션 종료함
-- 서버종료, 타임아웃 등이 발생해도 트랜잭션 종료함

SHOW VARIABLES LIKE 'autocommit%';		-- autocommit 설정 확인
SET autocommit = TRUE	-- autocommit 설정
SET autocommit = FALSE	-- autocommit 해제
-- autocommit 해제 이후 마지막에는 반드시 설정으로 바꿔놔야 한다. 그렇지 않으면 데드락

-- 트랜잭션 연습
CREATE TABLE jiktab3 AS SELECT * FROM jikwon;	-- 연습용 테이블


-- 연습1
SET autocommit = FALSE;
DELETE FROM jiktab3 WHERE jikwonno=2;	-- 트랜잭션 시작
SELECT * FROM jiktab3;
-- ROLLBACK;	-- 트랜잭션 종료
COMMIT;
SELECT * FROM jiktab3;
SET autocommit = TRUE;

-- 연습2 : savepoint(저장점)를 이용해 부분적인 트랜잭션 처리 가능
SET autocommit = FALSE;
SELECT * FROM jiktab3 WHERE jikwonno=4;
UPDATE jiktab3 SET jikwonpay=7777 WHERE jikwonno=4;	-- 트랜잭션 시작
SAVEPOINT a;
UPDATE jiktab3 SET jikwonpay=8888 WHERE jikwonno=5;
SELECT * FROM jiktab3 WHERE jikwonno=4 or jikwonno=5;
ROLLBACK TO SAVEPOINT a;	-- 부분 작업 취소 : 트랜잭션 종료 X
SELECT * FROM jiktab3 WHERE jikwonno=4 or jikwonno=5;
ROLLBACK;	-- 전체 작업 취소 : 트랜잭션 종료
SELECT * FROM jiktab3 WHERE jikwonno=4 or jikwonno=5;

UPDATE jiktab3 SET jikwonpay=9999 WHERE jikwonno=5;	-- 트랜잭션 시작
COMMIT;	-- 트랜잭션 종료
SET autocommit = TRUE;
SHOW VARIABLES LIKE 'autocommit%';

-- 교착상태(Deadlock) : 두 개 이상의 트랜젝션이 서로 상대방이 가진 락(lock)을 기다리면서 영원히 진행하지 못하는 상태
-- 해결책은 트랜잭션을 수행완료 또는 취소하는 것
-- 일관성 유지가 둥요
SET autocommit = FALSE;
SELECT * FROM jiktab3 WHERE jikwonno=7;
UPDATE jiktab3 SET jikwonpay=1234 WHERE jikwonno=7;	-- 트랜잭션 시작
SELECT * FROM jiktab3 WHERE jikwonno=7;
COMMIT;


-- view 파일 
-- 물리적인 테이블을 근거로 select문(조건 포함)을 파일로 저장하여, 가상의 테이블로 사용한다.
-- 물리적인 테이블이 아니므로 메모리 소모가 거의 없다.
-- 복잡하고 긴 쿼리문을 단순화 가능, 보안 강화, 자료의 독립성 확보
-- 형식 : create or replace view 뷰파일명 as select문
--			 alter view 뷰파일명 ...
--			 drop view 뷰파일명 

SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonibsail < '2010-12-31';

CREATE OR REPLACE VIEW v_a AS
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonibsail < '2010-12-31';
SHOW TABLES;
SELECT * FROM v_a;
DESC v_a;

SHOW FULL TABLES IN test WHERE table_type LIKE 'VIEW';	-- view file 목록 확인
SELECT SUM(jikwonpay) AS 연봉합 FROM v_a;

CREATE VIEW v_b AS SELECT * FROM jikwon 
WHERE jikwonname LIKE '김%' OR jikwonname LIKE '이%'  OR jikwonname LIKE '박%';
SELECT * FROM v_b;

ALTER TABLE jikwon RENAME kbs;
SELECT * FROM v_b;	-- err
ALTER TABLE kbs RENAME jikwon;
SELECT * FROM v_b;	-- success

CREATE VIEW v_c AS SELECT * FROM jikwon ORDER BY jikwonpay DESC;
SELECT * FROM v_c;

CREATE VIEW v_d AS SELECT jikwonno, jikwonname, jikwonpay*10000 AS ypay FROM jikwon;
SELECT * FROM v_d;

CREATE VIEW v_e AS SELECT jikwonname, ypay FROM v_d WHERE ypay >= 50000000;
SELECT * FROM v_e;

UPDATE v_e SET jikwonname='김치국' WHERE jikwonname='김부만';
SELECT * FROM jikwon;

DELETE FROM v_d WHERE jikwonname='최미숙';
SELECT * FROM v_d;
SELECT * FROM jikwon;

DELETE FROM v_d WHERE ypay=41000000;	-- 계산에 의한 열도 조건에 참여 가능
SELECT * FROM v_d;
SELECT * FROM jikwon;

SELECT * FROM v_d;
UPDATE v_d SET ypay=1111 WHERE jikwonname='홍길동';	-- err

CREATE OR REPLACE view v_e AS SELECT jikwonno, jikwonname, busernum, jikwonpay FROM jikwon;
SELECT * FROM v_e;
INSERT INTO v_e VALUES(31, '김밥', 20, 5000);	-- view의 insert는 원본 not null에 주의
SELECT * FROM v_e;
SELECT * FROM jikwon;

CREATE OR REPLACE view v_f 
AS SELECT jikwonno, jikwonname, busernum, jikwonpay, jikwonibsail FROM jikwon
WHERE jikwonibsail < '2015-1-1';

SELECT * FROM v_f;
INSERT INTO v_f VALUES(32, '공기밥', 10, 6000, '2014-5-6');
INSERT INTO v_f VALUES(33, '주먹밥', 10, 7000, '2025-5-6');
SELECT * FROM v_f;
SELECT * FROM jikwon;

CREATE VIEW v_group AS
SELECT jikwonjik, SUM(jikwonpay) AS hap, AVG(jikwonpay) AS ave
FROM jikwon GROUP BY jikwonjik;

SELECT * FROM v_group;	-- group by에 의한 view는 참조만 가능(insert, update, delete 불가)

CREATE OR REPLACE VIEW v_join AS
SELECT jikwonno, jikwonname, busername, jikwonjik 
FROM jikwon INNER JOIN buser ON jikwon.busernum=buser.buserno
WHERE jikwon.busernum IN (10, 20);

SELECT * FROM v_join;

UPDATE v_join SET jikwonname='손오공' WHERE jikwonname='박명화';
SELECT * FROM v_join;
UPDATE v_join SET jikwonname='사오정', busername='영업부' WHERE jikwonname='손오공';	-- err
-- join에 의한 view는 한 개의 테이블만 수정에 참여해야 함

delete FROM v_join WHERE jikwonname='손오공';	-- err. 삭제 불가. Oracle에서는 삭제 가능

-- 문1) 사번   이름    부서  직급  근무년수  고객확보
-- 조건 : 직급이 없으면 임시직, 전산부 자료는 제외
CREATE OR REPLACE VIEW v_exam1 AS
	SELECT distinct jikwonno 사번, jikwonname 이름, busername 부서, 
		nvl(jikwonjik, '임시직') 직급, 
		YEAR(NOW())-YEAR(jikwonibsail) 근무년수, 
		case nvl(gogekname, 'a') when 'a' then 'X' ELSE 'O' END AS 고객확보
	FROM jikwon 
		LEFT OUTER JOIN buser ON jikwon.busernum=buser.buserno
		LEFT OUTER JOIN gogek ON jikwon.jikwonno=gogek.gogekdamsano
	WHERE busername <> '전산부' OR busername IS NULL;
SELECT * FROM v_exam1;

-- 문2) 부서명   인원수
-- 조건 : 직원수가 가장 많은 부서 출력	
CREATE OR REPLACE VIEW v_exam2 AS
	SELECT busername 부서명, COUNT(*) 인원수
	FROM jikwon	LEFT OUTER JOIN buser ON jikwon.busernum=buser.buserno
	GROUP BY busername
	HAVING 인원수 = (SELECT MAX(cnt) FROM (SELECT COUNT(*) cnt
		FROM jikwon LEFT OUTER JOIN buser ON jikwon.busernum=buser.buserno
		GROUP BY busername) t);
SELECT * FROM v_exam2;

CREATE OR REPLACE VIEW v_exam2 AS
SELECT busername AS 부서명, COUNT(*) AS 인원수 FROM buser
INNER JOIN jikwon ON buser.buserno=jikwon.busernum
GROUP BY busername
HAVING COUNT(*)=(SELECT COUNT(*) FROM jikwon 
						GROUP BY busernum
						ORDER BY COUNT(*) desc
						LIMIT 1);

CREATE OR REPLACE VIEW v_exam2 AS
SELECT busername AS 부서명, COUNT(*) AS 인원수 FROM buser
INNER JOIN jikwon ON buser.buserno=jikwon.busernum
GROUP BY busername
ORDER BY COUNT(*) desc LIMIT 1;
SELECT * FROM v_exam2;

-- 문3) 가장 많은 직원이 입사한 요일에 입사한 직원 출력
-- 직원명   요일     부서명   부서전화
-- 한국인  수요일   전산부   222-2222
create or replace view v_exam3 AS
	SELECT jikwonname 직원명, 
	case WEEKDAY(jikwonibsail)
    when '0' then '월요일'
    when '1' then '화요일'
    when '2' then '수요일'
    when '3' then '목요일'
    when '4' then '금요일'
    when '5' then '토요일'
    when '6' then '일요일'
    end as 요일,
	busername 부서명,
	busertel 부서전화
	FROM jikwon LEFT OUTER JOIN buser ON jikwon.busernum=buser.buserno
	WHERE WEEKDAY(jikwonibsail) IN (select WEEKDAY(jikwonibsail)
										from jikwon
										GROUP BY WEEKDAY(jikwonibsail)
										HAVING COUNT(*)=(SELECT MAX(cnt) 
										FROM (SELECT COUNT(*) cnt
												FROM jikwon 
												GROUP BY WEEKDAY(jikwonibsail)) t));

create or replace view v_exam3 AS
	SELECT jikwonname 직원명, 
	case WEEKDAY(jikwonibsail)
    when '0' then '월요일'
    when '1' then '화요일'
    when '2' then '수요일'
    when '3' then '목요일'
    when '4' then '금요일'
    when '5' then '토요일'
    when '6' then '일요일'
    end as 요일,
	busername 부서명,
	busertel 부서전화
	FROM jikwon 
	LEFT OUTER JOIN buser ON jikwon.busernum=buser.buserno
where WEEKDAY(jikwonibsail)=(
		SELECT weekday_num FROM (
			SELECT weekday(jikwonibsail) weekday_num, COUNT(*) cnt
			FROM jikwon 
			GROUP BY WEEKDAY(jikwonibsail)
			ORDER BY COUNT(*) DESC LIMIT 1
		) t
);

create or replace view v_exam3 AS
SELECT jikwonname 직원명, DATE_FORMAT(jikwonibsail, '%W') 요일, busername 부서명, busertel 부서전화
FROM jikwon LEFT OUTER JOIN buser ON jikwon.busernum=buser.buserno
WHERE DATE_FORMAT(jikwonibsail, '%W')=(SELECT DATE_FORMAT(jikwonibsail, '%W') 
				FROM jikwon 
				GROUP BY DATE_FORMAT(jikwonibsail, '%W')
				HAVING COUNT(*) = (SELECT COUNT(*) FROM jikwon
										GROUP BY DATE_FORMAT(jikwonibsail, '%W')
										ORDER BY COUNT(*) DESC LIMIT 1));

SELECT * FROM v_exam3;
