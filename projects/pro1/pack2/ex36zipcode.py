# 우편정보 파일 자료 읽기
# 키보드에서 입력한 동이름으로 해당 주소 정보 출력
def zipProcess():
    dongIrum = input('동 이름을 입력하세요 : ')
    # dongIrum = '도곡'
    with open(r'zipcode.txt', mode='r', encoding='euc-kr') as f:
        line = f.readline() # 한 행 읽기
        # print(line)
        # 135-806 서울    강남구  개포1동 경남아파트              1
        # lines = line.split('\t')    # 구분자 tab으로 문자열 자르기
        while line:
            lines = line.split(chr(9))    # chr(tab에 해당하는 ascii코드)
            if lines[3].startswith(dongIrum):
                # print(lines)
                print('우편번호 : ' + lines[0] + ', ' + lines[1] + ', ' + lines[2] + ', ' + lines[3])
            line = f.readline()
        # print(lines)
    pass

if __name__ == '__main__':
    zipProcess()