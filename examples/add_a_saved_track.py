import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

logger = logging.getLogger('examples.add_a_saved_track')
logging.basicConfig(level='DEBUG')

scope = 'user-library-modify'
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Add tracks to Your '
                                                 'Collection of saved tracks')
    parser.add_argument('-t', '--tids', action='append',
                        required=True, help='Track ids')
    return parser.parse_args()


def main():
    args = get_args()
    sp.current_user_saved_tracks_add(tracks=args.tids)


if __name__ == '__main__':
    main()
