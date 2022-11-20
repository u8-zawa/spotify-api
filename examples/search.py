# Shows artist info for a URN or URL
import argparse
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from settings import CLIENT_ID, CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                      client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Searches for an item')
    parser.add_argument('-q', '--query', required=True,
                        help='Search query')
    return parser.parse_args()


def main():
    args = get_args()
    results = sp.search(args.query)
    pprint(results)


if __name__ == '__main__':
    main()
