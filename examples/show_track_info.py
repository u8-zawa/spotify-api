# Shows track info for a URN or URL
import argparse
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from utils import spotify

client_credentials_manager = SpotifyClientCredentials(client_id=spotify.CLIENT_ID,
                                                      client_secret=spotify.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Get single track.')
    parser.add_argument('-t', '--tid', required=True,
                        help='Track id')
    return parser.parse_args()


def main():
    args = get_args()
    track = sp.track(args.tid)
    pprint(track)


if __name__ == '__main__':
    main()
