import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

logger = logging.getLogger('examples.add_tracks_to_playlist')
logging.basicConfig(level='DEBUG')

scope = 'playlist-modify-public'
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Adds track to user playlist')
    parser.add_argument('-t', '--tids', action='append',
                        required=True, help='Track ids')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Playlist to add track to')
    return parser.parse_args()


def main():
    args = get_args()
    sp.playlist_add_items(args.playlist, args.tids)


if __name__ == '__main__':
    main()
