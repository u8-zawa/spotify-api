import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from utils import spotify

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

client_credentials_manager = SpotifyClientCredentials(client_id=spotify.CLIENT_ID,
                                                      client_secret=spotify.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print((album['name']))
