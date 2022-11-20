import argparse

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

scope = [
    'playlist-modify-private',
    'playlist-modify-public'
]
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Follows a playlist based on playlist ID')
    parser.add_argument('-p', '--playlist', required=True, help='Playlist ID')

    return parser.parse_args()


def main():
    args = get_args()
    sp.current_user_follow_playlist(args.playlist)


if __name__ == '__main__':
    main()
