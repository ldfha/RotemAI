# 문1) 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
n = 1
hap = 0
while n <= 100:
    if n % 3 == 0 and n % 2 != 0:
        print(n)
        hap += n
    n +=1
print(hap)

# 문2) 2 ~ 5 까지의 구구단 출력
# --------for---------
# for i in range(2, 6):
#     print(f'----{i}단----')
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')

# --------while---------
i = 2    
while i < 6:
    print(f'----{i}단----')
    j = 1
    while j <= 9:
        print(f'{i} * {j} = {i*j}')
        j += 1
    i +=1

# 문3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
i = 1
tot = 0
while i <= 100:
    if i % 2 == 0:
        tot += i
    else:
        tot -= i
    i += 1
print(tot)

# 문4) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
i = 1
iter = 0
tot = 0
while i < 100:
    if iter % 2 == 0:
        j = -i
        tot += j
    else:
        tot += i
    i += 2
    iter += 1
print(tot)

# 문5) 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력
i = 1
while i <= 100:
    i_str = list(str(i))
    # print(i_str)
    i_int = list(map(int, i_str))
    # print(i_int)
    i_sum = sum(i_int)
    if(i_sum) >= 10:
        print(i, end =' ')
    i += 1

num = 1
while num <= 100:
    temp = num
    digit_sum = 0
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum >= 10:
        print(num, end=' ')
    num += 1

# 문6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력
i = 1
total = 0
while total <= 1000:
    total += i
    i += 1

print(i-1, total)

# # 문7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
# # --------for---------
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i * j > 30 :
#             break
#         print(f'{i} * {j} = {i * j}')

# # --------while---------
i = 1
while i < 9:
    j = 0
    i += 1
    while j < 9:
        j += 1
        if i * j > 30 : 
            break
        print(f'{i} * {j} = {i * j}', end=' ')


# 문8) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
i = 2
num = 0
while i <= 1000:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else: 
        num += 1
        j += 1
        print(i, end=' ')
    i += 1
print('\n', num)

# -----선생님 답안-----
num = 2
count = 0
while num <= 1000:
    i = 2
    is_Prime = True
    while i < num:
        if num % i == 0:
            is_Prime = False
            break
        i += 1
    if is_Prime:
        print(num, end=' ')
        count += 1
    num += 1
print('\n갯수 :', count)


# ----------continue-----------

# 문제1) 1부터 50까지의 숫자 중 3의 배수는 건너뛰고 나머지 수만 출력하라
i = 1
while i <= 50:
    if i % 3 == 0:
        i += 1
        continue
    else:
        print(i, end=' ')
    i += 1

print()

# 문제2) 1부터 100까지 출력하되 4의 배수, 6의 배수는 건너뛴다. 그 외의 수 중 5의 배수만 출력하고 그들의 합도 출력하라
i = 1
total = 0
while i <= 100:
    if i % 4 == 0 or i % 6 == 0 or i % 5 != 0:
        i += 1
        continue
    else:
        print(i, end=' ')
        total += i
        i += 1
print('\ntotal: ', total)