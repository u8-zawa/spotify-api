# Shows a user's playlists
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

scope = 'playlist-read-private'
auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))
