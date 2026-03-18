import numpy as np

# 문1) 정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 
# 각 행 단위로 합계, 최댓값을 구하시오.
a = np.random.randn(5, 4)
for i in range(len(a)):
    print(str(i) + '행 합계 : ' + str(np.sum(a[i])))
    print(str(i) + '행 최댓값 : ' + str(np.max(a[i])))

# 문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
# 조건1> 36개의 셀에 1~36까지 정수 채우기
# 조건2> 2번째 행 전체 원소 출력하기 
#             출력 결과 : [ 7.   8.   9.  10.  11.  12.]
# 조건3> 5번째 열 전체 원소 출력하기
#             출력결과 : [ 5. 11. 17. 23. 29. 35.]
# 조건4> 15~29 까지 아래 처럼 출력하기
#             출력결과 : 
#             [[15.  16.  17.]
#             [21.  22.  23]
#             [27.  28.  29.]]

b = np.zeros(36).reshape(6, 6)
for i in range(6):
    for j in range(6):
        b[i][j] = (j + 1) + 6*i
print(b)
print(b[1])
print(b.T[4])
# print(b[2:5].T[2:5].T)
print(b[2:5, 2:5])

# 문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.
# 조건1> 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 난수 정수를 저장하고, 두 번째 열부터는 1씩 증가시켜 원소 저장하기
# 조건2> 첫 번째 행에 1000, 마지막 행에 6000으로 요소값 수정하기
import random
c = np.zeros(24).reshape(6, 4)
print(c)
for i in range(6):
    c[i][0] = random.randint(20, 100)
    for j in range(1, 4):
        c[i][j] = c[i][j - 1] + 1
print(c)
c[0]=1000; c[len(c)-1]=6000
print(c)

# 3) step3 : unifunc 관련문제
# 표준정규분포를 따르는 난수를 이용하여 4행 5열 구조의 다차원 배열을 생성한 후
# 아래와 같이 넘파이 내장함수(유니버설 함수)를 이용하여 기술통계량을 구하시오.
# 배열 요소의 누적합을 출력하시오.
d = np.random.randn(4, 5)
print(d)
print('평균 : ', np.average(d))
print('합계 : ', np.sum(d))
print('표준편차 : ', np.std(d))
print('분산 : ', np.var(d))
print('최댓값 : ', np.max(d))
print('최솟값 : ', np.min(d))
print('1사분위 수 : ', np.percentile(d, 1))
print('2사분위 수 : ', np.percentile(d, 2))
print('3사분위 수 : ', np.percentile(d, 3))
print('요소값 누적합 : ', np.cumsum(d))

