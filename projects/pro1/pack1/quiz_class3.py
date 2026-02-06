class Animal:
    def __init__(self):
        pass
    
    def move(self):
        print('움직인다.')

class Dog(Animal):
    name = '개'
    
    def move(self):
        print('dog move')

class Cat(Animal):
    name = '고양이'
    def move(self):
        print('cat move.')

class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    def move(self):
        print('fox move')

    def foxMethod(self):
        print('foxMethod')

fox = Fox()
print(fox.name)
fox.foxMethod()
fox.move()

wolf = Wolf()
print(wolf.name)
wolf.move()