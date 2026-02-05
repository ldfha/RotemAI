# 재귀함수 : 함수가 자기 자신을 호출 - 반복 처리
def countDown(n):
    if n == 0:
        print(('완료'))
        # return
    else :
        print(n, end=' ')
        countDown(n-1)      # 재귀 호출

countDown(5)

print('--1부터 n까지의 합')
def totFunc(n):
    if n == 0:
        print('exit')
        return 0
    else:
        return n + totFunc(n-1)

result = totFunc(5)
print(result)

print('------factorial-------')
def factFunc(n):
    if n == 1:
        return 1
    print(n)
    return n * factFunc(n-1)
result2 = factFunc(5)
print(result2)
print('end')
