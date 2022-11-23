# Shows artist info for a URN or URL
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI)
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
