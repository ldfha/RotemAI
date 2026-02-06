# 2. 클래스의 상속관계 연습문제 - 다형성 
class ElecProduct:
    volume = 0

    def volumeControl(self, volume):
        print('volume : ', self.volume)


class ElecTv(ElecProduct):
    def tv1(self):
        print('ElecTv 고유 메소드')
    def volumeControl(self, volume):
        print('Tv Volume :', volume)

class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        print('Radio Volume : ', volume)

# q1 = [ElecTv(), ElecRadio()]
# for q in q1:
#     q.volumeControl()


elecP = ElecProduct()
elecP.volumeControl(0)

tv = ElecTv()
elecp = tv
elecP.volumeControl(10)

radio = ElecRadio()
elecP = radio
elecP.volumeControl(20)