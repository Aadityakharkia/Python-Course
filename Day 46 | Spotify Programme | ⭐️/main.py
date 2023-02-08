# One of the Hardest Project

# Using spotipy API to access Spotify

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
date = input(f"Please Enter the Date in the formate of YYYY-MM-DD\n")

Spotify_Clint_id = "Your ID"
Spotify_Clint_Secret = "Your ID"
Spotify_API_URL = "https://api.spotify.com/v1"

 # ------------------- Read the API to understand the parameters ------------------

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Spotify_Clint_id,
        client_secret=Spotify_Clint_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

#---------------------------------------- Web Scrapping ------------------------------

response = requests.get(URL + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("div", class_="o-chart-results-list-row-container")
song_names = [container.h3.getText().strip() for container in song_names_spans]

print(song_names)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# ----------------------------------------- Description ----------------------------------------

# This was one of the hardest project i have ever done, had to take help from the discord section in order to get the exacct address of the element
# In the web i am looking for. SharahZ helped me find the exact address.