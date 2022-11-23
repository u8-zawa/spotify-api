# Shows tracks for the given artist
import argparse

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from utils import spotify

client_credentials_manager = SpotifyClientCredentials(client_id=spotify.CLIENT_ID,
                                                      client_secret=spotify.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-a', '--artist', required=True,
                        help='Name of Artist')
    return parser.parse_args()


def main():
    args = get_args()
    results = sp.search(q=args.artist, limit=20)
    for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'])


if __name__ == '__main__':
    main()
