from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

articles = soup.find_all(name="span", class_="titleline")
# print(articles.find(name="a").getText())

for article_tag in articles:
    print(article_tag.find(name="a").getText())

