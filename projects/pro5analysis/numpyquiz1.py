import numpy as np

# 문1) 정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 
# 각 행 단위로 합계, 최댓값을 구하시오.
a = np.random.randn(5, 4)
# for i in range(len(a)):
#     print(str(i + 1) + '행 합계 : ' + str(np.sum(a[i])))
#     print(str(i + 1) + '행 최댓값 : ' + str(np.max(a[i])))

i = 1
for row in a:
    # print(str(i) + '행 합계 : ' + row.sum())
    print(str(i) + '행 합계 : ', np.sum(row))
    print(str(i) + '행 최댓값 : ',  np.max(row))
    i += 1
    

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

# b = np.zeros(36).reshape(6, 6)
b = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        b[i][j] = (j + 1) + 6*i
print(b)
# print(b[1])
print(b[1, :])
# print(b.T[4])
print(b[:, 4])
# print(b[2:5].T[2:5].T)
print(b[2:5, 2:5])

# 문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.
# 조건1> 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 난수 정수를 저장하고, 두 번째 열부터는 1씩 증가시켜 원소 저장하기
# 조건2> 첫 번째 행에 1000, 마지막 행에 6000으로 요소값 수정하기
import random
# c = np.zeros(24).reshape(6, 4)
c = np.zeros((6, 4))
print(c)

# for i in range(6):
#     c[i][0] = random.randint(20, 100)
#    for j in range(1, 4):
#        c[i][j] = c[i][j - 1] + 1

ran = np.random.randint(20, 100, 6)
print(ran)
ran=list(ran)
for row in range(len(c)):
    num = ran.pop(0)
    for col in range(len(c[0])):
        c[row][col]=num
        num += 1

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
print('1사분위 수 : ', np.percentile(d, 25))
print('2사분위 수 : ', np.percentile(d, 50))
print('3사분위 수 : ', np.percentile(d, 75))
print('요소값 누적합 : ', np.cumsum(d))

# Q1) 브로드캐스팅과 조건 연산
# 다음 두 배열이 있을 때,
# a = np.array([[1], [2], [3]])
# b = np.array([10, 20, 30])
# 두 배열을 브로드캐스팅하여 곱한 결과를 출력하시오.
# 그 결과에서 값이 30 이상인 요소만 골라 출력하시오.
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
result = a* b
print(result)
print(result[result >= 30])

# Q2) 다차원 배열 슬라이싱 및 재배열
#  - 3×4 크기의 배열을 만들고 (reshape 사용),  
#  - 2번째 행 전체 출력
#  - 1번째 열 전체 출력
#  - 배열을 (4, 3) 형태로 reshape
#  - reshape한 배열을 flatten() 함수를 사용하여 1차원 배열로 만들기
c = np.random.randint(1,50,12).reshape(3, 4)
print(c)
print(c[1,:])
print(c[:,0])
c = c.reshape(4, 3)
print(c)
print(c.flatten())

# Q3) 1부터 100까지의 수로 구성된 배열에서 3의 배수이면서 5의 배수가 아닌 값만 추출하시오.
# 그런 값들을 모두 제곱한 배열을 만들고 출력하시오.
d = np.arange(1, 101)
imsi = (d % 3 == 0) & (d % 5 != 0)
filtered = d[imsi]
print(filtered)
squ = filtered ** 2
print(squ)

# Q4) 다음과 같은 배열이 있다고 할 때,
# arr = np.array([15, 22, 8, 19, 31, 4])
# 값이 10 이상이면 'High', 그렇지 않으면 'Low'라는 문자열 배열로 변환하시오.
# 값이 20 이상인 요소만 -1로 바꾼 새로운 배열을 만들어 출력하시오. (원본은 유지)
# 힌트: np.where(), np.copy()
arr = np.array([15, 22, 8, 19, 31, 4])
labels = np.where(arr >= 10, "High", "Low")
print(labels)
new_arr = np.copy(arr)
new_arr[new_arr >= 20] = -1
print(new_arr)

# Q5) 정규분포(평균 50, 표준편차 10)를 따르는 난수 1000개를 만들고, 상위 5% 값만 출력하세요.
# 힌트 :  np.random.normal(), np.percentile()
data = np.random.normal(loc=50, scale=10, size=1000)
print(data)
threshold = np.percentile(data, 95)
top5 = data[data > threshold]
print(top5)