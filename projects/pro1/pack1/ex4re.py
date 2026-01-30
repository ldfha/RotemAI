import re       # 정규표현식 지원 모듈 로딩

ss = "1234 abc가나다abcABC_123555집에가나78요_6'Python is fun'"
print(ss)
print(re.findall(r'123', ss))   # r 반드시 필요함 | return type : list
print(re.findall(r'가나', ss))
print(re.findall(r'[0-9]', ss)) # 숫자[0-9]
print(re.findall(r'[0-9]+', ss)) # 숫자 1개 이상 붙어있으면 붙어나옴
print(re.findall(r'[0-9]{2}', ss)) # 숫자 2개씩 묶음
print(re.findall(r'[0-9]{2,3}', ss)) # 숫자 2개묶음, 3개묶음
print(re.findall(r'[a-zA-Z]', ss)) # 영어
print(re.findall(r'[가-힣]', ss)) # 한글
print(re.findall(r'\d', ss)) # 숫자
print(re.findall(r'\D+', ss)) # 숫자만 빼고


