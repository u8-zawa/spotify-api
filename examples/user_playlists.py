# Shows a user's playlists (need to be authenticated via oauth)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = 'smedjan'
playlists = sp.user_playlists(user_id)

for playlist in playlists['items']:
    print(playlist['name'])
