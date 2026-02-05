kor = 100       # 모듈의 전역변수

def abc():
    kor = 0     # 함수 내의 지역 변수
    print('모듈의 멤버 함수')

class My:
    kor = 80    # My 멤버 변수(field)
    
    def abc(self):
        print('My member method')

    def show(self):
        # kor = 77        # 메소드 내의 지역 변수
        print(kor)
        print(self.kor)
        self.abc()
        abc()

my = My()
my.show()

print('-------------------')
print(My.kor)
tom = My()
print(tom.kor)
tom.kor = 88
print(tom.kor)

oscar = My()    # 새로운 객체
print(oscar.kor)