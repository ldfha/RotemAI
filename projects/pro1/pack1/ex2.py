""" print('출력1', end = ',') # 줄바꿈 대신 ","로 출력 이어가기
print('출력2')
print('출력3')

# 연산자
v1 = 3  # 치환 연산자
v1 = v2 = v3 = 5
print(v1, v2, v3)

v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print('값 할당 : packing 연산')
v1 = 1,2,3,4,5      # v1 = (1,2,3,4,5)
v1 = [1,2,3,4,5]
*v1, v2 = [1,2,3,4,5]  
print(v1, '  ', v2)
v1, *v2 = [1,2,3,4,5]  
print(v1, '  ', v2)
*v1, v2, v3 = [1,2,3,4,5]  
print(v1, '  ', v2, '  ', v3)

print(format(1.5678, '10.3f'))      # 전체 10자리, 소수 이하 셋째짜리까지 반올림
print('나는 나이가 %d 이다.'%23)    # 숫자 %d, 문자 %s, 실수 %f
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))    # 대응 순서
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))
abc = 123
print(f"abc의 값은 {abc}이다.") 

print('\n본격적 연산 -------')  # escape 문자 \n(다음줄), \b(back), \t(tap), ...
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 3)
#       8       2     15 1.6666666666666667 1(몫) 2(나머지)    125
print(divmod(5, 3))     # (몫, 나머지)
result = 3 + 4 * 5 + (2 + 3) / 2  
# 산술 연산자 우선순위 1.소괄호 2.곱셈, 나눗셈 3.덧셈, 뺄셈 4.치환
# () -> ** -> 단항 -> 산술연산자(*, / -> +, -) -> 관계 -> 논리(not -> and -> or) -> =
print(result)

# 비교 연산자
print(5 > 3, 5 == 3, 5 != 3)

# 논리 연산자 and가 or보다 연산 순위가 높다
print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3))
print(True or False and False)
print(True and False or False)

print(4 + 5) # 산술 연산
print('4' + "5") # 문자열 더하기 연산
print('한' + '국' + '만세')
print('한국' * 5) 

# 누적
a = 10
a = a + 1
a += 1      # -= , *= , /= 연산속도가 빠르다
print(f"a는 {a}")

# print(a++)  # ++, -- : 증감 연산자 X

# 부호 연산
print(--a) 
print(-a)
print(a * -1)

# print(('1' + '1') + 1)  # TypeError
print(int('1' + '1') + 1)  # int(문자열) -> 정수화
print(float('1' + '1') + 1)  # float(문자열) -> 실수화
# print((1 + 1) + '1')  # TypeError
print(str(1 + 1) + '1')  # str(숫자) -> 문자화
print('boolean 처리 : ', bool(True), bool(False))
print(bool(1), bool(12.3), bool('ok'), bool([12]))
print(bool(0), bool(0.0), bool(''), bool([]), bool(None)) """

# r 선행문자
print('aa\tbb')
print('aa\nbb')
print(r'aa\tbb')
print(r'aa\nbb')