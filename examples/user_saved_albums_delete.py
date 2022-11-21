# Deletes user saved album
import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

logger = logging.getLogger('examples.user_saved_albums_delete')
logging.basicConfig(level='DEBUG')

scope = 'user-library-modify'
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Delete a playlist for user')
    parser.add_argument('-a', '--aids', action='append',
                        required=True, help='Album ids')
    return parser.parse_args()


def main():
    args = get_args()
    sp.current_user_saved_albums_delete(albums=args.aids)


if __name__ == '__main__':
    main()
