# numpy의 ndarray는 단순한 배열이라기 보다,
# 벡터/행렬 연산도 가능한 다차원 수치 데이터 구조이다.
import numpy as np

ss = ['tom','james','oscar', 1, True]   # 여러 type의 자료로 구성
print(ss, ' ', type(ss))

ss2 = np.array(ss)  # 같은 type의 자료로만 구성
print(ss2, ' ', type(ss2))  

li = list(range(1, 10))
print(li)
print(li[0], ' ', li[1], ' ', id(li[0]), ' ', id(li[1]))
# li 요소 각각에 10을 곱하려고 한다
print(li * 10)  # li를 10번 반복함
print('----'*10)

for i in li:
    print(i * 10, end=' ')
print()

# numpy 배열 활용
np_arr = np.array(li)
print(np_arr[0], ' ', np_arr[1], ' ', id(np_arr[0]),  ' ', id(np_arr[1]))
# 주소가 동일함
print(np_arr * 10)  # 벡터화 연산이 가능

a = np.array([1, 2, 3.5], dtype='float32')  # type 명시
print(a, ' ', type(a))  # ndarray는 동일 타입 데이터만 취급
# 여러 타입의 자료가 입력되면 상위 타입으로 자동 변환. (하위)int -> float -> complex -> str(상위)

print()
b = np.array([[1,2,3], [4,5,6]])
print(b.shape, ' ', b[0][0], ' ', b[0]) # b[0], b[[0]] 차이?

print()

c = np.zeros((2, 2))    # 2행 2열짜리 0으로 채워진 행렬
print(c)

d = np.ones((2, 2))    # 2행 2열짜리 1으로 채워진 행렬
print(d)

e = np.eye(3)    # 2행 2열짜리 단위 행렬. 주대각 성분이 1
print(e)

print()
print(np.random.rand(5))    # 균등 분포
print(np.random.randn(5))   # 정규 분포

np.random.seed(0)
print(np.random.randn(2, 3))    # 실행마다 값이 다름

print(list(range(0, 10)))
print(np.arange(10))

print()
# 인덱싱/슬라이싱
a = np.array([1,2,3,4,5])
print(a, ' ', a[1]) # 인덱싱
print(a[1:4])
print(a[1:])
print(a[1:5:2]) # 시작:끝:step 1이상 5미만 2
print(a[-2:])

b = a     # 주소 치환
print(a[0], ' ', b[0])
print(id(a[0]), ' ', id(b[0]))
b[0] = 88
print(a[0], ' ', b[0])

c = np.copy(a)      # 복사본 생성
print(a[0], ' ', c[0])
b[0] = 33
print(a[0], ' ', c[0])
