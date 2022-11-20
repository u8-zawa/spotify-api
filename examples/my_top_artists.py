# Shows the top artists for a user
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

scope = 'user-top-read'
ranges = ['short_term', 'medium_term', 'long_term']
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_artists(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'])
    print()
