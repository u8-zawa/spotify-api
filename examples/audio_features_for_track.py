# Shows acoustic features for tracks for the given artist
from __future__ import print_function  # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys

from settings import CLIENT_ID, CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                      client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True

if len(sys.argv) > 1:
    tids = sys.argv[1:]
    print(tids)

    start = time.time()
    features = sp.audio_features(tids)
    delta = time.time() - start
    print(json.dumps(features, indent=4))
    print("features retrieved in %.2f seconds" % (delta,))
