# Shows artist info for a URN or URL
import sys
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from utils import spotify

client_credentials_manager = SpotifyClientCredentials(client_id=spotify.CLIENT_ID,
                                                      client_secret=spotify.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = 'plamere'

user = sp.user(username)
pprint(user)
