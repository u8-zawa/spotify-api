from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint

from settings import CLIENT_ID, CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                      client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = 'spotify:playlist:5RIbzhG2QqdkaP24iXLnZX'
offset = 0

while True:
    response = sp.playlist_items(playlist_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])

    if len(response['items']) == 0:
        break

    pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])
