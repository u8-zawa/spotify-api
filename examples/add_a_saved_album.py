import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

logger = logging.getLogger('examples.add_a_saved_album')
logging.basicConfig(level='DEBUG')

scope = 'user-library-modify'
auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Creates a playlist for user')
    parser.add_argument('-a', '--aids', action='append',
                        required=True, help='Album ids')
    return parser.parse_args()


def main():
    args = get_args()
    sp.current_user_saved_albums_add(albums=args.aids)


if __name__ == '__main__':
    main()
