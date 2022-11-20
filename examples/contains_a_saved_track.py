# Prints whether a track exists in your collection of saved tracks
import pprint
import sys

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

scope = 'user-library-read'
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

if len(sys.argv) > 1:
    tid = sys.argv[1]
else:
    print("Usage: %s track-id ..." % (sys.argv[0],))
    sys.exit()

results = sp.current_user_saved_tracks_contains(tracks=[tid])
pprint.pprint(results)
