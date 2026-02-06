# 추상 클래스
# 추상 메소드를 가진 클래스를 추상 클래스라고 하며
# 인스턴스 할 수 없다. 객체 생성 불가
# 부모 클래스로만 사용됨

from abc import *

class AbstractClass(metaclass=ABCMeta):
    @abstractmethod     # 추상 메소드를 하나라도 가지고 있으면 추상 클래스가 된다
    def abcMethod(self):
        pass

    def normalMethod(self): 
        print('추상 클래스 내의 일반 메소드')

# parent = AbstractClass()      # 에러 : 추상클래스는 객체 생성 불가

class Child1(AbstractClass):
    name ='난 Child1'

    def abcMethod(self):
        print('abcMethod')

c1 = Child1()
print('name : ', c1.name)
c1.abcMethod()
c1.normalMethod()

class Child2(AbstractClass):
    def abcMethod(self):
        print('추상 클래스 내의 abcMethod 재정의')

    def normalMethod(self):     # 일반 메소드 재정의
        print('일반 메소드 내 맘대로 내용 변경')

c2 = Child2()
c2.abcMethod()
c2.normalMethod()

print('---------- 다형성')
happy = c1
happy.abcMethod()
happy = c2
happy.abcMethod()