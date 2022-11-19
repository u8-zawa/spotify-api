import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

if __name__ == '__main__':
    scope = [
        'user-top-read',
        'user-read-recently-played'
    ]
    auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                redirect_uri=REDIRECT_URI,
                                scope=scope)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # よく聞く曲 (20曲)
    top_tracks = sp.current_user_top_tracks(limit=20)['items']
    top_tracks_id = [track['id'] for track in top_tracks]

    # 最近聞いた曲 (30曲)
    recently_played_tracks = sp.current_user_recently_played(limit=30)['items']
    recently_played_tracks_id = [track['track']['id'] for track in recently_played_tracks]

    # よく聞く曲 : 最近聞いた曲 = 3 : 2 の割合でそれぞれ無作為抽出をする
    seed_tracks = random.sample(top_tracks_id, 3) + random.sample(recently_played_tracks_id, 2)

    recommend = sp.recommendations(seed_tracks=seed_tracks)

    for idx, item in enumerate(recommend['tracks']):
        print(idx, item['artists'][0]['name'], " – ", item['name'])
