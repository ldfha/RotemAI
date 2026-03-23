# BeautifulSoup 객체 메소드 활용
from bs4 import BeautifulSoup

html_page = """
<html><body>
<h1>제목 태그</h1>
<p>웹문서 연습</p>
<p>원하는 자료 확인</p>
</body></html>
"""
print(type(html_page))
soup = BeautifulSoup(html_page, 'html.parser')
print(type(soup))
print()
h1 = soup.html.body.h1

soup3 = BeautifulSoup(html_page, 'html.parser')
# 정규표현식 쓰기
import re
links2 = soup3.find_all(href=re.compile(r'^https'))
for k in links2:
    print(k.attrs['https'])


print('---bugs 사이트 음악 순위 읽기---')
import requests
url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
bsoup = BeautifulSoup(response.text, 'html.parser')
musics = bsoup.find_all("td", class_="check")
for idx, music in enumerate(musics):
    print(f"{idx + 1}위) {music.input['title']}")