# pack1/ex15module - main
print('사용자 지정 모듈')

print('\n경로 지정 방법1 : import [모듈명]')

import pack1.mymod1
print(dir(pack1.mymod1))
print(pack1.mymod1.__file__)  # 경로
print(pack1.mymod1.__name__)  # 모듈명

list1 = [1,2]
list2 = [3, 4, 5]
pack1.mymod1.listHap(list1, list2)

if __name__ == '__main__':
    print('나는 ex15module 메인')

print('\n경로 지정 방법2 : from [모듈명] import [함수명] 또는 변수')
from pack1.mymod1 import kbs
kbs()
from pack1.mymod1 import mbc, tot
mbc()
print(tot)

from pack1.mymod1 import *    # *을 사용해 pack1.mymod1 모듈의 모든 멤버 로딩(비권장)
print(tot)

from pack1.mymod1 import mbc as 엠비씨만새별명
엠비씨만새별명()

print('\n경로 지정 방법3 : import 하위패키지.모듈명')
import pack1.subpack.sbs
pack1.subpack.sbs.sbsMansae()

import pack1.subpack.sbs as nickname
nickname.sbsMansae()

print('\n경로 지정 방법4 : 현재 package와 동등한 다른 패키지 모듈 읽기')
# import ../pack1_other.mymod2  # VScode에서는 사용할 수 없는 방법
from pack1_other import mymod2
print(mymod2.hapFunc(4, 3))

import mymod3
result = mymod3.gopFunc(4, 3)
print('path가 설정된 곳의 module 읽기 - result:', result)
