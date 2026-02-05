# #함수 처리 -----------------------------

# # # 연습문제) 키보드를 통해 직원 자료를 입력받아 가공 후 출력하기
# # def inputFunc():
# #     datas_list=[]
# #     while True:
# #         data = input("사번, 이름, 기본급, 입사년도")
# #         data_list = data.split(',')
# #         datas_list.append(list(data_list))
# #         # print(datas_list)
# #         stop = input("계속 입력할까요?[y/n]")
# #         if stop == 'n' or stop == 'N':
# #             return datas_list
# #         elif stop == 'y' or stop == 'Y':
# #             continue

def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas

import datetime

def processFunc(datas):
    CURRENT_YEAR = datetime.date.today().year
    count = 0
    print('사번\t이름\t기본급\t근무년수\t근속수당\t공제액\t수령액')
    print('-------------------------------------------------------------------------------')
    for data in datas:
        count += 1
        years = CURRENT_YEAR - data[3]    # 근무 년수
        plus = 150000       # 근속 수당
        if 4 <= years <= 8:
            plus = 450000
        elif years >= 9:
            plus = 1000000
        money = data[2] + plus     # 급여액

        tax = 0.15         # 공제 세율
        if money >= 3000000:
            tax = 0.5
        elif money >= 2000000:
            tax = 0.3
        
        gongje = money * tax
        wage = money - gongje

        print(f'{data[0]}\t{data[1]}\t{data[2]}\t{years}\t{plus}\t{gongje}\t{wage}')
    print(f'처리 건수 : {count}')
processFunc(inputfunc())


# #연습문제 ) 키보드를 통해 상품자료를 입력받아 가공 후 출력하기
# def inputFunc():
#     datas_list=[]
#     while True:
#         data = input("지역코드.상품명,수량")
#         data_list = data.split(',')
#         datas_list.append(list(data_list))
#         # print(datas_list)
#         stop = input("계속 입력할까요?[y/n]")
#         if stop == 'n' or stop == 'N':
#             return datas_list
#         elif stop == 'y' or stop == 'Y':
#             continue

# def processFunc(datas):
#     print('지역\t상품명\t수량\t단가\t금액')
#     potato = 0
#     shirimp = 0
#     for data in datas:
#         region = ""
#         if data[0] == "100":
#             region = "강북"
#         elif data[0] == "200":
#             region = "강남"
#         elif data[0] == "300":
#             region = "강서"
#         else:
#             region = "unknown"
        
#         price = 0
#         if data[1] == "감자깡":
#             price = 450
#             potato += int(data[2])
#         elif data[1] == "새우깡":
#             price = 300
#             shirimp += int(data[2])

#         print(f"{region}\t{data[1]}\t{data[2]}\t{price}\t{int(data[2])*price}")
#     print(f"소계 감자깡:{potato} 소계액:{potato*450}")
#     print(f"소계 새우깡:{shirimp} 소계액:{shirimp*300}")
#     print(f"총 건수:{potato+shirimp} 총액:{potato*450+shirimp*300}")

# datas = inputFunc()
# processFunc(datas)


def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

def processFunc(datas):
    print('상품명\t수량\t단가\t금액')
    potato_cnt = 0
    shirimp_cnt = 0
    onion_cnt = 0
    potato_price = 300
    shirimp_price = 450
    onion_price = 350
    for data in datas:
        data_split = data.split(',')
        
        price = 0
        if data_split[0] == "감자깡":
            price = potato_price
            potato_cnt += int(data_split[1])
        elif data_split[0] == "새우깡":
            price = shirimp_price
            shirimp_cnt += int(data_split[1])
        elif data_split[0] == "양파깡":
            price = onion_price
            onion_cnt += int(data_split[1])

        print(f"{data_split[0]}\t{data_split[1]}\t{price}\t{int(data_split[1])*price}")
    print(f"소계 새우깡:{shirimp_cnt} 소계액:{shirimp_cnt*shirimp_price}")
    print(f"소계 감자깡:{potato_cnt} 소계액:{potato_cnt*potato_price}")
    print(f"소계 양파깡:{onion_cnt} 소계액:{onion_cnt*onion_price}")
    print(f"총 건수:{potato_cnt+shirimp_cnt+onion_cnt} 총액:{potato_cnt*potato_price+shirimp_cnt*shirimp_price+onion_cnt*onion_price}")

processFunc(inputfunc())

