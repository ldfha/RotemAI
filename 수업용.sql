CREATE TABLE dept(NO INT PRIMARY KEY, NAME VARCHAR(10), 
tel VARCHAR(15), inwon INT, addr TEXT) CHARSET=UTF8;	-- 테이블 생성

-- 자료 추가
# insert into 테이블명(칼럼명, ...) values(입력자료, ...)
INSERT INTO dept(NO, NAME, tel, inwon, addr) 
					VALUES(1, '인사과', '111-1111', 3, '삼성동12');
INSERT INTO dept VALUES(2, '영업과', '111-2222', 5, '서초동12');
INSERT INTO dept(NO, NAME) VALUES(3, '자재과');
INSERT INTO dept(NO, addr, tel, NAME) VALUES(4, '역삼2동33', '111-5555', '자재2과');

# INSERT INTO dept VALUES(5, '자재과');	-- err : 입력자료와 칼럼 갯수 불일치
# INSERT INTO dept(NAME, tel) VALUES('판매2과', '111-6666-);	-- NO:pk, 생략 불가
# INSERT INTO dept(NO, NAME) VALUES(5, 		-- err : Name(10자) 자릿수 넘침
						'판매과부서는 사람들이 좋아 일하기 좋은 우수한 부서임');

SELECT * FROM dept;
SELECT * FROM dept WHERE NO=1;

-- 자료 수정
-- update 테이블명 set 수정칼럼명=수정값, ... where 조건 <== 수정 대상 칼럼을 지정
-- pk 칼럼의 자료는 수정 대상에서 제외
UPDATE dept SET tel='123-4567' WHERE NO=2;
UPDATE dept SET addr='압구정동33', inwon=7, tel='777-8888' WHERE NO=3;

-- 자료 삭제
-- delete from 테이블명 where 조건 	-- 전체 또는 부분적 레코드 삭제
-- truncate table 테이블명 	-- where 조건을 사용X, 전체 레코드 삭제 가능
DELETE FROM dept WHERE NAME='자재2과';
SELECT * FROM dept;

truncate table dept;
SELECT * FROM dept;

DROP TABLE dept;		--  테이블 자체(구조, 자료)가 제거됨

-- 무결성 제약조건 
-- : 테이블 생성시 잘못된 자료 입력을 막고자 다양한 입력 제한 조건을 줄 수 있다.
-- 1) 기본키 제약 : primary key(pk) 사용, 중복 레코드 입력 방지
CREATE TABLE aa(bun INT PRIMARY KEY, irum CHAR(10)); -- bun:NOT NULL, UNIQUE
SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME='aa';
INSERT INTO aa VALUES(1, 'tom');
INSERT INTO aa VALUES(2, 'tom');
INSERT INTO aa VALUES(2, 'tom');	  # err : Duplicate entry '2' for key 'PRIMARY'
INSERT INTO aa(irum) VALUES('tom');		# err : Field 'bun' doesn't have a default value 
INSERT INTO aa(bun) VALUES('3');
SELECT * FROM aa;
DROP TABLE aa;

CREATE TABLE aa(bun INT, irum CHAR(10), CONSTRAINT aa_bun_pk PRIMARY KEY(bun));
INSERT INTO aa VALUES(1, 'tom');
INSERT INTO aa VALUES(2, 'tom');
SELECT * FROM aa;
DROP TABLE aa;

-- 2) check 제약 : 입력 자료의 특정 칼럼값 조건 검사
CREATE TABLE aa(bun INT, nai INT CHECK(nai>=20));
INSERT INTO aa VALUES(1, 23);
INSERT INTO aa VALUES(1, 13);		-- err : CONSTRAINT `aa.nai` failed for `test`.`aa`
SELECT * FROM aa;
DROP TABLE aa;

-- 3) unique 제약 : 특정 칼럼값 중복 불허
CREATE TABLE aa(bun INT, irum VARCHAR(10) NOT NULL UNIQUE);
INSERT INTO aa VALUES(1, 'tom');
INSERT INTO aa VALUES(2, 'john');
INSERT INTO aa VALUES(3, 'john');	-- err : Duplicate entry 'john' for key 'irum'
SELECT * FROM aa;
DROP TABLE aa;

-- 4) foreign key(fk), 외부키, 참조키 제약 : 특정 칼럼이 다른 테이블의 칼럼을 참조
-- fk 대상은 pk다!!

CREATE TABLE jikwon(
	bun INT PRIMARY KEY, 
	irum VARCHAR(10) NOT NULL, 
	buser CHAR(10) NOT NULL
);
INSERT INTO jikwon VALUES(1, '한송이', '인사과');
INSERT INTO jikwon VALUES(2, '이기자', '인사과');
INSERT INTO jikwon VALUES(3, '한송이', '판매과');
SELECT * FROM jikwon;

CREATE TABLE gajok(
	CODE INT PRIMARY KEY, 
	NAME VARCHAR(10) NOT NULL, 
	birth DATETIME, 
	jikwonbun INT, 
	FOREIGN KEY(jikwonbun) REFERENCES jikwon(bun)
);

INSERT INTO gajok VALUES(10, '한가해', '2015-05-12', 3);
INSERT INTO gajok VALUES(20, '공기밥', '2011-12-02', 2);
INSERT INTO gajok VALUES(30, '김밥', '2010-06-23', 5);	-- err:Cannot add or update a child row: a foreign key constraint fails
INSERT INTO gajok VALUES(40, '심심해', '2003-04-13', 3);
SELECT * FROM gajok;

