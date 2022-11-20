# Removes tracks from a playlist
import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

logger = logging.getLogger('examples.remove_specific_tracks_from_playlist')
logging.basicConfig(level='DEBUG')

scope = 'playlist-modify-public'
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Remove track from user playlist')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Playlist to remove track to')
    parser.add_argument('-i', '--items', action='append',
                        required=True, help='Track ids and Position of the track in the playlist')
    return parser.parse_args()


def main():
    args = get_args()
    items = []
    for item in args.items:
        tid, pos = item.split(',')
        items.append({"uri": tid, "positions": [int(pos)]})
    sp.playlist_remove_specific_occurrences_of_items(args.playlist, items)


if __name__ == '__main__':
    main()
