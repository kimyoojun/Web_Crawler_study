# 크롤링한 데이터 엑셀로 저장

import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for i in range(1, 5):
    response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".product")

    for item in items:
        category = item.select_one(".product-category").text
        name = item.select_one(".product-name").text
        link = item.select_one(".product-name > a").attrs["href"]
        price = item.select_one(".product-price").text.split("원")[0].replace(",", "")

        # print("상품 카테고리: ", category)
        # print("상품명: ", name)
        # print("상품 링크: ", link)
        # print("상품 가격: ", price)

        # data 리스트에 리스트 형태로 값을 추가하여 2차원 리스트 생성
        data.append([category, name, link, price])

# 데이터 프레임 만들기   
df = pd.DataFrame(data, columns = ["카테고리", "상품명", "상세페이지링크", "가격"])

# 엑셀 저장
df.to_excel("result.xlsx", index=False)
