# Shows a user's saved tracks (need to be authenticated via oauth)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

scope = 'user-library-read'
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def show_tracks(results):
    for item in results['items']:
        track = item['track']
        print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


results = sp.current_user_saved_tracks()
show_tracks(results)

while results['next']:
    results = sp.next(results)
    show_tracks(results)
