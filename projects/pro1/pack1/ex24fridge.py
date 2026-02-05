# 클래스의 포함관계 연습 - 냉장고 객체에 음식 객체 담기

class Fridge:
    isOpen = False
    foods = []
    
    def open(self):
        self.isOpen = True
        print("냉장고 문 열기")
    
    def close(self):
        self.isOpen = False
        print("냉장고 문 닫기")

    def foodsList(self):    # 냉장고 문이 열린 경우
        for f in self.foods:
            print(f' - {f.name} {f.expiry_date}')
        print()
        
    def put(self, thing):
        if self.isOpen:
            self.foods.append(thing)
            print(f'냉장고에 {thing.name} 넣음')
            self.foodsList()
        else:
            print('냉장고 문이 닫혀있음')


class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date
    

fObj = Fridge()
apple = FoodData('apple', '2026-08-01')
fObj.put(apple)
fObj.open()
fObj.put(apple)
fObj.close()
print()
coke = FoodData('coke', '2027-11-01')
fObj.open()
fObj.put(coke)
fObj.close()