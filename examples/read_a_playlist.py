from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

from settings import CLIENT_ID, CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                      client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJiZcmkrIHGU'
results = sp.playlist(playlist_id)
print(json.dumps(results, indent=4))
