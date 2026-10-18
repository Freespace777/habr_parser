from bs4 import BeautifulSoup
import requests

base_url = "https://habr.com/ru/articles/top/daily/"
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

for article in soup.select("article"):
    name = article.select_one("h2 a span")
    view_count= article.select_one("span.tm-icon-counter__value")
    print(f'{name.text}; Количество просмотров {view_count.text}')
    

