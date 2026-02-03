# 사용자 정의 함수
"""
def 함수명(arg, , ,):
    return 반환값   # 1개만 반환, return이 없으면 None 반환

함수명(arg1, arg2, ...)        # 함수 호출
"""

def doFunc1():
    print('doFunc1 수행')

def doFunc2(name):
    print('name :', name)
    

def doFunc3(arg1, arg2):
    re = arg1 + arg2
    return re

def doFunc4(arg1, arg2):
    re = arg1 + arg2
    if re % 2 == 1:
        return
    else:
        return re

# doFunc1()   # 함수 호출
# print("함수 주소는 ", doFunc1)          
# print("함수 주소는 ", id(doFunc1))      # 주소값을 해시코드로 변환하여 나타냄
# imsi = doFunc1      # doFunc1은 함수의 주소를 기억함
# imsi()
# print(doFunc1())

# doFunc2(7)
# doFunc2("길동")
# doFunc2("길동", "순신")

# print(doFunc3("대한", "민국"))
# print(doFunc3(5, 6))
# result = doFunc3("5", "6")
# print(result)

# print(doFunc4(3, 4))
# print(doFunc4(3, 5))

# def triArea(a, b):
#     c = a * b / 2
#     triAreaPrint(c)     # 함수 내에서 다른 함수 호출

# def triAreaPrint(cc):
#     print('삼각형의 넓이는 ',cc)

# triArea(20, 30)

# def passResult(kor, eng):
#     ss = kor + eng
#     if ss >= 50 :
#         return True
#     else:
#         return False

# if passResult(20, 50):
#     print('합격')
# else:
#     print('불합격')

# def swapFunc(a, b):
#     return b, a     # 튜플형 반환

# a = 10; b = 20
# print(a, ' ',b)
# print(swapFunc(a, b))

# def funcTest():
#     print('funcTest 멤버 처리')
#     def funcInner():
#         print('내부 함수')
#     funcInner()
# funcTest()

# # if 조건식 안에 함수 사용
# def isOdd(para) :
#     return para % 2 == 1    # 홀수이면 True 반환

# mydict = { x:x * x for x in range(11) if isOdd(x) }
# print(mydict)

player = '전국대표'     # 전역변수(현재 모듈 어디서든 호출 가능)
name = '한국인'
def funcSoccer():
    name = '홍길동'     # 지역변수(현재 함수내에서만 호출 가능 )
    player = '지역대표'
    print(f'이름은 {name} 수준은 {player}')

funcSoccer()
print(f'이름은 {name} 수준은 {player}')

print()
a = 10; b = 20; c = 30
def Foo():
    a = 7           # 지역변수 
    b = 100
    def Bar():
        global c    # Bar 함수의 멤버가 아니라 모듈(파일)의 멤버가 됨. 전역 변수
        nonlocal b
        b = 8       # 지역 변수
        print(f"Bar 수행 수 a:{a}, b:{b}, c:{c}")
        c = 9
        b = 200 # Foo의 멤버가 됨
    Bar()
    print(f"Foo 수행 수 a:{a}, b:{b}, c:{c}")

Foo()
print(f"함수 수행 수 a:{a}, b:{b}, c:{c}")

print()
g = 1
print('g = ', g)
def func():
    global g
    a = g
    g = 2
    return a

print(func())
print('g = ', g)
