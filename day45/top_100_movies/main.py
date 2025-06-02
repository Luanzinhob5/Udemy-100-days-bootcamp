from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

site_span = soup.find_all(name="h2")
film_list = [film_text.getText() for film_text in site_span]

del film_list[:3]
corret_film_list = film_list[::-1]

with open("top_100_movies.txt", "w") as lista_filmes:
    for film in corret_film_list:
        lista_filmes.write(f"{film}\n")
        
