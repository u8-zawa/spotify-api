# Replaces all tracks in a playlist
import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

logger = logging.getLogger('examples.replace_tracks_in_playlist')
logging.basicConfig(level='DEBUG')

scope = 'playlist-modify-public'
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Replace all tracks/episodes in a playlist')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Playlist to replace track to')
    parser.add_argument('-t', '--tids', action='append',
                        required=True, help='Track ids')
    return parser.parse_args()


def main():
    args = get_args()
    sp.playlist_replace_items(args.playlist, args.tids)


if __name__ == '__main__':
    main()
