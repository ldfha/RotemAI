# 반복문 for
# for i in [1,2,3,4,5]:
# for i in (1,2,3,4,5):
# for i in {1,2,3,4,5}:
#     print(i, end = ' ')

# print("분산/표준편차 --- ")
# numbers = [1, 3, 5, 7, 9]       # 40.0 / 8.0 / 2.8284271247461903
# # numbers = [3, 4, 5, 6, 7]     # 10.0 / 2.0 / 1.4142135623730951
# # numbers = [-3, 4, 5, 7, 12]   # 118.0 / 23.6 / 4.857983120596447
# tot = 0
# for a in numbers:
#     tot += a
# print(f"합은 {tot}, 평균은 {tot / len(numbers)}")
# avg = tot / len(numbers)
# # 편차제곱의 합
# hap = 0
# for i in numbers:
#     hap += (i - avg) ** 2
# print(f"편차 제곱의 합 {hap}")
# vari = hap / len(numbers)
# print(f"분산은 {vari}")
# print(f"표준편차는 {vari ** 0.5}")

# colors = ['r', 'g', 'b']
# for v in colors:
#     print(v, end = ' ')

# print('\niter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수')
# iterator = iter(colors)
# for v in iterator:
#     print(v, end = ', ')

# print()
# for idx, d in enumerate(colors):    # 인덱스와 값을 반환
#     print(idx, ' ', d)

# print('사전형 ---' )
# datas = {'python':'만능언어', 'java':'웹용언어', 'mariadb':'RDBMS'}
# for data in datas.items():
#     # print(data)
#     print(data[0], ' ~~ ', data[1])
# print()
# for k, v in datas.items():
#     print(k, ' -- ', v)
# print()
# for k in datas.keys():
#     print(k, end = " ")
# print()
# for v in datas.values():
#     print(v , end=" ")
# print()

# print("------- 다중 for문 -------")
# for n in [2, 3]:
#     print("--- {}단 ---".format(n))
#     for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#         print("{} * {} = {}".format(n, i, n*i))

# print('continue와 break')
# nums = {1,2,3,4,5}
# for i in nums:
#     if i == 2 : continue
#     # if i == 4 : break
#     print(i, end=" ")
# else :
#     print("정상 종료")

# print("정규 표현식 + for")
# str = """전 세계를 충격에 빠뜨린 트럼프 미국 대통령이 마두로 베네수엘라 대통령을 급습한 당시 상황이 공개된다. 1일 방송되는 채널A ‘이제 만나러 갑니다’ (연출 김군래/작가 장주연, 이하 ‘이만갑’)에서는 새해를 맞이한 지 얼마 되지 않은 1월 3일 새벽 베네수엘라 수도 카라카스에서 엄청난 폭발음이 들려왔던 사건에 대해 살펴본다. 이는 미국이 베네수엘라의 방공망과 주요 군사 시설을 타격해 마두로 대통령 부부가 은신 중이던 대통령 궁을 급습한 것이었는데. 한 나라의 대통령이 자국 수도에서 생포되는 초유의 상황에 전 세계가 충격에 휩싸였다는 후문이다."""
# import re
# str2 = re.sub(r'[^가-힣\s]', '', str)    # 한글과 공백 이외의 문자는 공백 처리
# print(str2)
# print()
# str3 = str2.split(' ')  # 공백을 기준으로 문자 분리
# print(str3)

# print()
# cou = {}    # 단어의 발생 횟수 set 혹은 dict

# for i in str3:
#     if i in cou:
#         cou[i] += 1     # 같은 단어가 있으면 누적
#     else:
#         cou[i] = 1      # 최초 단어인 경우는 '단어':1

# print(cou)

# print('정규표현식 연습2')
# import re
# for test_ss in ['111-1234', '일이삼-일이삼사', '222-2345', '333&5132']:
#     if re.match(r'^\d{3}-\d{4}$', test_ss):
#         print(test_ss, '전화번호 맞아요')
#     else:
#         print(test_ss, '전화번호 아니야')

# print('comprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현')
# a = [1,2,3,4,5,6,7,8,9,10]
# li = []
# for i in a:
#     if i % 2 == 0:
#         li.append(i)
# print(li)

# print(list(i for i in a if i % 2 == 0))

# # datas = [1, 2, 'a', True, 3.0]
# datas = {1, 2, 'a', True, 3.0, 2, 1, 2, 1, 2, 2}    # 중복 배제
# li2 = [i * i for i in datas if type(i) == int]
# print(li2)

# id_name = {1:'tom', 2:'oscar'}
# name_id = {val:key for key, val in id_name.items()}
# print(name_id)

# print([1,2,3])
# print(*[1,2,3])     # * : unpack

# aa = [(1, 2), (3, 4), (5, 6)]
# for a, b in aa:
#     print(a + b)
# print([a + b for a, b in aa])
# print(*[a + b for a, b in aa], sep='\n')

# print("수열 생성 : range")
# print(list(range(1, 6)))    # [1, 2, 3, 4, 5]
# print(tuple(range(1, 6, 2)))    # (1, 3, 5)
# print(list(range(-10, -100, -20)))    # [-10, -30, -50, -70, -90]
# print(set(range(1, 6, 2)))    # {1, 3, 5}

# for i in range(6):
#     print(i, end = ' ')

# for _ in range(6):
#     print('반복')

# tot = 0
# for i in range(1, 11):
#     tot += i
# # print(tot)
# print(sum(range(1, 11)))
# for i in range(1, 10):
#     print(f'2 * {i} = {2 * i}')
# print('end')

# 문제 1 : for문 2~9 구구단 출력 (단은 행 단위 출력)
for i in range (2, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}', end=' ')
    print()

# 문제 2 : 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# import random
# for i in range(10):
#     dice1 = random.randrange(1, 7)
#     dice2 = random.randrange(1, 7) 
#     print(dice1, dice2)
#     if (dice1 + dice2) % 4 == 0:
#         print(dice1 + dice2)
for i in range(1, 7):
    for j in range(1, 7):
        if (i + j) % 4 == 0:
            print(i, j)
