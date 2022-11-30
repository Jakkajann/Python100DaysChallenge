# 100 top movies

import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

with open("Day_45/movies.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.get_text() for movie in all_movies]
movie_titles = movie_titles[::-1]

with open("Day_45/movies.txt", "w", encoding="utf-8") as file:
    for titles in movie_titles:
        file.write(titles + "\n")