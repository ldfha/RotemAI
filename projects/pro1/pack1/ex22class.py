# 클래스는 새로운 타입을 만들어 자원을 공유한다.

# class Singer:
#     title_song = "빛나라 대한민국"  # 멤버 필드

#     def sing(self):
#         msg = "노래는 "     # 지역변수
#         print(msg, self.title_song)


# import ex22singer
# bts = ex22singer.Singer()

from ex22singer import Singer

bts = Singer()  # 생성자 호출하여 객체 생성 후 주소 치환
bts.sing()
print(type(bts))
bts.title_song = "Permission to Dance"
bts.sing()
bts.co = "빅히트 엔터테인먼트"
print('소속사:', bts.co)

print()

ive = Singer()
ive.sing()
print(type(ive))
# print('소속사:', ive.co)
Singer.title_song = '아 대한민국'
bts.sing()
ive.sing()

niceGroup = ive
niceGroup.sing()
print(f'niceGroup : {id(niceGroup)}, ive : {id(ive)}')