DELETE FROM jikwon WHERE bun=1;
SELECT * FROM jikwon;

DELETE FROM jikwon WHERE bun=3;		-- err : 참조 자료(가족)가 있으므로 삭제 불가
DROP TABLE jikwon;	-- err

DELETE FROM gajok WHERE jikwonbun=2;	-- 1) 참조키(pk가 2번) 가족 자료 삭제
DELETE FROM jikwon WHERE bun=2;			-- 2) 참조 가족이 없으므로 2번 직원 삭제 가능

-- 참고
-- CREATE TABLE gajok(CODE INT PRIMARY KEY, ...) on delete cascade
-- 직원 자료를 삭제하면 관련있는 가족 자료도 함께 삭제됨

DROP TABLE gajok;
DROP TABLE jikwon;

-- defalut : 특정 칼럼에 초기치 부여. null 예방
CREATE TABLE aa(
	bun INT AUTO_INCREMENT PRIMARY KEY,	-- auto_increment : bun 자동 증가
	juso CHAR(20) DEFAULT '강남구 역삼동'
);

INSERT INTO aa VALUES(1, '서초구 서초2동');
INSERT INTO aa(juso) VALUES('서초구 서초3동');
INSERT INTO aa(juso) VALUES('서초구 서초4동');
INSERT INTO aa(bun) VALUES(5);
INSERT INTO aa(bun) VALUES(6);
SELECT * FROM aa;
DROP TABLE aa;

-- 문제 : 제약조건 연습
CREATE TABLE professor(
	CODE INT PRIMARY KEY,
	NAME CHAR(10),
	lab INT CHECK(100 <= lab AND lab <= 500)
);
CREATE TABLE SUBJECT(
	CODE INT PRIMARY KEY AUTO_INCREMENT,
	NAME CHAR(10) UNIQUE,
	book VARCHAR(10),
	professor INT,
	FOREIGN KEY(professor) REFERENCES professor(CODE)
);
CREATE TABLE student(
	hakbun INT PRIMARY KEY,
	NAME CHAR(10),
	SUBJECT INT,
	grade INT DEFAULT '1' CHECK(grade<=4 AND grade >= 1) ,
	FOREIGN KEY(SUBJECT) REFERENCES SUBJECT(CODE)
);
INSERT INTO professor VALUES(1, '김교수', 100);
INSERT INTO professor VALUES(2, '이교수', 110);
INSERT INTO professor VALUES(3, '박교수', 400);
INSERT INTO professor VALUES(3, '박교수', 600);		-- err
SELECT * FROM professor;

INSERT INTO subject VALUES(1, '김교수의 이해', '작가 김교수', 1);
INSERT INTO subject(NAME, book, professor) VALUES('귀가학', '귀가학의 정석', 2);
INSERT INTO subject(NAME, book, professor) VALUES(3, '마리아디비', '이것이 마리아디비', 400);	-- err
INSERT INTO subject(NAME, book, professor) VALUES('파이썬', '파이썬 프로그래밍', 3);
SELECT * FROM subject;

INSERT INTO student VALUES(2020, '김학생', 1, -4); 	-- err
INSERT INTO student VALUES(2020, '김학생', 1, 4);
INSERT INTO student(hakbun, NAME, subject) VALUES(2021, '이학생', 2);
INSERT INTO student VALUES(2022, '박학생', 2, 2);
SELECT * FROM student;
SELECT * FROM subject;
SELECT * FROM professor;

DROP TABLE student;
DROP TABLE subject;
DROP TABLE professor;

-- index(색인) : 검색 속도 향상을 위해 특정  column에 색인 부여 가능
-- pk column은 자동으로 인덱싱됨(ascending sort : 오름차순 정렬)
-- index를 자제해야 하는 경우 : 입력, 수정, 삭제 등의 작업이 빈번한 경우
CREATE TABLE aa(
	bun INT PRIMARY KEY,
	irum VARCHAR(10) NOT NULL,
	juso VARCHAR(50)
);
INSERT INTO aa VALUES(1, '신선해', '테헤란로111');
ALTER TABLE aa ADD INDEX ind_juso(juso);	-- juso column에 인덱스 부여
SELECT * FROM aa;
EXPLAIN SELECT * FROM aa;
DESC aa;
SHOW INDEX FROM aa;
ALTER TABLE aa DROP INDEX ind_juso;
DROP TABLE aa;

-- 테이블 관련 주요 명령
-- CREATE TABLE 테이블명 ...
-- ALTER TABLE 테이블명 ...	: 수정
-- DROP TABLE 테이블명 ... : 삭제
CREATE TABLE aa(
	bun INT,
	irum VARCHAR(10),
	juso VARCHAR(50)
);
INSERT INTO aa VALUES(1, 'tom', 'seoul');
SELECT * FROM aa;

ALTER TABLE aa RENAME kbs;		-- 테이블명 변경
SELECT * FROM aa;
ALTER TABLE kbs RENAME aa;

-- 칼럼 관련 명령
ALTER TABLE aa ADD (job_id INT DEFAULT 10);	-- 칼럼 추가
SELECT * FROM aa;
ALTER TABLE aa CHANGE job_id job_num INT;		-- 칼럼 수정(이름이나 성격 변경)
SELECT * FROM aa;
ALTER TABLE aa MODIFY job_num VARCHAR(10); 	-- 칼럼 성격 변경
DESC aa;

ALTER TABLE aa DROP COLUMN job_num;		-- 칼럼 삭제
SELECT * FROM aa;