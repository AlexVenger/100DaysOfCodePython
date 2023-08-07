import json
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which date would you wish to travel to? Type the date in YYYY-MM-DD format: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select("li.lrv-u-width-100p h3")
artists = soup.select("li.lrv-u-width-100p h3 + span")

bad_chars = ["\n", "\t"]

songs_list = []
for i in range(100):
    song = songs[i].text
    artist = artists[i].text
    # To remove these symbols from titles of the songs
    for c in bad_chars:
        song = song.replace(c, "")
        artist = artist.replace(c, "")
    songs_list.append({"song": song, "artist": artist})

with open("spotify_credentials.json") as credentials:
    data = json.load(credentials)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=data["client_id"],
        client_secret=data["secret"],
        redirect_uri=data["uri"],
        scope="playlist-modify-private"
    ))

playlist = sp.user_playlist_create(user=f"{sp.current_user()['id']}", name=date, public=False)

not_on_spotify = []
spotify_songs = []

year = date.split("-")[0]
for song in songs_list:
    try:
        spotify_song = sp.search(q=f"track:{song['song']} year:{year}")
        spotify_songs.append(spotify_song["tracks"]["items"][0]["uri"])
    except Exception:
        not_on_spotify.append(song)

sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_songs)
if len(not_on_spotify) > 0:
    tracks_not_found = "Unfortunately, the following tracks were not found:"
    for track in not_on_spotify:
        tracks_not_found += f"\n{track['song']} by {track['artist']}"
    print(tracks_not_found)
