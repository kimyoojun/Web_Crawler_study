import requests
from bs4 import BeautifulSoup

# 주소에 해당하는 페이지의 데이터를 가져옴
reponse = requests.get("https://startcoding.pythonanywhere.com/basic")

# 응답 코드 출력 (성공시 200, 실패시 404)
# print(reponse.status_code)

# 웹 페이지 HTML 출력
# print(reponse.text)

html = reponse.text

# HTML 을 "html.parser"가 태그 객체로 잘라서 soup에 담아줌
soup = BeautifulSoup(html, "html.parser")

# print(soup)

# 하나의 속성을 가져올수 있음 () 안에 속성을 입력
# soup.select_one(".brand-name")

# print(soup.select_one(".brand-name").text)

# 태그 속성의 접근 [] 안에 키값을 입력
# soup.select_one(".brand-name").attrs["href"]


