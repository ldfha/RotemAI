# # 문1) 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
# n = 1
# sum = 0
# while n <= 100:
#     if n % 3 == 0 and n % 2 != 0:
#         print(n)
#         sum += n
#     n +=1
# print(sum)

# # 문2) 2 ~ 5 까지의 구구단 출력
# for i in range(2, 6):
#     print(f'----{i}단----')
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')
    
# # 문3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
# i = 1
# tot = 0
# while i <= 100:
#     if i % 2 == 0:
#         tot += i
#     else:
#         tot -= i
#     i += 1
# print(tot)

# # 문4) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
# i = 1
# iter = 0
# tot = 0
# while i < 100:
#     if iter % 2 == 0:
#         j = -i
#         tot += j
#     else:
#         tot += i
#     i += 2
#     iter += 1
# print(tot)

# # 문5) 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력
# i = 1
# while i <= 100:
#     i_str = list(str(i))
#     # print(i_str)
#     i_int = list(map(int, i_str))
#     # print(i_int)
#     i_sum = sum(i_int)
#     if(i_sum) >= 10:
#         print(i)
#     i += 1

# # 문6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력
# i = 1
# total = 0
# while total <= 1000:
#     total += i
#     i += 1

# print(i, total)

# # 문7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i * j > 30 :
#             break
#         print(f'{i} * {j} = {i * j}')

# # 문8) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
# i = 2
# num = 0
# while i <= 1000:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             break
#         j += 1
#     else: 
#         num += 1
#         j += 1
#         print(i)
#     i += 1
# print(num)


# # 문제1) 1부터 50까지의 숫자 중 3의 배수는 건너뛰고 나머지 수만 출력하라
# i = 1
# while i <= 50:
#     if i % 3 == 0:
#         i += 1
#         continue
#     else:
#         print(i)
#     i += 1

# # 문제2) 1부터 100까지 출력하되 4의 배수, 6의 배수는 건너뛴다. 그 외의 수 중 5의 배수만 출력하고 그들의 합도 출력하라
# i = 1
# total = 0
# while i <= 100:
#     if i % 4 == 0 or i % 6 == 0:
#         i += 1
#         continue
#     else:
#         print(i)
#         total += i
#         i += 1
# print(total)



#함수 처리 -----------------------------

# # 연습문제) 키보드를 통해 직원 자료를 입력받아 가공 후 출력하기
# def inputFunc():
#     datas_list=[]
#     while True:
#         data = input("사번, 이름, 기본급, 입사년도")
#         data_list = data.split(',')
#         datas_list.append(list(data_list))
#         # print(datas_list)
#         stop = input("계속 입력할까요?[y/n]")
#         if stop == 'n' or stop == 'N':
#             return datas_list
#         elif stop == 'y' or stop == 'Y':
#             continue

# def processFunc(datas):
#     print('사번\t이름\t기본급\t근무년수\t근속수당\t공제액\t수령액')
#     for data in datas:
#         plus = 150000       # 근속수당
#         years = 2026 - int(data[3])
#         if 4 <= years <= 8:
#             plus = 450000
#         elif years >= 9:
#             plus = 1000000
#         money = int(data[2]) + plus     # 급여액

#         tax = 0.15
#         if money >= 3000000:
#             tax = 0.5
#         elif money >= 2000000:
#             tax = 0.3
#         else:
#             tax = 0.15
        
#         wage = money - money*tax

#         print(f'{data[0]}\t{data[1]}\t{data[2]}\t{years}\t{plus}\t{money*tax}\t{wage}')
    

# datas = inputFunc()
# processFunc(datas)


#연습문제 ) 키보드를 통해 상품자료를 입력받아 가공 후 출력하기
def inputFunc():
    datas_list=[]
    while True:
        data = input("지역코드.상품명,수량")
        data_list = data.split(',')
        datas_list.append(list(data_list))
        # print(datas_list)
        stop = input("계속 입력할까요?[y/n]")
        if stop == 'n' or stop == 'N':
            return datas_list
        elif stop == 'y' or stop == 'Y':
            continue

def processFunc(datas):
    print('지역\t상품명\t수량\t단가\t금액')
    potato = 0
    shirimp = 0
    for data in datas:
        region = ""
        if data[0] == "100":
            region = "강북"
        elif data[0] == "200":
            region = "강남"
        elif data[0] == "300":
            region = "강서"
        else:
            region = "unknown"
        
        price = 0
        if data[1] == "감자깡":
            price = 450
            potato += int(data[2])
        elif data[1] == "새우깡":
            price = 300
            shirimp += int(data[2])

        print(f"{region}\t{data[1]}\t{data[2]}\t{price}\t{int(data[2])*price}")
    print(f"소계 감자깡:{potato} 소계액:{potato*450}")
    print(f"소계 새우깡:{shirimp} 소계액:{shirimp*300}")
    print(f"총 건수:{potato+shirimp} 총액:{potato*450+shirimp*300}")

datas = inputFunc()
processFunc(datas)

