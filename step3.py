# 여러 페이지 크롤링

import requests
from bs4 import BeautifulSoup

for i in range(1, 5):
    # 페이지 번호 부분만 반복문으로 바꿔주면서 출력
    response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".product")

    for item in items:
        category = item.select_one(".product-category").text
        name = item.select_one(".product-name").text
        link = item.select_one(".product-name > a").attrs["href"]
        price = item.select_one(".product-price").text.split("원")[0].replace(",", "")

        print("상품 카테고리: ", category)
        print("상품명: ", name)
        print("상품 링크: ", link)
        print("상품 가격: ", price)
