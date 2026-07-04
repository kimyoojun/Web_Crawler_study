# 단일 상품 크롤링

import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding.pythonanywhere.com/basic")
html = response.text
soup = BeautifulSoup(html, "html.parser")

# 매칭되는 여러개의 태그중 첫번째만 반환
soup.select_one(".product-category")

# 하위 태그를 가져올때는 > "태그명" 로 가져올수 있음
soup.select_one(".product-name > a")

# print(soup.select_one(".product-category"))
category = soup.select_one(".product-category").text
# print(soup.select_one(".product-name"))
name = soup.select_one(".product-name").text
link = soup.select_one(".product-name > a").attrs["href"]
# strip()으로 앞뒤 공백 제거
# replase("변경전 문자","변경후 문자")
price = soup.select_one(".product-price").text.strip().replace(",", "").replace("원", "")

print("상품 카테고리: ", category)
print("상품명: ", name)
print("상품 링크: ", link)
print("상품 가격: ", price)
