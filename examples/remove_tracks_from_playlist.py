# Removes tracks from playlist
import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

logger = logging.getLogger('examples.remove_tracks_from_playlist')
logging.basicConfig(level='DEBUG')

scope = 'playlist-modify-public'
auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Remove track from user playlist')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Playlist to remove track to')
    parser.add_argument('-t', '--tids', action='append',
                        required=True, help='Track ids')
    return parser.parse_args()


def main():
    args = get_args()
    sp.playlist_remove_all_occurrences_of_items(args.playlist, args.tids)


if __name__ == '__main__':
    main()
