# Shows a user's playlists (need to be authenticated via oauth)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = 'smedjan'
playlists = sp.user_playlists(user_id)

for playlist in playlists['items']:
    print(playlist['name'])
