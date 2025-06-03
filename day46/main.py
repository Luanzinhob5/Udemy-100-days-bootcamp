import requests
from bs4 import BeautifulSoup

SPOTIFY_ID = "215afc444abf4f0fb85c5c5fb1a0b7de"
SPOTIFY_SECRET = "08f8142595cb41748bf3ca9a0cd1021a"

date = input("Which year you want travel to? Type the date in this format YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/" + date
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=url,headers=header)
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)




