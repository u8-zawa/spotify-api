# Delete a track from 'Your Collection' of saved tracks
import pprint
import sys

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

scope = 'user-library-modify'
auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

if len(sys.argv) > 1:
    tid = sys.argv[1]
else:
    print("Usage: %s track-id ..." % (sys.argv[0],))
    sys.exit()

results = sp.current_user_saved_tracks_delete(tracks=[tid])
pprint.pprint(results)
