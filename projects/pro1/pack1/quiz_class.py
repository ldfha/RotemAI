class Machine:
    cupCount = 1
    def __init__(self):
        self.coin = int(input('동전을 입력하세요 : '))
        self.cupCount = int(input('몇 잔을 입력하세요 : '))
        self.coinin = CoinIn()
        
    def showData(self):
        success, change = self.coinin.culc(self.coin, self.cupCount)
        if success:
            print(f'커피 {self.cupCount}잔과 잔돈 {change}원')
        else: print('요금 부족')

class CoinIn:
    PRICE = 200
    def __init__(self):
        pass
    
    def culc(self, coin, cupCount):
        if coin < self.PRICE * cupCount:
            return False, 0
        return True, coin - (self.PRICE * cupCount)

if __name__ == '__main__':
    machine = Machine()
    machine.showData()