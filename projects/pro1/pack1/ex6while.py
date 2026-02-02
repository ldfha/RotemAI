# 반복문 while
# a = 1
# while a <= 5:
#     print(a, end=' ')
#     a += 1
# else :
#     print("수행 성공")

# print()
# i = 1
# while i <= 3:
#     j = 1
#     while j <= 4:
#         print('i=' + str(i) + '/j=' + str(j))
#         j = j + 1
#     i = i + 1

# print('1 ~ 100 사이의 정수 중 3의 배수의 합 ---')
# n = 1
# sum = 0
# while(n <= 100):
#     if(n % 3 == 0):
#         # print(n)
#         sum += n    # sum = sum + n
#     n += 1
# print('합은 ', sum)

# colors = ["빨강", "파랑", "노랑", "검정"]
# a = 0
# # while a < 3:
# while a < len(colors):
#     print(colors[a])
#     a += 1

# print("별 찍기-----")
# i = 1
# while(i <= 10):
#     j = 1
#     msg=''
#     while(j <= i):
#         msg += "*"
#         j += 1
#     print(msg)
#     i += 1

# print("if 블럭 내 while 블럭 사용 ----- ")
# import time
# sw = input('폭탄 스위치를 누를까요?[y/n]')
# print("sw : ", sw)
# if sw =='y' or sw == "Y":
#     count = 5
#     while 1 <= count :
#         print('%d초 남았습니다.'%count)
#         time.sleep(1)  # 초단위. 1초 후 다음 문장 수행
#         count -= 1
#     print('폭발')
# elif sw == 'n' or sw == 'N':
#     print("작업 취소")
# else:
#     print('y 또는 n을 누르세요.')

# print("continue와 break --- ")
# a = 0
# while a < 10:
#     a += 1
#     if a == 3: 
#         continue    # 아래 문을 무시하고 while로 이동
#     if a == 5: continue
#     # if a == 7: break    # 무조건 탈출
#     print(a)
# else :
#     print('정상 종료')

# print('while 수행 후 %d'%a)


print('키보드로 숫자를 입력 받아 홀수 짝수 확인하기(무한 반복)')
while True:
    num = int(input("숫자를 입력하세요 : "))
    if num == 0:
        print("종료합니다.")
        break
    elif (num % 2 == 0):
        print("%d는 짝수"%num)
    elif num % 2 == 1 :
        print("%d는 홀수"%num)
print('end')