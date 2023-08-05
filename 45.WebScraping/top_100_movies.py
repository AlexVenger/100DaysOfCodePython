from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select("h3.title")
movie_list = []
for movie in movies:
    movie_list.append(movie.text)

with open("movies.txt", "w", encoding="utf-8") as movies_file:
    for i in range(-1, -len(movie_list)-1, -1):
        movies_file.write(f"{movie_list[i]}\n")
