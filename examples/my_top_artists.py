# Shows the top artists for a user
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

scope = 'user-top-read'
ranges = ['short_term', 'medium_term', 'long_term']
auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_artists(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'])
    print()
