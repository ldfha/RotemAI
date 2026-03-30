# 알고리즘은 특정 문제를 해결하기 위한 명확하고 단계적인 절차나 규칙의 집합.
# 입력값을 받아 유한한 시간 내에 정해진 논리적 순서에 따라 문제를 해결하고 
# 결과물을 도출하는 과정으로, 컴퓨터 프로그래밍 및 일상생활의 문제 해결(예: 요리법)에
# 모두 적용됩니다. 

# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

print(sum_n(10))
print(sum_n(100))

def sum_n2(n):
    return n*(n+1) // 2

print(sum_n2(10))
print(sum_n2(100))

print("최대값 구하기 ---")
d = list(map(int, input().split()))
def find_max(d):
    n = len(d)
    max_v = d[0]
    for i in range(1,n):
        if d[i] > max_v:
            max_v = d[i]
    return max_v
print(find_max(d))

print("최대 공약수 -- 유클리드 호제법")
a, b = map(int, input().split())
def ucle(a, b):
    while b != 0:
        a, b = b,a % b     # 뭐가 큰지 중요하지 않은게 어차피 정렬됨
                        # 4 6 이면 한번 돌때 6 4 됨 
    return a
print(ucle(a,b))