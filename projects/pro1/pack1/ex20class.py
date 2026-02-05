class Car:
    handle = 0
    speed = 0

    def __init__(self, name, speed):
        self.name = name    # 현재 객체의 name(self.name)에게 지역변수 name 인자값 치환
        self.speed = speed

    def showData(self):
        km = "킬로미터"
        msg = "속도:" + str(self.speed) + km
        return msg

print(Car.handle)   # 원형(prototype) 클래스의 멤버 호출
car1 = Car('tom', 10) # 생성자 호출 후 객체 생성(인스턴스화)
print('car1 : ', car1.name, ' ', car1.speed, ' ', car1.handle)