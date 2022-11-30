# Live website web scraping

from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/newest")



soup = BeautifulSoup(response.text, "html.parser")

with open("Day_45/news.html", "w") as file:
    file.write(soup.prettify())

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles: 

    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)