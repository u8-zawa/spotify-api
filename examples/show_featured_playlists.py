# Shows artist info for a URN or URL
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI)
sp = spotipy.Spotify(auth_manager=auth_manager)

response = sp.featured_playlists()
print(response['message'])

while response:
    playlists = response['playlists']
    for i, item in enumerate(playlists['items']):
        print(playlists['offset'] + i, item['name'])
    if playlists['next']:
        response = sp.next(playlists)
    else:
        response = None
