# Shows artist info for a URN or URL
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI)
sp = spotipy.Spotify(auth_manager=auth_manager)

response = sp.new_releases()

while response:
    albums = response['albums']
    for i, item in enumerate(albums['items']):
        print(albums['offset'] + i, item['name'])
    if albums['next']:
        response = sp.next(albums)
    else:
        response = None
