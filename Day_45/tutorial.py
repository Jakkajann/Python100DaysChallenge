# Web scraping

from bs4 import BeautifulSoup
# import lxml

with open("Day_45/website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)