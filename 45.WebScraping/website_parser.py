from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

articles = soup.select(".titleline > a")
upvotes = soup.select(".score")

texts = []
links = []
scores = []

for article in articles:
    texts.append(article.text)
    links.append(article.get("href"))
for upvote in upvotes:
    scores.append(int(upvote.text.strip()[0]))

max_score_indexes = []
max_score = 0
for i in range(len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]

for i in range(len(scores)):
    if scores[i] == max_score:
        max_score_indexes.append(i)

for index in max_score_indexes:
    print(texts[index])
    print(links[index])
    print(scores[index])
    print()
