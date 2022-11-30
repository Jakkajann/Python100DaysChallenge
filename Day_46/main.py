# Couldn't complete this, need to study spotipy documentation

from http import client
import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client = os.environ.get("SPOTIFY_CLIENT")
client_secret = os.environ.get("SPOTIFY_SECRET")

billboard_ulr = "https://www.billboard.com/charts/hot-100/"

sp = spotipy.Spotify(
    auth_manager = spotipy.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

date = date.split(sep="-")

year = date[0]
month = date[1]
day = date[2]

response = requests.get(url=f"{billboard_ulr}{year}-{month}-{day}")

soup = BeautifulSoup(response.text, "html.parser")


with open("Day_46/playlist.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())


song_name_spans = soup.find_all("h3", id="title-of-a-story", class_="c-title")
song_names = [song_names.get_text().strip() for song_names in song_name_spans]
song_names = list(dict.fromkeys(song_names))
song_names.remove("Songwriter(s):")
song_names.remove("Producer(s):")
song_names.remove("Imprint/Promotion Label:")
song_names.remove("Gains in Weekly Performance")
song_names.remove("Additional Awards")
song_names = song_names[1:101:]
print(song_names)