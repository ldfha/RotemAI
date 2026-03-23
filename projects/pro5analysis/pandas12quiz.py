import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent":"Mozilla/5.0"}
with open("stock.csv", mode='w', encoding='utf-8-sig') as f:
    f.write("종목명,시세,시가총액\n")
    for page in range(1, 3):
        url = f"https://finance.naver.com/sise/sise_market_sum.naver?&page={page}"
        res = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        rows = soup.select("table.type_2 tr")
        for row in rows[2:]:
            name_tag = row.select_one("a.tltle")
            cols = row.select("td.number")

            if name_tag and len(cols) > 0:
                name = name_tag.get_text(strip=True)
                sise = int(cols[0].get_text(strip=True).replace(',',''))
                total = int(cols[4].get_text(strip=True).replace(',',''))
                # print(name, sise, total)
                f.write(f"{name},{sise},{total}\n")

stock = pd.read_csv("stock.csv")
# print(stock)
top3 = stock.sort_values(by='시가총액', ascending=False).head(3)
print(top3[['종목명','시가총액']])