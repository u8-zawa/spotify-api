# Shows artist info for a URN or URL
import sys
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from settings import CLIENT_ID, CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                      client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = 'plamere'

user = sp.user(username)
pprint(user)
