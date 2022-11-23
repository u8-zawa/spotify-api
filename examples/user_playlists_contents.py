# Shows a user's playlists (need to be authenticated via oauth)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

scope = 'playlist-read-private'
auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        print(
            "   %d %32.32s %s" %
            (i, track['artists'][0]['name'], track['name']))


if __name__ == '__main__':
    playlists = sp.current_user_playlists()
    user_id = sp.me()['id']

    for playlist in playlists['items']:
        if playlist['owner']['id'] == user_id:
            print()
            print(playlist['name'])
            print('  total tracks', playlist['tracks']['total'])

            results = sp.playlist(playlist['id'], fields="tracks, next")
            tracks = results['tracks']
            show_tracks(tracks)

            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
