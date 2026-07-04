# 여러 상품 크롤링

import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding.pythonanywhere.com/basic")
html = response.text
soup = BeautifulSoup(html, "html.parser")

# select는 매칭되는 태그를 전부 가져오고 리스트로 반환
items = soup.select(".product")

# for문으로 리스트 순회
for item in items:
    category = item.select_one(".product-category").text
    name = item.select_one(".product-name").text
    link = item.select_one(".product-name > a").attrs["href"]
    # split으로 "원"을 기준으로 텍스트를 자르고 0번째 인덱스를 가져옴
    price = item.select_one(".product-price").text.split("원")[0].replace(",", "")

    print("상품 카테고리: ", category)
    print("상품명: ", name)
    print("상품 링크: ", link)
    print("상품 가격: ", price)
