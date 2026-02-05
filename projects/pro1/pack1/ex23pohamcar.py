# 여러개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함 관계 사용 (자원의 재활용)
# 다른 클래스를 마치 자신의 멤버처럼 선언하고 사용

from ex23pohamhandle import PohamHandle

class PohamCar:
    # 멤버 필드
    turnShowMessage = "정지"
    
    def __init__(self, ownerName):
        # ownerName = ownerName
        self.ownerName = ownerName
        self.handle = PohamHandle()     # 클래스의 포함 관계


    def turnHandle(self, q):
        if q > 0 :
            self.turnShowMessage = self.handle.rightTurn(q)
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0 :
            self.turnShowMessage = self.handle.goStraight(q)

if __name__ == '__main__':      # 메인 모듈인지 확인
    tom = PohamCar("미스터 톰")
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + ' ' + str(tom.handle.quantity))
    john = PohamCar("미스터 존")
    john.turnHandle(-20)
    print(john.ownerName + '의 회전량은 ' + john.turnShowMessage + ' ' + str(john.handle.quantity))
    john.turnHandle(0)
    print(john.ownerName + '의 회전량은 ' + john.turnShowMessage + ' ' + str(john.handle.quantity))
